# 🐍 CodeAlpha Python Programming Internship

This repository contains my project submissions for the **CodeAlpha Python Programming Internship**. Each task is implemented as a standalone, beginner-friendly Python script with clear scope, no external dependencies, and console-based input/output.

---

## 📂 Repository Structure

```
codealpha-python-internship/
├── stock_portfolio_tracker/
│   ├── stock_tracker.py
│   └── README.md
├── hangman_game/
│   ├── hangman.py
│   └── README.md
├── .gitignore
└── README.md          # (this file)
```

> Each project folder also contains its own README with project-specific details, but this top-level README gives an overview of the full repo.

---

## 📋 Projects Overview

| # | Project                  | Description                                                                 | Key Concepts                                              |
|---|---------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------|
| 1 | [Stock Portfolio Tracker](#-1-stock-portfolio-tracker) | Calculates total investment value from user-entered stocks and quantities.    | Dictionaries, Input/Output, Basic Arithmetic, File Handling  |
| 2 | [Hangman Game](#-2-hangman-game)             | A classic word-guessing game with a limited number of incorrect attempts.      | `random`, `while` loops, `if-else`, Strings, Lists           |

---

## 📊 1. Stock Portfolio Tracker

A command-line tool that tracks a simple stock portfolio using hardcoded stock prices, calculates the total investment value, and optionally saves the summary to a file.

**Run it:**
```bash
cd stock_portfolio_tracker
python stock_tracker.py
```

**Highlights:**
- User inputs stock names and quantities
- Prices are stored in a hardcoded dictionary (e.g. `{"AAPL": 180, "TSLA": 250}`)
- Calculates and displays total investment value
- Optionally exports results to a `.txt` file

📄 See [`stock_portfolio_tracker/README.md`](./stock_portfolio_tracker/README.md) for full details, usage examples, and enhancement ideas.

---

## 🎮 2. Hangman Game

A simple text-based Hangman game where the player guesses a hidden word one letter at a time, with a limited number of incorrect guesses allowed.

**Run it:**
```bash
cd hangman_game
python hangman.py
```

**Highlights:**
- Randomly selects a word from a predefined 5-word list
- Limits players to 6 incorrect guesses
- Tracks guessed letters and displays word progress
- Supports replaying multiple rounds

📄 See [`hangman_game/README.md`](./hangman_game/README.md) for full details, usage examples, and enhancement ideas.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external libraries required — both projects use only the Python standard library

### Clone the Repository
```bash
git clone <your-repo-url>
cd codealpha-python-internship
```

### Run Any Project
Navigate into the relevant project folder and run its script:
```bash
cd stock_portfolio_tracker
python stock_tracker.py
```
or
```bash
cd hangman_game
python hangman.py
```

---

## 🧠 Skills Demonstrated

Across both projects, this repository demonstrates:
- Working with **dictionaries** and **lists** to store structured data
- **Input validation** and handling user errors gracefully
- **Control flow** with `while` loops and `if-else` conditionals
- **File handling** (reading/writing `.txt` output)
- Writing **clean, modular, well-documented** Python code with functions

---

## 📝 License

This repository is created for educational purposes as part of the CodeAlpha internship program.

---

## 🙌 Acknowledgements

Developed as part of **CodeAlpha's Python Programming Internship — Module 1**.
