print('''
                      .   *        .       .
       *      -0-
          .                .  *       - )-
       .      *       o       .       *
 o                |
           .     -O-
.                 |        *      .     -0-
       *  o     .    '       *      .        o
              .         .        |      *
   *             *              -O-          .
         .             *         |     ,
                .           o
        .---.
  =   _/__~0_\\_     .  *            o       '
 = = (_________)             .
                 .                        *
       *               - ) -       *
''')
print("Welcome to SpaceEscape v1.0\n"
      "\n"
      "Prison break... in space!\n"
      "Try to escape the space jail and avoid capture - or worse.\n")
# Write your code below this line 👇
print("You just broke out of your jail cell, in front of you stands\n"
      "a door and two buttons: one red, one blue.")
decision = input("Which button do you press?\n> ").lower()
if decision == "red":
    print("The red button opens the door, which leads to a hallway that\n"
          "stretches out to your right and left.")
    decision = input("Do you go right or left?\n> ").lower()
    if decision == "left":
        print("You walk down the left hallway for a while, stopping when you\n"
              "come to another cell. There appears to be an alien\n"
              "trapped in here.")
        decision = input("Do you free him?\n> ").lower()
        if decision == "yes":
            friend = True
            print("You free the alien, and he agrees to help you escape.")
        else:
            friend = False
            print("You choose to ignore the alien and continue on your way.")
        print("You come upon a launchpad. On it: a ship ready for takeoff.")
        decision = input("Do you steal the ship?\n> ").lower()
        if decision == "yes" and friend is True:
            print("You and your new friend hop on board the ship.\n"
                  "You don't know how to fly, but thankfully the alien does.\n"
                  "You both fly away and go on to live long, happy lives.")
            print('''
* * * * * * * *
*  YOU WIN!!  *
* * * * * * * *
''')
        elif decision == "yes" and friend is False:
            print("You hop on board the ship and take off\n"
                  "However, you forgot one key thing:\n"
                  "you don't know how to fly.\n"
                  "You immediately crash and burn.")
            print('''
* * * * * * * * *
* GAME OVER  :( *
* * * * * * * * *
''')
        else:
            print("You decide against stealing the ship. Too risky.\n"
                  "Suddenly, an alarm blares and guards rush in to the room.\n"
                  "You've been caught!\n"
                  "The guards take you back to your cell and lock you up.")
            print('''
* * * * * * * * *
* GAME OVER  :( *
* * * * * * * * *
''')
    else:
        print("Oh no! There's guards that way.\n"
              "You were captured and thrown back into jail.")
        print('''
* * * * * * * * *
* GAME OVER  :( *
* * * * * * * * *
''')

else:
    print("Unfortunately, the blue button opens the airlock.\n"
          "You are sucked out into the vacuum of space.")
    print('''
* * * * * * * * *
* GAME OVER  :( *
* * * * * * * * *
''')
