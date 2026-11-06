"""Mystery Island — The Lost Lighthouse: first playable lesson."""


def main():
    name = input("Enter your nickname: ").strip()
    if not name:
        name = "Explorer"

    energy = 5
    running = True

    print(f"\nWelcome to Mystery Island, {name}!")
    print("Your mission is to restore the lost lighthouse beacon.")

    while running:
        print(f"\nEnergy: {energy}")
        print("1. Explore (coming in the next lesson)")
        print("2. Quit")
        choice = input("Choose 1 or 2: ").strip()

        if choice == "1":
            print("Exploration is not available yet. The adventure begins soon!")
        elif choice == "2":
            print(f"Goodbye, {name}!")
            running = False
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
