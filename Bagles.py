import random
import time
import sys
import os

NUM_DIGITS = 3
MAX_GUESSES = 10

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"

def animated_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_animated_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{BOLD}{CYAN}
***********************************************
*        {YELLOW}BAGELS: THE LOGIC GAME 🎲{CYAN}        *
*   Guess the {NUM_DIGITS}-digit secret number!  *
***********************************************{RESET}
"""
    for line in banner.split("\n"):
        animated_text(line, 0.02)
    time.sleep(0.5)

def print_game_instructions():
    instructions = f"""
{BOLD}{WHITE}📝 How to Play:{RESET}
{BOLD}1️⃣{RESET} I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
{BOLD}2️⃣{RESET} Try to guess the number!
{BOLD}3️⃣{RESET} I'll give you clues:
   🟢 {BOLD}Fermi{RESET}  - One digit is correct and in the right position.
   🟡 {BOLD}Pico{RESET}   - One digit is correct but in the wrong position.
   🔴 {BOLD}Bagels{RESET} - No digits are correct.
{BOLD}4️⃣{RESET} Use logic and deduction to crack the code!
"""
    animated_text(instructions, 0.03)
    input(f"{CYAN}Press Enter to start the game...{RESET}")

def print_partitioned_message(message, symbol='*', color=RESET):
    separator = f"{color}{symbol * (len(message) + 4)}{RESET}"
    print(separator)
    print(f"{color}* {message.ljust(len(message) + 2)} *{RESET}")
    print(separator)
    time.sleep(0.5)

def generate_secret_number():
    return ''.join(random.sample('0123456789', NUM_DIGITS))

def get_valid_guess(attempt):
    while True:
        guess = input(f"🔢 {BOLD}Guess #{attempt}:{RESET} ").strip()
        if len(guess) == NUM_DIGITS and guess.isdigit():
            return guess
        print_partitioned_message(f"⚠️ Invalid input! Enter a {NUM_DIGITS}-digit number.", RED)

def generate_clues(guess, secret_number):
    if guess == secret_number:
        return f"🎉 {GREEN}You got it!{RESET}"
    
    clues = [
        "🟢 Fermi" if guess[i] == secret_number[i] else "🟡 Pico"
        for i in range(NUM_DIGITS) if guess[i] in secret_number
    ]
    
    clue_message = ' '.join(sorted(clues)) if clues else "🔴 Bagels"
    animated_text(f"{YELLOW}{clue_message}{RESET}", 0.05)
    return clue_message

def play_again():
    return input(f"{BOLD}🔄 Do you want to play again? (yes or no) > {RESET}").strip().lower().startswith('y')

def console_sfx(sound_type):
    if sound_type == "correct":
        print(f"\n{CYAN}🎶 *Ding* - Correct Guess!{RESET}")
    elif sound_type == "error":
        print(f"\n{RED}💥 *Error* - Invalid Guess!{RESET}")
    elif sound_type == "game_over":
        print(f"\n{MAGENTA}💔 *Game Over* - Better luck next time!{RESET}")
    time.sleep(0.5)

def main():
    print_animated_banner()
    print_game_instructions()
    
    while True:
        secret_number = generate_secret_number()
        print_partitioned_message(f"🤔 I have thought of a number.\nYou have {MAX_GUESSES} guesses!", CYAN)

        for attempt in range(1, MAX_GUESSES + 1):
            guess = get_valid_guess(attempt)
            clues = generate_clues(guess, secret_number)

            if guess == secret_number:
                console_sfx("correct")
                print_partitioned_message(f"🎉 {GREEN}Congratulations! You guessed the number {secret_number}!{RESET}", GREEN)
                break
            elif attempt == MAX_GUESSES:
                console_sfx("game_over")
                print_partitioned_message(f"❌ {RED}You ran out of guesses. The correct number was {secret_number}.{RESET}", RED)
        else:
            console_sfx("error")
        
        if not play_again():
            print_partitioned_message("🎮 Thanks for playing! Goodbye! 👋", BLUE)
            break

if __name__ == '__main__':
    main()