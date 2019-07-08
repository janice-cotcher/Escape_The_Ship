import random
import enemies


class MapTile:
    """ Map with x and y coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        """Added modify_player to every tile"""
        pass


class StartTile(MapTile):
    """Player starting position"""
    def intro_text(self):
        return """
        You find yourself in space under attack by an unknown enemy that
        is boarding your ship.
        You need an escape pod to travel to safety on the nearby planet.
        You need supplies for the trip and suriving on the planet.
        You can go four directions: forward, aftward, port, starboard
        You have two actions: inventory, attack
        """


class BoringTile(MapTile):
    """Position with no matierals"""
    def intro_text(self):
        return """
        There are no supplies or an escape pod here.
        """


class SuppliesTile(MapTile):
    """Position that contains survival supplies"""
    def intro_text(self):
        return """
        You see a large metal trunk. You open it.
        It's supplies! You found a first aid kit, an oxygen tank,
        a space suit, food, water, a pocket knife, and a ray gun.
        """


class EscapePod(MapTile):
    """Position that contains the escape pod"""
    def intro_text(self):
        return """
        You found the escape pod! You open the door and enter the pod.
        """


class EnemyTile(MapTile):
    """Enemy position and messages"""
    def __init__(self, x, y):
        """Creates a random position for each enemy"""
        r = random.random()
        # encounter Drones about 50% of the time
        if r < 0.50:
            self.enemy = enemies.Drone()
            # print(r)
        # encounter Soldiers about 30% of the time
        elif r < 0.80 and r >= 50:
            self.enemy = enemies.Soldier()
            # print(r)
        # encounter robots about 15% of the time
        elif r < 0.95 and r >= 0.80:
            self.enemy = enemies.Robot()
            # print(r)
        # encounter trolls about 5% of the time
        elif r < 0.98 and r >= 0.95:
            self.enemy = enemies.Troll()
            # print(r)
        else:
            self.enemy = enemies.SpaceDucks()
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            return "A {} awaits!".format(self.enemy.name)
        else:
            return "You've defeated the {}.".format(self.enemy.name)

    def modify_player(self, player):
        """
        Checks the enemy's current strength so it can respond to the player
        """
        if self.enemy.is_alive():
            player.hp -= self.enemy.damage
            print("The {} does damage {}. You have {} HP remaining".
                  format(self.enemy.name, self.enemy.damage, player.hp))


# defining the layout of the space ship
ship_map = [
    [EnemyTile(0, 0), SuppliesTile(1, 0), None],
    [None, BoringTile(1, 1), None],
    [EnemyTile(0, 2), StartTile(1, 2), EnemyTile(2, 2)],
    [EscapePod(0, 3), BoringTile(1, 3), None]
]


def tile_at(x, y):
    """Locates the tile at a coordinate"""
    if x < 0 or y < 0:
        return None
    try:
        return ship_map[y][x]
    except IndexError:
        return None
