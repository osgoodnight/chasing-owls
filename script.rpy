## The script of the game goes in this file.

### Splash screen before game ##################################################

label splashscreen:

    show warning at truecenter with pixellate
    show warning_text_blink at warning_text_pos
    $ renpy.pause (10, hard=True)
    show logo3 at truecenter with pixellate
    hide warning
    hide warning_text_blink
    pause 3
    hide logo3 with pixellate

    return

################################################################################
