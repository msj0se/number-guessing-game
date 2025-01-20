# Number Guessing Game

## Description

This is a simple console application I created as a fun challenge to pass the time. It’s a Number Guessing game where the user has to guess a randomly generated number within a given range. The user can choose from three difficulty levels, which affect the number of guesses they have to make.

This project was done for practice as part of the [Roadmap - Number Guessing Game](https://roadmap.sh/projects/number-guessing-game) challenge.

## Features

- Randomly generated number between 1 and 100.
- Three difficulty levels:
  - **Easy**: 10 chances.
  - **Medium**: 5 chances.
  - **Hard**: 3 chances.
- Input validation to ensure the user enters a valid number.
- Feedback after each guess to guide the player (higher or lower than the target number).
- Congratulatory message when the user guesses the correct number.

## How to Play

1. **Choose your difficulty level**:
   - **Easy**: 10 chances to guess the number.
   - **Medium**: 5 chances to guess the number.
   - **Hard**: 3 chances to guess the number.

2. **Guess the number**: Enter your guess, and the program will tell you whether the correct number is higher or lower than your guess.

3. **Keep guessing** until you either guess the number correctly or run out of chances.

4. **Victory message**: When you guess correctly, you’ll see a message telling you how many attempts it took.

## How to Run

1. Make sure Python is installed on your computer.
2. Copy the code into a Python file (e.g., `number_guessing_game.py`).
3. Open a terminal or command prompt and run the file by typing:
   
```bash
python number_guessing_game.py
```
