# Create a dictionary mapping month numbers to the number of days
days_in_a_month = {
    1: ("January", 31),
    2: ("February", 28),  # Will adjust for leap year
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}

# Ask the user for the month number
while True:  # Loop until valid month number is entered
    try:
        month_number = int(input("Enter the month number (1-12): "))  # Ask for month number and convert to int
        if 1 <= month_number <= 12:  # Make sure the month number is between 1 and 12
            break  # Exit loop if valid
        else:
            print("Invalid month number. Please enter a number between 1 and 12.")  # Prompt user again
    except ValueError:  # Catch non-integer inputs
        print("Invalid input. Please enter a number between 1 and 12.")

# Get the month name and number of days
month_name, days = days_in_a_month[month_number]

# Check if the month is February for leap year handling
if month_number == 2:  # Case for February
    while True:  # Loop until valid input for leap year is received
        is_leap_year = input("Is it a leap year? (yes or no): ").strip().lower()  # Ask if it's a leap year
        if is_leap_year == "yes":  # Check if user says it's a leap year
            days = 29  # Adjust days for leap year
            print(f"{month_name} has 29 days in a leap year.")
            break  # Exit loop if valid input is given
        elif is_leap_year == "no":  # Check if user says it's not a leap year
            print(f"{month_name} has 28 days.")
            break  # Exit loop if valid input is given
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")  # Prompt user for valid input
else:
    # For all other months, print the name of the month and its number of days
    print(f"{month_name} has {days} days.")
