from random import randint

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
print('You have 5 chances to guess the correct number.')

print('Please select the difficulty level:')
print('1. Easy (10 chances)')
print('2. Medium (5 chances)')
print('3. Hard (3 chances)')

easy = 10
medium = 5
hard = 3
random_number = randint(1, 100)

while True:
    try:
        difficulty_level = int(input('Enter your choice: '))
        break
    except ValueError:
        print('Sorry! Wrong input.')

if difficulty_level == 1:
    print('Great! You have selected the Easy difficulty level.')
    print("Let's start the game!")

    while easy != 0:
        while True:
            try:
                guess = int(input('Enter your guess: '))
                break
            except ValueError:
                print('Sorry! Wrong input.')

        if guess == random_number:
            print(f'Congratulations! You guessed the correct number in {easy - 1} attempts.')
            easy = 0
            break
        elif guess < random_number:
            print(f'Incorrect! The number is greater than {guess}.')
        elif guess > random_number:
            print(f'Incorrect! The number is less than {guess}.')

        easy -= 1
elif difficulty_level == 2:
    print('Great! You have selected the Medium difficulty level.')
    print("Let's start the game!")

    while medium != 0:
        while True:
            try:
                guess = int(input('Enter your guess: '))
                break
            except ValueError:
                print('Sorry! Wrong input.')

        if guess == random_number:
            print(f'Congratulations! You guessed the correct number in {medium - 1} attempts.')
            medium = 0
            break
        elif guess < random_number:
            print(f'Incorrect! The number is greater than {guess}.')
        elif guess > random_number:
            print(f'Incorrect! The number is less than {guess}.')

        medium -= 1
elif difficulty_level == 3:
    print('Great! You have selected the Hard difficulty level.')
    print("Let's start the game!")

    while hard != 0:
        while True:
            try:
                guess = int(input('Enter your guess: '))
                break
            except ValueError:
                print('Sorry! Wrong input.')

        if guess == random_number:
            print(f'Congratulations! You guessed the correct number in {hard - 1} attempts.')
            hard = 0
            break
        elif guess < random_number:
            print(f'Incorrect! The number is greater than {guess}.')
        elif guess > random_number:
            print(f'Incorrect! The number is less than {guess}.')

        hard -= 1