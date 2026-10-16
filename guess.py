import time
import random
# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode
GAME_MODES = ["Easy Mode", "Medium Mode", "Hard Mode"] #Levels
ROUND_MODES = ["Classic", "Time Challenge"] #Modes
LOW = None
HIGH = None
ATTEMPTS = None
COUNTER = 0
RESULT = None
# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

while(True):

    print("Welcome to the Number Guessing Game!!\n")
    for index, g in enumerate(GAME_MODES):
            print(f"{index + 1}. {g}")
    level = input("Choose a level (1-3): ")
    if level.isdigit() and 1 <= int(level) <= 3:
        level = int(level)
    else:
        print("Please enter a valid level.")
        continue

    match level:
        case 1:
            LOW = 1
            HIGH = 50
            ATTEMPTS = 10
            break   
        case 2:
            LOW = 1
            HIGH = 100
            ATTEMPTS = 8
            break
        case 3:
            LOW = 1
            HIGH = 500
            ATTEMPTS = 10 
            break      

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.
while(True):
    
    for index, m in enumerate(ROUND_MODES):
        print(f"{index + 1}. {m}")
    mode = input("Choose a mode (1-2): ")
    if mode.isdigit() and 1 <= int(mode) <= 2:
        mode = int(mode)
        break
    else:
        print("Please enter a valid mode.")

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

if DEBUG_SECRET is not None:
    gen_number = DEBUG_SECRET
else:
    gen_number = random.randint(LOW, HIGH)

start_time = time.time()

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

while(True):
    
    if mode == 2:
        time_left = int(TIME_LIMIT - (time.time() - start_time))
        print(f"Time Remaining: {time_left} seconds")
    guess = input(f"Enter your guess between {LOW} and {HIGH}: ")

    if guess.isdigit() == False or int(guess) < LOW or int(guess) > HIGH:
        print(f"Invalid Guess. Guess a number between {LOW} and {HIGH}. Attempts left: {ATTEMPTS-COUNTER}")
        continue
    
    COUNTER += 1
    if mode == 2 and time.time() - start_time > TIME_LIMIT:
        RESULT = "timeout!"
        break

    guess = int(guess)
    if guess == gen_number:
        RESULT = "win!"
        break
    elif guess < gen_number:
        print(f"Too low! Try again. Attempts left: {ATTEMPTS-COUNTER}")
    elif guess > gen_number:
        print(f"Too high! Try again. Attempts left: {ATTEMPTS-COUNTER}")
    if COUNTER == ATTEMPTS:
        RESULT = "lose!"
        break
            
# ---------- End of round ----------
# Goal: show the result that matches how the round ended.

if RESULT == "win!":
    print(f"Congratulations! You guessed the number {gen_number} in {COUNTER} attempts.")
elif RESULT == "lose!":
    print(f"Sorry, you've used all your attempts. The number was {gen_number}.")        
elif RESULT == "timeout!":
    print(f"Time's Up,  the number was {gen_number}.")