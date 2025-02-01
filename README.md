# Bagels: The Logic Game 🎲

## Description
Bagels is a number-guessing logic game where players must deduce a secret three-digit number based on clues provided after each guess. The game ensures an engaging console experience with animations and color-coded hints.

## How to Play
1. The game will generate a secret 3-digit number without repeating digits.
2. Players have 10 attempts to guess the correct number.
3. After each guess, clues will be provided:
   - 🟢 **Fermi**: A digit is correct and positioned correctly.
   - 🟡 **Pico**: A digit is correct but in the wrong position.
   - 🔴 **Bagels**: No digits are correct.
4. Use logic and deduction to guess the correct number within the allowed attempts.
5. If you guess the number correctly, you win! Otherwise, the correct answer is revealed after 10 failed attempts.
6. Players can choose to play again or exit the game.

## Features
- Smooth animated text output for better user experience.
- Randomly generated secret numbers with no duplicate digits.
- Color-coded feedback for easy readability.
- Input validation to ensure only valid guesses are accepted.
- Console sound effects simulated through text messages.
- Play-again option after game completion.

## Installation & Usage
1. Ensure you have Python installed (version 3.x recommended).
2. Download or clone the script.
3. Open a terminal or command prompt and navigate to the script directory.
4. Run the script using:
   ```sh
   python bagels.py
   ```

## Dependencies
- Standard Python libraries: `random`, `time`, `sys`, `os`.
- No external dependencies are required.

## Customization
- Change `NUM_DIGITS` to modify the number of digits in the secret number.
- Adjust `MAX_GUESSES` to increase or decrease the number of attempts.
- Modify the colour codes and animations for a personalized console experience.

## License
This project is open-source and can be modified or distributed freely.

## Author
Developed by [Abhimanyu Banerjee].

