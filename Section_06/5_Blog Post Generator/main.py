import os

# Directory where all blog posts will be stored
BLOG_DIR = 'Blogs'

def save_blog(title, content):
    """
    Saves a blog post to a text file.
    Args:
        title (str): The title of the blog post (used as filename)
        content (str): The main content of the blog post
    """
    # Create the Blogs directory if it doesn't exist
    if not os.path.exists(BLOG_DIR):
        os.makedirs(BLOG_DIR)
    # Convert filename to lowercase and append .txt extension
    filename = os.path.join(BLOG_DIR, f"{title}.txt").lower()
    # Write content to file
    with open (filename, 'w') as file:
        file.write(content)
    print(f"\nBlog post {title} saved to {filename} successfully.")

def view_blog():
    """
    Displays a list of all available blog posts in the Blogs directory.
    Returns None if no blogs are found.
    """
    # Check if directory exists and contains files
    if not os.path.exists(BLOG_DIR) or not os.listdir(BLOG_DIR):
        print("No blog posts found.")
        return
    print('\nAvailable blog posts:')
    # List all blog posts (removing .txt extension for display)
    for file in os.listdir(BLOG_DIR):
        print(f"- {file[:-4]}")

def preview_blog(title):
    """
    Shows the content of a specific blog post.
    Args:
        title (str): The title of the blog post to preview
    """
    filename = os.path.join(BLOG_DIR, f"{title}.txt")
    try:
        # Attempt to read and display the blog content
        with open(filename, 'r') as file:
            content = file.read()
            print(f'\nPreview of blog post "{title}":\n\n{content}')
    except FileNotFoundError:
        print(f"Blog post {title} not found.")

def delete_blog(title):
    """
    Deletes a specific blog post file.
    Args:
        title (str): The title of the blog post to delete
    """
    filename = os.path.join(BLOG_DIR,f"{title}.txt")
    # Check if file exists before attempting deletion
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\nBlog post {title} deleted successfully.")
    else:
        print(f"\nBlog post {title} not found.")

def main():
    """
    Main program loop that provides a command-line interface for the blog post generator.
    Handles user input and calls appropriate functions based on user choice.
    """
    while True:
        # Display menu options
        print('\nBlog Post Generator')
        print('1. Create a blog post')
        print('2. View blog posts')
        print('3. Preview a blog post')
        print('4. Delete a blog post')
        print('5. Exit')

        # Get user choice
        choices = int(input('Enter your choice (1/2/3/4): '))

        # Process user choice
        if choices == 1:
            title = input('Enter the title of the blog post: ')
            content = input('Enter the content of the blog post: ')
            save_blog(title, content)
        elif choices == 2:
            view_blog()
        elif choices == 3:
            title = input('Enter the title of the blog post to preview: ').lower()
            preview_blog(title)
        elif choices == 4:
            title = input('Enter the title of the blog post to delete: ').lower()
            delete_blog(title)
        elif choices == 5:
            print('👋 Goodbye! Exiting the program.')
            break
        else:
            print('Invalid choice. Please select a valid option (1/2/3/4).')

# Entry point of the program
if __name__ == '__main__':
    main()

