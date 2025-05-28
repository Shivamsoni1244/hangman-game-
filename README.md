# Hangman Game (Terminal Version)

Welcome to the **Hangman Game Generator** — a fun, classic word guessing game made with Python!

---

## Game Objective

You have to guess the hidden word **one letter at a time**. If you guess wrong, the hangman gets drawn piece by piece.

Guess the full word **before the drawing completes**, or you lose!

---

##  How to Play

- You'll be shown blank spaces like: `_ _ _ _`
- Type a letter and press Enter.
- If the letter is correct:
  - It's revealed in the word.
- If the letter is wrong:
  - A part of the hangman is drawn.
- You have **6 lives** in total.
- Already guessed letters will be tracked, and repeated guesses will be notified.

---

## Features

- Random word selection from a predefined list.
- ASCII art to show hangman stages.
- Clear message for each guess (correct, wrong, or already guessed).
- Game ends with a win or loss message and reveals the word.

---

## How to Run

1. Make sure Python is installed (Python 3+ recommended).
2. Save the code in a file named `hangman.py`.
3. Open your terminal or command prompt.
4. Run the file with:
   ```bash
   python hangman.py
