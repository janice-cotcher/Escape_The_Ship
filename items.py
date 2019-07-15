class Weapon():
    """Weapon Class to raise errors and return the weapon's name"""
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
        return "{} (+ {} Damage)".format(self.name, self.damage)


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
                            A knife with one blade that can fit
                            in the pocket when the blade is
                            folded into the handle.
                           """
        self.damage = 2


class Consumable():
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+ {} HP)".format(self.name, self.healing_value)


class Water(Consumable):
    def __init__(self):
        self.name = "Water"
        self.healing_value = 10


class OxygenTank(Consumable):
    def __init__(self):
        self.name = "Oxygen Tank"
        self.healing_value = 20


class FirstAid(Consumable):
    def __init__(self):
        self.name = "First Aid Kit"
        self.healing_value = 50


class Protection():
    def __init__(self):
        raise NotImplementedError("Do not create raw Protection objects.")

    def __str__(self):
        return "{} (- {} Damage)".format(self.name, self.protect_value)


class SpaceSuit(Protection):
    def __init__(self):
        self.name = "Space Suit"
        self.protect_value = 50


class Shelter(Protection):
    def __init__(self):
        self.name = "Portable Shelter"
        self.protect_value = 100


class CrustyBread(Consumable, Protection):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 5
        self.protect_value = 0
