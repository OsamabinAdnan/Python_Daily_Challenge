# Bulk File Uploader for Google Drive

A Python script that automatically uploads multiple files to Google Drive using the PyDrive library.

## Features

- Batch upload multiple files to Google Drive
- Automatic authentication with Google Drive API
- Uploads files to a specified Google Drive folder
- Provides feedback with file IDs after successful uploads

## Prerequisites

- Python 3.x
- PyDrive library
- Google Drive API credentials (`client_secrets.json`)

## Installation

1. Install the required package:
```bash
pip install PyDrive
```

2. Place your `client_secrets.json` file in the project root directory. You can obtain this file from the Google Cloud Console:
   - Go to Google Cloud Console
   - Create a new project or select existing one
   - Enable Google Drive API
   - Create credentials (OAuth 2.0 Client ID)
   - Download the client configuration file and rename it to `client_secrets.json`

## Usage

1. Place the files you want to upload in the project directory
2. Update the `upload_list` in `main.py` with your file names
3. Update the parent folder ID in the script with your desired Google Drive folder ID
4. Run the script:
```bash
python main.py
```

## File Structure

```
├── main.py                 # Main script file
├── client_secrets.json     # Google Drive API credentials
├── 1.txt                   # Sample files to upload
├── 2.txt
└── 3.txt
```

## How It Works

1. The script authenticates with Google Drive using OAuth2
2. It reads the list of files to be uploaded
3. For each file:
   - Creates a new file instance on Google Drive
   - Sets the target folder
   - Uploads the file content
   - Prints confirmation with the file's Google Drive ID

## Notes

- Make sure you have proper permissions for the target Google Drive folder
- Keep your `client_secrets.json` secure and never share it publicly
- The script currently uses a hardcoded folder ID - update it according to your needs

## License

This project is open source and available under the MIT License.