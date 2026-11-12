
"""Mystery Island — The Lost Lighthouse.

A terminal-based adventure game where the player explores
an island, collects useful items, manages energy, and
restores the lighthouse beacon.
"""


# Maximum energy a player can have.
MAX_ENERGY = 5


def describe_location(location):
    """Display a description of the player's current location."""

    if location == "Beach":
        print("\nYou are standing on a quiet sandy beach.")
        print("Waves gently crash against the shore.")
        print("The jungle lies ahead, waiting to be explored.")

    elif location == "Jungle":
        print("\nYou are surrounded by thick trees and tall plants.")
        print("Strange sounds come from deep inside the jungle.")
        print("A narrow path leads further into the island.")

    elif location == "Cave":
        print("\nYou are inside a dark and mysterious cave.")
        print("Rough rocks surround you.")
        print("A broken bridge blocks the path to the lighthouse.")

    elif location == "Old Bridge":
        print("\nYou have reached an old, damaged bridge.")
        print("A dangerous gap separates you from the lighthouse.")
        print("Your rope helped you cross safely.")

    elif location == "Lighthouse":
        print("\nYou are standing before the old lighthouse.")
        print("Its beacon is dark, and ships need its light.")
        print("Restore the beacon to complete your mission.")


def display_status(location, energy, inventory):
    """Display the player's current location, energy and inventory."""

    print("\n" + "=" * 50)
    print(f"LOCATION: {location.upper()}")
    print(f"ENERGY: {energy}/{MAX_ENERGY}")

    if inventory:
        print("INVENTORY: " + ", ".join(inventory))
    else:
        print("INVENTORY: Empty")

    print("=" * 50)


def display_menu():
    """Display the available game options."""

    print("\nWHAT WOULD YOU LIKE TO DO?")
    print("1. Explore        - Travel to the next location.")
    print("2. Quit           - Leave the adventure.")
    print("3. Collect item   - Search this location for useful items.")
    print("4. Go back        - Return to the previous location.")
    print("5. Restore beacon - Light the lighthouse with your lantern.")
    print("6. Eat fruit      - Eat collected fruit to restore energy.")


def check_energy(energy):
    """Check the player's energy and display a warning if necessary."""

    if energy <= 0:
        print("\nGAME OVER!")
        print("You have run out of energy.")
        print("The island adventure has come to an end.")
        return False

    elif energy <= 2:
        print("\nWARNING: Your energy is getting low!")
        print("Find and eat fruit to restore your energy.")

    return True


def collect_item(location, inventory):
    """Allow the player to collect items available at their location."""

    items = {
        "Beach": "fruit",
        "Jungle": "rope",
        "Cave": "lantern"
    }

    if location in items:
        item = items[location]

        if item not in inventory:
            inventory.append(item)
            print(f"\nYou collected {item}!")
        else:
            print(f"\nYou already have {item}!")

    else:
        print("\nThere is nothing to collect here.")


def explore(location, inventory):
    """Move the player to the next location when possible."""

    if location == "Beach":
        new_location = "Jungle"

    elif location == "Jungle":
        new_location = "Cave"

    elif location == "Cave":
        if "rope" in inventory:
            new_location = "Old Bridge"
            print("\nYou used your rope to cross the broken bridge!")
        else:
            print("\nYou cannot cross the broken bridge without a rope.")
            return location, False

    elif location == "Old Bridge":
        new_location = "Lighthouse"

    else:
        print("\nThere is nowhere new to explore.")
        return location, False

    print(f"\nYou have reached {new_location}!")
    return new_location, True


def go_back(location):
    """Move the player to the previous location."""

    previous_locations = {
        "Jungle": "Beach",
        "Cave": "Jungle",
        "Old Bridge": "Cave",
        "Lighthouse": "Old Bridge"
    }

    if location in previous_locations:
        new_location = previous_locations[location]
        print(f"\nYou returned to the {new_location}!")
        return new_location

    print("\nYou cannot go back from here.")
    return location


def eat_fruit(energy, inventory):
    """Allow the player to eat fruit and recover energy."""

    if "fruit" not in inventory:
        print("\nYou don't have any fruit to eat!")
        return energy

    if energy >= MAX_ENERGY:
        print("\nYour energy is already full!")
        return energy

    energy = min(energy + 2, MAX_ENERGY)
    inventory.remove("fruit")

    print("\nYou ate the fruit!")
    print("You restored some energy.")

    return energy


def restore_beacon(location, inventory, name):
    """Allow the player to restore the lighthouse beacon."""

    if location != "Lighthouse":
        print("\nYou must reach the Lighthouse first!")
        return False

    if "lantern" not in inventory:
        print("\nYou need a lantern to restore the beacon!")
        return False

    print("\n" + "=" * 50)
    print("              MISSION COMPLETED!")
    print("=" * 50)
    print("\nYou have restored the lighthouse beacon!")
    print("Its bright light shines across the sea.")
    print("Ships can now find their way safely home.")
    print(f"\nCongratulations, {name}!")
    print("You are the hero of Mystery Island!")
    print("=" * 50)

    return True


def play_game():
    """Run one complete game session."""

    # STEP 1: Ask the player for a nickname.
    name = input("Enter your nickname: ").strip()

    if not name:
        name = "Explorer"

    # STEP 2: Set up the player's starting state.
    energy = MAX_ENERGY
    location = "Beach"
    inventory = []
    running = True

    print(f"\nWelcome to Mystery Island, {name}!")
    print("Your mission is to restore the lost lighthouse beacon.")

    # Display the starting location.
    describe_location(location)

    # STEP 3: Main game loop.
    while running:

        display_status(location, energy, inventory)
        display_menu()

        choice = input("\nChoose an option (1-6): ").strip()

        # OPTION 1: EXPLORE.
        if choice == "1":

            previous_location = location
            location, moved = explore(location, inventory)

            if moved:
                energy -= 1
                describe_location(location)

                if not check_energy(energy):
                    running = False

        # OPTION 2: QUIT.
        elif choice == "2":
            print(f"\nGoodbye, {name}!")
            print("Thank you for exploring Mystery Island.")
            running = False

        # OPTION 3: COLLECT ITEM.
        elif choice == "3":
            collect_item(location, inventory)

        # OPTION 4: GO BACK.
        elif choice == "4":
            previous_location = location
            location = go_back(location)

            if location != previous_location:
                describe_location(location)

        # OPTION 5: RESTORE BEACON.
        elif choice == "5":
            if restore_beacon(location, inventory, name):
                running = False

        # OPTION 6: EAT FRUIT.
        elif choice == "6":
            energy = eat_fruit(energy, inventory)

        # INVALID INPUT.
        else:
            print("\nInvalid choice.")
            print("Please enter a number from 1 to 6.")
