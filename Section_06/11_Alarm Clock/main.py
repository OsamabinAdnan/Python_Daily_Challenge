# Importing required modules
import time  # Provides time-related functions like sleep
from datetime import datetime  # For getting current system time
from playsound import playsound  # For playing alarm sound when time matches

# Function to set and run the alarm
def set_alarm():
    # Ask the user to input the alarm time in HH:MM:SS format
    alarm_time = input('Enter alarm time (HH:MM:SS): ')
    
    # Start an infinite loop to keep checking the current time
    while True:
        # Get the current system time and format it as a string (HH:MM:SS)
        current_time = datetime.now().strftime('%H:%M:%S')
        
        # Check if current time matches the user-set alarm time
        if current_time == alarm_time:
            # Notify the user that the alarm has triggered
            print('Alarm! Time to Wake up!\n')
            
            # Play the alarm sound (make sure 'Assets/alarm.wav' exists at this path)
            playsound('Assets/alarm.wav')
            
            # Exit the loop after alarm triggers
            break
        
        # Wait for 1 second before checking the time again to reduce CPU usage
        time.sleep(1)

# Main function that runs when the script is executed
def main():
    # Display a message to the user
    print('\nSet your alarm')
    
    # Show the current system time to help the user input a valid alarm time
    print(f'Current Time: {datetime.now().strftime("%H:%M:%S")}\n')
    
    # Call the set_alarm function to start the alarm process
    set_alarm()

# Entry point of the program
if __name__ == '__main__':
    main()
