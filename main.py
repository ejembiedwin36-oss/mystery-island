
"""Mystery Island — The Lost Lighthouse.

A terminal-based adventure game where the player explores
an island, collects useful items, manages energy, and
attempts to restore the lighthouse beacon.
"""


def play_game():
    # STEP 1: Ask the player to enter a nickname.
    # strip() removes extra spaces before and after the name.
    name = input("Enter your nickname: ").strip()

    # Use a default name if the player enters nothing.
    if not name:
        name = "Explorer"

    # STEP 2: Set up the player's starting game state.
    energy = 5               # The player starts with 5 energy points.
    location = "Beach"       # Every adventure begins at the Beach.
    inventory = []           # An empty list stores collected items.
    running = True           # Controls whether the game continues.

    # Display the welcome message and the player's mission.
    print(f"\nWelcome to Mystery Island, {name}!")
    print("Your mission is to restore the lost lighthouse beacon.")

    # STEP 3: Start the main game loop.
    # The loop continues while running is True.
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

        # Ask the player what they want to do.
        choice = input("Choose 1, 2, 3, 4 or 5: ").strip()

        # OPTION 1: EXPLORE THE ISLAND
        # Move forward based on the player's current location.
        if choice == "1":

            # Move from Beach to Jungle.
            if location == "Beach":
                location = "Jungle"
                energy -= 1
                print("You have entered the Jungle!")

            # Move from Jungle to Cave.
            elif location == "Jungle":
                location = "Cave"
                energy -= 1
                print("You have entered the Cave!")

            # The player needs rope to cross the Old Bridge.
            elif location == "Cave":

                # Check whether rope exists in the inventory.
                if "rope" in inventory:
                    location = "Old Bridge"
                    energy -= 1
                    print("You used your rope to cross the broken bridge!")
                else:
                    # No movement or energy deduction without rope.
                    print("You need a rope to cross the bridge!")

            # Move from Old Bridge to Lighthouse.
            elif location == "Old Bridge":
                location = "Lighthouse"
                energy -= 1
                print("You have reached the Lighthouse!")

            # There is no further location after Lighthouse.
            else:
                print("There is nowhere new to explore yet.")

            # Check whether the player has run out of energy.
            # Zero or negative energy causes the player to lose.
            if energy <= 0:
                print("Game Over! You have run out of energy.")
                running = False

        # OPTION 2: QUIT THE GAME
        elif choice == "2":

            # End the game when the player chooses to quit.
            print(f"Goodbye, {name}!")
            running = False

        # OPTION 3: COLLECT ITEMS
        elif choice == "3":

            # The rope can only be collected in the Jungle.
            if location == "Jungle":

                # Prevent collecting the same rope more than once.
                if "rope" not in inventory:
                    inventory.append("rope")
                    print("You collected a rope!")
                else:
                    print("You already have a rope!")

            # The lantern can only be collected in the Cave.
            elif location == "Cave":

                # Prevent collecting the same lantern more than once.
                if "lantern" not in inventory:
                    inventory.append("lantern")
                    print("You collected a lantern!")
                else:
                    print("You already have a lantern!")

            # Other locations have no collectible items yet.
            else:
                print("There is nothing to collect here.")

        # OPTION 4: GO BACK
        # Backward movement currently does not consume energy.
        elif choice == "4":

            # Return from Cave to Jungle.
            if location == "Cave":
                location = "Jungle"
                print("You returned to the Jungle!")

            # Return from Old Bridge to Cave.
            elif location == "Old Bridge":
                location = "Cave"
                print("You returned to the Cave!")

            # Other backward routes are not implemented yet.
            else:
                print("You cannot go back from here yet.")

        # OPTION 5: RESTORE THE LIGHTHOUSE BEACON
        elif choice == "5":

            # The player must be at the Lighthouse to win.
            if location == "Lighthouse":

                # The lantern is required to restore the beacon.
                if "lantern" in inventory:

                    # Display the victory message and end the game.
                    print("Congratulations! You restored the lighthouse beacon!")
                    print(f"You won the game, {name}!")
                    running = False

                else:
                    # The player cannot win without the lantern.
                    print("You need a lantern to restore the beacon!")

            else:
                # The beacon cannot be restored from another location.
                print("You must reach the Lighthouse first!")

        # HANDLE INVALID USER INPUT
        # This prevents unrecognized choices from crashing the game.
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")


# Start the program only when this file is run directly.

def main():
    while True:
        play_game()

        answer = input("\nPlay again? (yes/no): ").strip().lower()

        if answer != "yes":
            print("Thanks for playing Mystery Island!")
            break
            
if __name__ == "__main__":
    main()
