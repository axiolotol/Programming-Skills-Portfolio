# Define the correct password
correct_password = "12345"

# Set the maximum number of attempts
max_attempts = 5
attempts = 0  # Start with no attempts made

# Loop until the user enters the correct password or runs out of attempts
while attempts < max_attempts:
    # Ask the user to input the password, showing how many attempts they have left
    user_input = input(f"Enter the password (Attempt {attempts + 1}/{max_attempts}): ").strip()

    # Error handling: check if the input is empty
    if not user_input:
        print("Input cannot be empty. Please enter a password.")
        continue  # Go back to the start of the loop

    # Check if the input is the correct password
    if user_input == correct_password:
        print("Password correct! Access granted.")  # Print if the password is correct
        break  # Exit the loop
    else:
        attempts += 1  # Increase the attempt count by 1
        remaining_attempts = max_attempts - attempts  # Calculate the remaining attempts

        # If there are still attempts left
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")  # If no attempts are left
