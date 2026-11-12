
"""Mystery Island — The Lost Lighthouse.

A terminal-based adventure game where the player explores
an island, collects useful items, manages energy, and
attempts to restore the lighthouse beacon.
"""


def play_game():
    # STEP 1: Ask the player to enter a nickname.
    name = input("Enter your nickname: ").strip()

    # Use a default name if the player enters nothing.
    if not name:
        name = "Explorer"

    # STEP 2: Set up the player's starting game state.
    energy = 5
    location = "Beach"
    inventory = []
    running = True

    # Display the welcome message and the player's mission.
    print(f"\nWelcome to Mystery Island, {name}!")
    print("Your mission is to restore the lost lighthouse beacon.")

    # STEP 3: Start the main game loop.
    while running:

        # Show the player's current game state.
        print(f"\nLocation: {location}")
        print(f"Energy: {energy}")
        print(f"Inventory: {inventory}")

        # Display the available menu options.
        print("1. Explore")
        print("2. Quit")
        print("3. Collect item")
        print("4. Go back")
        print("5. Restore beacon")
        print("6. Eat fruit")

        # Ask the player what they want to do.
        choice = input("Choose 1, 2, 3, 4, 5 or 6: ").strip()

        # OPTION 1: EXPLORE THE ISLAND
        if choice == "1":

            if location == "Beach":
                location = "Jungle"
                energy -= 1
                print("You have entered the Jungle!")

            elif location == "Jungle":
                location = "Cave"
                energy -= 1
                print("You have entered the Cave!")

            elif location == "Cave":
                if "rope" in inventory:
                    location = "Old Bridge"
                    energy -= 1
                    print("You used your rope to cross the broken bridge!")
                else:
                    print("You need a rope to cross the bridge!")

            elif location == "Old Bridge":
                location = "Lighthouse"
                energy -= 1
                print("You have reached the Lighthouse!")

            else:
                print("There is nowhere new to explore yet.")

            # Check whether the player has run out of energy.
            if energy <= 0:
                print("Game Over! You have run out of energy.")
                running = False

        # OPTION 2: QUIT THE GAME
        elif choice == "2":
            print(f"Goodbye, {name}!")
            running = False

        # OPTION 3: COLLECT ITEMS
        elif choice == "3":

            # Fruit can only be collected at the Beach.
            if location == "Beach":
                if "fruit" not in inventory:
                    inventory.append("fruit")
                    print("You collected some fruit!")
                else:
                    print("You already have fruit!")

            # The rope can only be collected in the Jungle.
            elif location == "Jungle":
                if "rope" not in inventory:
                    inventory.append("rope")
                    print("You collected a rope!")
                else:
                    print("You already have a rope!")

            # The lantern can only be collected in the Cave.
            elif location == "Cave":
                if "lantern" not in inventory:
                    inventory.append("lantern")
                    print("You collected a lantern!")
                else:
                    print("You already have a lantern!")

            else:
                print("There is nothing to collect here.")

        # OPTION 4: GO BACK
        elif choice == "4":

            if location == "Cave":
                location = "Jungle"
                print("You returned to the Jungle!")

            elif location == "Jungle":
                location = "Beach"
                print("You returned to the Beach!")

            elif location == "Old Bridge":
                location = "Cave"
                print("You returned to the Cave!")

            elif location == "Lighthouse":
                location = "Old Bridge"
                print("You returned to the Old Bridge!")

            else:
                print("You cannot go back from here yet.")

        # OPTION 5: RESTORE THE LIGHTHOUSE BEACON
        elif choice == "5":

            if location == "Lighthouse":
                if "lantern" in inventory:
                    print("Congratulations! You restored the lighthouse beacon!")
                    print(f"You won the game, {name}!")
                    running = False
                else:
                    print("You need a lantern to restore the beacon!")

            else:
                print("You must reach the Lighthouse first!")

        # OPTION 6: EAT FRUIT
        elif choice == "6":

            # First, check whether the player has fruit.
            if "fruit" in inventory:

                # Check whether the player needs more energy.
                if energy < 5:

                    # Restore 2 energy points.
                    energy += 2

                    # Never allow energy to exceed 5.
                    if energy > 5:
                        energy = 5

                    # Remove fruit after successful eating.
                    inventory.remove("fruit")

                    print("You ate the fruit and restored your energy!")

                else:
                    print("Your energy is already full!")

            else:
                print("You don't have any fruit to eat!")

        # HANDLE INVALID USER INPUT
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5 or 6.")


# Start the program only when this file is run directly.
def main():
    while True:
        play_game()

        answer = input("\nPlay again? (yes/no): ").strip().lower()

        while answer not in ["yes", "no"]:
            print("Please enter yes or no.")
            answer = input("Play again? (yes/no): ").strip().lower()

        if answer == "no":
            print("Thanks for playing Mystery Island!")
            break


if __name__ == "__main__":
    main()
