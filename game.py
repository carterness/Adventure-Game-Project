import gamefunctions as gf


def get_main_menu_choice():
    while True:
        print("\nYou are in town.")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Equip Weapon")
        print("4) Quit")

        choice = input("Enter choice: ")

        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("Invalid choice.")


def main():
    player_name = input("Enter your name: ")

    state = gf.initialize_game_state(player_name)

    gf.print_welcome(player_name)

    gf.add_to_inventory(state, gf.create_sword())
    gf.add_to_inventory(state, gf.create_bomb())

    while True:
        print(f"\nHP: {state['player_hp']} | Gold: {state['player_gold']}")

        choice = get_main_menu_choice()

        if choice == "1":
            gf.fight_monster(state)

        elif choice == "2":
            gf.sleep_inn(state)

        elif choice == "3":
            gf.equip_item(state, "weapon")

        elif choice == "4":
            print("Thanks for playing!")
            break

        if state["player_hp"] <= 0:
            print("Game Over!")
            break


if __name__ == "__main__":
    main()
