"""
Hangman Game
------------
A simple text-based Hangman game where the player guesses a word
one letter at a time.

Simplified Scope:
- Uses a small list of 5 predefined words
- Limits incorrect guesses to 6
- Basic console input/output only

Key Concepts Used: random, while loop, if-else, strings, lists
"""

import random

# Predefined list of words
WORDS = ["python", "hangman", "computer", "keyboard", "internet"]

MAX_ATTEMPTS = 6


def choose_word():
    """Randomly select a word from the predefined list."""
    return random.choice(WORDS)


def display_state(word, guessed_letters, attempts_left):
    """Display the current word progress, guessed letters, and attempts left."""
    display_word = " ".join(
        [letter if letter in guessed_letters else "_" for letter in word]
    )
    print("\nWord: " + display_word)
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Attempts left: {attempts_left}")


def get_guess(guessed_letters):
    """Prompt the user for a single valid letter guess."""
    while True:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        return guess


def play_game():
    """Run a single round of Hangman."""
    word = choose_word()
    guessed_letters = set()
    attempts_left = MAX_ATTEMPTS

    print("=== Welcome to Hangman! ===")
    print(f"The word has {len(word)} letters. You have {MAX_ATTEMPTS} incorrect guesses allowed.")

    while attempts_left > 0:
        display_state(word, guessed_letters, attempts_left)

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You guessed the word: '{word}'")
            return

    # Loss condition
    print(f"\n💀 Game over! You've run out of attempts. The word was: '{word}'")


def main():
    """Run the Hangman game, allowing the player to replay."""
    while True:
        play_game()

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()