class Enemy():
    """Enemy Class to raise errors and return the enemy's name"""
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Robot(Enemy):
    """Robot enemy with name, health points and damage"""
    def __init__(self):
        self.name = "Robot"
        self.hp = 30
        self.damage = 10


class Soldier(Enemy):
    """Enemy Soldier with name, health points and damage"""
    def __init__(self):
        self.name = "Enemy Soldier"
        self.hp = 10
        self.damage = 2


class Drone(Enemy):
    """Enemy Drone with name, health points and damage"""
    def __init__(self):
        self.name = "Enemy Drone"
        self.hp = 5
        self.damage = 1


class Troll(Enemy):
    """Enemy Space Troll with name, health points and damage"""
    def __init__(self):
        self.name = "Space Troll"
        self.hp = 80
        self.damage = 150


class SpaceDucks(Enemy):
    """A flock of blue space ducks with name, health points and damage"""
    def __init__(self):
        self.name = "Flock of Blue Space Ducks"
        self.description = "Follows red space bread crumbs."
        self.hp = 100
        self.damage = 30
