# Disappearing Text Writing App

A minimalist, anxiety-driven writing tool inspired by "The Most Dangerous Writing App".

**If you stop typing for more than 5 seconds → everything you've written disappears.**

Perfect for beating procrastination, freewriting, or forcing yourself to keep the words flowing.

## Features

- Clean, distraction-free writing interface (Tkinter)
- Text **vanishes completely** if you pause typing for > 5 seconds
- Real-time typing detection using key press events
- **Save** button to keep your text when you're happy with it
- Simple, dark-themed look (easy to customize)

## How It Works

- Every time you press a key → timer resets
- A background check runs every ~0.5 seconds
- If more than 5 seconds have passed since last keypress → text is deleted
- Click "Save" → text is saved to a timestamped `.txt` file

## Requirements

Only built-in Python modules:

- `tkinter`
- `time`
- `datetime` (for filename timestamps)

→ Works out of the box on any Python 3 installation (no pip install needed)

## How to Run

1. Clone or download the repository:

```bash
git clone https://github.com/YOUR-USERNAME/disappearing-text-app.git
cd disappearing-text-app
