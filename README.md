# 🧠 DON: Destroyer of Numbers 

---

## 📜 Overview

**DON: Destroyer of Numbers** is a strategic and luck-based text game where players embody the hero "DON", champion of the letter-kind, on a mission to eliminate evil numbers. Armed only with logic, bravery, and a dynamic life score, DON must make critical choices in each of his 20 encounters.

---

## 🎮 Gameplay Guide

- You play as **DON**, starting with a random **life score (1-50)**.
- In **20 attempts**, you face 5 random enemy numbers in each round.
- Select a number:
  - ✅ If it’s **≤ life score**: you defeat the number, and its value is added to your life score.
  - ❌ If it’s **> life score**: you’re defeated, and the game ends.
- Invalid input (e.g., not in the given list, letters, or empty input) also ends the game.
- Win by surviving all 20 rounds!

---

## 📊 Value Ranges per Attempt

| Attempt No | Enemy Number Range     |
|------------|-------------------------|
| 1 - 5      | 15 – 100                |
| 6 - 10     | 250 – 2000              |
| 11 - 15    | 3000 – 10,000           |
| 16 - 20    | 20,000 – 100,000        |

---

## 🔧 Technologies Used

- **Python 3.x**
- `random` – for dynamic enemy generation and life score
- `datetime` – for timestamping logs
- File handling and user input validation

---

## 🚀 How to Play

1. Run the main script:
   ```bash
   python main.py
---

## 🏁

This game is not just about numbers—it's about making bold decisions, managing risk, and protecting the letter-kind from numerical doom. With randomized challenges and progressive difficulty, DON: Destroyer of Numbers offers an engaging way to test both logic and luck!
