import requests
import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Replace with your Imgur Client ID
CLIENT_ID = "enter your CLIENT ID here"

# Replace with your album ID
album_id = "enter Album ID here"

# Imgur Album API endpoint
api_url = f"https://api.imgur.com/3/album/{album_id}/images"

# Headers for authentication
headers = {
    "Authorization": f"Client-ID {CLIENT_ID}"
}

# Function to load existing JSON data
def load_existing_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    return {"images": []}

# Function to create a centered popup window
def create_centered_window(title, message):
    popup = tk.Tk()
    popup.title(title)
    popup.geometry("450x250")  # Adjusted size to ensure all elements fit
    popup.eval('tk::PlaceWindow . center')  # Center the window

    label = tk.Label(popup, text=message, font=("Helvetica", 20, "bold"), wraplength=400)
    label.pack(pady=20)

    button = tk.Button(popup, text="OK", font=("Helvetica", 20, "bold"), command=popup.destroy)
    button.pack(pady=10)

    popup.mainloop()

# Initialize Tkinter for dialog handling
root = tk.Tk()
root.withdraw()  # Hide the root Tkinter window

# Ask user if they already have an images.json file
use_existing = messagebox.askquestion(
    "Existing File", "Do you already have an images.json file?", icon="question"
)

if use_existing == "yes":
    messagebox.showinfo("Select File", "Please select your existing images.json file.")
    existing_file_path = filedialog.askopenfilename(
        title="Select your images.json file",
        filetypes=[("JSON files", "*.json")]
    )
    if existing_file_path:
        existing_data = load_existing_json(existing_file_path)
        existing_urls = set(existing_data.get("images", []))
    else:
        messagebox.showwarning("File Not Found", "No file was selected. A new images.json will be created.")
        existing_file_path = "images.json"
        existing_data = {"images": []}
        existing_urls = set()
else:
    # Ask if the user wants to change the default filename
    change_filename = messagebox.askquestion(
        "Change Filename", "Would you like to change the default filename (images.json)?", icon="question"
    )
    if change_filename == "yes":
        new_file_path = filedialog.asksaveasfilename(
            title="Save as", defaultextension=".json", filetypes=[("JSON files", "*.json")]
        )
        if new_file_path:
            existing_file_path = new_file_path
        else:
            existing_file_path = "images.json"  # Fall back to default
    else:
        existing_file_path = "images.json"

    existing_data = {"images": []}
    existing_urls = set()

# Send the request to fetch album images
response = requests.get(api_url, headers=headers)
response.raise_for_status()  # Raise error if the request fails

# Parse the response JSON
data = response.json()

# Extract and transform image URLs to the i.imgur.com format
new_image_urls = []
for item in data['data']:
    original_link = item['link']
    # Extract the image ID and file extension from the original link
    image_id = original_link.split('/')[-1].split('.')[0]  # Extract ID
    file_extension = original_link.split('.')[-1]         # Extract extension
    # Construct the i.imgur.com URL
    transformed_link = f"https://i.imgur.com/{image_id}.{file_extension}"
    # Add to the list if not already present
    if transformed_link not in existing_urls:
        new_image_urls.append(transformed_link)

# Combine existing and new URLs
existing_data["images"].extend(new_image_urls)

# Save updated data back to the JSON file
with open(existing_file_path, 'w') as json_file:
    json.dump(existing_data, json_file, indent=2)

messagebox.showinfo("Success", f"Image URLs saved to {existing_file_path}")