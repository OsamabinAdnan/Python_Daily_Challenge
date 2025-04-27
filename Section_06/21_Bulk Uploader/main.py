# Import required Google Drive API libraries
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Initialize Google authentication
google_auth = GoogleAuth()
# Create a GoogleDrive instance with authenticated credentials
drive_app = GoogleDrive(google_auth)

# List of files to be uploaded
upload_list = ['1.txt', '2.txt', '3.txt']

# Iterate through each file in the upload list
for file_to_upload in upload_list:
    # Create a new file on Google Drive
    # Set the parent folder ID where files will be uploaded
    file = drive_app.CreateFile({'parents': [{'id': '1J35Em0cdPUSz-yDi6DTYJzcm-PQd0lhN'}]})
    
    # Set the content of the file from local file system
    file.SetContentFile(file_to_upload)
    
    # Upload the file to Google Drive
    file.Upload()
    
    # Print confirmation message with file name and its Google Drive ID
    print(f'Uploaded {file_to_upload} to Google Drive with ID: {file.get("id")}')