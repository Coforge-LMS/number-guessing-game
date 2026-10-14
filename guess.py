import time
import random
# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode
low = 1
high = 100
attempts = 0
print("Welcome to the Number Guessing Game!!\n")
number = random.randint(low, high)

while(True):
    guess = input(f"Enter your guess between {low} and {high}: ")

    if guess.isdigit() == False:
        print("Please enter a valid number.")
        continue

    attempts += 1
    guess = int(guess)
    if guess < low or guess > high:
        print(f"Your guess is out of bounds! Please guess a number between {low} and {high}.")
        continue
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        break
# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.

