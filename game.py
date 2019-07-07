from player import Player


def play():
    """ Input for character movement and accessing inventory"""
    print("Escape from the Ship!")
    print("""
          Do you want to go forward, aftward, port, starboard, or check
          inventory
          """)
    player = Player()
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
            player.print_inventory()

        else:
            print("Invalid action!")


def get_play_command():
    """Input command for user """
    return input("Action: ")


play()
