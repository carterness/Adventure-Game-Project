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

def fight_monster(player_hp, player_gold):
    monster = new_random_monster()

    print("\nA wild monster appears!")
    print(f"{monster['name']}: {monster['description']}")

    monster_hp = monster["health"]

    while player_hp > 0 and monster_hp > 0:
        display_fight_stats(player_hp, monster)

        action = get_user_fight_action()

        if action == "1":
            # Player attacks
            player_damage = random.randint(8, 15)
            monster_damage = monster["power"]

            monster_hp -= player_damage
            player_hp -= monster_damage

            print(f"You deal {player_damage} damage!")
            print(f"The {monster['name']} deals {monster_damage} damage!")

        elif action == "2":
            print("You ran away!")
            break

        else:
            print("Invalid choice! Please enter 1 or 2")

    if player_hp <= 0:
        print("You were defeated...")
        player_hp = 0

    elif monster_hp <= 0:
        print(f"You defeated the {monster['name']}!")
        print(f"You earned {monster['money']} gold!")
        player_gold += monster["money"]

    return player_hp, player_gold

if __name__ == "__main__":
    main()
