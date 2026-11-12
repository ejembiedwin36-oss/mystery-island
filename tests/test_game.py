
"""Automated tests for Mystery Island."""

import unittest
from unittest.mock import patch
from io import StringIO

from main import play_game


class TestMysteryIsland(unittest.TestCase):

    def test_quit_game(self):
        answers = ["Edwin", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        self.assertIn("Goodbye, Edwin!", output.getvalue())

    def test_beach_to_jungle(self):
        answers = ["Edwin", "1", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You have reached Jungle!", game_output)
        self.assertIn("LOCATION: JUNGLE", game_output)
        self.assertIn("ENERGY: 4/5", game_output)

    def test_collect_rope(self):
        answers = ["Edwin", "1", "3", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You collected rope!", game_output)
        self.assertIn("INVENTORY: rope", game_output)

    def test_duplicate_rope(self):
        answers = ["Edwin", "1", "3", "3", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You collected rope!", game_output)
        self.assertIn("You already have rope!", game_output)
        self.assertIn("INVENTORY: rope", game_output)
        self.assertNotIn("INVENTORY: rope, rope", game_output)

    def test_collect_lantern(self):
        answers = ["Edwin", "1", "1", "3", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You collected lantern!", game_output)
        self.assertIn("INVENTORY: lantern", game_output)

    def test_bridge_requires_rope(self):
        answers = ["Edwin", "1", "1", "1", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn(
            "You cannot cross the broken bridge without a rope.",
            game_output
        )
        self.assertIn("LOCATION: CAVE", game_output)

    def test_cross_bridge_with_rope(self):
        answers = ["Edwin", "1", "3", "1", "1", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn(
            "You used your rope to cross the broken bridge!",
            game_output
        )
        self.assertIn("LOCATION: OLD BRIDGE", game_output)

    def test_lighthouse_victory(self):
        answers = ["Edwin", "1", "3", "1", "3", "1", "1", "5"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("MISSION COMPLETED!", game_output)
        self.assertIn(
            "You have restored the lighthouse beacon!",
            game_output
        )
        self.assertIn("Congratulations, Edwin!", game_output)
        self.assertIn("You are the hero of Mystery Island!", game_output)

    def test_lighthouse_requires_lantern(self):
        answers = ["Edwin", "1", "3", "1", "1", "1", "5", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn(
            "You need a lantern to restore the beacon!",
            game_output
        )
        self.assertNotIn("MISSION COMPLETED!", game_output)

    def test_return_from_lighthouse(self):
        answers = ["Edwin", "1", "3", "1", "1", "1", "4", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You returned to the Old Bridge!", game_output)
        self.assertIn("LOCATION: OLD BRIDGE", game_output)

    def test_return_to_beach(self):
        answers = ["Edwin", "1", "1", "4", "4", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You returned to the Jungle!", game_output)
        self.assertIn("You returned to the Beach!", game_output)
        self.assertIn("LOCATION: BEACH", game_output)

    def test_collect_fruit(self):
        answers = ["Edwin", "3", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You collected fruit!", game_output)
        self.assertIn("INVENTORY: fruit", game_output)

    def test_duplicate_fruit(self):
        answers = ["Edwin", "3", "3", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You collected fruit!", game_output)
        self.assertIn("You already have fruit!", game_output)
        self.assertIn("INVENTORY: fruit", game_output)
        self.assertNotIn("INVENTORY: fruit, fruit", game_output)

    def test_eat_fruit_restores_energy(self):
        answers = ["Edwin", "3", "1", "6", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("You ate the fruit!", game_output)
        self.assertIn("You restored some energy.", game_output)
        self.assertIn("ENERGY: 4/5", game_output)
        self.assertIn("ENERGY: 5/5", game_output)
        self.assertIn("INVENTORY: Empty", game_output)

    def test_cannot_eat_without_fruit(self):
        answers = ["Edwin", "6", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn(
            "You don't have any fruit to eat!",
            game_output
        )
        self.assertIn("ENERGY: 5/5", game_output)

    def test_full_energy_does_not_consume_fruit(self):
        answers = ["Edwin", "3", "6", "2"]

        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=StringIO) as output:
                play_game()

        game_output = output.getvalue()

        self.assertIn("Your energy is already full!", game_output)
        self.assertIn("ENERGY: 5/5", game_output)
        self.assertIn("INVENTORY: fruit", game_output)


if __name__ == "__main__":
    unittest.main()
