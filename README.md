# [2][0][4][8]

This is a Python with PyGameCE implementation of the 2048 game.
_For now works in CLI mode only._

I was always curious about video games and how they work behind the scenes, so I decided to build my own implementation of something familiar: the game 2048. While the original is simple in concept, it still offers a surprisingly rich environment for exploration, such as designing core mechanics (e.g. tile movement, merging and scoring) and creating a user-friendly and responsive interface.

## Table of contents

1. [About](#2048)
2. [Table of contents](#table-of-contents)
3. [How to run](#how-to-run)
4. [Usage](#usage)
    - [CLI output example](#cli-output-example)
5. [Contributing](#contributing)
6. [Roadmap](#roadmap)
    - [Logic](#logic)
    - [User Interface](#user-interface)

## How to run

For now UI is not awailable, so to run the app you sinmply need a Python interpreter installed.
Download the `main.py` and `mechanics.py` files in the same folder. Then in your terminal run:

- for Linux/MacOS `python3 main.py`
- for Windows `py main.py`

## Usage

There are 6 types of input to the CLI available:

- `a` - move left
- `d` - move right
- `s` - move down
- `w` - move up
- `u` - undo move (you can undo up to 3 moves in a row)
- any other input will cause exit

Don't forget to press enter after each input

### CLI output example

```text
 | | |
--------
8|4| |
--------
8|4|2|2
--------
4|32|64|
```

## Contributing

1. Clone the repo
2. run `pip install -r requirements.txt` _unnecessary till I make a UI_

## Roadmap

### Logic

1. ✔️ Add sum elements on collision
2. ✔️ Add move left/right
3. ✔️ Add move down/up
4. ✔️ Add CLI controls
5. ✔️ Add "undo" action
6. :x: Add current score counter
7. :x: Add all-time score counter
8. :x: Add tests
9. :x: Refactoring

### User Interface

1. :x: Create a basic window
2. :x: Set a grid size and color
3. :x: Set cell size and probably shape
4. :x: Set font style, size and color for text elements
5. :x: Set colors for:
  a) empty slots
  b) slots filled with 2 - 2048
6. :x: Add a game name title and a table for scores
7. :x: Add start menu
