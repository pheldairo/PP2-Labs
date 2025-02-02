import random


print("Hello! What is your name?\n")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.\n")
number_to_guess = random.randint(1, 20)
guesses_taken = 0

while True:
    print("Take a guess.\n")
    guess = int(input())
    guesses_taken += 1

    if guess < number_to_guess:
        print("Your guess is too low.\n")
    elif guess > number_to_guess:
        print("Your guess is too high.\n")
    else:
        print(f"Good job, {name}! You guessed my number in {guesses_taken + 1} guesses!\n")
        break

