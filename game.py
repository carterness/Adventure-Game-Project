import json
import gamefunctions as gf
from WanderingMonster import WanderingMonster

def save_game(state, filename="savegame.json"):
    with open(filename, "w") as f:
        json.dump(state, f, indent=4)
    print(f"Game saved to {filename}!")



def save_game(state, filename):
    import copy

    state_copy = copy.deepcopy(state)

    state_copy["monsters"] = [m.to_dict() for m in state["monsters"]]

    with open(filename, "w") as f:
        json.dump(state_copy, f, indent=4)

    print("Game saved!")


def get_main_menu_choice():
    while True:
        print("\nYou are in town.")
        print("1) Open Map")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Equip Weapon")
        print("4) Visit Shop")
        print("5) View Inventory")
        print("6) Save and Quit")
        print("7) Quit WITHOUT Saving")

        choice = input("Enter choice: ")

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
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
        print(f"\nHP: {state['player']['hp']} | Gold: {state['player']['gold']}")

        choice = get_main_menu_choice()

        if choice == "1":
            result = gf.run_map_interface(state)

            if result == "monster":
                gf.fight_monster(state)
                
        elif choice == "2":
            gf.sleep_inn(state)
            
        elif choice == "3":
            gf.equip_item(state, "weapon")

        elif choice == "4":
            gf.print_shop_menu()

        elif choice == "5":
            gf.view_inventory(state)

        elif choice == "6":
            filename = input("Enter save filename: ")
            save_game(state, filename)
            print("Game saved. Goodbye!")
            return
            
        elif choice == "7":
            print("Goodbye!")
            return

        if state["player"]["hp"] <= 0:
            print("Game Over!")
            break

def normalize_map_state(state):
    if "monster_positions" not in state["map"]:
        single = state["map"].get("monster_pos")
        if single:
            state["map"]["monster_positions"] = [single]
        else:
            state["map"]["monster_positions"] = []

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
        
        normalize_map_state(state)

        gf.print_welcome(state["player"]["name"])
        print(f"Welcome back, {state['player']['name']}!")
        
    else:
        print("Invalid choice.")
        return

    game_loop(state)

if __name__ == "__main__":
    main()
