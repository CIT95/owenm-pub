import random

# Formatted as: Method title, Caffeine level, Time required
coffee_methods = [["Pourover", 1, 15], ["French press", 2, 10],
                  ["Aeropress", 3, 5], ["Espresso", 3, 20]]

messages = ["Have a good day!", "Go get 'em!", "Enjoy your coffee!",
            "Caffenation in progress...", "I can smell your brew already!",
            "The best thing about waking up is... Python!"]

time_available = int(input("How much time do you have, in minutes?\n"))

selection = []
for method in coffee_methods:
    if method[2] < time_available:
        selection.append(method)

if len(selection) < 1:
    print(f"{time_available} minutes isn't enough time to make coffee!"
          " You need to get going.")
else:
    print("Here are your choices:")
    n = 1
    for choice in selection:
        print(f"{n}: {choice[0]}, with a caffeine level of {choice[1]}")
        n += 1

    number_choice = int(input("Make your selection by typing the number to"
                              "the right of your desired method.\n"))-1

    if number_choice < len(selection):
        final_choice = selection[number_choice]

        print(f"Making {final_choice[0]} will take {final_choice[2]}"
              " minutes.")
        print(random.choice(messages))
    else:
        print("That's not a valid choice!")
