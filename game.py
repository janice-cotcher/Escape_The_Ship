from player import Player
import ship


def play():
    """ Input for character movement and accessing inventory"""
    print("Escape from the Ship!")
    print("""
          Do you want to go forward, aftward, port, starboard, or check
          inventory
          """)
    player = Player()
    while True:
        position = ship.tile_at(player.x, player.y)
        print(position.intro_text())
        action_input = get_play_command()
        if action_input.lower() in ["forward", "for", "fore", "f"]:
            print("Go forward!")
            player.move_forward()
        elif action_input.lower() in ["aftward", "aft", "a", "afterward",
                                      "aftword"]:
            print("Go aftward!")
            player.move_aftward()
        elif action_input.lower() in ["port", "p", "part", "portward"]:
            print("Go portside!")
            player.move_port()
        elif action_input.lower() in ["starboard", "star board", "star", "s"]:
            print("Go starboard side!")
            player.move_starboard()
        elif action_input.lower() in ["i", "inventory"]:
            player.print_inventory()

        else:
            print("Invalid action!")


def get_play_command():
    """Input command for user """
    return input("Action: ")


play()
