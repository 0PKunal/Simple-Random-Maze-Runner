Got it ✅ You want a **clean README.md** for your project *Simple Random Maze Runner*.
Since you have only the `.py` source and `.exe` build, and it’s MIT licensed, I’ll include:

* Project title + description
* Features
* Controls
* Screenshots placeholder
* How to run (Python & EXE)
* Build instructions (PyInstaller for Windows/Linux)
* License

Here’s the **README.md code** 👇

```markdown
# 🌀 Simple Random Maze Runner

A simple maze game built with **Python** and **Pygame**, where the player navigates through a randomly generated maze to reach the exit.  
Each play generates a new maze, making every run unique!

---

## 🎮 Features
- Randomly generated maze every game
- Smooth box movement (Arrow keys or WASD)
- Start (blue) and End (red) points
- Win screen with **time taken**
- Restart shortcut: **Ctrl + R**
- Standalone **Windows .exe** build (no Python needed)
- MIT Licensed (free to use & modify)

---

## 🕹️ Controls
- **Move**: Arrow Keys ⬆️⬇️⬅️➡️ or **WASD**
- **Restart**: `Ctrl + R`
- **Quit**: Close window (or `Alt+F4`)

---

## 📷 Screenshot
*(Add your screenshot here, e.g. `![Maze Screenshot](screenshot.png)`)*
```

---

## ▶️ Run the Game

### Option 1: Run the `.exe` (Windows)

1. Download the pre-built `maze_game.exe` from the `dist/` folder (or release page if available).
2. Double-click it to play — no Python or Pygame required!

### Option 2: Run from Python (Cross-platform)

1. Install [Python 3](https://www.python.org/downloads/)
2. Install Pygame:

   ```bash
   pip install pygame
   ```
3. Run the script:

   ```bash
   python maze_game.py
   ```

---

## ⚙️ Build Instructions

### Windows (.exe)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed maze_game.py
```

Output: `dist/maze_game.exe`

### Linux (binary)

```bash
pip install pyinstaller
pyinstaller --onefile maze_game.py
```

Output: `dist/maze_game`
(make it executable with `chmod +x dist/maze_game`)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
You are free to use, modify, and distribute this game.