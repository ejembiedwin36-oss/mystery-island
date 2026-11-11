"""Mystery Island — The Lost Lighthouse: first playable lesson."""


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

        choice = input("Choose 1, 2 or 3: ").strip()

        if choice == "1":
            if location == "Beach":
                location = "Jungle"
                energy -= 1
                print("You have entered the Jungle!")

            elif location == "Jungle":
                location = "Cave"
                energy -= 1
                print("You have entered the Cave!")

            else:
                print("There is nowhere new to explore yet.")

            if energy <= 0:
                print("Game Over! You have run out of energy.")
                running = False

        elif choice == "2":
            print(f"Goodbye, {name}!")
            running = False

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

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()