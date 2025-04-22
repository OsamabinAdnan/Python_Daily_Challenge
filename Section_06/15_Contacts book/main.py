#!/usr/bin/env python3
"""
Contact Book Application
A simple command-line contact management system that allows users to store,
search, and manage contact information including names, phone numbers, and email addresses.

Author: [Your Name]
Date: April 2025
Version: 1.0

This application provides a command-line interface for managing contacts with the following features:
- Add new contacts with input validation
- Search existing contacts
- Delete contacts
- Display all contacts
- Persistent storage using text file
"""

import os  # For file operations
import re  # For regex pattern matching in validation
from typing import Dict, Any  # Type hints for better code documentation

# Constants
FILENAME = 'contacts.txt'  # File used for persistent storage of contacts

class ContactBook:
    """
    A class to manage contacts with functionality for adding, searching,
    deleting, and displaying contact information.
    
    The class maintains an in-memory dictionary of contacts and syncs with
    a text file for persistent storage.
    
    Attributes:
        contacts (Dict[str, Dict[str, str]]): Dictionary storing contact information
            with name as key and contact details (phone, email) as nested dictionary
    """
    
    def __init__(self):
        """
        Initialize the ContactBook instance.
        Creates an empty contacts dictionary and loads any existing contacts from file.
        """
        # Initialize empty dictionary to store contacts in memory
        self.contacts: Dict[str, Dict[str, str]] = {}
        # Load existing contacts from file if any
        self.load_contacts()

    def load_contacts(self) -> None:
        """
        Load contacts from the text file at startup.
        Each line in the file should be in format: name,phone,email
        Handles file reading exceptions gracefully.
        
        File Format:
            Each line contains: name,phone_number,email_address
            Example: John Doe,+1234567890,john@example.com
        """
        # Check if the storage file exists
        if os.path.exists(FILENAME):
            try:
                # Open and read the file line by line
                with open(FILENAME, 'r') as file:
                    for line in file:
                        # Split each line into components and strip whitespace
                        name, phone, email = line.strip().split(',')
                        # Store contact in the dictionary with nested structure
                        self.contacts[name] = {
                            'phone_number': phone,
                            'email_address': email
                        }
            except Exception as e:
                # Handle any file reading errors gracefully
                print(f"Error loading contacts: {e}")

    def save_contacts(self) -> None:
        """
        Save all contacts to the text file.
        Writes each contact as a comma-separated line: name,phone,email
        Handles file writing exceptions gracefully.
        
        This method is called after any modification to contacts (add/delete)
        to ensure persistent storage is always up to date.
        """
        try:
            # Open file in write mode (overwrites existing content)
            with open(FILENAME, 'w') as file:
                # Write each contact as a comma-separated line
                for name, info in self.contacts.items():
                    file.write(f"{name},{info['phone_number']},{info['email_address']}\n")
        except Exception as e:
            # Handle any file writing errors gracefully
            print(f"Error saving contacts: {e}")

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        Validate phone number format using regex.
        
        Accepts formats:
        - Optional '+' prefix
        - Optional country code '1'
        - 9-15 digits
        
        Examples of valid numbers:
        - +1234567890
        - 1234567890
        - +11234567890
        
        Args:
            phone (str): Phone number to validate
            
        Returns:
            bool: True if phone number format is valid, False otherwise
        """
        # Regex pattern explanation:
        # ^\+?      - Optional '+' at start
        # 1?        - Optional '1' country code
        # \d{9,15}$ - 9 to 15 digits at the end
        return bool(re.match(r'^\+?1?\d{9,15}$', phone))

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate email format using regex.
        Checks for standard email format: username@domain.tld
        
        Pattern matches:
        - Alphanumeric username with . _ % + -
        - @ symbol
        - Alphanumeric domain with . -
        - TLD of 2 or more characters
        
        Args:
            email (str): Email address to validate
            
        Returns:
            bool: True if email format is valid, False otherwise
        """
        # Complex regex to validate email format
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

    def add_contact(self) -> None:
        """
        Add a new contact with validation.
        
        Process:
        1. Get contact details from user input
        2. Validate all inputs
        3. Store in contacts dictionary
        4. Save to persistent storage
        
        Validation includes:
        - Checking for duplicate names
        - Phone number format validation
        - Email format validation
        """
        # Get and clean user input
        name = input('Enter name of contact: ').strip()
        
        # Check for duplicate contact names
        if name in self.contacts:
            print('Contact already exists!')
            return

        # Get and validate phone number
        phone = input('Enter phone number: ').strip()
        if not self.validate_phone(phone):
            print('Invalid phone number format!')
            return

        # Get and validate email
        email = input('Enter email: ').strip()
        if not self.validate_email(email):
            print('Invalid email format!')
            return

        # Store the new contact
        self.contacts[name] = {
            'phone_number': phone,
            'email_address': email,
        }
        
        # Update persistent storage
        self.save_contacts()
        print('Contact added successfully.')

    def search_contact(self) -> None:
        """
        Search for a contact by exact name match.
        Displays all stored information if contact is found.
        
        Note: The search is case-sensitive and requires exact match.
        Future enhancement could include case-insensitive or partial matching.
        """
        # Get and clean search input
        name = input('Enter name of contact: ').strip()
        
        # Check if contact exists and display info
        if name in self.contacts:
            info = self.contacts[name]
            print(f'\nName: {name}')
            print(f'Phone: {info["phone_number"]}')
            print(f'Email: {info["email_address"]}')
        else:
            print('Contact not found.')

    def delete_contact(self) -> None:
        """
        Delete a contact by exact name match.
        Updates the storage file after successful deletion.
        
        Process:
        1. Get contact name from user
        2. Check if contact exists
        3. Delete from dictionary if found
        4. Update persistent storage
        """
        # Get and clean input
        name = input('Enter name of contact to delete: ').strip()
        
        # Check if contact exists
        if name in self.contacts:
            # Remove contact and update storage
            del self.contacts[name]
            self.save_contacts()
            print(f'Contact {name} deleted.')
        else:
            print('Contact not found.')

    def show_all_contacts(self) -> None:
        """
        Display all stored contacts in a formatted list.
        Shows a message if no contacts are stored.
        
        Format:
        Name: [name], Phone: [phone], Email: [email]
        """
        # Check if contacts exist
        if not self.contacts:
            print('\nNo contacts found.')
            return
        
        # Display all contacts in formatted output
        print('\nAll contacts:')
        for name, info in self.contacts.items():
            print(f"Name: {name}, Phone: {info['phone_number']}, Email: {info['email_address']}")

    def run(self) -> None:
        """
        Main program loop displaying menu and handling user input.
        
        Menu Options:
        1. Add contact
        2. Search contact
        3. Delete contact
        4. Show all contacts
        5. Exit
        
        The loop continues until user chooses to exit (option 5)
        """
        while True:
            # Display menu options
            print('\n1. Add contact')
            print('2. Search contact')
            print('3. Delete contact')
            print('4. Show all contacts')
            print('5. Exit')

            # Get user choice
            choice = input('\nEnter your choice (1-5): ').strip()

            # Dictionary mapping choices to their corresponding methods
            actions = {
                '1': self.add_contact,
                '2': self.search_contact,
                '3': self.delete_contact,
                '4': self.show_all_contacts,
                '5': lambda: exit(0)  # Lambda function to exit program
            }

            # Execute the chosen action if valid
            if choice in actions:
                actions[choice]()
            else:
                print('Invalid choice. Please try again.')

def main():
    """
    Entry point of the program.
    Creates ContactBook instance and starts the application.
    """
    contact_book = ContactBook()
    contact_book.run()

# Standard boilerplate to call the main() function
if __name__ == '__main__':
    main()