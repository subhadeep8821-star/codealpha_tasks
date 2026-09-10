# 🎮 Hangman Game

A simple text-based Hangman game built in Python, where the player guesses a hidden word one letter at a time before running out of attempts.

Built as part of **CodeAlpha Python Programming Internship — Task 5**.

---

## ✨ Features

- 🎲 Randomly selects a word from a predefined list each round
- ⌨️ Simple console-based input/output — no graphics or audio required
- ❌ Limits the player to 6 incorrect guesses
- 🔁 Tracks and displays previously guessed letters
- ✅ Input validation (rejects non-letters and duplicate guesses)
- 🔄 Option to play multiple rounds without restarting the script

---

## 🧠 Key Concepts Used

| Concept     | Usage in Project                                              |
|-------------|-----------------------------------------------------------------|
| `random`    | Selecting a random word from the predefined word list           |
| `while` loop| Driving the guessing loop until the game is won or lost          |
| `if-else`   | Checking correct/incorrect guesses and win/loss conditions       |
| Strings     | Building the masked word display (e.g. `_ y t h _ n`)            |
| Lists       | Storing the predefined word list                                 |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation
\`\`\`bash
git clone <your-repo-url>
cd hangman-game
\`\`\`

No external dependencies are required — the project uses only Python's standard library.

### Running the Program
\`\`\`bash
python hangman.py
\`\`\`

---

## 🖥️ Usage

1. Run the script — a random word is chosen from the predefined list.
2. The word length and number of allowed incorrect guesses are shown.
3. Enter one letter at a time when prompted.
4. Correct guesses reveal the letter's position(s) in the word.
5. Incorrect guesses reduce your remaining attempts.
6. Win by guessing the full word before running out of attempts.
7. Choose to play again or exit at the end of each round.

### Example Session
\`\`\`
=== Welcome to Hangman! ===
The word has 6 letters. You have 6 incorrect guesses allowed.

Word: _ _ _ _ _ _
Guessed letters: None
Attempts left: 6

Guess a letter: p
Good guess! 'p' is in the word.

Word: p _ _ _ _ _
Guessed letters: p
Attempts left: 6

Guess a letter: z
Wrong guess! 'z' is not in the word.
...
🎉 Congratulations! You guessed the word: 'python'
\`\`\`

---

## 📚 Word List

The game currently selects from 5 predefined words:

\`\`\`python
WORDS = ["python", "hangman", "computer", "keyboard", "internet"]
\`\`\`

> 💡 To customize the game, simply edit the \`WORDS\` list in \`hangman.py\`.

---

## 📁 Project Structure

\`\`\`
hangman-game/
├── hangman.py       # Main game script
└── README.md        # Project documentation
\`\`\`

---

## 🔧 Possible Enhancements

- [ ] Add ASCII art for the hangman figure at each incorrect guess
- [ ] Support word categories (animals, countries, tech terms, etc.)
- [ ] Load words from an external file instead of a hardcoded list
- [ ] Add a scoring system across multiple rounds
- [ ] Build a GUI version using Tkinter

---

## 📝 License

This project is created for educational purposes as part of the CodeAlpha internship program.

---

## 🙌 Acknowledgements

Developed as part of **CodeAlpha's Python Programming Internship — Module 1, Task 5**.