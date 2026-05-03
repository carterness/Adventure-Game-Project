import random


class WanderingMonster:
    def __init__(self, x, y, monster_type, color, hp):
        import random

        self.x = x
        self.y = y
        self.monster_type = monster_type
        self.color = color
        self.hp = hp

        # Existing fields
        self.is_ally = False
        self.role = random.choice(["fighter", "healer", "tank"])

        if self.role == "fighter":
            self.ability = "fireball"
        elif self.role == "healer":
            self.ability = "heal"
        else:
            self.ability = "stun"

        self.personality = random.choice(["aggressive", "timid", "loyal"])

    # ---------------- RANDOM SPAWN ---------------- #
    @staticmethod
    def random_spawn(occupied, forbidden, grid_w, grid_h):
        while True:
            x = random.randint(0, grid_w - 1)
            y = random.randint(0, grid_h - 1)

            if (x, y) not in occupied and (x, y) not in forbidden:
                monster_type = random.choice(["Goblin", "Orc", "Dragon"])
                color = [255, 0, 0]  # red
                hp = random.randint(20, 50)

                return WanderingMonster(x, y, monster_type, color, hp)

    # ---------------- LOAD FROM SAVE ---------------- #
    @staticmethod
    def from_dict(data):
        monster = WanderingMonster(
            data["x"],
            data["y"],
            data["monster_type"],
            data["color"],
            data["hp"]
        )
        monster.is_ally = data.get("is_ally", False)
        monster.role = data.get("role", "fighter")
        monster.is_ally = data.get("is_ally", False)
        monster.ability = data.get("ability", None)
        monster.personality = data.get("personality", "aggressive")

        return monster

    # ---------------- SAVE ---------------- #
    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "monster_type": self.monster_type,
            "color": self.color,
            "hp": self.hp,
            "is_ally": self.is_ally,
            "role": self.role,
            "ability": self.ability,
            "personality": self.personality
        }

    # ---------------- MOVEMENT ---------------- #
    def move(self, occupied, forbidden, grid_w, grid_h):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy

            if not (0 <= new_x < grid_w and 0 <= new_y < grid_h):
                continue

            if (new_x, new_y) in occupied:
                continue

            if (new_x, new_y) in forbidden:
                continue

            self.x = new_x
            self.y = new_y
            return

        # If no valid move → stay put
