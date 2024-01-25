import streamlit as st
import random

# Set page title
st.title("Guess the Number Game")

# Generate a random number between 1 and 100
number = random.randint(1, 100)
st.write(number)
# Counter for the number of guesses
num_of_guesses = 0

# Main game loop
while True:
    # Get user input for the next guess
    guess = st.number_input("Guess again:", min_value=1, max_value=100)

    # Increase the number of guesses
    num_of_guesses += 1
    
    # Check if the guess is correct
    if guess == number:
        st.success(f"Congratulations! You guessed the number in {num_of_guesses} attempts.")
        break
    elif guess > number:
        st.warning(f"Too high! Try a lower number.{num_of_guesses} attempts")
    elif guess < number:
        st.warning(f"Too low! Try a higher number.{num_of_guesses} attempts")

   