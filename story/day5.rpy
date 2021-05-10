label day5:

    $ day += 1

    #Start of Day 5#
    scene gry
    "The black room fades to grey. Off in the distance there seems to be two people having an argument."
    "These people are blurry, but he can tell it’s Somchai and Dominic."
    w "*screams*"
    #The image fades and cracks to black#
    #Wren wakes up in the hospital#

    #show bg28 with flash2
    scene bg28 with flash2:
        subpixel True
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.02
        alignaround (.5, .5)
        linear 5.0 yalign 1.0 clockwise circles 1
        repeat 3

    $ persistent.unlock_bg28 = True
    $ renpy.notify("New Background Unlocked")
    show kyran reg at pos8
    "Wren is a bit disoriented and the room shakes around him. Sitting in a chair is Kyran.
    Kyran notices Wren awake."
    k "I’ll go get the Doctor."
    hide kyran with easeoutleft
    "Shit I really did pass out. Ahh! Come back to me world."
    #Doctor Enters Quickly#
    show kyran reg at pos8 with easeinleft
    #show doctor at pos3 with easeinleft
    play music theme1 fadein 2.0
    doc "Good Afternoon, Wren."
    w "Hi, doctor."
    doc "Let's get started shall we. Wren, do you have a past history of panic attacks?"
    w "No."
    doc "Do you have any past history of anxiety?"
    w "No..."
    doc "Does your family have any issues with Anxiety?"
    w "No......"
    "No offense to doctor man, but all my answers to the questions will be \"No\".
    So, like can we hurry this up here. So, I can continue my peaceful existence."
    doc "Is there anyone in your family we can contact to verify this information?"
    w "No, I am not in contact with them and would prefer to keep it that way."
    doc "Okay. I can recommend we put you on medication."
    w "No, need. I think this is just a one-time incidence."
    doc "We will release you today then. Just remember to come back if you have any more issues."
    #Doctor exits slowly seeming unsure about releasing him#
    "The Doctor looks at Kyran, then back at Wren, a little worried he set off out of the room."
    #hide doctor with easeoutleft
    k "You should know everyone was really worried. I made them all go home at 2 am."
    w "What time is it now?"
    k "It’s almost been a day Wren."
    w "Damn, I survived this long without coffee. You better get me some quick before I die!!!! "
    k "I’ll get you coffee before we leave. Also, don’t worry I told the teacher you wouldn’t be in class today.
    Though, it seems you were more occupied with your thoughts of coffee. But luckily you have the weekend to rest, and so do I."
    w "Sorry you were here all night. And that I made you worry."
    k " It’s fine, Wren. Now, you can be honest with me, you know.
    Are you stressed because of the dealings with the tribe or the boy issues?"
    "In all honesty it’s probably a mixture of both. I don't want to tell Kyran that, though.
    Just be honest you clown."
    w "I think it’s a bit of both."
    k "Well, everyone was worried about you: the tribe, our friends, the \"himbo\" and the cold prince."
    w "Cold prince?"
    k "You like Somchai’s new nickname? You get it because he’s cold to everyone but you.
    He’s so formal all the time too. They were so worried about you they stopped their little fist fight."
    w "It became a fist fight?"
    "Jesus fucking Christ can these two get a life. Preferably one that does not revolve around making mine difficult."
    k "Yeah, before you passed out Dominic through a mean left hook at Somchai.
    Excuse me, let me correct myself, that himbo threw a nasty left hook right in that asshole’s face."
    w "Did Somchai fight back?"
    k "Hell yeah he did. That boy has anger issues too."
    w "I wish they wouldn’t fight."
    k "Don’t we all. They were both really concerned though. *rolls eyes*"
    w "Fighting doesn't solve anything. He made the right option."
    k "Whatever you say."
    "A knock comes from the door and a tiny voice is heard before a nurse enters."
    nur "Here are your papers for your release. You should be out within the hour."
    w "Thank you."
    stop music

    scene bg29
    show wren reg at pos4 with easeinleft
    show kyran reg at pos2 with easeinleft
    "After about an hour of waiting, Wren is finally able to leave.
    Him and Kyran start walking out of the hospital as two familiar guys walk up to them."
    #Enter Dominic and Somchai#
    show somchai reg at pos6 with easeinright
    show dominic reg at pos8 with easeinright
    d "I’m sorry."
    s "I’m more sorry. My arrogance caused the fight."
    d "I’m double sorry!"
    "Gods, what is this? A game of who’s sorrier?"
    k "Cut it out you two."
    d "We didn’t mean to stress you out."
    w "You know I’m stressed about a lot of things. Not just you two.
    You need to get over yourselves, quite honestly. There was no reason to get physical with each other.
    That is quite frankly greatly unappealing to me."
    d "I am greatly sorry that it came to that point."
    s "I’m sorry that it came to that point as well."
    k "Enough. He doesn’t want to hear it."
    #At same time#
    d_s "Can I take you out to make it up to you?"
    "Dominic and Somchai looked at each other."
    d_s  "I asked him first?"
    k "You said it at the same time you idiots."
    "What an absolute joke… They need to grow up."
    "Kyran leans over to Wren and whispers into his ear."
    k "I’d recommend you chose one to go out with. If not they’ll never let us
    leave and I want to go home. Nicki’s got a new release tonight. I heard it’s the next anaconda."
    w "Uuuuuhh~ keep me posted on the new release."

    #If Kyran: go with Kyran and end of day.#
    #If Somchai: go with somchai then have the option to go with Dominic or go home with kyran.#
    #If Dominic: go with Dominic then have the option to go with Somchai or go home with kyran.#

################################################################################

    default persistent.som5 = False
    default persistent.dom5 = False
    default persistent.somdom5 = False
    $ shuffle_menu()
    menu day_5_date:

        "Who should I go with?"


        "Go with Somchai first":
            $ somchai_points += 1

            "Wren decides that he has the strength to deal with these guys."
            w "Okay, I’ll hang out with both of you. But, if I feel tired, I'm going home so be on your best behavior."
            d_s "Of course!"
            w "First, I’ll go with Somchai and when I’m finished, I’ll text you Dominic. Sounds good?"
            "Dominic and Somchai vigorously nod. Somchai and Wren leave the two and head to his car. They end up closer downtown."

            show blk
            $ persistent.somdom5 = True
            jump som_day_5

        "Go with Dominic first":
            $ dominic_points += 1

            "Wren decides that he has the strength to deal with these guys."
            w "Okay, I’ll hang out with both of you. But, if I feel tired, I'm going home so be on your best behavior."
            d_s "Of course!"
            w "First, I’ll go with Dominic and when I’m finished, I’ll text you Somchai. Sounds good?"
            "Dominic and Somchai vigorously nod. Dominic and Wren leave the two and head towards the direction of downtown."

            show blk
            $ persistent.somdom5 = True
            jump dom_day_5

        "Go with Kyran":
            $ dominic_points -= 1
            $ somchai_points -= 1

            "Wren decides that he’s tired of the boys’ antics for one day and chooses to go with Kyran."
            w "Come on Kyran I’m angry at these fools."
            k "Okay, Wren, let’s go."
            show blk
            "Kyran and Wren walk away from the boys. When Wren looks back the two losers, full of defeat, stare back at Wren."
            "They need to learn how to be adults."

            jump ky_day_5

################################################################################
################################################################################

label som_day_5:
    #Spending time with Somchai#

    #Day 5 continued#
    scene bg17
    $ persistent.unlock_bg17_18 = True
    $ renpy.notify("New Background Unlocked")
    show somchai reg at pos5 with easeinright
    show wren reg at pos8 with easeinright
    "Wren and Somchai walk together silently until Somchai comes to an abrupt stop in front of a diner."
    #Outside of Diner#
    s "If I still remember correctly, it’s best to feed you before we talk."
    w "You remember I liked this diner?"
    s "I remember you feeling out of place when we went to places that were more \"high end\"."
    w "I have not come back since you left."
    s "I will do everything I can to make up for it. If you let me."
    "Wren felt his heart start to beat faster. Somchai always has that effect on him."
    w "Let's go in."
    scene bg18
    play sound cafe fadein 3.0 loop
    "Somchai and Wren enter the diner. They quickly get seated. Somchai politely
    pulls out Wren’s chair and lets him sit first. They both order pancakes and coffee."
    show wren reg at pos6dwn
    show somchai reg at pos4dwn
    w "Did you enroll at my college?"
    s "I did. It is a nice school, and you were there. It made sense once coming
    back I enrolled in the same college as you."
    w "What field?"
    s "Pre-medical Biology"
    "That doesn’t seem right. I know he doesn’t want to be a doctor. He wants to be a musician."
    w "You would much rather be a musician though? Why would you give up on that?"
    s "My family has high expectations for me. I have high expectations of myself
    because of it, too. It would be easier for me to provide for you if I was a Doctor."
    w "I would rather you follow your dream. I’m following mine. You should do the same."
    s "Are you at least open to getting back together?"
    w "I do miss you. But right now, I’m still upset."
    "Fuck... It's hard when he looks at me with those eyes. I never fully got over him.
    Though it’s the truth. It is too soon for me to know if I want us to get back together."
    s "Remember that one time we went ice skating. We both kept falling.
    Every Time I am with you, I fall deeper, Wren. I know what I did is hard to forgive,
    but I just want you to know I’ll never stop falling for you, Wren.
    Hopefully, we can move past this, and who knows, maybe get back together."
    w "I remember. I was so sore the next day. Falling for you was hard and I do not want things to be harder on me, Somchai.
    Give me some time, please. Please stay out of fights with Dominic, too; It’s not worth it."
    s "I am just trying to keep and protect what’s mine, Wren."
    w "You don't own me Somchai; remember that."
    s "I did, and I intend to again. I’ll give you time though."
    "The waiter comes with the food and then quickly dashes away."
    w "What did you miss the most about me?"
    s "I missed watching and seeing you be headstrong. It was really inspiring.
    I miss you teasing me too. I miss the things we used to do together. I miss all of it. I miss us.
    There’s a divide now and I, so, desperately want to have you back."
    w "I don’t know if I will ever get over you leaving."
    s "I will wait forever then. Forever is worth it if it’s for you."
    stop sound fadeout 3.0
    scene bg17
    hide wren
    hide somchai
    "Wren and Somchai finish eating and exit the diner."
    show somchai happy at pos8 with easeinleft
    show wren reg at pos5 with easeinleft
    s "Let’s go out again soon. Maybe we can go ice skating"
    w "It was nice talking to you again. I’ll let you know if I feel up to it."
    hide somchai with easeoutright
    "Wren and Somchai go their separate ways."
    "After Wren is finally alone, he takes his phone out to text..."
    #Go to Dominic (Day5_Dominic)#
    #Go home to meet Kryan (Day5_Kryan)#

################################################################################
    $ persistent.som5 = True
    menu:

        "Who should I go with, now?"

        "Kyran":

            "Deciding it’s time to head home, Wren texts Kyran to pick him up."
            "A moment later he gets a confirmation that Kyran is on his way."
            show blk
            jump ky_day_5

        "Dominic" if not persistent.dom5:

            "After he gets a reply, he goes to meet up with Dominic up the street."
            show dominic reg at pos3 with easeinleft
            d "Hey, Wren, how are you feeling?"
            w "I’m okay, so what are we going to do?"
            d "Follow me."

            jump dom_day_5

################################################################################
################################################################################

label dom_day_5:
    #Spending time with Dominic#

    define dom_carry = False
    scene blk
    #Day 5 continued#
    "Dominic and Wren walk through the city together. The walk is uphill, and Wren starts to feel tired."
    scene bg19
    hide blk
    show dominic reg at pos7 with easeinleft
    show wren reg at pos4 with easeinleft
    w "You know I just got out of the hospital, right? Where are we going?"
    d "Are you tired? I can carry you..."

################################################################################
    $ shuffle_menu()
    menu:
        "Let him carry you" if dominic_points >= 4:
            $ dom_carry = True
            $ dominic_points += 1

            "What’s the worst that can happen? He keeps me warm?"
            w "Okay, carry me. But no funny business!"
            d "I would never! Okay hold on, then."
            show blk
            "Dominic quickly wraps his arms around Wren and lifts him up like he weighs nothing."
            hide blk
            #show cg10
            w "Wow, you picked me up like I was a bag of feathers."
            d "I think you lost weight… you are pretty light."
            play music sweet

        "Say: \"I’m not that tired\"":
            $ dominic_points -= 1

            w "I’m not that tired"
            d "It’s just a little longer. It’ll be really cool. Trust me. Just hang in there."
            "Dominic obviously has good intentions but I cannot tell if he’s trying to kill me or not.
            I was not meant for hiking in this life."

################################################################################

    w "I cannot recall if I have asked what’s your major?"
    d "Take a guess. ITS A SUPERCOOL MAJOR!!!!!"
    w "I don’t know... hmmmm~ something sporty probably."
    d "It’s exactly what you’d think, hottie. It’s physical therapy. Though just between us I’m more interested in aerospace.
    But physical therapy is cool too!!!!!"
    w "Okay, I believe you Dominic."
    d "What is your major?"
    w "Oh, you don’t know? My friends just pay me to show up. I’m actually a part time stripper."
    "He looks confused. I forgot he doesn’t understand humor."
    d "Well money is important. I will support you in your endeavors no matter what!"
    w "Dominic I was not being serious. Though support and respect sex workers.
    You have the right idea going at least. You're so cute. You’ll support me no matter who I am."
    d "Well like I said I don’t care what you are as long as you love me."
    w "There’s a lot of stuff you do not know about me."
    d "I’m willing to learn all of it. There’s a lot of stuff you don’t know about me either."
    w "I’m willing to learn about you, too."
    d "What’s your favorite color?"
    w "Probably Purple. What about you?"
    d "Red."
    w "Are we close to being there yet? It’s getting darker."
    d "Almost there. Just another block."
    "Wren and Dominic walk up another block to see a beautiful view of the city.
    The sky was clear, and the city lights were shining bright."
    w "Oh my god, Dominic, this is so gorgeous!!!!"
    d "You see why we had to come here now?"
    w "I definitely see why now."
    d "Let’s sit and watch the lights."
    w "Okay, we can do that."

################################################################################
    #If Carried#
    if dom_carry:

        "Dominic lets Wren down and they sit near the edge of the hill overlooking the city."
        show blk
        #show bg27
        stop music

    #If walked#
    else:

        "Dominic and Wren sit down at the edge of the hill overlooking the city."
        #show bg27

################################################################################

    "Dominic slyly wraps his hand around Wren’s as they sit. Wren pretends not to notice."
    play sound night loop
    d "Why don’t you live with your family?"
    w "Long story… Probably a story for another time."
    d "You will tell me at some point though, right?"
    w "I will at some point."
    d "Do you not get along with them?"
    w "No, we do. I love them. I just can’t be what they want me to be, you know?"
    d "I see. That’s hard."
    w "I always want to be my own person. I cannot stand to be controlled."
    d "I understand."
    w "Do you?"
    d "I do. It’s really cool that you're strong enough to be your own person.
    That’s the thing I admire the most about you. IT MAKES ME LIKE YOU EVEN MORE!!!!!"
    w "You're strange. I like it though."

    "Dominic and Wren watch the city lights for an hour then go their separate ways."
    stop sound fadeout 3.0
    show bg21
    show wren reg at pos5
    "After Wren is finally alone, he takes his phone out to text..."
    #Choice:#
    #Go to Somchai (Day5_Somchai)#
    #Go to Kryan (Day5_Kryan)#

################################################################################
    $ persistent.dom5 = True
    menu:

        "Who should I go with, now?"

        "Kyran":

            "Deciding it’s time to head home, Wren texts Kyran to pick him up."
            "A moment later he gets a confirmation that Kyran is on his way."

            jump ky_day_5

        "Somchai" if not persistent.som5:

            "After he gets a reply, he goes to meet up with Somchai."
            s "Hey, Wren, how are you feeling?"
            w " I’m okay, so what are we going to do?"
            s "I have an idea. Come with me."

            jump som_day_5
################################################################################
################################################################################

label ky_day_5:
    #Kyran's part of day#
    if persistent.somdom5:
        scene bg23n
    else:
        scene bg23

    $ persistent.unlock_bg23 = True
    $ renpy.notify("New Background Unlocked")
    "Kyran and Wren are sitting in Kyran’s car driving to Wren’s house. It has been less than peaceful."
    k "BOY TOY NAMED TROY USED TO LIVE IN DETROIT!!!! BIG DOPE DEALER MONEY HE WAS GETTING SOME COIN!!!!"
    "Should I say something? This is getting repetitive. I did not realize the hospital was so far away from my house."
    w "I understand the need for preparation before the release, but this is about the twentieth time we’ve listened to Anaconda."
    k "This song is high art. Please let's continue."
    w "One more time. Then we need to talk."
    k  "Come on Wren join in!!!! MY ANACONDA DON’T MY ANACONDA DON’T WANT NUN UNLESS YOU GOT BUNS HUN."
    w "LITTLE IN THE MIDDLE BUT SHE GOT MUCH BACK!!!!"
    k "Okay, we can be done. What’s up?"
    w "I miss my family."
    play music sweet
    k "They miss you too Wren."
    w "I can’t go back. I can’t lead the tribe. They should just let my Dad do it. Then the boys uhhhh..."
    k "I know. Though one quarter life crisis issue at a time. Let’s switch to the boys because there’s something you can do about that at least."
    w "MEN!! HATE EM!!!!"
    k "ME TOO!!!! BUT WAIT WE ARE MEN!"
    w "Men in general. You, Tobias and I are just \"vibe-ing\". "
    k "Ahh to be fought over by two eligible bachelors. That only happens in movies."
    w "I do not want my life to be like in the movies."
    k """
    If only I liked them... then I’d want to be you. Let’s try to think logically we’ve got a Himbo and a Cold Prince.

    First thing’s first you need to actually get to know Dominic to see if you would be compatible.
    Second, as much as I hate to say reconnect with Somchai to see if you're still compatible.
    I am sure things have changed since you last saw each other.
    """
    "Can I just live my life and not have to worry about boys..."
    w "Is there a third option?"
    k "You reject both of them and end up with Tobias who’s persistence will get the better of you. Pick your poison friend."
    w "What if I just... died."
    k "Haha, I know you're being sarcastic but still no. You can be an independent strong male and reject both of them.
    Then live peacefully with your owl. I do think they may not take no for an answer though."
    w "You are stressing me out more."
    k "Would now be a bad time to tell you that the tribe was thinking of sending a representative to convince you who isn’t me."
    "My soul has just left my body."
    w "Girl, What?!?!"
    k "It was a joke. Your mind got off the boys though. I got ya’ didn’t I?"
    w "Kyran that was not funny..."
    k "We’re here. Let’s get you some rest. See you tomorrow. I’ll bring the girls and Tobias."
    w "See you tomorrow."
    k "Remember the new release is at 10pm."
    w "I will. Goodnight."
    stop music fadeout 3.0

    show blk with fade

    jump day_5_end

################################################################################
################################################################################

label day_5_end:
    #End of day.#
    if persistent.somdom5:
        scene bg04 with fade
        play sound night loop
    else:
        scene bg03 with fade
        play music theme1
    show wren reg at pos5 with easeinright
    """
    What the fuck was even today? Things just seem to be caving in. I am so stressed and have so many worries right now.
    They just expect me to choose between them.

    They expect me to choose between my dreams and the tribe.

    They expect me to choose between my ex lover and a new suitor.

    It feels so suffocating.
    """

    w "Fuck it. I’ve got to worry about now, and right now I need to feed my owl."
    o "WOO-WOO-WOO"
    w "I’m coming! Sorry, I was kind of like in the hospital. I’m not trying to starve you."
    hide wren with easeoutleft
    "Wren grabs the meat he uses to feed his owl. Then runs quickly to bring him the food."
    scene bg26
    show wren reg at pos7 with easeinright
    w "See I’ve got you. Eat you starved little creature."
    "I just need to relax.{w} Breathe in.{w} Breathe out."
    "Wren decides to go up to his room and lie down."
    hide wren with easeoutright

    if persistent.somdom5:
        scene bg02 with fade
    else:
        scene bg01 with fade

    show wren reg at pos5 with easeinleft
    "Okay, Relax... relax. Ahh~ maybe repeating that in my head won’t help. It’s like I’m an object to be fought over.
    I want my own autonomy. I want to make my own choices without people trying to influence me."
    hide wren with easeoutbottom
    show blk with dissolve
    "Wren, still in great turmoil, tries to sleep to no avail."
    "Maybe, if I roll over I’ll be more comfortable. Like rolling away from all my problems."
    w "Sleep, please, enter my body. Anxiety, I expel you."
    "Like voicing it will help me sleep. Ahhh, ways to exhaust myself think well there’s one way."
    stop music fadeout 1.5
    #masturbation#
    "Wren slowly removes his pants and puts his hand on his cock. He rapidly moves his hand up and down his shaft until he starts to get hard."
    #scene cg11_1
    w "Fuck, this feels good..."
    "If someone else were doing it might be better, though. Nothing feels better than the hand of a lover."
    "Wren uses his free hand to rub his nipples until they are hard. His hand motions get faster as he’s really sexually frustrated now.
    Wren moves the hand rubbing his nipples and uses it to slap his own face."
    #show cg11_2
    "Ahhh that's about right. It’s been a while since anyone’s slapped me to get me off. Have to do everything myself around here."
    "Wren starts to get closer to finishing and he pulls his hair with his free hand. Wren starts to feel the euphoria of release and cums."
    #show cg11_3
    "Soon after he feels the exhaustion."
    "That idea definitely worked. Good one, Wren."
    "Wren closes his eyes and finally drifts off to sleep."
    scene blk
    stop sound fadeout 2.0
    #Day 5 End#

    $ persistent.dom5 = False
    $ persistent.som5 = False
    $ persistent.somdom5 = False

    jump end
