label story_split_1:


    if dominic_points >= somchai_points:
        jump dom_day_7

    elif dominic_points <= somchai_points:
        jump som_day_7

    else:
        jump tie_day_7


label dom_day_7:
    $ dominic_points = 0

    "Congratulations! You've made it to Dominic's route!"

    jump end

label som_day_7:
    $ somchai_points = 0

    "Congratulations! You've made it to Somchai's route!"

    jump end

label tie_day_7:

    "WOW~! You got a tied score, so you get to choose which route."

    menu:

        "Dominic's Route":
            jump dom_day_7

        "Somchai's Route":
            jump som_day_7
