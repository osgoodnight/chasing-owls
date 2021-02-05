## The script of the game goes in this file.

## Splash screen before game
label splashscreen:
    scene grn with fade
    pause 1
    show logo at truecenter with pixellate
    pause 3
    hide logo with pixellate
    pause 1
    return


# The game starts here.

label start:
    $ day = 1
    $ somchai_points = 0
    $ dominic_points = 0
    A "Hello Everyone! Thank you for downloading 'Born to Chase Owls'!"
    A "The whole team has been excited working on this with me and are very appreciative for all the support."
    A "All characters, situations, and references are a work of fiction.
    Any reference to people, places or things are completely accidental."
    A "'Born to Chase Owls' is an 18+ game and may contain situations not intended for children."
    A "This visual novel is still a work in progress, so sit back and enjoy!"

    jump day1

label end:

    A "Thank you for playing this installment of 'Born to Chase Owls'."
    A "There are new unlocked options to see extra content on Day 3. Go back and look for those!"
    A "Check our game page on itch.io to download the most current version of the game
    and any game updates."
    A "Also, please support us on Patreon! It'll give everyone the strength to continue making this project possible!"
    A "See you next time!"

    $ persistent.ending_unlock = True
    # This ends the game.
    return
