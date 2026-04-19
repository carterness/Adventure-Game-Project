# gamefunctions.py
# Carter Ness
# 2/22/26
# This file calls each of these functions three separate times with
# three different inputs to demonstrate them working within
# the program. The fucntions are purchase_item() and new_random_monster()

"""Utility functions for a simple text-based adventure game.

This module provides helper functions used in a basic game
environment where players can purchase items, encounter random
monsters, and interact with a shop system. It includes logic for
handling purchases, generating randomized monster encounters,
and displaying formatted game messages.

Functions:
  purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    Calculates how many items a player can afford and returns
    the quantity purchased along with remaining money.

  new_random_monster():
    Generates and returns a dictionary representing a random
    monster with attributes such as health, power, and money.

  print_welcome(player_name):
    Displays a welcome message for the player.

  print_shop_menu():
    Prints a formatted shop menu with item names and prices.

Dependencies:
  random: Used to generate random monster types and attributes.

Example:
  quantity, remaining = purchase_item(10, 50, 3)
  monster = new_random_monster()
  print_welcome("Player")
  print_shop_menu()
"""

import random

def purchase_item(itemPrice: int, startingMoney: int, quantityToPurchase: int = 1):
    """
    Determine how many items a player can purchase.

    Calculates the maximum number of items a player can afford
    based on available money and item price. Returns the number
    of items actually purchased and the remaining money.

    Parameters:
        itemPrice (int): The cost of a single item.
        startingMoney (int): The amount of money the player has.
        quantityToPurchase (int): Desired number of items to buy.
            Defaults to 1.

    Returns:
        tuple:
            quantity_purchased (int): Number of items bought.
            remaining_money (int): Money left after purchase.

    Example:
        >>> purchase_item(10, 50, 3)
        (3, 20)
    """
    
    max_affordable = startingMoney // itemPrice
    quantity_purchased = min(quantityToPurchase, max_affordable)
    remaining_money = startingMoney - (quantity_purchased * itemPrice)

    return quantity_purchased, remaining_money


def new_random_monster():
    """
    Generate a random monster with stats.

    Randomly selects a monster type (Goblin, Orc, or Dragon)
    and assigns randomized attributes such as health, power,
    and money.

    Parameters:
        None

    Returns:
        dict: A dictionary containing:
            name (str): Monster name.
            description (str): Description of the monster.
            health (int): Health points.
            power (int): Attack strength.
            money (int): Money dropped when defeated.

    Example:
        >>> monster = new_random_monster()
        >>> print(monster["name"])
        Goblin
    """

    monster_type = random.choice(["Goblin", "Orc", "Dragon"])

    if monster_type == "Goblin":
        monster = {
            "name": "Goblin",
            "description": "A sneaky green creature.",
            "health": random.randint(50, 80),
            "power": random.randint(5, 12),
            "money": random.randint(5, 20)
        }

    elif monster_type == "Orc":
        monster = {
            "name": "Orc",
            "description": "A large brutish warrior.",
            "health": random.randint(80, 120),
            "power": random.randint(10, 18),
            "money": random.randint(15, 35)
        }

    else:  # Dragon
        monster = {
            "name": "Dragon",
            "description": "A massive fire-breathing beast.",
            "health": random.randint(150, 250),
            "power": random.randint(20, 40),
            "money": random.randint(50, 100)
        }

    return monster

def print_welcome(player_name):
    """
    Display a welcome message to the player.

    Prints a formatted greeting introducing the player to the
    game.

    Parameters:
        player_name (str): The name of the player.

    Returns:
        None

    Example:
        >>> print_welcome("Alex")
    """
    
    print("="*40)
    print(f"Welcome {player_name} to the Carter's Game!")
    print("You will face monsters, find treasures, and accomplish greatness!")
    print("="*40)

def print_shop_menu():
    """
    Display the shop menu with item prices.

    Prints a formatted table showing available items and their
    prices.

    Parameters:
        None

    Returns:
        None

    Example:
        >>> print_shop_menu()
    """
    items = [("Potion", 10),
             ("Sword", 50),
             ("Shield", 40),
             ("Food", 5)]
    
    border = "+" + "-"*22 + "+"
    print(border)
    print("| SHOP MENU           |")
    print(border)

    for item_name, price in items:

        print(f"| {item_name:<12}{price:>8.2f} |".replace(f"{price:>8.2f}", f"${price:>7.2f}"))
    
    print(border)
def buy_sword(state):
    if state["player"]["gold"] >= 50:
        state["player"]["gold"] -= 50
        add_to_inventory(state, create_sword())
    else:
        print("Not enough gold!")

def view_inventory(state):
    inventory = state["player"]["inventory"]

    if not inventory:
        print("Your inventory is empty.")
        return

    print("\n--- Inventory ---")

    for i, item in enumerate(inventory, start=1):
        line = f"{i}) {item['name']}"

        # Show durability if it exists
        if "currentDurability" in item:
            line += f" ({item['currentDurability']}/{item['maxDurability']})"

        # Show if equipped
        if item.get("equipped"):
            line += " [EQUIPPED]"

        print(line)

def sleep_inn(state):
    if state["player"]["gold"] >= 5:
        state["player"]["gold"] -= 5
        state["player"]["hp"] = 30
        print("You feel rested! HP restored to 30.")
    else:
        print("Not enough gold!")

def display_fight_stats(player_hp, monster_name, monster_hp):
    print("\n--- Fight Status ---")
    print(f"Your HP: {player_hp}")
    print(f"{monster_name} HP: {monster_hp}")

def get_user_fight_action():
    while True:
        print("\nChoose an action:")
        print("1) Attack")
        print("2) Run Away")

        choice = input("Enter choice: ")

        if choice in ["1", "2"]:
            return choice
        else:
            print("Invalid choice. Please enter 1 or 2.")

def fight_monster(state):
    import random

    current_pos = state["map"]["player_pos"]
    state["map"]["monster_positions"].remove(current_pos)

    # Spawn a new monster somewhere else
    size = state["map"]["size"]
    town = state["map"]["town_pos"]

    while True:
      new_pos = [random.randint(0, size - 1), random.randint(0, size - 1)]
      if new_pos != town and new_pos not in state["map"]["monster_positions"]:
        state["map"]["monster_positions"].append(new_pos)
        break
    
    monster = new_random_monster()

    print("\nA wild monster appears!")
    print(f"{monster['name']}: {monster['description']}")

    monster_hp = monster["health"]

    # Bomb check (instant win)
    if use_bomb(state):
        print(f"You defeated the {monster['name']} instantly!")
        print(f"You earned {monster['money']} gold!")
        state["player"]["gold"] += monster["money"]
        state["game"]["monsters_defeated"] += 1
        return

    while state["player"]["hp"] > 0 and monster_hp > 0:
        display_fight_stats(state["player"]["hp"], monster["name"], monster_hp)

        print("\nChoose an action:")
        print("1) Attack")
        print("2) Use Potion")
        print("3) Run Away")

        choice = input("Enter choice: ")

        if choice == "1":
            base_damage = random.randint(5, 12)

            weapon = get_equipped_weapon(state)
            if weapon:
                base_damage += weapon["damage"]
                weapon["currentDurability"] -= 1

                print(f"Using {weapon['name']}! +{weapon['damage']} damage "
                    f"(Durability: {weapon['currentDurability']}/{weapon['maxDurability']})")

                if weapon["currentDurability"] == 0:
                    print(f"Your {weapon['name']} broke!")
                    state["player"]["inventory"].remove(weapon)

            # Critical hit (20% chance)
            if random.random() < 0.2:
                base_damage *= 2
                print("CRITICAL HIT!")

            monster_hp -= base_damage
            print(f"You deal {base_damage} damage!")

        elif choice == "2":
            inventory = state["player"]["inventory"]
            for item in inventory:
                if item["name"] == "Potion":
                    state["player"]["hp"] += 15
                    state["player"]["hp"] = min(state["player"]["hp"], 30)
                    inventory.remove(item)
                    print("You used a Potion! (+15 HP)")
                    break
            else:
                print("No potions available!")
                continue

        elif choice == "3":
            if random.random() < 0.5:
                print("You successfully ran away!")
                return
            else:
                print("You failed to escape!")

        else:
            print("Invalid choice.")
            continue

        if monster_hp > 0:
            damage = random.randint(monster["power"] - 3, monster["power"] + 3)

            # Shield reduction
            shield = None
            for item in state["player"]["inventory"]:
                if item.get("type") == "armor":
                    shield = item
                    break

            if shield:
                damage = max(0, damage - 3)
                print("Your shield reduces damage!")

            state["player"]["hp"] -= damage
            state["player"]["hp"] = max(0, state["player"]["hp"])

            print(f"The {monster['name']} deals {damage} damage!")

    if state["player"]["hp"] <= 0:
        print("You were defeated...")
        state["player"]["hp"] = 0

    elif monster_hp <= 0:
        print(f"You defeated the {monster['name']}!")
        print(f"You earned {monster['money']} gold!")
        state["player"]["gold"] += monster["money"]
        state["game"]["monsters_defeated"] += 1

def initialize_game_state(player_name):
    """
    Initialize the game state dictionary for a new player.

    Returns a dictionary containing player info and game stats.
    """
    size = 10
    town_pos = [0, 0]

    monster_positions = []

    # Generate 2 unique monster positions
    while len(monster_positions) < 2:
        pos = [random.randint(0, size - 1), random.randint(0, size - 1)]

        if pos != town_pos and pos not in monster_positions:
            monster_positions.append(pos)

    return {
        "player": {
            "name": player_name,
            "gold": 1000,       # starting gold
            "hp": 30,           # starting HP
            "inventory": []     # empty inventory
        },
        "game": {
            "monsters_defeated": 0
        },
        "map": {
            "player_pos": town_pos.copy(),     # starting at town
            "town_pos": town_pos,
            "monster_pos": monster_positions,
            "size": size
        }
    }

def create_sword():
    return {
        "name": "Sword",
        "type": "weapon",
        "damage": 5,
        "maxDurability": 10,
        "currentDurability": 10
    }

def create_bomb():
    return {
        "name": "Bomb",
        "type": "consumable",
        "effect": "instant_kill"
    }

def add_to_inventory(state, item):
    state["player"]["inventory"].append(item)
    print(f"{item['name']} added to inventory!")

def get_items_by_type(state, item_type):
    return [item for item in state["player"]["inventory"] if item["type"] == item_type]

def equip_item(state, item_type):
    valid_items = get_items_by_type(state, item_type)

    if not valid_items:
        print(f"No {item_type}s available to equip.")
        return

    print(f"\nChoose a {item_type} to equip:")

    for i, item in enumerate(valid_items, start=1):
        dur = item.get("currentDurability", "N/A")
        max_dur = item.get("maxDurability", "")
        if max_dur != "":
            dur = f"{dur}/{max_dur}"

    print(f"{i}) {item['name']} (Durability: {dur})")

    print("0) None")

    choice = input("Enter choice: ")

    if choice == "0":
        print("Nothing equipped.")
        return

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(valid_items):
        print("Invalid choice.")
        return

    selected_item = valid_items[int(choice) - 1]

    # Unequip all other items of this type
    for item in state["player"]["inventory"]:
        if item.get("type") == item_type and "equipped" in item:
            item["equipped"] = False

    # Equip selected item
    selected_item["equipped"] = True

    print(f"{selected_item['name']} equipped!")

def get_equipped_weapon(state):
    for item in state["player"]["inventory"]:
        if item.get("type") == "weapon" and item.get("equipped"):
            return item
    return None

def use_bomb(state):
    inventory = state["player"]["inventory"]

    for item in inventory:
        if item["name"] == "Bomb":
            inventory.remove(item)
            print("You used a Bomb! Monster defeated instantly!")
            return True

    return False

def move_player(state, direction):
    x, y = state["map"]["player_pos"]
    size = state["map"]["size"]

    if direction == "up":
        y -= 1
    elif direction == "down":
        y += 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1

    # Boundary check
    if x < 0 or x >= size or y < 0 or y >= size:
        return "invalid"

    state["map"]["player_pos"] = [x, y]

    if [x, y] == state["map"]["town_pos"]:
        return "returned_to_town"

    elif [x, y] in state["map"]["monster_positions"]:
        return "monster_encounter"

    else:
        return "moved"

def display_map(state):
    size = state["map"]["size"]
    player = state["map"]["player_pos"]
    town = state["map"]["town_pos"]
    monster = state["map"]["monster_positions"]

    print("\n--- Map ---")

    for y in range(size):
        row = ""
        for x in range(size):
            if [x, y] == player:
                row += " P "
            elif [x, y] == town:
                row += " T "
            elif [x, y] in monster:
                row += " M "
            else:
                row += " . "
        print(row)

def run_map_interface(state):
    print("\nEntering the world map...")

    while True:
        display_map(state)

        print("\nMove: w=up, s=down, a=left, d=right")
        choice = input("Enter move: ").lower()

        if choice == "w":
            result = move_player(state, "up")
        elif choice == "s":
            result = move_player(state, "down")
        elif choice == "a":
            result = move_player(state, "left")
        elif choice == "d":
            result = move_player(state, "right")
        else:
            print("Invalid input.")
            continue

        if result == "invalid":
            print("You can't move there!")
        elif result == "moved":
            pass
        elif result == "returned_to_town":
            print("You returned to town.")
            return "town"
        elif result == "monster_encounter":
            print("A monster blocks your path!")
            return "monster"

# Demonstration Section

def test_functions():

    # ---- purchase_item tests ----
    print("Test 1 - Default quantity:")
    quantity, remaining = purchase_item(itemPrice=10, startingMoney=50)
    print("Quantity purchased:", quantity)
    print("Remaining money:", remaining)
    print()

    print("Test 2 - Cannot afford full quantity:")
    quantity, remaining = purchase_item(
        itemPrice=10, startingMoney=50, quantityToPurchase=10)
    print("Quantity purchased:", quantity)
    print("Remaining money:", remaining)
    print()

    print("Test 3 - Can afford all items:")
    quantity, remaining = purchase_item(
        itemPrice=12, startingMoney=50, quantityToPurchase=3)
    print("Quantity purchased:", quantity)
    print("Remaining money:", remaining)

    # ---- new_random_monster tests ----
    print("\nMonster 1:", new_random_monster())
    print("Monster 2:", new_random_monster())
    print("Monster 3:", new_random_monster())

    # ---- print_welcome tests ----
    print()
    print_welcome("Jeff")

    # ---- print_shop_menu tests ----
    print()
    print_shop_menu()
def test_inventory_system():
    state = initialize_game_state("Carter")

    add_to_inventory(state, create_sword())
    add_to_inventory(state, create_bomb())

    equip_item(state, "weapon")

    print(state)
def test_equipping():
    state = initialize_game_state("Jeff")

    add_to_inventory(state, create_sword())
    add_to_inventory(state, create_sword())  # multiple swords
    add_to_inventory(state, create_bomb())

    equip_item(state, "weapon")

    print("\nFinal Inventory:")
    for item in state["player_inventory"]:
        print(item)

if __name__ == "__main__":
    test_functions()
