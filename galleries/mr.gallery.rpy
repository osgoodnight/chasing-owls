init python:
    #MusicRoom
    mr = MusicRoom(fadeout=1.0)
    #Music files.
    #1
    mr.add("audio/theme_1.mp3", always_unlocked=True)
    #2
    mr.add("audio/sweet_moments.mp3", always_unlocked=True)
    #3
    mr.add("audio/suspense.mp3", always_unlocked=True)
    #4
    #mr.add("audio/Partymix1.mp3", always_unlocked=True)
    #5
    #mr.add("audio/Partymix1.mp3", always_unlocked=True)
    #6
    #mr.add("audio/Partymix1.mp3", always_unlocked=True)
    #7
    #mr.add("audio/Partymix1.mp3", always_unlocked=True)
    #8
    #mr.add("audio/Partymix1.mp3", always_unlocked=True)


################################################################################
################################################################################
screen music_room():

    tag menu
    use game_menu(_("Music"), scroll="viewport"):

        frame:

            area (0.0, 0.0, 1150, 440)

            has vbox:

                align (0.0, 0.0)
                spacing gui.pref_music_text_spacing

            frame:
                textbutton "{size=28}{b}Theme 1{/b}{/size}" action mr.Play("audio/theme_1.mp3")
            frame:
                textbutton "{size=28}{b}Sweet Moments{/b}{/size}" action mr.Play("audio/sweet_moments.mp3")
            frame:
                textbutton "{size=28}{b}Suspense{/b}{/size}" action mr.Play("audio/suspense.mp3")
            #frame
                #textbutton "{size=28}{b}Song 4{/b}{/size}" action mr.Play("audio/Partymix1.mp3")
            #frame
                #textbutton "{size=28}{b}Song 5{/b}{/size}" action mr.Play("audio/Partymix1.mp3")
            #frame
                #textbutton "{size=28}{b}Song 6{/b}{/size}" action mr.Play("audio/Partymix1.mp3")
            #frame
                #textbutton "{size=28}{b}Song 7{/b}{/size}" action mr.Play("audio/Partymix1.mp3")
            #frame
                #textbutton "{size=28}{b}Song 8{/b}{/size}" action mr.Play("audio/Partymix1.mp3")

        frame:
            area (0.0, 0.2, 1150, 60)

            has hbox:
                xalign 0.5
                yalign 0.5
                spacing 150

            # Buttons that let us advance tracks.
            textbutton "{size=30}{b}|<<Prev{/b}{/size}" action mr.Previous()
            textbutton "{size=30}{b}Stop{/b}{/size}" action mr.Stop()
            textbutton "{size=30}{b}Play{/b}{/size}" action mr.Play()
            textbutton "{size=30}{b}Next>>|{/b}{/size}" action mr.Next()

    #add "gui/overlay/music_title.png"
    text "{size=40}M{vspace=60}u{vspace=60}s{vspace=60}i{vspace=60}c{/size}" xalign 0.05 yalign 0.1
