# Number Guessing Game

A number guessing game that runs in the terminal. The computer picks a secret number and I try to guess it. After each guess the game tells me if the guess is too low or too high. I can pick a difficulty level and play either Classic mode or a timed Time Challenge.

The whole game is in one file, `guess.py`. It uses only variables, `if` statements and loops.

## How to run

1. Install Python 3.10 or newer (the level menu uses `match`).
2. Clone the repository and open the folder:
   ```
   git clone https://github.com/<my-username>/number-guessing-game.git
   cd number-guessing-game
   ```
3. Create and activate a virtual environment (PyCharm does this for me). It is called `.venv` and is ignored by Git:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   On Windows, use `.venv\Scripts\activate` instead.
4. Run the game:
   ```
   python guess.py
   ```

No extra packages are needed.

## How to play

1. Pick a level from the numbered list.
2. Pick Classic or Time Challenge from the numbered list.
3. Type a number in the range shown. The game says too low, too high, or correct, and shows how many attempts are left.
4. The round ends when I guess the number, run out of attempts, or (in Time Challenge) run out of time. If I lose, the game shows the secret number.

Invalid input does not use an attempt. Invalid means letters or symbols, a blank entry, or a number outside the range. The game shows a message and asks again.

### Levels

| Level  | Range    | Attempts allowed |
|--------|----------|------------------|
| Easy   | 1 to 50  | 10               |
| Medium | 1 to 100 | 8                |
| Hard   | 1 to 500 | 10               |

### Modes

- **Classic:** no time limit. The attempt limit of the chosen level applies.
- **Time Challenge:** I have 60 seconds for the whole round and the attempt limit still applies. The game shows the seconds remaining before each guess. After a valid guess it checks the clock. If time has run out, the round ends and the number is revealed, even if that guess was correct. `input()` pauses the program, so the game only notices a timeout after I press Enter.

## Settings

Settings are at the top of `guess.py`:

| Name            | Value on `main`            | Meaning                                              |
|-----------------|----------------------------|------------------------------------------------------|
| `DEBUG_SECRET`  | `None`                     | Set a number such as 42 to test with a fixed secret  |
| `TIME_LIMIT`    | `60`                       | Seconds allowed in Time Challenge                    |
| `GAME_MODES`    | Easy, Medium, Hard         | Names shown in the level menu                        |
| `ROUND_MODES`   | Classic, Time Challenge    | Names shown in the mode menu                         |

## Git workflow

I built the game on three feature branches and merged each one into `main` with a pull request:

- `feature/classic-mode`: secret number, hints, attempt counter, input validation (PR #1)
- `feature/difficulty-levels`: level menu, ranges, attempt limits, attempts remaining (PR #2)
- `feature/time-challenge`: mode menu, 60-second timer, timeout handling (PR #3)

## Test plan

I tested with `DEBUG_SECRET = 42` so the secret number was known. For the timeout tests I set `TIME_LIMIT = 3` so I did not have to wait 60 seconds. Both settings were restored to `None` and `60` before the final commit.

| #  | What I tested | What I did | Expected result | Actual result | Pass? |
|----|---------------|------------|-----------------|---------------|-------|
| 1  | A guess that is too low | Easy, Classic. Secret 42. Guessed 10. | `Too low! Try again. Attempts left: 9` | `Too low! Try again. Attempts left: 9` | Yes |
| 2  | A guess that is too high | Easy, Classic. Secret 42. Guessed 49. | `Too high! Try again. Attempts left: 9` | `Too high! Try again. Attempts left: 9` | Yes |
| 3  | A correct guess with the right attempt count | Easy, Classic. Secret 42. Guessed 49, then 42. | Win message showing 2 attempts | `Congratulations! You guessed the number 42 in 2 attempts.` | Yes |
| 4  | Letters are rejected and do not use an attempt | Easy, Classic. Typed `abc` as the first guess. | Invalid message, attempts left stays 10 | First run: attempts left dropped from 10 to 9 because the attempt counter went up before the input was checked. Fix: moved `COUNTER += 1` to after the validation check. After the fix: `Invalid Guess... Attempts left: 10`. | Yes (after fix) |
| 5  | A blank entry is rejected and does not use an attempt | Easy, Classic. Pressed Enter with nothing typed. | Invalid message, attempts left stays 10 | `Invalid Guess... Attempts left: 10` | Yes |
| 6  | A number below the range is rejected | Easy, Classic. Typed `0`. | Invalid message, attempts left stays 10 | `Invalid Guess... Attempts left: 10` | Yes |
| 7  | A number above the range is rejected | Easy, Classic. Typed `51`. | Invalid message, attempts left stays 10 | `Invalid Guess... Attempts left: 10`. After all the invalid entries in rows 4 to 7 plus `-3`, I guessed 42 and the win message said 1 attempt. | Yes |
| 8  | Easy level range and attempt limit | Picked Easy. Typed `51`, then made 10 wrong guesses of `1`. | `51` rejected. The 10th wrong guess shows 0 attempts left and ends the round. | `51` was rejected. The count went from 9 down to 0 and the round ended. | Yes |
| 9  | Medium level range and attempt limit | Picked Medium. Typed `101`, then 8 wrong guesses of `1`. | `101` rejected. Attempts go 7 down to 0 over 8 guesses. | `101` was rejected. The 8th wrong guess showed `Attempts left: 0`. | Yes |
| 10 | Hard level range and attempt limit | Picked Hard. Typed `501`, then `500`. | `501` rejected. `500` accepted and attempts left is 9 (10 allowed). | `501` was rejected. `500` gave `Too high! ... Attempts left: 9`. | Yes |
| 11 | Running out of attempts reveals the number | Medium, Classic. Secret 42. Guessed `1` eight times. | Attempts left 7 down to 0, then the game ends and shows the number | `Sorry, you've used all your attempts. The number was 42.` | Yes |
| 12 | Timeout in Time Challenge reveals the number | Easy, Time Challenge, `TIME_LIMIT = 3`. Guessed 1, waited 4 seconds, then guessed 42 (correct). | Game ends and reveals the number even though the guess was correct | First run: the message said "run out of attempts", which is wrong for a timeout. Fix: changed the timeout message to say time is up. After the fix: `Time's Up, the number was 42.` | Yes (after fix) |
| 13 | Remaining time is shown before each guess | Easy, Time Challenge. Looked at the output before each guess. | `Time Remaining: N seconds` before every prompt | First run: the game asked for guesses forever because an old copy of the guess loop was left in the file. Fix: merged the two loops into one. After the fix: `Time Remaining: 60 seconds` before the first guess and a lower value before later ones. | Yes (after fix) |
| 14 | Classic mode does not show a timer | Easy, Classic. Played a round. | No `Time Remaining` line | No timer lines were printed | Yes |
| 15 | Invalid level and mode choices ask again | At the level menu typed `x`, a blank, and `4`. At the mode menu typed `9` and a blank. | `Please enter a valid level.` or `Please enter a valid mode.`, then the menu again | Each bad entry showed the message and asked again. Typing `1` and `2` then started the round. | Yes |
