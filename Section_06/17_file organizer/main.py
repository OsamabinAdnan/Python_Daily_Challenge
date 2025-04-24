# Import required libraries
import os  # For file and directory operations
import shutil  # For moving files

def organize_file(directory):
    """
    Organizes files in the specified directory into categorized subdirectories based on file extensions.
    
    Args:
        directory (str): The path to the directory containing files to be organized
    """
    # Dictionary defining file categories and their corresponding extensions
    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif'],  # Image file extensions
        'videos':['.mp4', '.mkv', '.flv', '.avi', '.mov'],  # Video file extensions
        'documents':['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],  # Document file extensions
        'others': []  # For files that don't match any category
    }

    # Create subdirectories for each category if they don't exist
    for subdir in file_types:
        os.makedirs(os.path.join(directory, subdir), exist_ok=True)
    
    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory,filename)
        # Check if the current item is a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file extension in lowercase
            file_extension = os.path.splitext(filename)[1].lower()

            # Flag to track if file has been moved
            file_moved = False
            # Check each category to find matching extension
            for category, extension in file_types.items():
                if file_extension in extension:
                    # Move file to appropriate category folder
                    shutil.move(file_path, os.path.join(directory, category, filename))
                    file_moved = True
                    break
            # If file extension didn't match any category, move to 'others' folder
            if not file_moved:
                shutil.move(file_path, os.path.join(directory, 'others', filename))
    
    print("Files have been organized successfully!")

# Example usage with a specific directory path
directory_path = 'C://Users/AOTHHSA/Downloads'  # Change this to your desired directory path
organize_file(directory_path)