class Weapon():
    """Weapon Class to raise errors and return the weapon's name"""
    def __str__(self):
        raise NotImplementedError("Do not create raw Weapon objects")
        return self.name


class Blaster(Weapon):
    """Blaster weapon class with description and damage"""
    def __init__(self):
        self.name = "Blaster"
        self.description = """
                            A ray gun for clearing obstacles and damaging
                            enemies
                            """
        self.damage = 5


class Knife(Weapon):
    """Knife weapon class with description and damage"""
    def __init__(self):
        self.name = "Pocket Knife"
        self.description = """
                            A foldable knife with one blade that can fit
                            in the pocket when the blade is
                            folded into the handle.
                           """
        self.damage = 2


def play():
    """ Input for character movement and accessing inventory"""
    inventory = ["oxygen", "space suit", "first aid kit", "food", "water",
                 Blaster(), Knife()]
    print("Escape from the Ship!")
    print("""
          Do you want to go forward, aftward, port, starboard, or check
          inventory?
          """)
    while True:
        action_input = get_play_command()
        if action_input.lower() in ["forward", "for", "fore", "f"]:
            print("Go forward!")

        elif action_input.lower() in ["aftward", "aft", "a", "afterward",
                                      "aftword"]:
            print("Go aftward!")

        elif action_input.lower() in ["port", "p", "part", "portward"]:
            print("Go portside!")

        elif action_input.lower() in ["starboard", "star board", "star", "s"]:
            print("Go starboard side!")

        elif action_input.lower() in ["i", "inventory"]:
            for item in inventory:
                print("*" + str(item))
        elif action_input.lower() in ["b", "best"]:
            most_powerful_weapon(inventory)
        else:
            print("Invalid action!")


def get_play_command():
    """Input command for user """
    return input("Action: ")


def most_powerful_weapon(inventory):
    """Determine the most power weapon in the inventory"""
    max_damage = 0
    best_weapon = None
    for item in inventory:
        try:
            if item.damage > max_damage:
                best_weapon = item
                max_damage = item.damage
        except AttributeError:
            pass
    print(best_weapon)
    return best_weapon


play()
