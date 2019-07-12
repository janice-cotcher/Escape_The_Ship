import random
import enemies
import sys
import items


class MapTile:
    """ Map with x and y coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.inventory

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
        You need supplies for the trip and surviving on the planet.
        You can go four directions: forward, aftward, port, starboard
        You have four actions: inventory, attack, heal, protect
        """


class BoringTile(MapTile):
    """Position with no materials"""
    def intro_text(self):
        return """
        There are no supplies or an escape pod here.
        """


class SuppliesTile(MapTile):
    """Position that contains survival supplies"""
    def __init__(self, x, y):
        """Initial supplies at the tile"""
        self.name = "Supplies"
        self.inventory = [items.Blaster(), items.OxygenTank(),
                          items.SpaceSuit(), items.FirstAid(),
                          items.CrustyBread(), items.Water(), items.Shelter()]

        super().__init__(x, y)

    def intro_text(self):
        return """
        You see a large metal trunk. You open it.
        It's supplies! You found a first aid kit, an oxygen tank,
        a space suit, food, water, a pocket knife, and a ray gun.
        """

    def suppy(self):
        """Message for what items were added"""
        for i, item in enumerate(self.inventory, 1):
            print("You added the following items to your inventory!")
            print("{}. {}.".format(i, item.name))
        self.add_inventory()

    def add_inventory(self, current_inventory):
        """Add items from the supply tile to the player's inventory"""
        for item in self.inventory:
            current_inventory.append(item)
        # remove supplies from the tile
        self.inventory = []


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
            self.alive_text = """
            You hear a buzzing noise. You turn around and see an enemy drone
            with its guns aimed at you
            """
            self.dead_text = """
            The buzzing stops, the drone explodes and falls to the floor
            """
            # print(r)
        # encounter Soldiers about 30% of the time
        elif r < 0.80 and r >= 50:
            self.enemy = enemies.Soldier()
            self.alive_text = """
            An enemy solider in a space suit jumps out from around the corner
            and starts to fire.
            """
            self.dead_text = """
            The solider drops its weapon and slumps to the floor.
            """
            # print(r)
        # encounter robots about 15% of the time
        elif r < 0.95 and r >= 0.80:
            self.enemy = enemies.Robot()
            self.alive_text = """
            Your eye catches the glint of chrome in the flickering light. A
            large red eye turns, scans your body, pauses and then opens fire.
            """
            self.dead_text = """
            The large red eye grows dim as sparks fly from the disabled robot.
            """
            # print(r)
        # encounter trolls about 5% of the time
        elif r < 0.98 and r >= 0.95:
            self.enemy = enemies.Troll()
            self.alive_text = """
            Debris flies every where as a large space troll smashes equipment.
            It suddenly stops and notices you trying to hide. It approaches
            quickly and swings at you with its large fists.
            """
            self.dead_text = """
            The troll clutches its mortal wounds as it falls with a loud thud
            that shakes the whole ship.
            """
            # print(r)
        else:
            self.enemy = enemies.SpaceDucks()
            self.alive_text = """
            You hear a deafening chorus of quacks. Suddenly you are lost in a
            flock of blue space ducks as they peck at your head.
            """
            self.dead_text = """
            The last duck explodes into a cloud of feathers. You wade through
            large banks of blue feathers and try to clean off the ship's
            equipment and unclog the blocked air ducts.
            """
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            return self.alive_text
        else:
            return self.dead_text

    def modify_player(self, player):
        """
        Checks the enemy's current strength so it can respond to the player
        """
        if self.enemy.is_alive():
            # continue play if there's enough health points
            if player.hp > self.enemy.damage:
                player.hp -= self.enemy.damage
                print("The {} does {} damage. You have {} HP remaining".
                      format(self.enemy.name,
                             self.enemy.damage,
                             player.hp))
            # end the game if the player runs out of health points
            elif player.hp <= self.enemy.damage:
                print("The {} causes mortal damage. You die.".
                      format(self.enemy.name))
                sys.exit()


# defining the layout of the space ship
ship_map = [
    [EnemyTile(0, 0), SuppliesTile(1, 0), BoringTile(2, 0)],
    [BoringTile(0, 1), BoringTile(1, 1), BoringTile(2, 1)],
    [EnemyTile(0, 2), StartTile(1, 2), EnemyTile(2, 2)],
    [EscapePod(0, 3), BoringTile(1, 3), BoringTile(2, 3)]
]


def tile_at(x, y):
    """Locates the tile at a coordinate"""
    if x < 0 or y < 0:
        return None
    try:
        return ship_map[y][x]
    except IndexError:
        return None


# ship's map
ship_dsl = """
|ET|IT|  |
|  |  |  |
|ET|ST|ET|
|EP|  |  |
"""


def is_dsl_valid(dsl):
    """
    Check to makre there is only one start tile and escape pod.
    Also check that each row has the same number of columns
    """
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|EP|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True


tile_type_dict = {"EP": EscapePod,
                  "ST": StartTile,
                  "IT": SuppliesTile,
                  "ET": EnemyTile,
                  "  ": None}

start_tile_location = None


def parse_ship_dsl():
    """Taking the ship map as a string and returning a list"""
    if not is_dsl_valid(ship_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = ship_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    # Iterate over each line in the DSL.
    for y, dsl_row in enumerate(dsl_lines):
        # Create an object to store the tiles
        row = []
        # Split the line into abbreviations
        dsl_cells = dsl_row.split("|")
        # The split method includes the beginning
        # and end of the line so we need to remove
        # those nonexistent cells
        dsl_cells = [c for c in dsl_cells if c]
        # Iterate over each cell in the DSL line
        for x, dsl_cells in enumerate(dsl_cells):
            # Look up the abbreviation in the dictionary
            tile_type = tile_type_dict[dsl_cells]
            # set the start tile location
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            # If the dictionary returned a valid type, create
            # a new tile object, pass it the X-Y coordinates
            # as required by the tile __init__(), and add
            # it to the row object. If None was found in the
            # dictionary, we just add None.
            row.append(tile_type(x, y) if tile_type else None)
        # Add the whole row to the ship_map
        ship_map.append(row)
