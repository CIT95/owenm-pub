import messages

import random
from time import sleep

# List for displaying stat names
STAT_NAMES = ["STR", "DEX", "INT"]


def generate_stats(max_upgrade):
    """Generates enemy stats given maximum parameter."""
    enemy_stats = {
        'STR': 1
        'DEX': 1
        'INT': 1
    }
    up = max_upgrade
    while up > 0:
        enemy_stats[random.choice(STAT_NAMES)] + 1
        # Psssst... look here!
    return enemy_stats


def list_stats(stats):
    """Lists a single dictionary in format 'key: value'"""
    for key in stats:
        print(f"{key}: {stats[key]}")


def compare_stats(stats1, stats2):
    """Lists two dictionaries side by side in format
    'key1: value1       key2: value2'"""
    print("ENEMY STATS:      YOUR STATS:")
    for key in stats1:
        print("{key}: {stats1[key]}            {key}: {stats2[key]}")


def upgrade():
    """Upgrades player stats."""
    global max_stat
    global health
    upgrade_points = 2 + bonus
    while upgrade_points > 0:
        upgrade = input(f"\n    You have {upgrade_points} upgrade point(s)."
                        " Choose a stat to upgrade by entering"
                        " its 3-letter ID.\n    Or, type 'heal' to"
                        " spend 3 upgrade points to regain 1 heart\n"
                        "    > ").upper()

        while (upgrade not in STAT_NAMES) or (upgrade != 'HEAL'):  # Validate!
            upgrade = input(f"\n    {upgrade} is not a valid option. Please"
                            " type STR, DEX, INT, or HEAL.\n    > ").upper()

        if upgrade = 'HEAL':
            if upgrade_points < 3:
                print(f"\nSorry, but you need {3 - upgrade_points} more "
                      "upgrade point(s) to do that.")
            elif health >= 3:
                print("\nYou already have max health!")
            else:
                upgrade_points -= 3
                max_stat += 3
                health += 1
                print("\n3 upgrade points spent to regain 1 heart."
                      " You now have {health} hearts.")
                print(art.health[health])
        else:
            player_stats[upgrade] += 1
            print(f"\nYou have upgraded {upgrade}")
            # There should be something here... ;)
            max_stat += 1

    print("\nHere are your new stats:")
    list_stats(player_stats)


# Initial varible setup
max_stat = 0
health = 3
game_round = 0
game_over = False
speed = 2
bonus = 0
player_stats = {
    'STR': 1,
    'DEX': 1,
    'INT': 1
}

# Get player name, difficulty and prepare to start
print(art.text[0])
playername = input("    Enter your name\n    > ").upper()
difficulty = int(input("\n    How many rounds would you like to play?"
                       " Enter a number\n    > "))

begin = input(f"\n    Are you ready to enter the "
              "Dungeon? [y/n]\n    > ").lower()
# Validate input
while begin != "y":
    print(f"\n{random.choice(messages.begin_messages)}")
    begin = input("    Are you ready to begin? [y/n]\n    > ").lower()

print("Into the darkness we go...")

sleep(1)

while not game_over:  # Check if the player has either won or lost the game.
    print(f"\n{playername}, Here are your stats:")
    list_stats(player_stats)
    upgrade()  # Upgrade player stats

    sleep(speed)

    # Generate and list stats
    print("\nROUND " + str(game_round + 1))
    print("A monster approaches!")

    sleep(speed)

    monster_stats = generate_stats(max_stat)
    print(random.choice(art.creatures))  # Chose a random monster graphic from art.py  # noqa
    monster = random.choice(messages.monster_names).upper()
    print(monster)

    sleep(speed)

    print("")
    compare_stats(player_stats, monster_stats)

    sleep(speed)

    # Choose which stat monster should attack with
    monster_attack = random.choice(STAT_NAMES)

    # List the values of the selected stat for player and monster
    print(f"\n{monster} attacked with {monster_attack}.")
    print(f"{monster} {monster_attack}: "
          f"{monster_stats[monster_attack]}")
    print(f"{playername} {monster_attack}: "
          f"{player_stats[monster_attack]}")

    bonus = 0

    # Conditions for win, loss, and tie.
    if monster_stats[monster_attack] > player_stats[monster_attack]:
        print(f"\n{monster} beats {playername}. Lose a life")
        health -= 1
    elif monster_stats[monster_attack] < player_stats[monster_attack]:
        print(f"{playername} beats {monster}. {monster} gets hurt.")
        if bonus <= 3:
            bonus += 1
            print("+1 upgrade point!")
    else:
        print("It's a tie. You both take a step back and regroup")

    sleep(speed)

    # Choose which stat player will attack with
    player_attack = input("\n    Choose a stat to attack with\n    > ").upper()
    while player_attack not in STAT_NAMES:  # Validate input
        player_attack = input(f"    {player_attack} is not a valid choice."
                              " Choose a stat by typing its"
                              " 3-letter ID\n    > ").upper()

    # Conditions for win, loss, and tie.
    if monster_stats[player_attack] > player_stats[player_attack]:
        print(f"\n{monster} beats {playername}. Lose a life")
        health -= 1
    elif monster_stats[player_attack] < player_stats[player_attack]:
        print(f"\n{playername} beats {monster}. {monster} dies.")
        if bonus <= 3:
            bonus += 1
            print("+1 upgrade point!")
    else:
        print("\nIt's a tie. You both run away, defeated.")

    sleep(speed)

    # If health below zero, set it back to zero. Print health on screen
    if health < 0:
        health = 0
    print("\nYour health:")
    print(art.health[health])

    # Game end conditions
    if health == 0 or game_round == difficulty - 1:
        game_over = True

    game_round += 1

# Display the game win or loss messages.
if health == 0:
    sleep(speed)
    print("The monsters overpowered you, and you perished.")
    sleep(speed)
    print(art.text[1])
    sleep(speed)
    print("\nFinal stats:")
    list_stats(player_stats)
else:
    sleep(speed)
    print("You defeated all the monsters.")
    sleep(speed)
    print(art.text[2])
    sleep(speed)
    print("\nFinal stats:")
    list_stats(player_stats)
    print("\nFinal health:")
    print(art.health[health])
