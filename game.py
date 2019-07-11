from player import Player
import ship
from collections import OrderedDict


def play():
    """ Input for character movement and accessing inventory"""
    print("Escape from the Ship!")
    player = Player()
    # Possible player directions and actions
    while True:
        # define the player's start position
        position = ship.tile_at(player.x, player.y)
        print(player.x, player.y)
        # print the intro at the start position
        print(position.intro_text())
        # modify health points of player when attacked
        position.modify_player(player)
        choose_action(position, player)


def get_available_actions(position, player):
    """Only make valid actions available. Actions are stored in a dictionary"""
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, "i", player.print_inventory, "Print Inventory")
    if isinstance(position, ship.EnemyTile) and position.enemy.is_alive():
        action_adder(actions, "a", player.attack, "Attack")
        action_adder(actions, "p", player.protect, "Protection")
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
    if player.hp < 100:
        action_adder(actions, "h", player.heal, "Heal")

    return actions


def action_adder(action_dict, hotkey, action, name):
    """Add actions to the dictionary"""
    hotkey = hotkey.lower()
    action_dict[hotkey] = action
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


play()
