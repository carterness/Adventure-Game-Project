import gamefunctions as gf


def get_main_menu_choice():
    while True:
        print("\nYou are in town.")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Quit")

        choice = input("Enter choice: ")

        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def main():
    player_name = input("Enter your name: ")
    gf.print_welcome(player_name)

    hp = 30
    gold = 10

    while True:
        print(f"\nCurrent HP: {hp}, Current Gold: {gold}")

        choice = get_main_menu_choice()

        if choice == "1":
            hp, gold = gf.fight_monster(hp, gold)

        elif choice == "2":
            hp, gold = gf.sleep_inn(hp, gold)

        elif choice == "3":
            print("Thanks for playing!")
            break

        if hp <= 0:
            print("Game Over!")
            break


if __name__ == "__main__":
    main()
