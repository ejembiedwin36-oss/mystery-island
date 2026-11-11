
"""Mystery Island — The Lost Lighthouse."""


def main():
    name = input("Enter your nickname: ").strip()

    if not name:
        name = "Explorer"

    energy = 5
    location = "Beach"
    inventory = []
    running = True

    print(f"\nWelcome to Mystery Island, {name}!")
    print("Your mission is to restore the lost lighthouse beacon.")

    while running:
        print(f"\nLocation: {location}")
        print(f"Energy: {energy}")
        print(f"Inventory: {inventory}")
        print("1. Explore")
        print("2. Quit")
        print("3. Collect item")
        print("4. Go back")

        choice = input("Choose 1, 2, 3 or 4: ").strip()

        # Option 1: Explore the island
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

            else:
                print("There is nowhere new to explore yet.")

            if energy <= 0:
                print("Game Over! You have run out of energy.")
                running = False

        # Option 2: Quit the game
        elif choice == "2":
            print(f"Goodbye, {name}!")
            running = False

        # Option 3: Collect items
        elif choice == "3":
            if location == "Jungle":
                if "rope" not in inventory:
                    inventory.append("rope")
                    print("You collected a rope!")
                else:
                    print("You already have a rope!")

            elif location == "Cave":
                if "lantern" not in inventory:
                    inventory.append("lantern")
                    print("You collected a lantern!")
                else:
                    print("You already have a lantern!")

            else:
                print("There is nothing to collect here.")

        # Option 4: Return from Cave to Jungle
        elif choice == "4":
            if location == "Cave":
                location = "Jungle"
                print("You returned to the Jungle!")
            elif location == "Old Bridge":
                location = "Cave"
                print("You return to the Cave!")
                
            else:
                print("You cannot go back from here yet.")


        # Handle invalid input
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
