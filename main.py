"""Main entry point for Mystery Island."""

from game import play_game


def show_introduction():
    """Display the story and instructions before the adventure begins."""

    print("\n" + "=" * 50)
    print("          MYSTERY ISLAND")
    print("          THE LOST LIGHTHOUSE")
    print("=" * 50)

    print("\nAn adventure of courage, discovery and survival.")

    print("\nTHE STORY")
    print("You are an explorer stranded on a mysterious island.")
    print("The lighthouse that once guided ships safely through")
    print("the sea has gone dark.")
    print("Without its light, ships are in danger.")

    print("\nYOUR MISSION")
    print("Explore the island, collect useful items,")
    print("overcome obstacles and restore the lighthouse beacon")
    print("before your energy runs out.")

    print("\nHOW TO PLAY")
    print("1. Explore different locations around the island.")
    print("2. Collect useful items and keep them in your inventory.")
    print("3. Watch your energy because exploring uses energy.")
    print("4. Use items to overcome obstacles.")
    print("5. Find the lantern and restore the lighthouse.")

    print("\nAre you ready, explorer?")
    print("=" * 50)



def main():
    show_introduction()

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
