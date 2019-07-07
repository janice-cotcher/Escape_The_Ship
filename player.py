import items


class Player:
    """Player class with inventory and best weapon"""
    def __init__(self):
        self.inventory = [items.Blaster(), items.Knife(), "oxygen",
                          "space suit", "first aid kit", "food", "water"]

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
