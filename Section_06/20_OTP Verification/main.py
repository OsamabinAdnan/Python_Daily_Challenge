# Import required libraries
import os
import math
import random
import smtplib
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Gmail credentials from environment variables
app_id_pwd = os.getenv('GOOGLE_APP_PWD')  # App password for Gmail
account_id = os.getenv('GMAIL_ID')    # Gmail account

# Define possible digits for OTP
digit = '0123456789'

# Generate a 6-digit random OTP
OTP = ''
for i in range(6):
    OTP += digit[math.floor(random.random()*10)]

# Create the OTP message
otp = f'{OTP} is your OTP for verification.'
msg = otp

# Initialize SMTP server for Gmail
s = smtplib.SMTP('smtp.gmail.com', 587)  # Using Gmail's SMTP server with port 587

# Start TLS for security
s.starttls()

# Authentication using environment variables
s.login(account_id, app_id_pwd)

# Get recipient's email address
email_id = input('Enter your email id: ')

# Send email with OTP
# Parameters: sender's email, recipient's email, message
s.sendmail(account_id, email_id, msg)  # Fixed sender email to use account_id

# Verify OTP
a = input('Enter the OTP sent to your email: ')
if a == OTP:
    print('OTP verified successfully.')
else:
    print('Invalid OTP.')

