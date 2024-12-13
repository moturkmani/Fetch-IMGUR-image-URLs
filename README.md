Fetch Image URLs from Imgur Album

This Python script interacts with the Imgur API to retrieve image URLs from a specified album and save them to a JSON file. It provides an easy-to-use interface for handling JSON files and transforming image URLs.

Features

Fetches all image URLs from a specified Imgur album.

Saves the URLs to a JSON file for reuse.

Handles existing or new JSON files interactively.

Converts Imgur URLs to the i.imgur.com format.

Prerequisites

Python Installation:

Download Python from python.org.

During installation, check the box to "Add Python to PATH."

Verify installation:

python --version
pip --version

Install Required Libraries:

Install the requests library:

pip install requests

Imgur Client ID:

Register an application on Imgur to get your Client ID.

How to Use

Download or Clone the Script:
Save the provided fetch_imageurl2.py script to your desired directory.

Run the Script:

Open a terminal or command prompt.

Navigate to the folder where the script is saved.

Execute the script:

python fetch_imageurl2.py

Provide Required Inputs:

Enter your Imgur Client ID and Album ID when prompted.

Choose to use an existing JSON file or create a new one.

JSON Output:

The script saves all retrieved image URLs in images.json.

This file can be found in the same directory as the script.

Notes

The script uses Tkinter for GUI interactions; ensure your Python installation supports it.

Use Notepad++ or any text editor to view or edit the script if needed.

If errors occur, ensure you have a valid Client ID and Album ID.
