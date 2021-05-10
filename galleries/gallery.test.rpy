init python:

    g = Gallery()

#BG#############################################################################

    g.navigation = True
    g.transition = dissolve

    g.button("bg01")
    g.condition("persistent.unlock_bg1_2")#(day1)(ln:7)
    g.image("bg01")
    g.image("bg02")

    g.button("bg03")
    g.condition("persistent.unlock_bg3_4")#(day1)(ln:81)
    g.image("bg03")
    g.image("bg04")

    g.button("bg05")
    g.condition("persistent.unlock_bg5_6")#(day1)(ln:210)
    g.image("bg05")
    g.image("bg06")

    g.button("bg07")
    g.condition("persistent.unlock_bg7_8")#(day1)(ln:371)
    g.image("bg07")
    g.image("bg08")

    g.button("bg09")
    g.condition("persistent.unlock_bg9_10")#(day1)(ln:394)
    g.image("bg09")
    g.image("bg10")

    g.button("bg11")
    g.condition("persistent.unlock_bg11_12")#(day1)(ln:365)
    g.image("bg11")
    g.image("bg12")

    g.button("bg13")
    g.condition("persistent.unlock_bg13_14")#(day1)(ln:312)
    g.image("bg13")
    g.image("bg14")

    g.button("bg15")
    g.condition("persistent.unlock_bg15_16")#(day1)(ln:125)
    g.image("bg15")
    g.image("bg16")

    g.button("bg19")
    g.condition("persistent.unlock_bg19_21")#(day2)(ln:679)
    g.image("bg19")
    g.image("bg20")
    g.image("bg21")

    g.button("nightmare")
    g.condition("persistent.unlock_nightmare")#(day3)(ln:3)
    g.image("nightmare")

    g.button("bg17")
    g.condition("persistent.unlock_bg17_18")#10(day5)(ln:164)
    g.image("bg17")
    g.image("bg18")

    g.button("bg22d")
    g.condition("persistent.unlock_bg22")#11
    g.image("bg22d")
    g.image("bg22")

    g.button("bg23")
    g.condition("persistent.unlock_bg23")#(day3b)(ln:90)
    g.image("bg23")
    g.image("bg23n")

    g.button("bg24")
    g.condition("persistent.unlock_bg24_25")#(day3c)(ln:16)
    g.image("bg24")
    g.image("bg25")

    g.button("bg26")
    g.condition("persistent.unlock_bg26")#(day2)(ln:35)
    g.image("bg26")

    g.button("bg27")
    g.condition("persistent.unlock_bg27")#15
    g.image("bg27")

    g.button("bg28")
    g.condition("persistent.unlock_bg28")#(day5)(ln:13)
    g.image("bg28")
    g.image("bg29")


#CG#############################################################################

    g.button("cg01")
    g.unlock_image("cg01")

    g.button("cg02")
    g.unlock_image("cg02")

    g.button("cg03")
    g.unlock_image("cg03")

    g.button("cg04_1")
    g.unlock_image("cg04_1")
    g.unlock_image("cg04_2")
    g.unlock_image("cg04_3")

    g.button("cg05_1")
    g.unlock_image("cg05_1")
    g.unlock_image("cg05_2")

    g.button("cg06_1")
    g.unlock_image("cg06_1")
    g.unlock_image("cg06_2")
    g.unlock_image("cg06_3")

    g.button("cgsecret1_1")
    g.unlock_image("cgsecret1_1")
    g.unlock_image("cgsecret1_2")
    g.unlock_image("cgsecret1_3")

    g.button("cg7_1")
    g.unlock_image("cg7_1")
    g.unlock_image("cg7_2")
    g.unlock_image("cg7_3")
    g.unlock_image("cg7_4")
    g.unlock_image("cg7_5")
    g.unlock_image("cg7_6")
    g.unlock_image("cg7_7")
    g.unlock_image("cg7_8")
    g.unlock_image("cg7_9")
    g.unlock_image("cg7_10")
    g.unlock_image("cg7_11")
    g.unlock_image("cg7_12")
    g.unlock_image("cg7_13")
    g.unlock_image("cg7_14")
    g.unlock_image("cg7_15")
    g.unlock_image("cg7_16")
    g.unlock_image("cg7_17")
    g.unlock_image("cg7_18")
    g.unlock_image("cg7_19")
    g.unlock_image("cg7_20")

    g.button("cg08")
    g.unlock_image("cg08")

    g.button("cg09")
    g.unlock_image("cg09")

    g.button("cg10")
    g.unlock_image("cg10")

    g.button("cg11_1")
    g.unlock_image("cg11_1")
    g.unlock_image("cg11_2")
    g.unlock_image("cg11_3")



################################################################################


    g.button("wren_gallery")
    g.condition("persistent.wren")
    g.image("wren_gallery")

    g.button("dominic_gallery")
    g.condition("persistent.dominic")
    g.image("dominic_gallery")

    g.button("somchai_gallery")
    g.condition("persistent.somchai")
    g.image("somchai_gallery")

    g.button("tobias_gallery")
    g.condition("persistent.tobias")
    g.image("tobias_gallery")

    g.button("kyran_gallery")
    g.condition("persistent.kyran")
    g.image("kyran_gallery")

    g.button("shaula_gallery")
    g.condition("persistent.shaula")
    g.image("shaula_gallery")

    g.button("evanora_gallery")
    g.condition("persistent.evanora")
    g.image("evanora_gallery")

    g.button("figure_gallery")
    g.condition("persistent.figure")
    g.image("figure_gallery")


################################################################################
screen sprites():

    tag menu

    use gallery(_("Character Gallery"))

    text "{size=40}C{vspace=5}h{vspace=5}a{vspace=5}r{vspace=5}a{vspace=5}c{vspace=5}t{vspace=1}e{vspace=5}r{vspace=5}s{/size}" xalign 0.05 yalign 0.1


################################################################################
screen cg():

    tag menu

    use gallery(_("CG Gallery"))

    text "{size=40}C{vspace=1}G {vspace=1}G{vspace=1}a{vspace=1}l{vspace=1}l{vspace=1}e{vspace=1}r{vspace=1}y{/size}" xalign 0.05 yalign 0.1
    #add "gui/overlay/cg_title.png"

################################################################################
screen bg():

    tag menu

    use gallery(_("Background Gallery"))

    text "{size=40}B{vspace=1}a{vspace=1}c{vspace=1}k{vspace=1}g{vspace=1}r{vspace=1}o{vspace=1}u{vspace=1}n{vspace=1}d{vspace=1}s{/size}" xalign 0.05 yalign 0.1

    #add "gui/overlay/bg_title.png"

################################################################################
screen gallery(title):

    use game_menu(_(title), scroll="viewport"):

        vpgrid:
            cols 3
            style_prefix "slot"
            spacing gui.slot_spacing
################################################################################
            if renpy.get_screen("bg"):

                add g.make_button("bg01", "bg01s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg03", "bg03s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg05", "bg05s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg07", "bg07s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg09", "bg09s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg11", "bg11s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg13", "bg13s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg15", "bg15s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg19", "bg19s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("nightmare", "nightmares", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg17", "bg17s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg23", "bg23s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg28", "bg28s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg22d", "bg22s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("bg24", "bg24s", "lock", xalign=0.5, yalign=0.5)
                #add g.make_button("bg26", "bg26s", "logothumb", xalign=0.5, yalign=0.5)
                #add g.make_button("bg27", "bg27s", "logothumb", xalign=0.5, yalign=0.5)

################################################################################
            if renpy.get_screen("cg"):

                add g.make_button("cg01", "cg01s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("cg02", "cg02s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("cg03", "cg03s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("cg04_1", "cg04s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("cg05_1", "cg05s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("cg06_1", "cg06s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("cgsecret1_1", "cgsecret1_1s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("cg7_1", "cg07s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("cg08", "cg08s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("cg09", "cg09s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("cg10", "cg10s", "lock", xalign=0.5, yalign=0.5)
                add g.make_button("cg11_1", "cg11s", "lock", xalign=0.5, yalign=0.5)
                #add g.make_button("cg12", "cg12s", "lock", xalign=0.5, yalign=0.5)
                #add g.make_button("cg13_1", "cg13s", "lock", xalign=0.5, yalign=0.5)

################################################################################
            if renpy.get_screen("sprites"):

                add g.make_button("wren_gallery", "wren_thumb", "lock2", xalign=0.5, yalign=0.5)
                add g.make_button("dominic_gallery", "dominic_thumb", "lock2", xalign=0.5, yalign=0.5)
                add g.make_button("somchai_gallery", "somchai_thumb", "lock2", xalign=0.5, yalign=0.5)
                add g.make_button("kyran_gallery", "kyran_thumb", "lock2", xalign=0.5, yalign=0.5)
                add g.make_button("tobias_gallery", "tobias_thumb", "lock2", xalign=0.5, yalign=0.5)
                add g.make_button("shaula_gallery", "shaula_thumb", "lock2", xalign=0.5, yalign=0.5)
                add g.make_button("evanora_gallery", "evanora_thumb", "lock2", xalign=0.5, yalign=0.5)
                add g.make_button("figure_gallery", "figure_thumb", "lock2", xalign=0.5, yalign=0.5)
