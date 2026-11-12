
"""Automated tests for Mystery Island."""

import unittest
from unittest.mock import patch
from io import StringIO

from main import play_game


class TestMysteryIsland(unittest.TestCase):

    def test_quit_game(self):
        # Simulate a player entering a name and choosing Quit.
        with patch("builtins.input", side_effect=["Edwin", "2"]):

            # Capture the text the game prints.
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        # Check that the game displayed the goodbye message.
        self.assertIn("Goodbye, Edwin!", output.getvalue())

    def test_beach_to_jungle(self):
        # ARRANGE: Enter a nickname, explore, then quit.
        answers = ["Edwin", "1", "2"]

        with patch("builtins.input", side_effect=answers):

            # ACT: Capture the output of one adventure.
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        # ASSERT: Confirm movement and energy reduction.
        game_output = output.getvalue()

        self.assertIn("You have entered the Jungle!", game_output)
        self.assertIn("Location: Jungle", game_output)
        self.assertIn("Energy: 4", game_output)


    def test_collect_rope(self):
        # ARRANGE: Move to the Jungle, collect the rope, then quit.
        answers = ["Edwin", "1", "3", "2"]

        with patch("builtins.input", side_effect=answers):

            # ACT: Run the game and capture its output.
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        # ASSERT: Verify that the rope was collected.
        game_output = output.getvalue()

        self.assertIn("You collected a rope!", game_output)
        self.assertIn("Inventory: ['rope']", game_output)


    def test_duplicate_rope(self):
        # ARRANGE: Move to Jungle and attempt rope collection twice.
        answers = ["Edwin", "1", "3", "3", "2"]

        with patch("builtins.input", side_effect=answers):

            # ACT: Run the game and capture its output.
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        # ASSERT: Check that the rope was collected once.
        game_output = output.getvalue()

        self.assertIn("You collected a rope!", game_output)
        self.assertIn("You already have a rope!", game_output)
        self.assertIn("Inventory: ['rope']", game_output)
        self.assertNotIn("Inventory: ['rope', 'rope']", game_output)


    def test_collect_lantern(self):
        answers = ["Edwin", "1", "1", "3", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()
            game_output = output.getvalue()
            self.assertIn("You collected a lantern!", game_output)
            self.assertIn("Inventory: ['lantern']", game_output)


    def test_bridge_requires_rope(self):
        answers = ["Edwin", "1", "1", "1", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You need a rope to cross the bridge!", game_output)
        self.assertIn("Location: Cave", game_output)

    def test_cross_bridge_with_rope(self):
        answers = ["Edwin", "1", "3", "1", "1", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()
        game_output = output.getvalue()
        self.assertIn("You used your rope to cross the broken bridge!", game_output)
        self.assertIn("Location: Old Bridge", game_output)

    def test_lighthouse_victory(self):
        answers = ["Edwin", "1", "3", "1", "3", "1", "1", "5"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("Congratulations! You restored the lighthouse beacon!", game_output)
        self.assertIn("You won the game, Edwin!", game_output)

    def test_lighthouse_requires_lantern(self):
        answers = ["Edwin", "1", "3", "1", "1", "1", "5", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()


        self.assertIn("You need a lantern to restore the beacon!", game_output)
        self.assertNotIn("Congratulations! You restored the lighthouse beacon!", game_output)


    def test_return_from_lighthouse(self):
        answers = ["Edwin", "1", "3", "1", "1", "1", "4", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You returned to the Old Bridge!", game_output)
        self.assertIn("Location: Old Bridge", game_output)


    def test_return_to_beach(self):
        answers = ["Edwin", "1", "1", "4", "4", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You returned to the Jungle!", game_output)
        self.assertIn("You returned to the Beach!", game_output)
        self.assertIn("Location: Beach", game_output)


if __name__ == "__main__":
    unittest.main()
