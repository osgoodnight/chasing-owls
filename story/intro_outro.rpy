#### The game starts here. #####################################################

label start:

    $ day = 1
    $ somchai_points = 0
    $ dominic_points = 0
    A "Hello Everyone! Thank you for downloading \"Born to Chase Owls\"!"
    A "The whole team has been excited working on this with me and are very appreciative for all the support."
    A "This visual novel is still a work in progress, so sit back and enjoy!"
    A "Disclaimer: Translations aren't complete, so not everything will be translated."

    jump day1

### The game ends here. ########################################################

label end:

    show text "{size=50}To Be Continued...{/size}" at truecenter with fade
    pause 3.0
    hide text with dissolve
    stop music fadeout 5.0
    stop sound
    A "Thank you for playing this installment of \"Born to Chase Owls\"."
    #A "There are new unlocked options to see extra content on Day 3. Go back and look for those!"
    A "Check out our game page on {a=https://chasing-owl-productions.itch.io/born-to-chase-owls}itch.io{/a} to download the most current version of the game."
    A "Also, please support us on {a=https://www.patreon.com/Chasing_Owls}Patreon!{/a} It'll give everyone the strength to continue making this project possible!"
    A "See you next time!"
    $ persistent.ending_unlock = True

    return
