#images used in-game and gallery
init-1:

### Logos ######################################################################
################################################################################
    image logo = "Logo.png"
    image logothumb = im.FactorScale("owl.png", 0.60)
    image logo3 = "Logo3.png"
    image warning = "18_warning.png"
    image lock = im.FactorScale("lock_logo.png", 0.65)
    image lock2 = im.FactorScale("lock_logo2.png", 1.0)
    image warning_text_blink:
        "warning_text"
        pause 0.5
        linear .5 alpha 0.0
        pause 0.5
        linear .5 alpha 1.0
        repeat
    image warning_text = Text(_("{font=fonts/immortal.ttf}R18 Warning{/font}"), size=100)
### Colors #####################################################################
################################################################################
    image blk = "#000"
    image wht = "#f4f4ff"
    image grn = "#637044"
    image gry = "#696969"

### Names ######################################################################
################################################################################
    #Sprite peremeters
    define A = Character("Author", color = "#ffffff")
    define uv = Character("Unknown Voice", color = "#a9a9a9")
    define f = Character("Figure", color = "#a9a9a9", what_font = "fonts/exquisite-corpse.ttf")
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
    define d_s = Character("Dominic & Somchai", color = "#ffffff")
    define nur = Character("Nurse", color = "#ffffff")
    define doc = Character("Doctor", color = "#ffffff")

### Sprites ####################################################################
################################################################################

#### Wren ######################################################################
    image wren reg = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren happy = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren happy blush = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren sad = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren angry = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren surprised = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren surprised blush = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren thinking = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)
    image wren embarrassed = Image("Sprites/wren_reg.png", 0.1, xanchor=0.5, yoffset=-50)

### Somchai ####################################################################
    image somchai reg = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai happy = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai happy blush = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai sad = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai angry = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai surprised = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai surprised blush = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai thinking = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)
    image somchai embarrassed = Image("Sprites/somchai_reg.png", xanchor=0.5, yoffset=-20)

### Dominic ####################################################################
    image dominic reg = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=-60)
    image dominic happy = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=-60)
    image dominic happy blush = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=-60)
    image dominic sad = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=-60)
    image dominic angry = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=-60)
    image dominic surprised = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=-60)
    image dominic surprised blush = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=-60)
    image dominic thinking = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=-60)
    image dominic embarrassed = Image("Sprites/dominic_reg.png", xanchor=0.5, yoffset=-60)

### Tobias #####################################################################
    image tobias reg = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias happy = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias sad = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias angry = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias surprised = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias thinking = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)
    image tobias embarrassed = im.FactorScale("Sprites/tobias_reg.png", 0.998, xanchor=0.55, yoffset=-60)

### Kyran ######################################################################
    image kyran reg = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.5, yoffset=-50)
    image kyran happy = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.5, yoffset=-50)
    image kyran sad = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.5, yoffset=-50)
    image kyran angry = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.5, yoffset=-50)
    image kyran surprised = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.5, yoffset=-50)
    image kyran thinking = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.5, yoffset=-50)
    image kyran embarrassed = im.FactorScale("Sprites/kyran_reg.png", 0.98, xanchor=0.5, yoffset=-50)

### Shaula #####################################################################
    image shaula reg = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.55, yoffset=15)
    image shaula happy = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.55, yoffset=15)
    image shaula sad = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.55, yoffset=15)
    image shaula angry = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.55, yoffset=15)
    image shaula surprised = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.55, yoffset=15)
    image shaula thinking = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.55, yoffset=15)
    image shaula embarrassed = im.FactorScale("Sprites/shaula_reg.png", 0.9, xalign=0.55, yoffset=15)

### Evanora ####################################################################
    image evanora reg = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora happy = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora sad = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora angry = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora surprised = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora thinking = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)
    image evanora embarrassed = Image("Sprites/evanora_reg.png", xalign=0.5, yoffset=-50)

### Side-characters ############################################################
    image owl = im.FactorScale("Sprites/owl_sprite.png",0.8, xalign=0.5, yalign=0.5)
    image figure = im.FactorScale("Sprites/figure.png",1.0 , xalign=0.5, yalign=0.0)
    image doctor = Placeholder("boy")

### Sprite Gallery #############################################################
    image wren_gallery = Composite(
        (1280,720),
        (0,0), "sprite_gallery_back.png",
        (50,0), "Sprites/wren_reg.png",
        (380,20), "wren_sgb.png")
    image dominic_gallery = Composite(
        (1280,720),
        (0,0), "sprite_gallery_back.png",
        (-30,0), "Sprites/dominic_reg.png",
        (380,20), "dominic_sgb.png")
    image somchai_gallery = Composite(
        (1280,720),
        (0,0), "sprite_gallery_back.png",
        (0,0), "Sprites/somchai_reg.png",
        (380,20), "somchai_sgb.png")
    image tobias_gallery = Composite(
        (1280,720),
        (0,0), "sprite_gallery_back.png",
        (0,0), "Sprites/tobias_reg.png",
        (380,20), "tobias_sgb.png")
    image kyran_gallery = Composite(
        (1280,720),
        (0,0), "sprite_gallery_back.png",
        (-50,0), "Sprites/kyran_reg.png",
        (380,20), "kyran_sgb.png")
    image shaula_gallery = Composite(
        (1280,720),
        (0,0), "sprite_gallery_back.png",
        (-50,0), "Sprites/shaula_reg.png",
        (380,20), "shaula_sgb.png")
    image evanora_gallery = Composite(
        (1280,720),
        (0,0), "sprite_gallery_back.png",
        (0,0), "Sprites/evanora_reg.png",
        (380,20), "evanora_sgb.png")
    image figure_gallery = Composite(
        (1280,720),
        (0,0), "sprite_gallery_back.png",
        (0,0), "Sprites/figure.png",
        (380,20), "figure_sgb.png")

### Sprite Thumbnails ##########################################################
    image wren_thumb = im.FactorScale("Sprites/wren_reg_thumb.png",1.0, xalign=0.5, yalign=0.5)
    image dominic_thumb = im.FactorScale("Sprites/dominic_reg_thumb.png",1.0, xalign=0.5, yalign=0.5)
    image somchai_thumb = im.FactorScale("Sprites/somchai_reg_thumb.png",1.0, xalign=0.5, yalign=0.5)
    image tobias_thumb = im.FactorScale("Sprites/tobias_reg_thumb.png",1.0, xalign=0.5, yalign=0.5)
    image kyran_thumb = im.FactorScale("Sprites/kyran_reg_thumb.png",1.0, xalign=0.5, yalign=0.5)
    image shaula_thumb = im.FactorScale("Sprites/shaula_reg_thumb.png",1.0, xalign=0.5, yalign=0.5)
    image evanora_thumb = im.FactorScale("Sprites/evanora_reg_thumb.png",1.0, xalign=0.5, yalign=0.5)
    image figure_thumb = im.FactorScale("Sprites/figure_thumb.png",1.0, xalign=0.5, yalign=0.5)

### Backgrounds ################################################################
################################################################################
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
    image bg22d = "Backgrounds/park_river_day.png"
    image bg22 = "Backgrounds/park_river.png"
    image bg23 = "Backgrounds/driving_day.png"
    image bg23n = "Backgrounds/driving_night.png"
    image bg24 = "Backgrounds/som_livingroom.png"
    #image bg25 = "Backgrounds/som_bedroom.png"
    #image bg26 = "Backgrounds/owl_room.png"
    #image bg27 = "Backgrounds/city_overlook_night.png"
    image bg28 = "Backgrounds/hospital_inside.png"
    image bg29 = "Backgrounds/hospital_outside.png"

### Background Thumbs ##########################################################
################################################################################
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
    image bg22s = im.FactorScale("Backgrounds/park_river_day.png", 0.27)
    image nightmares = im.FactorScale(im.Grayscale("Backgrounds/park_river.png"), 0.27)
    image bg23s = im.FactorScale("Backgrounds/driving_day.png", 0.27)
    #image bg24s = im.FactorScale("Backgrounds/som_livingroom.png", 0.27)
    #image bg26s = im.FactorScale("Backgrounds/owl_room.png", 0.27)
    image bg28s = im.FactorScale("Backgrounds/hospital_inside.png", 0.27)

### Computer Graphics ##########################################################
################################################################################
    image cg01 = "cgs/tobias_cg.png"
    image cg02 = "cgs/kyran_cg.png"
    image cg03 = "cgs/sh_ev_cg.png"
    image cg04_1 = "cgs/somwren_cg1-1.png"
    image cg04_2 = "cgs/somwren_cg1-2.png"
    image cg04_3 = "cgs/somwren_cg1-3.png"
    image cg05_1 = "cgs/domwren_cg2-1.png"
    image cg05_2 = "cgs/domwren_cg2-2.png"
    image cg06_1 = "cgs/somwren_cg3-1.png"
    image cg06_2 = "cgs/somwren_cg3-2.png"
    image cg06_3 = "cgs/somwrendom_cg3-3.png"
    image cgsecret1_1 = "cgs/secret_day3_date.png"
    image cgsecret1_2 = "cgs/secret_day3_bathroom1.png"
    image cgsecret1_3 = "cgs/secret_day3_bathroom2.png"
    image cg7_1 = "cgs/cg7_1.png"
    image cg7_2 = "cgs/cg7_2.png"
    image cg7_3 = "cgs/cg7_3.png"
    image cg7_4 = "cgs/cg7_4.png"
    image cg7_5 = "cgs/cg7_5.png"
    image cg7_6 = "cgs/cg7_6.png"
    image cg7_7 = "cgs/cg7_7.png"
    image cg7_8 = "cgs/cg7_8.png"
    image cg7_9 = "cgs/cg7_9.png"
    image cg7_10 = "cgs/cg7_10.png"
    image cg7_11 = "cgs/cg7_11.png"
    image cg7_12 = "cgs/cg7_12.png"
    image cg7_13 = "cgs/cg7_13.png"
    image cg7_14 = "cgs/cg7_14.png"
    image cg7_15 = "cgs/cg7_15.png"
    image cg7_16 = "cgs/cg7_16.png"
    image cg7_17 = "cgs/cg7_17.png"
    image cg7_18 = "cgs/cg7_18.png"
    image cg7_19 = "cgs/cg7_19.png"
    image cg7_20 = "cgs/cg7_20.png"
    image cg08 = "cgs/owlsom_cg6-1.png"
    image cg09 = "cgs/owldom_cg7-1.png"
    image cg10 = "cgs/dom_carry_wren.png"
    image cg11_1 = "cgs/cg11_1.png"
    image cg11_2 = "cgs/cg11_2.png"
    image cg11_3 = "cgs/cg11_3.png"

### Computer Graphics (Thumbs) ###################################################
################################################################################
    #Scaled CG for thumbnails
    image cg01s = im.FactorScale("cgs/tobias_cg.png", 0.27)
    image cg02s = im.FactorScale("cgs/kyran_cg.png", 0.27)
    image cg03s = im.FactorScale("cgs/sh_ev_cg.png", 0.27)
    image cg04s = im.FactorScale("cgs/somwren_cg1-1.png", 0.27)
    image cg05s = im.FactorScale("cgs/domwren_cg2-1.png", 0.27)
    image cg06s = im.FactorScale("cgs/somwren_cg3-1.png", 0.27)
    image cgsecret1_1s = im.FactorScale("cgs/secret_day3_date.png", 0.27)
    image cg07s = im.FactorScale("cgs/cg7_1.png", 0.27)
    image cg08s = im.FactorScale("cgs/owlsom_cg6-1.png", 0.27)
    image cg09s = im.FactorScale("cgs/owldom_cg7-1.png", 0.27)
    image cg10s = im.FactorScale("cgs/dom_carry_wren.png", 0.27)
    image cg11s = im.FactorScale("cgs/cg11_1.png", 0.27)
    #image cg12s = im.FactorScale("", 0.27)
    #image cg13s = im.FactorScale("", 0.27)
    #image cg14s = im.FactorScale("", 0.27)
    #image cg15s = im.FactorScale("", 0.27)
    #image cg16s = im.FactorScale("", 0.27)
    #image cg17s = im.FactorScale("", 0.27)

### Achievements ###############################################################
################################################################################
    #image ach01 = im.FactorScale("ach/ach01.png", 0.27)

### Music ######################################################################
################################################################################
    define audio.theme1 = "audio/theme_1.mp3" #music
    define audio.theme2 = "audio/theme_1.mp3" #music
    define audio.awkward = "audio/sweet_moments.mp3" #music
    define audio.romantic = "audio/sweet_moments.mp3" #music
    define audio.sweet = "audio/sweet_moments.mp3" #music
    define audio.suspence = "audio/suspense.mp3" #music

### Sounds #####################################################################
################################################################################
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
    #define audio.sex1 = ""
