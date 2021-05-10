label day4:
    #Day 4 Start#
    #We see a black screen. That turns to show Dominic and Somchai fighting in the park both looking angry.
    #Dominic throws a mean left hook at Somchai. They start arguing.
    play music suspense
    scene nightmare with flash2
    "As Wren opens his eyes, he sees Dominic and Somchai fighting."
    show dominic angry at pos3
    show somchai angry at pos7
    """
    *YAWNS*{w} What in the flying fuck. It’s too early for this clown shit.

    Yet here we are in the midst of a shitshow. Why can’t they both just leave me alone?
    Maybe I should stop them?
    """
    show figure at pos5 with dissolve
    f "They are not your only problems."
    w "Not you again."

    hide figure with dissolve

################################################################################
    $ shuffle_menu()
    menu:

        "I'm tired of this"

        "Go stop the fight!":
            $ dominic_points += 1

            d "Screw you. I’ll make him fall in love with me, twat."
            s "Good luck. He already loves me, meathead."
            d "Not for much longer."
            s "You will never have the connection I have with Wren."
            d "Your right. I’ll have a better one."
            w "Knock it off you assholes! You're causing a scene!"
            show blk
            hide nightmare
            "Darkness consumes Wren and everything goes black."
            show figure at pos5 with dissolve
            pause 1.0
            f "If you keep being like this, you will surely fall!"

            jump day4_1

        "Do nothing":
            $ somchai_points += 1

            d "Screw you. I’ll make him fall in love with me, twat."
            s "Good luck. He already loves me, meathead."
            d "Not for much longer."
            s "You will never have what I have with Wren."
            d "Your right, what I’ll have with Wren will be so many times better."
            s "You don’t know him like I do, and you never will."
            show blk
            hide nightmare
            "Darkness consumes Wren and everything goes black."
            show figure at pos5 with dissolve
            pause 1.5
            f "If you keep being like this, you will surely fall!"

            jump day4_1

################################################################################

label day4_1:

    $ day += 1

    stop music
    show bg01 with flash1
    with hpunch
    hide figure with dissolve
    show wren surprised at pos5
    "Wren wakes up in a rage and nearly hits his head on his bed frame."
    w "What in the fuckity fuck was that?! {i}They are not your only problems? If you keep being like this, you will surely fall!{/i}"
    w "What the fuck is that even supposed to mean? Ominous voice figure thing. UHHHHHH!!!"
    #Kryan enters#
    show kyran reg at pos2 with easeinleft
    k "Wakey! Wakey! We need to go get coffee now so we’re not \"late-y\"."
    w "That does not rhyme correctly. I have to go get dressed first. Of course, we’re getting coffee. What kind of day is it if we don't?"
    k "Your right. Hurry though!!!!!!!!!!!!!"

    #Cafe#
    scene bg16 with dissolve
    show wren reg at pos7dwn
    show kyran reg at pos2dwn
    play sound cafe fadein 3.0 loop
    #Wren and Kyran drink their coffee in the middle of the cafe. Off to the side Somchai is watching unnoticed by Wren and Kyran.#
    k "What a beautiful day! It’s sunny! We have our coffee and class does not start for 30 more minutes."
    w "Yeah and you really acted like we were going to be late."
    k "We needed ample time to enjoy it, Wren."
    "He’s right! I feel my soul slowly returning to my body with this delectable sweet, delicious coffee. Breathe in and out.
    Today will be a good day! Think positive!"
    w "You're right it is a nice day. I am enjoying our ample time. My soul just returned to my body. It feels like."
    k "Well not to burst both our bubbles but I just noticed Somchai. What the literal hell! How long has he been there?"
    w "*SIGHS*"
    k "Should I go kick his ass?"
    w "No, let's just ignore him."
    "My soul has once again left my body. Why can’t he just leave me in peace? My dream said what it said.
    Therefore, I need them to leave me alone today. So, I can get it out of my head."
    k "He’s still staring like the mopey edgy lord he is. Why can’t Wren just forgive me? I only shattered him to pieces.
    I still deserve forgiveness because I am entitled to it. I bet that’s what he’s thinking."
    w "Can we please just let this go? Who cares what he’s thinking."
    k "I care... He can’t just hurt you and act like nothing happened."
    "Kyran has a look of murder on his face. It’s all distorted with anger. I don’t like that.
    Somchai still is quietly standing in the corner of the coffee shop observing still but no words leave his lips."
    "Kyran looks over to Somchai and yells."
    stop sound
    k "Hey Dipshit! Yes you!"
    w "Will you shut up before you get us kicked out!"
    k "Come tell us what you want!"
    show somchai reg at pos9 with easeinright
    s "Sorry to bother you. I was just wondering how you are doing today, Wren? I noticed you got a sweet drink and found it odd."
    w "I alternate drinks. Somethings have changed since you left."
    s "I am very sorry I left. You know I am. It was hard for me, too."
    w "It’s harder when you don’t know why, Somchai."
    s "That is understandable. I will not leave again. If you give me the chance I will not."
    k "Have you considered Wren might not want you back? Do you really think you can just come back, and everything will be okay?"
    "I wish he didn't look like a lost puppy dog. It makes this inevitably harder on me. Kyran might kill him if he stays here any longer though."
    w "I don’t think now is an appropriate time for that conversation."
    s "You are right. I will leave first then."
    hide somchai with easeoutright
    "Wren and Kyran resume drinking their coffee. Somchai still watches from afar this time better concealed."
    show blk with dissolve
    "They both walk to class after they finish their coffee. Somchai still watches them but slowly fades into the background."

    #Class#
    scene bg13 with fade
    pause 0.5
    play music theme1
    show wren reg at pos5dwn
    show tobias reg at pos2dwn
    show kyran reg at pos8dwn
    "*Breathe* Continue my peaceful existence.{w} *Breathe* Continue my peaceful existence."
    t "So what are we going to do about Somchai?"
    w "There is no \"we\" in this equation."
    t "There totally is! We as your friends need to help you not fall back into the arms of Somchai."
    "In a stern whisper Wren responds."
    w "{b}THERE IS NO WE IN THIS EQUATION. FOCUS ON SOMETHING MORE USEFUL THAN MY LIFE...{/b}{w} like this class."
    stop music fadeout 1.0
    "Tobias and Kyran looked at Wren in shock for a moment before looking at each other than looking back down at their papers, dejected."
    t "Okay, I get it. Then what are you going to do about it?"
    w "I don’t know yet..."
    t "That might be something you might want to figure out."
    "Kyran covers Tobias’s mouth and whispers into his ear."
    k "Just Shush."
    "Kyran and Tobias settle down a bit and focuses on the teacher…"
    show blk with fade
    hide wren
    hide tobias
    hide kyran
    show wren reg at pos5
    """
    Somchai is naturally very charming. Which makes my life REALLY SO MUCH FUCKING EASIER!!! AM I RIGHT?!?!

    It’s hard not to feel bad for him but it’s way too soon to forgive him. Even if he gets all mopey.

    UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!{nw}
    """
    show blk
    hide wren

    #Outside of class#
    scene bg07
    show wren reg at pos5 with easeinleft
    " After class, Tobias and Kyran leave for their next class leaving Wren to his own devices."
    w "While I love Tobias, he has been a bit much for me lately. What will we do about Somchai? Hell, if I know."
    #Enter Dominic#
    "Wren thinks internally."
    "Hell, if I know what I’ll do about Dominic either…"
    show dominic reg at pos8 with easeinright
    "Was he waiting there this whole time?"
    d "Coffee as sweet as you."
    w "...Thanks"
    show wren thinking
    "Okay, so he was waiting then. How did he know what class I even was in? I never say no to coffee, but this is a bit weird."

################################################################################
    $ shuffle_menu()
    menu:

        "How should I feel about this?"

        "Ask him how he knew": #Somchai#:
            $ somchai_points += 1

            show wren reg
            "How did he know? Who told him? Is it common knowledge. Is he stalking me, too?"
            w "How did you know what class I was in?"
            d "Just intuition."
            w "Really?"
            d "I feel that I may have overstepped yesterday. Though he seems like a massive prick.
            I thought I should do something nice for you."
            w "You just don’t know him. He has his moments."
            d "He obviously hurt you. Why defend him?"
            w "Because I did once care for him."
            "Well, this is a bit uncomfortable."
            w "Well, I need to go see my girls, but thanks again."
            d "So... see you around then..."
            "Wren awkwardly walks away towards the hang out tree."
            jump day4_2

        "Brush it off": #Dominic#:
            $ dominic_points += 1

            show wren reg
            d "I saw you during my daily jog entering the building.
            I felt that maybe I overstepped a bit yesterday and should apologize."
            w "Oh, thank you!"
            d "You're so adorable. You already thanked me."
            "Well, this is a bit cute."
            w "Well, I need to go see my girls but thanks again."
            d "See you around then!"
            "Wren waves goodbye to Dominic and walks towards the hang out tree."
            jump day4_2

#################################################################################

label day4_2:

    scene bg09 with dissolve
    show somchai sad at pos5
    "Wren passes through the quad near pretty flowers. He sees Somchai but continues to walk towards Shaula and Evanora"
    "Oh god…, there’s Somchai again. Do not engage. DO NOT ENGAGE!"
    hide somchai
    show evanora reg at pos4
    show shaula reg at pos2
    play music theme1
    show wren reg at pos7 with easeinright
    sh "So how did the date go?"
    w "Don’t even worry about it. It did not exactly happen."
    E "Meaning? Should we go fight him?"
    sh "Poor Wren. He did not stand you up did he?"
    w "No, he didn’t. He just came storming in, guns a blazing, when Somchai was explaining his disappearance. You know the one with zero explanation."
    sh "What was his reasoning? It better be good."
    w "He had to move back to Pattaya, and he said he couldn’t go against his parents demands. Unfortunately, for me, he wasn't man enough to tell me then."
    sh "Are you serious?...{w} WHAT KIND OF REASONING IS THAT!?"
    "Shaula explodes like a hand grenade during war time. Shaking the person closest to her for no reason.{w} ...Poor Evanora."
    E "He was too scared to tell you. So, he just emotionally wrecked you by not telling you, great."
    w "It gets worse. He even said he would have proposed just so he could be with me forever."
    sh "That is one juicy bombshell."
    E "Fuck, that has to mess with your head a bit."
    w "Yeah...{w} a bit...{w} It definitely messed with my head. My peaceful existence keeps getting disturbed."
    sh " *SIGHS* Has existence ever really been peaceful?"
    w "No, but I like to pretend it is. This is just one big stressful mess. It feels all so unnecessary."
    E "Do you know what you will do? It’s okay if you don’t. We are here for you."
    w "Thank you. I don’t know yet. It feels too soon to decide anything."
    sh "How about we met outside of your last class? We have a nice relaxing night or something to get your mind off two hot boys fighting over you."
    w "Don’t tease me! This is seriously fucking stressful. Never thought it would be me who would end up being an anime protagonist."
    sh "I know it is, but it got you to smile for a second at least."
    w "Fuck… I have class soon already."
    sh "It’s okay. Like a bird, fly into the loving embrace of your academics to get your mind off the loving embrace of two hot boys fighting over you."
    w "Bye you two. See you in an hour."
    show blk
    "Taking a deep breath, he turns and heads off to class."
    stop music fadeout 1.3
    #Class#

    scene bg13
    "Pay attention. This information is important for the midterm. Do not worry about boy problems. Gods, could this class be any longer?"
    scene bg13 with pixellate
    "30 minutes later... Wren heads out of class to meet up with his friends."
    #Class is dismissed#
    #After Class#

    scene bg09 with dissolve
    show wren reg at pos5 with easeinright
    """
    Finally, the day is over. I can continue my peaceful existence with my girls...{w} or not...{w}

    What are they watching?{w} I thought only my girls were coming but there’s Kyran and Tobias.
    """
    hide wren with easeoutleft
    show kyran reg at pos1
    show evanora surprised at pos3
    show tobias angry at pos5
    show shaula happy at pos7
    show wren reg at pos9 with easeinright
    play music theme2
    w "Ooh, what are we watching?"
    k "If you look 90 degrees to your left, you’ll see two man babies fighting."
    "Confused, Wren looks to his left. Off in the distance, an average Thai man points his finger at a taller man in basketball shorts."
    stop music
    "Fuck! Somchai and Dominic are fighting in the middle of the goddamn park."
    E "This does not have anything to do with you right?"
    t "Somchai, what a twat, he is picking a fight with someone much bigger than him."
    play music suspense
    hide wren
    hide kyran
    hide evanora
    hide tobias
    hide shaula
    hide bg09
    show bg09
    show dominic reg at pos6
    show somchai reg at pos4
    d "Screw you! I’ll make him fall in love with me, you punk!"
    s "Good luck. He already loves me meathead."
    "Oh God! This is just like my dream, right?"
    show blk
    hide dominic
    hide somchai
    hide blk
    show wren surprised at pos5 with flash1
    "Wren stands there completely still. He tries to step forward, but his legs don’t move."
    "Legs start working! Start walking the other way, smart one."
    hide wren with moveoutright
    "Wren starts running away and having a panic attack. Tears stream down his face as he hyperventilates.
    He is unable to control his breathing and eventually gets lightheaded. Everything suddenly goes dark, and he can’t see anything."
    play sound fallen
    stop music
    show blk with flash2
    #Screen goes black#
    #Day 4 End#
    jump day5
