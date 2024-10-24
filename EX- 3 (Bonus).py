# Prompt the user to enter their full name, ensuring it's not empty
while True:
    name = input("Enter your full name: ")
    if name.strip():  # Check if the input isn't empty or just spaces
        break  # Exit the loop when valid input is given
    else:
        print("Invalid input. Please enter your name.")  # Ask again if input is invalid

# Prompt the user to enter their hometown
hometown = input("Enter your hometown: ")

# Using a while loop to ensure the user inputs a valid numeric age
while True:
    age = input("Enter your age: ")
    
    # Check if the input is composed only of digits
    if age.isdigit():  
        age = int(age)  # Convert the valid age input from string to integer
        break   # Exit the loop when a valid age is entered
    else:
        print("Invalid age. Please enter a numeric value.")     # Prompt the user again if the input is invalid
 
# Store the user's information in a dictionary
user_info = {
    "Name": name,   # Key for the user's name
    "Hometown": hometown,   # Key for the user's hometown
    "Age": age,      # Key for the user's age
}

# Print the user's information on separate lines
print("Name: " + user_info['Name'] + "\nHometown: " + user_info['Hometown'] + "\nAge: " + str(user_info['Age']))
