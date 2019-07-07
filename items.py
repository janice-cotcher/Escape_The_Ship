class Weapon():
    """Weapon Class to raise errors and return the weapon's name"""
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
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
