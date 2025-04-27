# Import required libraries
import smtplib  # For sending emails using SMTP protocol
import schedule  # For scheduling tasks
import time     # For adding delays
import os       # For accessing environment variables
from dotenv import load_dotenv  # For loading environment variables from .env file

# Load environment variables from .env file
# This ensures sensitive information is not hardcoded in the script
load_dotenv()

# Get the email credentials from environment variables
# These should be defined in a .env file in the same directory
sender_email_address = os.getenv('SENDER_EMAIL')     # Your Gmail address
app_password = os.getenv('APP_PASSWORD')             # Your Gmail app-specific password
receiver_email_address = os.getenv('RECEIVER_EMAIL')  # Recipient's email address

def send_email():
    """
    Function to send an automated email using Gmail's SMTP server.
    Uses environment variables for email credentials and recipient address.
    """
    # Set up email parameters
    sender_email = sender_email_address
    receiver_email = receiver_email_address
    password = app_password

    # Define email content
    subject = 'Automated Email'
    body = 'This is an automated email sent using Python.'

    # Create email message with subject and body
    message = f'Subject: {subject}\n\n{body}'

    # Establish connection with Gmail's SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()          # Identify yourself to the server
        server.starttls()      # Start TLS encryption
        server.ehlo()          # Re-identify yourself over TLS connection
        server.login(sender_email, password)  # Login to the server
        server.sendmail(sender_email, receiver_email, message)  # Send the email
        print('Email sent successfully!')

# Schedule the email to be sent every minute
schedule.every(1).minutes.do(send_email)

# Schedule the email to be sent every day at a specific time
schedule.every().day.at("08:00").do(send_email)

# Infinite loop to keep the script running
while True:
    schedule.run_pending()  # Run any pending scheduled tasks
    time.sleep(1)          # Wait for 1 second before checking again
