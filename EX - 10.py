# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:  # If number is divisible by 2 with no remainder, it's even
        return "The number is even."
    else:
        return "The number is odd."  # Otherwise, it's odd

# Main function8
def main():
    while True:  # Loop until valid input is received
        # Ask the user to enter a number
        num_input = input("Enter a number: ")
        
        # Error handling: Check if the input is numeric
        if num_input.isdigit():  # This ensures the input is a valid number
            num = int(num_input)  # Convert the valid input to an integer
            break  # Exit the loop when valid input is received
        else:
            print("Invalid input. Please enter a numeric value.")  # Prompt the user again if the input is invalid
    
    # Call the function and get the result
    result = check_even_odd(num)
    
    # Print the result
    print(result)

# Call the main function
if __name__ == "__main__":
    main()
