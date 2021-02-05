#images used in-game and gallery
init-1:

    # logos
    image logo = "Logo.png"
    image logothumb = im.FactorScale("owl.png", 0.60)

    #color backgrounds
    image blk = "#000"
    image wht = "#f4f4ff"
    image grn = "#637044"

    #Sprite peremeters

    define A = Character("Author", color = "#ffffff")
    define uv = Character("Unknown Voice", color = "#a9a9a9")
    define f = Character("Figure", color = "#a9a9a9")
    define w = Character("Wren", color = "#ffc4c4")
    define W = Character("Wren", color = "#ffc4c4")
    define s = Character("Somchai", color = "#ffe8c4")
    define S = Character("Somchai", color = "#ffe8c4")
    define d = Character("Dominic", color = "#899dae")
    define D = Character("Dominic", color = "#899dae")
    define t = Character("Tobias", color = "#fffcc4")
    define T = Character("Tobias", color = "#fffcc4")
    define k = Character("Kyran", color = "#8db7a5")
    define K = Character("Kyran", color = "#8db7a5")
    define sh = Character("Shaula", color = "#cf9fbc")
    define Sh = Character("Shaula", color = "#cf9fbc")
    define e = Character("Evanora", color = "#a78bb2")
    define E = Character("Evanora", color = "#a78bb2")
    define o = Character("Owl", color = "#ffffff")
    define teach = Character("Teacher", color = "#ff9923")
    define e_sh = Character("Evanora & Shaula", color = "#ffffff")
    define w_sh = Character("Wren & shaula", color = "#ffffff")
    define k_w = Character("Kyran & Wren", color = "#ffffff")

    ##Character images
    image wren reg = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren happy = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren happy blush = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren sad = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren angry = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren surprised = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren surprised blush = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren thinking = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren embarrassed = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image somchai reg = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai happy = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai happy blush = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai sad = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai angry = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai surprised = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai surprised blush = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai thinking = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai embarrassed = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image dominic reg = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=5)
    image dominic happy = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=5)
    image dominic happy blush = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=5)
    image dominic sad = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=5)
    image dominic angry = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=5)
    image dominic surprised = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=5)
    image dominic surprised blush = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=5)
    image dominic thinking = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=5)
    image dominic embarrassed = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=5)
    image tobias reg = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias happy = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias sad = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias angry = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias surprised = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias thinking = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias embarrassed = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image kyran reg = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.4, yoffset=-50)
    image kyran happy = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.4, yoffset=-50)
    image kyran sad = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.4, yoffset=-50)
    image kyran angry = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.4, yoffset=-50)
    image kyran surprised = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.4, yoffset=-50)
    image kyran thinking = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.4, yoffset=-50)
    image kyran embarrassed = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.4, yoffset=-50)
    image shaula reg = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.5, yoffset=15)
    image shaula happy = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.5, yoffset=15)
    image shaula sad = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.5, yoffset=15)
    image shaula angry = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.5, yoffset=15)
    image shaula surprised = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.5, yoffset=15)
    image shaula thinking = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.5, yoffset=15)
    image shaula embarrassed = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.5, yoffset=15)
    image evanora reg = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora happy = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora sad = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora angry = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora surprised = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora thinking = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora embarrassed = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image owl = im.FactorScale("Sprites/owl_sprite.png",0.8, xalign=0.5, yalign=0.5)
    #image figure = "Sprites/figure_sprite.png"

    #BG
    image nightmare = im.Grayscale("Backgrounds/park_river.png")
    image bg01 = "Backgrounds/wrens_bedroom_day.png"
    image bg02 = "Backgrounds/wrens_bedroom_night.png"
    image bg03 = "Backgrounds/wrens_livingroom_day.png"
    image bg04 = "Backgrounds/wrens_livingroom_night.png"
    image bg05 = "Backgrounds/school_outside_day.png"
    image bg06 = "Backgrounds/school_outside_night.png"
    image bg07 = "Backgrounds/school_hallway_1.png"
    image bg08 = "Backgrounds/school_hallway_2.png"
    image bg09 = "Backgrounds/hangout_school_day.png"
    image bg10 = "Backgrounds/hangout_school_eve.png"
    image bg11 = "Backgrounds/classroom_1_day.png"
    image bg12 = "Backgrounds/classroom_1_eve.png"
    image bg13 = "Backgrounds/classroom_2_day.png"
    image bg14 = "Backgrounds/classroom_2_eve.png"
    image bg15 = "Backgrounds/cafe_inside_1.png"
    image bg16 = "Backgrounds/cafe_inside_2.png"
    image bg17 = "Backgrounds/resturant_outside.png"
    image bg18 = "Backgrounds/resturant_inside.png"
    image bg19 = "Backgrounds/park_field_day.png"
    image bg20 = "Backgrounds/park_field_eve.png"
    image bg21 = "Backgrounds/park_field_night.png"
    image bg22 = "Backgrounds/park_river.png"
    #image bg23 = "Backgrounds/driving_day.png"
    #image bg24 = "Backgrounds/som_livingroom.png"
    #image bg25 = "Backgrounds/som_bedroom.png"

    #Scaled BG for thumbnails
    image bg01s = im.FactorScale("Backgrounds/wrens_bedroom_day.png", 0.27)
    image bg03s = im.FactorScale("Backgrounds/wrens_livingroom_day.png", 0.27)
    image bg05s = im.FactorScale("Backgrounds/school_outside_day.png", 0.27)
    image bg07s = im.FactorScale("Backgrounds/school_hallway_1.png", 0.27)
    image bg09s = im.FactorScale("Backgrounds/hangout_school_day.png", 0.27)
    image bg11s = im.FactorScale("Backgrounds/classroom_1_day.png", 0.27)
    image bg13s = im.FactorScale("Backgrounds/classroom_2_day.png", 0.27)
    image bg15s = im.FactorScale("Backgrounds/cafe_inside_1.png", 0.27)
    image bg17s = im.FactorScale("Backgrounds/resturant_outside.png", 0.27)
    image bg19s = im.FactorScale("Backgrounds/park_field_day.png", 0.27)
    image bg22s = im.FactorScale("Backgrounds/park_river.png", 0.27)
    #image bg23s = im.FactorScale("Backgrounds/driving_day.png", 0.27)
    #image bg24s = im.FactorScale("Backgrounds/som_livingroom.png", 0.27)

    #CG's
    image cg01 = "cgs/tobias_cg.png"
    image cg02 = "cgs/kyran_cg.png"
    image cg03 = "cgs/sh_ev_cg.png"
    image cg04 = "cgs/somwren_cg1-1.png"
    image cg05 = "cgs/somwren_cg1-2.png"
    image cg06 = "cgs/somwren_cg1-3.png"
    image cg07 = "cgs/domwren_cg2-1.png"
    image cg08 = "cgs/domwren_cg2-2.png"
    image cg09 = "cgs/somwren_cg3-1.png"
    image cg10 = "cgs/somwren_cg3-2.png"
    image cg11 = "cgs/somwrendom_cg3-3.png"
    #image extra1 = "cgs/secret_day3_date.png"
    #image extra2 = "cgs/secret_day3_bathroom1.png"
    #image extra3 = "cgs/secret_day3_bathroom2.png"
    #image cg3c1 = "cgs/cg3c1.png"
    #image cg3c2 = "cgs/cg3c2.png"
    #image cg3c3 = "cgs/cg3c3.png"
    #image cg3c4 = "cgs/cg3c4.png"
    #image cg3c5 = "cgs/cg3c5.png"
    #image cg3c6 = "cgs/cg3c6.png"
    #image cg3c7 = "cgs/cg3c7.png"
    #image cg3c8 = "cgs/cg3c8.png"
    #image cg3c9 = "cgs/cg3c9.png"
    #image cg3c10 = "cgs/cg3c10.png"
    #image cg3c11 = "cgs/cg3c11.png"
    #image cg3c12 = "cgs/cg3c12.png"
    #image cg3c13 = "cgs/cg3c13.png"
    #image cg3c14 = "cgs/cg3c14.png"
    image cg12 = "cgs/somwren_cg4-1.png"
    image cg13 = "cgs/somwren_cg4-2.png"
    image cg14 = "cgs/domwren_cg5-1.png"
    image cg15 = "cgs/domwren_cg5-2.png"
    image cg16 = "cgs/owlsom_cg6-1.png"
    image cg17 = "cgs/owldom_cg7-1.png"

    #Scaled CG for thumbnails
    image cg01s = im.FactorScale("cgs/tobias_cg.png", 0.27)
    image cg02s = im.FactorScale("cgs/kyran_cg.png", 0.27)
    image cg03s = im.FactorScale("cgs/sh_ev_cg.png", 0.27)
    image cg04s = im.FactorScale("cgs/somwren_cg1-1.png", 0.27)
    image cg05s = im.FactorScale("cgs/somwren_cg1-2.png", 0.27)
    image cg06s = im.FactorScale("cgs/somwren_cg1-3.png", 0.27)
    image cg07s = im.FactorScale("cgs/domwren_cg2-1.png", 0.27)
    image cg08s = im.FactorScale("cgs/domwren_cg2-2.png", 0.27)
    image cg09s = im.FactorScale("cgs/somwren_cg3-1.png", 0.27)
    image cg10s = im.FactorScale("cgs/somwren_cg3-2.png", 0.27)
    image cg11s = im.FactorScale("cgs/somwrendom_cg3-3.png", 0.27)
    image cg12s = im.FactorScale("cgs/somwren_cg4-1.png", 0.27)
    image cg13s = im.FactorScale("cgs/somwren_cg4-2.png", 0.27)
    image cg14s = im.FactorScale("cgs/domwren_cg5-1.png", 0.27)
    image cg15s = im.FactorScale("cgs/domwren_cg5-2.png", 0.27)
    image cg16s = im.FactorScale("cgs/owlsom_cg6-1.png", 0.27)
    image cg17s = im.FactorScale("cgs/owldom_cg7-1.png", 0.27)


    #Music
    define audio.theme = "audio/sweet_moments.mp3" #music
    define audio.awkward = "audio/sweet_moments.mp3" #music
    define audio.romantic = "audio/sweet_moments.mp3" #music
    define audio.sweet = "audio/sweet_moments.mp3" #music
    define audio.suspence = "audio/sweet_moments.mp3" #music

    #Sounds
    define audio.alarm = "audio/alarm_clock.mp3" #sound
    define audio.door = "audio/door.mp3" #sound
    define audio.shower = "audio/showering.mp3" #sound
    define audio.footsteps = "audio/footsteps.mp3" #sound
    #define glasses = "audio/Partymix1.mp3"
    define audio.opencan = "audio/can_open.mp3" #sound
    define audio.owl = "audio/horned_owl.mp3" #sound
    define audio.fallen = "audio/painful_hurt.mp3" #sound
    define audio.sms = "audio/sms_alert.mp3" #sound
    define audio.cafe = "audio/cafe_noise.mp3" #sound
    define audio.night = "audio/nightime.mp3" #sound
