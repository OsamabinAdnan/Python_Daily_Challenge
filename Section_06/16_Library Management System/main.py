# Base class for all library items
class LibraryItems():
    def __init__(self, title, author, publication_year):
        """
        Initialize a library item with basic information
        Args:
            title (str): The title of the item
            author (str): The author of the item
            publication_year (int): Year the item was published
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True  # Track if item is available for checkout
    
    def __str__(self):
        """Return a string representation of the library item"""
        return f"{self.title} by {self.author}, publish in {self.publication_year}"
    
    def check_out(self):
        """
        Process checkout of the item if it's available
        Returns message indicating success or unavailability
        """
        if self.is_available:
            print(f"Check out: {self}")
            self.is_available = False
        else:
            print(f"{self} is not available for checkout.")
    
    def check_in(self):
        """Process return of the item and make it available again"""
        print(f"Check in: {self} has been checked in.")
        self.is_available = True


class Book(LibraryItems):
    def __init__(self, title, author, publication_year, genre):
        """
        Initialize a book with genre information
        Args:
            title (str): The title of the book
            author (str): The author of the book
            publication_year (int): Year the book was published
            genre (str): Genre/category of the book
        """
        super().__init__(title, author, publication_year)
        self.genre = genre
    
    def __str__(self):
        """Return a string representation of the book including its genre"""
        return f"{super().__str__()} - Genre: {self.genre}"


class User():
    def __init__(self, name):
        """
        Initialize a library user
        Args:
            name (str): Name of the user
        """
        self.name = name
    
    def borrow_item(self, item):
        """
        Process borrowing of an item by the user
        Args:
            item (LibraryItems): The item to be borrowed
        """
        item.check_out()
    
    def return_item(self, item):
        """
        Process return of an item by the user
        Args:
            item (LibraryItems): The item to be returned
        """
        item.check_in()

# Create a list to store library items
library = []

# Create sample books
book1 = Book("1. Python Programming", "John Doe", 2020, "Programming")
book2 = Book("2. Data Science", "Jane Smith", 2021, "Data Science")
book3 = Book("3. Machine Learning", "Alice Johnson", 2022, "AI",)

# Add books to the library
library.append(book1)
library.append(book2)
library.append(book3)

# Create sample users
user1 = User('Alice')
user2 = User('Bob')

# Demonstrate checkout process
print(f"\nBooks Checked Out:")
user1.borrow_item(book1)
user2.borrow_item(book2)

# Demonstrate check-in process
print(f"\nBooks Checked In:")
user1.return_item(book1)

# Display all library items
print(f'\nLibrary items:')
for items in library:
    print(items)