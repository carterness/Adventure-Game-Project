import json
import gamefunctions as gf


def save_game(state, filename="savegame.json"):
    with open(filename, "w") as f:
        json.dump(state, f, indent=4)
    print(f"Game saved to {filename}!")


def load_game(filename="savegame.json"):
    try:
        with open(filename, "r") as f:
            state = json.load(f)
        print(f"Game loaded from {filename}!")
        return state
    except FileNotFoundError:
        print("Save file not found.")
        return None


def get_main_menu_choice():
    while True:
        print("\nYou are in town.")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Equip Weapon")
        print("4) Visit Shop")
        print("5) Save and Quit")
        print("6) Quit WITHOUT Saving")

        choice = input("Enter choice: ")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice
        else:
            print("Invalid choice.")


def shop_menu(state):
    while True:
        print("\n--- Shop ---")
        gf.print_shop_menu()

        print(f"\nYour Gold: {state['player']['gold']}")
        print("1) Buy Potion ($10)")
        print("2) Buy Sword ($50)")
        print("3) Buy Shield ($40)")
        print("4) Buy Food ($5)")
        print("5) Exit Shop")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                amount = int(input("How many potions? "))
            except ValueError:
                print("Invalid amount.")
                continue

            qty, remaining = gf.purchase_item(10, state["player"]["gold"], amount)
            if qty > 0:
                state["player"]["gold"] = remaining
                for _ in range(qty):
                    gf.add_to_inventory(state, {"name": "Potion", "type": "consumable"})
            else:
                print("Not enough gold!")

        elif choice == "2":
            if state["player"]["gold"] >= 50:
                state["player"]["gold"] -= 50
                gf.add_to_inventory(state, gf.create_sword())
            else:
                print("Not enough gold!")

        elif choice == "3":
            if state["player"]["gold"] >= 40:
                state["player"]["gold"] -= 40
                gf.add_to_inventory(state, {"name": "Shield", "type": "armor"})
            else:
                print("Not enough gold!")

        elif choice == "4":
            try:
                amount = int(input("How much food? "))
            except ValueError:
                print("Invalid amount.")
                continue

            qty, remaining = gf.purchase_item(5, state["player"]["gold"], amount)
            if qty > 0:
                state["player"]["gold"] = remaining
                for _ in range(qty):
                    gf.add_to_inventory(state, {"name": "Food", "type": "consumable"})
            else:
                print("Not enough gold!")

        elif choice == "5":
            print("Leaving shop...")
            break

        else:
            print("Invalid choice.")



def game_loop(state):
    while True:
        player = state["player"]
        print(f"\nHP: {player['hp']} | Gold: {player['gold']}")

        choice = get_main_menu_choice()

        if choice == "1":
            gf.fight_monster(state)

        elif choice == "2":
            gf.sleep_inn(state)

        elif choice == "3":
            gf.equip_item(state, "weapon")

        elif choice == "4":
            shop_menu(state)

        elif choice == "5":
            filename = input("Enter save filename (or press Enter for default): ")
            if filename == "":
                filename = "savegame.json"

            save_game(state, filename)
            print("Game saved. Goodbye!")
            break

        elif choice == "6":
            print("Goodbye!")
            break

        if state["player"]["hp"] <= 0:
            print("Game Over!")
            break



def main():
    print("1) New Game")
    print("2) Load Game")

    start_choice = input("Enter choice: ")

    if start_choice == "1":
        player_name = input("Enter your name: ")
        state = gf.initialize_game_state(player_name)

        gf.print_welcome(player_name)

        # Starter items
        gf.add_to_inventory(state, gf.create_sword())
        gf.add_to_inventory(state, gf.create_bomb())

    elif start_choice == "2":
        filename = input("Enter save filename: ")
        state = load_game(filename)

        if state is None:
            return

        gf.print_welcome(state["player"]["name"])
        print(f"Welcome back, {state['player']['name']}!")

    else:
        print("Invalid choice.")
        return

    game_loop(state)



if __name__ == "__main__":
    main()
