# gamefunctions.py
# Carter Ness
# 2/22/26
# This file calls each of these functions three separate times with
# three different inputs to demonstrate them working within
# the program. The fucntions are purchase_item() and new_random_monster()

import random


def purchase_item(itemPrice: int, startingMoney: int, quantityToPurchase: int = 1):

    max_affordable = startingMoney // itemPrice
    quantity_purchased = min(quantityToPurchase, max_affordable)
    remaining_money = startingMoney - (quantity_purchased * itemPrice)

    return quantity_purchased, remaining_money


def new_random_monster():
    """
    Returns:
        A dictionary with keys:
        name (str)
        description (str)
        health (int)
        power (int)
        money (int)
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
    
    print("="*40)
    print(f"Welcome {player_name} to the Carter's Game!")
    print("You will face monsters, find treasures, and accomplish greatness!")
    print("="*40)

def print_shop_menu():
    """
    Prints a shop menu with nicely formatted item names and prices
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

# Demonstration Section
if __name__ == "__main__":

    # ---- purchase_item tests ----
    print("Test 1 - Default quantity:")
    quantity, remaining = purchase_item(itemPrice=10, startingMoney=50)
    print("Quantity purchased:", quantity)
    print("Remaining money:", remaining)
    print()
    print("Test 2 - Cannot afford full quantity:")
    quantity, remaining = purchase_item(itemPrice=10, startingMoney=50, quantityToPurchase=10)
    print("Quantity purchased:", quantity)
    print("Remaining money:", remaining)
    print()
    print("Test 3 - Can afford all items:")
    quantity, remaining = purchase_item(itemPrice=12, startingMoney=50, quantityToPurchase=3)
    print("Quantity purchased:", quantity)
    print("Remaining money:", remaining)

    # ---- new_random_monster tests ----
    print("\nMonster 1:", new_random_monster())
    print("Monster 2:", new_random_monster())
    print("Monster 3:", new_random_monster())


    # ---- print_welcome tests ----
    print_welcome("Jeff")
    print()

     # ---- print_shop_menu tests ----
    print_shop_menu()

