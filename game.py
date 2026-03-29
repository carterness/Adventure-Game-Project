import gamefunctions as gf


def main():
    # Get player name
    player_name = input("Enter your name: ")

    # Welcome message
    gf.print_welcome(player_name)

    hp = 30
    gold = 10

    while True:
        print("\nYou are in town.")
        print(f"Current HP: {hp}, Current Gold: {gold}")
        print("What would you like to do?")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Quit")

        while True:
            choice = input("Enter choice: ")
            if choice in ["1", "2", "3"]:
                break
            print("Invalid choice. Please enter 1, 2, or 3.")

        if choice == "1":
            hp, gold = gf.fight_monster(hp, gold)

        elif choice == "2":
            hp, gold = gf.sleep_inn(hp, gold)

        elif choice == "3":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
