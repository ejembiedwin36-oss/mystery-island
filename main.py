"""Mystery Island — The Lost Lighthouse: first playable lesson."""


def main():
    name = input("Enter your nickname: ").strip()
    if not name:
        name = "Explorer"

    energy = 5
    location = "Beach"
    running = True

    print(f"\nWelcome to Mystery Island, {name}!")
    print("Your mission is to restore the lost lighthouse beacon.")


    while running:
        print(f"\nLocation: {location}")
        print(f"Energy: {energy}")
        print("1. Explore")
        print("2. Quit")

        choice = input("Choose 1 or 2: ").strip()

        if choice == "1":
            if location == "Beach":
                location = "Jungle"
                energy -= 1
                print("You have entered the Jungle!")
            else:
                print("There is nowhere new to explore yet.")

        elif choice == "2":
            print(f"Goodbye, {name}!")
            running = False

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
