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
        print("3. collect rope")

        choice = input("Choose 1 or 2: ").strip()

        if choice == "1":
            if location == "Beach":
                location = "Jungle"
                energy -= 1
                print("You have entered the Jungle!")

                if energy <= 0:
                    print("Game Over! You have run out of energy")
                    running = False
            else:
                print("There is nowhere new to explore yet.")

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
            else:
                    print("You must enter the Jungle to collect the rope.")

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
