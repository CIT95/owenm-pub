## `Player` class:
### Attributes:
- `id` - (int) The numerical id of the player, ranging from 1 to infinity.
- `name` - (str) The player's name.
- `health` - (int) The player's health.
- `score` - (int) The player's score.
- `is_human` - (bool) If the player is human, which helps the game handle fights between human and computer characters.
- `bonus` - (int) The bonus upgrade points a player is awarded after a round.
- `stats` - (dict) The player's stats.
### Methods:
- `upgrade()` - Upgrades the player's stats and returns the amount of actions taken.
- `list_stats()` - Prints the player's stats.
- `attack()` - Facilitates attacks.

<br>

## `Enemy` class:
### Attributes:
- `stats` - (dict) The enemy's stats.
- `picture` - (str) The image to use for the enemy.
- `name` - (str) The enemy's name.
- `is_human` - (bool) If the player is human, which helps the game handle fights between human and computer characters.
### Methods:
- `generate_stats(max)` - Generates enemy stats, with `max` denoting the maximum enemy stat.
- `attack()` - Facilitates attacks.

<br>

## `Playerlist` class:
### Attributes:
- `players` - (list) The players in the current game as `Player` objects.
- `winners` - (list) The winner(s) of the current game as `Player` object(s).
### Methods:
- `get_players()` - Gets number of players and player names, assigns a playerid, and appends `players` with a `Player` object for each user.
- `list_scores()` - Prints final scores when the game is complete.
- `get_victory()` - Adds the winner to the `winners` list. If there is a tie, adds all players with the highest score.
- `list_winnners()` - Prints winner(s), along with their final score and stats.

<br>

## `Game` class:
### Attributes:
- `max_stat` - (int) The max player/enemy stat level.
- `g_round` - (int) The number of the current game round.
- `over` - (bool) Whether the current game is over or not.
### Methods:
- `compare_stats(player, enemy)` - Prints the player and enemy stats side by side.
- `get_winner(attacker, defender)` - Compares the attacker's selected stat with the defender's and declares a winner. `attacker` and `defender` can be either `Player` or `Enemy` objects.
- `confirm_start(player)` - Takes a `Player` object and asks if it is ready to start the round.
- `new_enemy(player)` - Creates a new `Enemy` object for the player to fight.
- `start_round(player)` - Starts a new round for a `Player` object. Then, checks who won the fight.
- `continue_game(player)` - Prints health, then checks if a `Player` object should continue the game.