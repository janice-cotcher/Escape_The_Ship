import items


class Player:
    """Player class with inventory and best weapon"""
    def __init__(self):
        # begining items in inventory
        self.inventory = [items.Blaster(), items.Knife(), "oxygen",
                          "space suit", "first aid kit", "food", "water"]
        # player starting coordinates
        self.x = 1
        self.y = 2

    def print_inventory(self):
        """Print the inventory of items and the best weapon"""
        print("Inventory:")
        for item in self.inventory:
            print("* " + str(item))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon is your {}".format(best_weapon))

    def most_powerful_weapon(self):
        """Determine the most power weapon in the inventory"""
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon

    def move(self, dx, dy):
        """Define player movement"""
        self.x += dx
        self.y += dy

    def move_forward(self):
        """Define forward movement"""
        self.move(dx=0, dy=-1)

    def move_aftward(self):
        """Define aftward movement"""
        self.move(dx=0, dy=1)

    def move_starboard(self):
        """Define movement towards the starboard side"""
        self.move(dx=1, dy=0)

    def move_port(self):
        """Define movement towards the port side"""
        self.move(dx=-1, dy=0)
