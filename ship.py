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
        """Descriptive text for the Start Tile"""
        return """
        You find yourself in space under attack by an unknown enemy that
        is boarding your ship.
        You need an escape pod to travel to safety on the nearby planet.
        You need supplies for the trip and survival on the planet.
        You can go four directions: forward, aftward, port, starboard
        You have four actions: inventory, attack, heal, protect
        """


class BoringTile(MapTile):
    """Position with no materials"""
    def intro_text(self):
        return """
        There are no supplies or escape pod here.
        """


class ViewMapTile(MapTile):
    """Position that prints a map"""
    def intro_text(self):
        """Descriptive text for the Viewable Map Tile"""
        return """
        You see a map on the wall.
        """

    def print_map(self):
        """Print a map of the ship with directions"""
        self.ship_printable = """
                            forward
                |          |Supplies|            |
        port    |          |        |You are Here|  starboard
                |          | Start  |            |
                |Esacpe Pod|        |            |
                            aftward
        """
        print(self.ship_printable)


class SuppliesTile(MapTile):
    """Position that contains survival supplies"""
    def __init__(self, x, y):
        """Initial supplies at the tile"""
        # index for switching descriptive messagages
        self.i = 0
        self.name = "Supplies"
        self.inventory = [items.Blaster(), items.OxygenTank(),
                          items.SpaceSuit(), items.FirstAid(),
                          items.CrustyBread(), items.Water(), items.Shelter()]

        super().__init__(x, y)

    def intro_text(self):
        """Descriptive texts for the Start Tile"""
        # initial description
        self.start_supplies = """
        You see a large metal trunk. You open it.
        It's supplies! You found a first aid kit, an oxygen tank,
        a space suit, food, water, a pocket knife, and a ray gun.
        """
        # description after supplies are added
        self.no_supplies = "No supplies left at this location"
        # define the descriptive text for the supply text
        supply_text = [self.start_supplies, self.no_supplies]
        # switch messages after the supplies are added
        if self.i == 0:
            self.i += 1
            return supply_text[0]
        else:
            return supply_text[1]

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
    def modify_player(self, player):
        """Player wins the game if they reach the escape pod"""
        player.victory = True
        sys.exit()

    def intro_text(self):
        return """
        You found the escape pod! You open the door and enter the pod.
        The escape pod slowly disengages from the ship and travels to
        the nearby planet. You are safe, for now...
        """


class EnemyTile(MapTile):
    """Enemy position and messages"""
    def __init__(self, x, y):
        """Creates a random position for each enemy"""
        # Indices j, k for switching alive_text and dead_text messages
        self.j = 0
        self.k = 0
        # generate a random number to estabilish a random enemy
        r = random.random()
        # encounter Drones about 50% of the time
        if r < 0.30:
            self.enemy = enemies.Drone()
            alive_start = """
            You hear a buzzing noise. You turn around and see an enemy drone
            with its guns aimed at you
            """
            alive_attack = "The drone attacks."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The buzzing stops, the drone explodes and falls to the floor
            """
            dead_return = "A disabled drone lays on the ground"
            self.dead_text = [dead_start, dead_return]
            # print(r)
        # encounter Soldiers about 30% of the time
        elif r < 0.60 and r >= 0.30:
            self.enemy = enemies.Soldier()
            alive_start = """
            An enemy solider in a space suit jumps out from around the corner
            and starts to fire.
            """
            alive_attack = "The solider attacks."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The solider drops its weapon and slumps to the floor.
            """
            dead_return = "A dead solider lays on the ground"
            self.dead_text = [dead_start, dead_return]
            # print(r)
        # encounter robots about 15% of the time
        elif r < 0.75 and r >= 0.60:
            self.enemy = enemies.Robot()
            alive_start = """
            Your eye catches the glint of chrome in the flickering light. A
            large red eye turns, scans your body, pauses and then opens fire.
            """
            alive_attack = "The robot attacks."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The large red eye grows dim as sparks fly from the disabled robot.
            """
            dead_return = "A disabled robot lays on the ground"
            self.dead_text = [dead_start, dead_return]
            # print(r)
        # encounter trolls about 5% of the time
        elif r < 0.90 and r >= 0.75:
            self.enemy = enemies.Troll()
            alive_start = """
            Debris flies everywhere as a large space troll smashes equipment.
            It suddenly stops and notices you trying to hide. It approaches
            quickly and swings at you with its large fists.
            """
            alive_attack = "The troll attacks."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The troll clutches its mortal wounds as it falls with a loud thud
            that shakes the whole ship.
            """
            dead_return = "A dead troll lays on the ground"
            self.dead_text = [dead_start, dead_return]
            # print(r)
        else:
            self.enemy = enemies.SpaceDucks()
            alive_start = """
            You hear a deafening chorus of quacks. Suddenly you are lost in a
            flock of blue space ducks as they peck at your head.
            """
            alive_attack = "The ducks attack."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The last duck explodes into a cloud of feathers. You wade through
            large banks of blue feathers and try to clean off the ship's
            equipment and unclog the blocked air ducts.
            """
            dead_return = "Dead ducks lie an a cloud of blue feathers"
            self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            # Switch from the intro message after the player starts attacking
            if self.j == 0:
                self.j += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # switch from the intro message if the player returns to the tile
        # where there is a dead enemy
        else:
            if self.k == 0:
                self.k += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

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
# ship_map = [
#     [EnemyTile(0, 0), SuppliesTile(1, 0), BoringTile(2, 0)],
#     [BoringTile(0, 1), BoringTile(1, 1), BoringTile(2, 1)],
#     [EnemyTile(0, 2), StartTile(1, 2), EnemyTile(2, 2)],
#     [EscapePod(0, 3), BoringTile(1, 3), BoringTile(2, 3)]
# ]
# initialize the ship's map
ship_map = []


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
|ET|IT|BT|
|BT|BT|MP|
|ET|ST|ET|
|EP|BT|BT|
"""


def is_dsl_valid(dsl):
    """
    Check to make sure there is only one start tile and escape pod.
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


# key to the ship's map
tile_type_dict = {"EP": EscapePod,
                  "ST": StartTile,
                  "IT": SuppliesTile,
                  "ET": EnemyTile,
                  "BT": BoringTile,
                  "MP": ViewMapTile,
                  "  ": None}
# initialize the start tile
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
