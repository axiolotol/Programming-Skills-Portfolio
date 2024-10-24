# Create a list of names to search through 
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Optional: Allow the user to input the name to search for
while True:
    search_name = input("Enter the name you're searching for: ").strip()  # Ask the user for a name and remove extra spaces
    
    # Error handling: Check if the input is empty
    if not search_name:
        print("Input cannot be empty. Please enter a valid name.")
        continue  # Ask for input again if it's empty

    # Check if the name is in the list
    if search_name in names:  # This checks if the user's input is in the list
        print(f"{search_name} found in the list!")  # Print if the name is found
        break  # Exit the loop after finding the name
    else:
        print(f"{search_name} not found in the list. Please try again.")  # Print if the name is not found
