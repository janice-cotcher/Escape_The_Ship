from player import Player
import ship
from collections import OrderedDict


def play():
    """ Input for character movement and accessing inventory"""
    print("Escape from the Ship!")
    ship.parse_ship_dsl()
    player = Player()
    # Possible player directions and actions continue as long as the player is
    # alive and they have not reached the escape pod
    while player.is_alive() and not player.victory:
        # define the player's start position
        position = ship.tile_at(player.x, player.y)
        # print(player.x, player.y)
        # print the intro at the start position
        print(position.intro_text())
        # modify health points of player when attacked
        position.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(position, player)


def get_available_actions(position, player):
    """Only make valid actions available. Actions are stored in a dictionary"""
    # store actions in a dictionary
    actions = OrderedDict()
    print("Choose an action: ")
    # print inventory option if there are any items
    if player.inventory:
        action_adder(actions, "i", player.print_inventory, "Print Inventory")
    # print the ship's map
    if isinstance(position, ship.ViewMapTile):
        action_adder(actions, "m", position.print_map, "Ship's Map")
    # add supplies option if there are any supplies left
    if isinstance(position, ship.SuppliesTile) and position.inventory:
        action_adder(actions, "s", player.add_supplies, "Add Supplies")
    # attack and protect options if the enemy is alive
    elif isinstance(position, ship.EnemyTile) and position.enemy.is_alive():
        action_adder(actions, "a", player.attack, "Attack")
        action_adder(actions, "p", player.protect, "Protection")
    # option to move to another tile once all other actions are completed
    else:
        if ship.tile_at(position.x, position.y - 1):
            action_adder(actions, "f", player.move_forward, "Go forward")
        if ship.tile_at(position.x, position.y + 1):
            action_adder(actions, "a", player.move_aftward, "Go aftward")
        if ship.tile_at(position.x - 1, position.y):
            action_adder(actions, "p", player.move_port, "Go portside")
        if ship.tile_at(position.x + 1, position.y):
            action_adder(actions, "s", player.move_starboard,
                         "Go starboard side")
    # healing option if the player has less than 100 HP
    if player.hp < 100:
        action_adder(actions, "h", player.heal, "Heal")

    return actions


def action_adder(action_dict, hotkey, action, name):
    """Add actions to the dictionary"""
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


def choose_action(position, player):
    """Ask the user to choose an action"""
    action = None
    while not action:
        available_actions = get_available_actions(position, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")


def move_player(actions, player, position):
    if ship.tile_at(position.x, position.y - 1):
        return action_adder(actions, "f", player.move_forward, "Go forward")
    if ship.tile_at(position.x, position.y + 1):
        return action_adder(actions, "a", player.move_aftward, "Go aftward")
    if ship.tile_at(position.x - 1, position.y):
        return action_adder(actions, "p", player.move_port, "Go portside")
    if ship.tile_at(position.x + 1, position.y):
        return action_adder(actions, "s", player.move_starboard,
                            "Go starboard side")


play()
