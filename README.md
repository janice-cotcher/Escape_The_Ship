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
