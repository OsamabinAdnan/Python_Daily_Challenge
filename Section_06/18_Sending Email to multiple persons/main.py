# Import required libraries
import csv  # For reading CSV files
import smtplib  # For sending emails using SMTP protocol
import ssl  # For creating secure SSL context
from datetime import date  # For getting current date
from dotenv import load_dotenv  # For loading environment variables from .env file
import os  # For accessing environment variables

load_dotenv()  # Load environment variables from .env file (if used)

my_password = os.getenv('GMAIL_APP_PASSWORD')  # Get Gmail App Password from environment variable

def send_email(from_address, password, to_address, message):
    """
    Send an email using Gmail's SMTP server with SSL encryption.
    
    Args:
        from_address (str): Sender's Gmail address
        password (str): Gmail App Password for authentication
        to_address (str): Recipient's email address
        message (str): Formatted email message including subject
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    context = ssl.create_default_context()  # Create secure SSL context
    try:
        # Establish secure connection to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(from_address, password)  # Authenticate with Gmail
            server.sendmail(from_address, to_address, message)  # Send the email
        return True
    except smtplib.SMTPAuthenticationError:
        print(f"Authentication failed for {from_address}. Check email/password or App Password.")
        return False
    except Exception as e:
        print(f"Error sending email to {to_address}: {e}")
        return False

def main():
    """
    Main function to read student data from CSV and send evaluation emails.
    The CSV should contain columns for name, email, and score.
    """
    # Get current date in Month DD, YYYY format
    today = date.today().strftime("%B %d, %Y")
    
    # Email template using string formatting
    message_template = """Subject: Your Evaluation

Hi {name},

The date of your Q3 evaluation is {today}.
Your score is {score}.

Regards,
Your Team
"""
    # --- Security Warning: Hardcoding credentials is not recommended ---
    # Consider using environment variables, a config file, or getpass
    from_address = 'osamabinadnan.freelancing@gmail.com'
    # IMPORTANT: If using Gmail with 2FA, you need an "App Password" here, not your regular password.
    password = my_password # Replace with your actual password or App Password

    try:
        # Open and read the CSV file containing student information
        with open('Students.csv') as file:
            reader = csv.reader(file)
            header = next(reader, None)  # Skip and store header row
            if header is None:
                print("Warning: Students.csv seems empty or has no header.")
                return

            # Process each student's data
            for row in reader:
                # Ensure row has all required fields (name, email, score)
                if len(row) >= 3:
                    # Extract and clean student data
                    name, email, score = row[0].strip(), row[1].strip(), row[2].strip()

                    # Format personalized email message for each student
                    message = message_template.format(name=name, today=today, score=score)

                    # Send email and track success/failure
                    if send_email(from_address, password, email, message):
                        print(f'Email sent successfully to {name} at {email}')
                    else:
                        print(f'Failed attempt to send email to {name} at {email}')
                else:
                    print(f"Skipping malformed row: {row}")

    except FileNotFoundError:
        print("Error: Students.csv not found in the current directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()  # Execute main function when script is run directly
