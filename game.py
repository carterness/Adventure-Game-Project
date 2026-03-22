import gamefunctions as gf


def main():

    # Get player name
    player_name = input("Enter your name: ")

    # Welcome message
    gf.print_welcome(player_name)

    # Show shop
    print("\nWelcome to the shop!")
    gf.print_shop_menu()

    # Simulate purchase
    print("\nLet's buy some potions!")
    money = 50
    quantity, remaining = gf.purchase_item(10, money, 3)

    print(f"You bought {quantity} potion(s).")
    print(f"You have ${remaining} left.")

    # Generate a monster
    print("\nA wild monster appears!")
    monster = gf.new_random_monster()

    print(f"Name: {monster['name']}")
    print(f"Description: {monster['description']}")
    print(f"Health: {monster['health']}")
    print(f"Power: {monster['power']}")
    print(f"Money dropped: {monster['money']}")


if __name__ == "__main__":
    main()
