# File Organizer

A Python script that automatically organizes files in a directory by categorizing them into subdirectories based on their file extensions. This tool helps keep your directories clean and well-structured by sorting files into appropriate categories like images, videos, documents, and others.

## Features

- Automatically creates category subdirectories if they don't exist
- Organizes files based on their extensions
- Supports multiple file formats:
  - Images (.jpg, .jpeg, .png, .gif)
  - Videos (.mp4, .mkv, .flv, .avi, .mov)
  - Documents (.pdf, .docx, .txt, .pptx, .xlsx)
  - Others (any unrecognized extension)
- Simple and easy to use
- Non-destructive operation (files are moved, not deleted)

## Usage

1. Clone or download this repository
2. Modify the `directory_path` variable in `main.py` to point to your target directory
3. Run the script:
   ```bash
   python main.py
   ```

## How It Works

The script performs the following operations:
1. Creates category subdirectories if they don't exist
2. Scans all files in the specified directory
3. Identifies file extensions and matches them with predefined categories
4. Moves files to their corresponding category folders
5. Places files with unrecognized extensions in the "others" folder

## Example Output

Below is an example of how the script organizes files:

![File Organization Example](Images/Output.png)

## Requirements

- Python 3.x
- Standard Python libraries (os, shutil)

## Project Structure

```
├── main.py
├── README.md
└── Images/
    └── Output.png
```

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. You can also open issues for any bugs found or feature requests.

## License

This project is open source and available under the MIT License.