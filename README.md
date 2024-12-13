# Fetch Image URLs from Imgur Album

This Python script interacts with the Imgur API to retrieve image URLs from a specified album and save them to a JSON file. It provides an easy-to-use interface for handling JSON files and transforming image URLs.

## Features
- Fetches all image URLs from a specified Imgur album.
- Saves the URLs to a JSON file for reuse.
- Handles existing or new JSON files interactively.
- Converts Imgur URLs to the `i.imgur.com` format.

## Prerequisites
1. **Python Installation**:
   - Download Python from [python.org](https://www.python.org/downloads/).
   - During installation, check the box to "Add Python to PATH."
   - Verify installation:
     ```bash
     python --version
     pip --version
     ```

2. **Install Required Libraries**:
   - Install the `requests` library:
     ```bash
     pip install requests
     ```

3. **Imgur Client ID**:
   - Register an application on [Imgur](https://api.imgur.com/oauth2/addclient) to get your Client ID.

## How to Use

1. **Download or Clone the Script**:
   Save the provided `fetch_imageurl2.py` script to your desired directory.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the folder where the script is saved.
   - Execute the script:
     ```bash
     python fetch_imageurl.py
     ```

3. **Provide Required Inputs**:
   - use [Notepad++](https://notepad-plus-plus.org/downloads/) to enter your Imgur Client ID and Album ID in the top section of the python script.
   - Choose to use an existing JSON file or create a new one.

4. **JSON Output**:
   - The script saves all retrieved image URLs in the default `images.json` or user-defined JSON file name.
   - This file can be found in the same directory as the script.

## Notes
- The script uses Tkinter for GUI interactions; ensure your Python installation supports it.
- Use Notepad++ or any text editor to view or edit the script if needed.
- If errors occur, ensure you have a valid Client ID and Album ID.
