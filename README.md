# Mystery Island — The Lost Lighthouse

A beginner-friendly Python 3 terminal adventure game built while learning Python programming.

## The Story

You are an explorer stranded on a mysterious island.

The lighthouse that once guided ships safely through the sea has gone dark. Without its light, ships are in danger.

Your mission is to explore the island, collect useful items, overcome obstacles, manage your energy, and restore the lighthouse beacon before your energy runs out.

## Game Features

- Introduction explaining the story, mission, and how to play.
- Player nickname (defaults to `Explorer` if left blank).
- Five explorable locations:
  - Beach
  - Jungle
  - Cave
  - Old Bridge
  - Lighthouse
- Descriptions of each location.
- Starting energy of 5 points.
- Energy warnings when energy becomes low.
- Fruit collection and energy recovery.
- Maximum energy limit of 5 points.
- Rope collection to cross the broken bridge.
- Lantern collection to restore the lighthouse beacon.
- Inventory management with duplicate collection prevention.
- Forward and backward movement.
- Six clearly explained menu options.
- Victory and game-over messages.
- Option to replay with a fresh adventure.
- Automated tests using Python's built-in `unittest` framework.

## Requirements

- Python 3 installed.
- A terminal or command-line application.

No external Python packages are required.

## How to Run

Clone the repository:

```bash
git clone https://github.com/ejembiedwin36-oss/mystery-island.git
```

Enter the project directory:

```bash
cd mystery-island
```

Start the game:

```bash
python3 main.py
```

## How to Play

When the game starts, read the introduction and enter your nickname.

Choose an option from the menu:

| Option | Action |
|---|---|
| 1 | Explore the island |
| 2 | Quit the game |
| 3 | Collect an item |
| 4 | Go back |
| 5 | Restore the lighthouse beacon |
| 6 | Eat fruit to restore energy |

## Game Rules

- You begin with 5 energy points.
- Exploring forward costs 1 energy point.
- Moving backward does not cost energy.
- Collect fruit at the Beach.
- Eating fruit restores 2 energy points.
- Energy cannot exceed 5 points.
- Fruit is consumed only when successfully eaten.
- You cannot eat fruit without collecting it.
- You need a rope to cross the broken bridge.
- You need a lantern to restore the lighthouse beacon.
- You can collect each available item only once.
- The adventure ends when you win, run out of energy, or quit.

## Automated Tests

The project uses Python's built-in `unittest` framework.

Run all tests:

```bash
python3 -m unittest discover -s tests -v
```

The 16 automated tests cover:

1. Quitting the game.
2. Moving from the Beach to the Jungle.
3. Collecting the rope.
4. Preventing duplicate rope collection.
5. Collecting the lantern.
6. Requiring a rope to cross the bridge.
7. Crossing the bridge with a rope.
8. Winning the lighthouse mission.
9. Requiring a lantern to restore the beacon.
10. Returning from the Lighthouse.
11. Returning to the Beach.
12. Collecting fruit.
13. Preventing duplicate fruit collection.
14. Eating fruit and restoring energy.
15. Preventing eating without fruit.
16. Preventing fruit consumption when energy is full.

## Project Structure

```text
mystery-island/
├── main.py
├── game.py
├── tests/
│   └── test_game.py
└── README.md
```

### Main Files

- `main.py` — Displays the introduction, starts the game, and manages replay.
- `game.py` — Contains the gameplay functions, movement, inventory, energy management, and victory conditions.
- `tests/test_game.py` — Contains the 16 automated tests.
- `README.md` — Project documentation and instructions.

## Learning Method

This project follows a practical learning approach:

1. Understand a programming concept.
2. Predict what the code will do.
3. Implement a change.
4. Run the program.
5. Test the result.
6. Review and commit completed progress to GitHub.

The goal is not just to build a game, but to understand the Python concepts behind every feature.