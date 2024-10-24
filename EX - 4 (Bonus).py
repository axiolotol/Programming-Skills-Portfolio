# A dictionary that contains European countries and their capitals
quiz_questions = {
    "Spain": "Madrid",
    "France": "Paris",
    "Italy": "Rome",
    "Ireland": "Dublin",
    "Germany": "Berlin",
    "United Kingdom": "London",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki"
}

# Loop through each country in the quiz
for country in quiz_questions:  # Go through each country
    while True:  # Start a loop to ensure valid input
        # Ask the user for the capital of the current country
        user_answer = input(f"What is the capital of {country}? ")  # Ask the question
        
        # Check if the user entered a valid response
        if user_answer.strip():  # Check if input is not empty or just spaces
            # Check if the user's answer is correct (ignoring capitalisation)
            if user_answer.lower() == quiz_questions[country].lower():  # Correct answer
                print("Correct! Well done.")
            else:  # Wrong answer
                print(f"Wrong! The capital of {country} is {quiz_questions[country]}.")
            break  # Exit the loop after the question is answered (right or wrong)
        else:
            print("You didn't enter anything. Please provide an answer.")  # Error message for empty input

# Print thanking the user for participating
print("\nThank you for taking the quiz!")
