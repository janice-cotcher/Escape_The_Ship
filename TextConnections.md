# RPG: Escape the Space Ship
## Notes and correlations to *Make Your Own Python Text Adventure*
* Step 1: p.25-26
    - add a print statement and conditions for user input for directions
    - added lower() instead of or statements
* Step 2: p.31
    - put the direction inputs into a function called play()
    - created a function get_player_command() for inputs and called it in play()
* Step 3: p.30
    - added an inventory list to play()
    - added the possible user inputs into a list
    - added an option to print the inventory
* Step 4: p.51
    - created a while loop for continuous user inputs
        - accidentally left get_player_command() outside the loop
    - created a for loop to print individual inventory items
* Step 5: p.60-61
    - create weapons classes for Blaster and Knife
    - the text book recommends adding __str__ so self.name can be printed
    - added the Blaster and Knife objects to the inventory list
* Step 6: p.62
    - created a parent class called Weapons and inherited __str__
* Step 7: p.67-69
    - added a function to check what which weapon in the inventory is the most
    powerful
    - added an exception to most_powerful_weapon(inventory) to pass on any
    inventory that does not have the attribute damage
    - added an exception to the Weapons class to prevent from accidentally
    creating objects
* Step 8: p.71-74
    - created an external file to store items classes called item.py
    - created an external file for the Player class called player.py
    - moved most_powerful_weapon to Player class
    - removed most_powerful_weapon option from game.py because it was added to
* Step 9: p.78-83
    - would be useful to connect the coordinate system to Processing
    - created a map class called ship.py
    - added classes for empty tiles, a supply tile, an escape pod tile
    - added a function that links the tile to coordinates
    - initialized the player's starting position in the Player class
    - add methods to the MapTile class that defines movement
    - add direction methods to game.py
    - the game crashes if the player is in an empty position (which the text
        says will be addressed later)
* Step 10: p.85 - 92
    - added enemies with name, health points and damage
    - added the random module to ship.py
    - added enemies at random positions on the Map
    - replaced some of the empty map tiles with enemy tiles
    - added a print statement for the random numbers generated for the enemy
    positions on the MapTile because Space Trolls were appear too often (later
        commented out)
        - changed the conditional statements to less and greater than and equal
        to and it seemed to fix the problem
    - added the ability for the player to attack
    - added the ability for the enemy to fight back to the MapTile class
    - added health points to the player class
    - modified the modify_player method from the Text suggestion p.89
        - used assignment by subtraction
        - added the enemy name to the print statement
        - added a condition that player health must be above 0 to continue
            - this is missing from the text
    - added a base method to the MapTile class to implement modify_player on
    every tile
* Step 11: p.92 - 93
    - added enemy introductions to the MapTile class
        - text uses \ for concatenation
            - using + caused errors text was switched to multi-line string
            blocks
        - different introductions for alive and dead enemies
            -  the text has a very strange way of stating the conditions that
            was ignored
* Step 12: p.94 - 98
    - added a Consumable class to items
    - added a Protection class to items
    - updated the inventory
    - add a function to check for consumables in the Inventory
        - used isinstance to check objects
        - used enumerate to print out the items
        - make sure to emphasize the difference between function reference and
        calling the function (also with objects)
        - added to the Player class
    - add a function to check for protection items in the Inventory
* Step 13: p.99 - 106
    - create a new function in game.py that stores all legal actions in a
    dictionary
    - used the get() method to account for invalid inputs
    - removed get_play_command and replaced them with new action functions
        - made the code much more efficient
* Step 14: p.107 - 114, 122-125
    - created a map of the ship
        - using domain specific language (DSL)
        - created a dictionary of title types
        - take the text map and create a list
        - updated the start location
* p. 115 - 122
    - the text talks about adding value to items to be bought but that can be
    added in the future if the game is expanded to nearby planet
* Step 15: p. 115 - 122
    - add supplies to the player's inventory once they find the supply tile
        - the text does not explicitly show these steps but parts of the
        for buying items was used
* Step 16: p.127 - 129
    - added conditions for winning to the Escape Pod tile
* Appendix: p. 145
    - has helpful suggests places to check in code for specific exceptions
    for the RPG
