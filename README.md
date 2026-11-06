# Mystery Island — The Lost Lighthouse

A beginner-friendly Python terminal adventure game, built in small learning steps.

## Mission

Explore an island, collect rope and a lantern, cross the old bridge, and restore the lighthouse beacon before your energy runs out.

## Current learning milestone

- Ask for a player nickname (blank nicknames use **Explorer**).
- Start with 5 energy points.
- Display a menu in a `while` loop.
- Accept a quit command that safely stops the loop.
- Handle invalid menu choices without crashing.

**Not implemented yet:** exploration, locations, inventory, obstacles, energy consumption, win/loss states, replay and automated tests. The exploration option currently displays a placeholder.

## Run the current lesson

```bash
python3 main.py
```

## Planned locations and items

Locations: Beach, Jungle, Cave, Old Bridge, Lighthouse.

Items: Rope (needed at the bridge), Lantern (needed at the lighthouse).

## Files

- `main.py`: entry point and first interactive menu.
- `game.py`: future game logic.
- `tests/test_game.py`: future tests.

## Learning method

Understand the concept, predict the output, implement one small change, test locally, then commit the progress.
