
# Mystery Island — The Lost Lighthouse

A beginner-friendly Python 3 terminal adventure game built step by step while learning Python programming.

## Mission

You are an explorer stranded on a mysterious island. Your mission is to explore the island, collect useful items, overcome obstacles, manage your energy, and restore the lost lighthouse beacon before your energy runs out.

## Game Features

- Enter a player nickname (defaults to `Explorer` if left blank).
- Start each adventure with 5 energy points.
- Explore five locations:
  - Beach
  - Jungle
  - Cave
  - Old Bridge
  - Lighthouse
- Collect fruit at the Beach.
- Collect a rope in the Jungle.
- Collect a lantern in the Cave.
- Eat fruit to restore 2 energy points.
- Maximum energy is limited to 5 points.
- Fruit is not consumed when energy is already full.
- Use the rope to cross the broken bridge.
- Use the lantern to restore the lighthouse beacon.
- Manage energy while exploring.
- Return to previously visited locations without losing energy.
- Prevent duplicate item collection.
- Handle invalid menu choices.
- Win by restoring the lighthouse beacon.
- Lose when energy runs out.
- Quit and replay with a fresh adventure.

## Requirements

- Python 3 installed.
- A terminal or command-line application.

No external Python packages are required to run the game.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/ejembiedwin36-oss/mystery-island.git
   ```

2. Enter the project directory:

   ```bash
   cd mystery-island
   ```

3. Start the game:

   ```bash
   python3 main.py
   ```

## How to Play

Choose an option from the game menu:

| Option | Action |
|---|---|
| 1 | Explore |
| 2 | Quit |
| 3 | Collect an item |
| 4 | Go back |
| 5 | Restore the beacon |
| 6 | Eat fruit to restore energy |

### Game Rules

- Exploring forward costs 1 energy point.
- Moving backward does not cost energy.
- The player starts with 5 energy points.
- Eating fruit restores 2 energy points.
- Energy cannot exceed the maximum of 5 points.
- Fruit can only be collected once.
- Fruit is removed from the inventory after successful eating.
- The player cannot eat fruit without having it.
- The player must collect a rope to cross the broken bridge.
- The player must collect a lantern to restore the lighthouse beacon.
- The adventure ends when the player wins, runs out of energy, or quits.

Collect the required items and reach the Lighthouse to complete your mission!

## Automated Tests

The project includes automated tests using Python's built-in `unittest` framework.

Run all tests from the project directory:

```bash
python3 -m unittest discover -s tests -v
```

The 16 automated tests cover:

1. Moving from the Beach to the Jungle.
2. Collecting the rope.
3. Preventing duplicate rope collection.
4. Collecting the lantern.
5. Collecting fruit.
6. Preventing duplicate fruit collection.
7. Eating fruit and restoring energy.
8. Preventing eating without fruit.
9. Preventing fruit consumption when energy is full.
10. Preventing bridge crossing without a rope.
11. Crossing the bridge with a rope.
12. Requiring a lantern to restore the lighthouse beacon.
13. Winning by restoring the lighthouse beacon.
14. Returning from the Lighthouse.
15. Returning to the Beach.
16. Quitting the game.

All tests are written using Python's built-in `unittest` framework.

## Project Structure

```text
mystery-island/
├── main.py
├── tests/
│   └── test_game.py
└── README.md
```

- `main.py` — Contains the game logic and program entry point.
- `tests/test_game.py` — Contains automated tests for the game.
- `README.md` — Project documentation and instructions.

## Learning Method

This project follows a practical learning approach:

1. Understand a programming concept.
2. Predict what the code will do.
3. Implement one small change.
4. Run the program.
5. Test the result.
6. Commit completed progress to GitHub.

The goal is not just to build a game, but to understand the Python concepts behind every feature.
