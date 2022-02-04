import random

# Each data point is formatted as: [method name, caffeine level, time required]
coffee_methods = [["Pourover", 1, 15], ["French press", 2, 10],
                  ["Aeropress", 3, 5], ["Espresso", 3, 20]]

# These are encouragin messages for when the program finishes.
messages = ["Have a good day!", "Go get 'em!", "Enjoy your coffee!",
            "Caffenation in progress...", "I can smell your brew already!",
            "The best thing about waking up is... Python!"]

# Get the time that the user has to make coffee:
time_available = int(input("How much time do you have, in minutes?\n"))

# Find out which coffee methods the user has time for.
selection = []
for method in coffee_methods:
    if method[2] < time_available:
        selection.append(method)

# If the user doesn't have time, tell them.
if len(selection) < 1:
    print(f"{time_available} minutes isn't enough time to make coffee!"
          " You need to get going.")
else:
    # List the user's choices.
    print("Here are your choices:")

    # Print the available choices with their respective caffeine levels.
    # "n" is so we can print choices as a numbered list.
    n = 1
    for choice in selection:
        print(f"{n}: {choice[0]}, with a caffeine level of {choice[1]}")
        n += 1

    # Get the user's choice out of available choices.
    number_choice = int(input("Make your selection by typing the number to"
                              "the right of your desired method.\n"))-1

    # Check if the user made a valid choice.
    if number_choice < len(selection):
        final_choice = selection[number_choice]

        # Print how long the selected method will take.
        print(f"Making {final_choice[0]} will take {final_choice[2]}"
              " minutes.")
        # Print a random encouraging message!
        print(random.choice(messages))
    else:
        print("That's not a valid choice!")
