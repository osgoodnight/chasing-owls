label day1:

    default persistent.ending_unlock = False
    $ persistent.gallery_unlock = True
    #Wren in bedroom
    scene bg01
    $ persistent.unlock_bg1_2 = True
    $ renpy.notify("New Background Unlocked")
    stop music fadeout 1.0
    pause 1
    play sound alarm
    show bg01 with hpunch
    "Why is it already morning???"
###############################################################################
    $ shuffle_menu()
    menu:
        "Should I wake up?"

        "Press snooze":

            $ dominic_points += 1

            stop sound

            w "A few more minutes..."

            """
            Wren slaps his hand on his phone to hit snooze and rolls over to go back to sleep.

	        Wren falls asleep again rather quickly.

            A few moments later...
            """
            pause 2
            play sound alarm
            show bg01 with hpunch

            "The alarm blares, scaring him awake."

            w "SON OF A BITCH!!!"

            jump after_alarm

        "Wake up":

            $ somchai_points += 1

            w "Why did I agree to this?"

            jump after_alarm

################################################################################
label after_alarm:

    "Wren fumbles with his phone to try and turn it off.
    The phone falls off his side table."
    w "Fucking piece of shit phone..."
    "Wren then stands up to find his phone now on the floor."
    stop sound
    show wren angry at pos5 with easeinbottom
    $ persistent.wren = True
    $ renpy.notify("New Character Unlocked")
    w "Well I’m awake now."
    hide wren with easeoutleft
    play music theme1
    show blk
    play sound shower
    """
    Wren walks out of his room towards the bathroom.

    He Turns on the shower, enough to scald anyone.

    Wren brushes his teeth, making sure to get each corner and the back of his tongue.

    The room fills with steam as the shower gets hotter and hotter.

    He strips the one piece of clothing he was wearing off and jumps into the
    shower expectedly burning his skin in the process.
    """
    w "Why does this hurt so good? What does this say about me? Am I into pain play?...{w} Probably?"
    stop sound fadeout 1.0
    "After his shower. Wren throws on his go-to-outfit."
    #wren's living room
    show bg03
    $ persistent.unlock_bg3_4 = True
    $ renpy.notify("New Background Unlocked")
    hide bg01
    show wren reg at pos3 with moveinleft
    "Gathering his belongings that are thrown around his room."
    w "Son of a bitch! First day and I’m probably already late. Way to go me!"
    #Kyran enters
    play sound door
    pause 3.0
    show kyran reg at pos6 with easeinright
    $ persistent.kyran = True
    $ renpy.notify("New Character Unlocked")
    """
    Kyran enters with his key that Wren gave to him the first day after moving into his new place.

    Knowing he needs someone to unlock the door in the inevitable case he loses his keys...{w}
    or locks himself out.
    """

    k "{b}GOODMORNING!!!{/b}"
    show wren surprised with hpunch
    pause 2
    show wren reg
    #hide wren reg
    #hide kyran reg
    #show cg02
    """
    This is Kyran. I couldn’t get rid of him as a kid.

    He was like a stray puppy that wouldn’t leave after giving them food or giving them attention,
    but then he became my best friend.
    """
    w "UGH! Why do you have to be so loud?... Morning."
    k "You need to wake up and get ready for the day."
    w "Coffee...{w} I need coffee."
    "I can’t start functioning without coffee. I tried quitting but it only lasted 4 hours.{w} Worst 4 hours of my life..."
    k "There’s always time for coffee. Just hurry up."
    w "You know me so well."
    "He knows everything, and I mean everything. Even that one time…{w} never mind."
    k "I've known you pretty much my entire life, of course I know you!
    I also remember everything that’s good for you. Without me you’re lost, admit it."
    w "You don’t have to be right all the time."
    "But he is right all the time…{w} well most of the time.{w} Yeah, all of the time."
    k "Just grab your shit and let’s go."
    #Wren kyran @ café
    scene bg15
    play sound cafe fadein 3.0 loop
    $ persistent.unlock_bg15_16 = True
    $ renpy.notify("New Background Unlocked")

    """
    Kyran and I head to the café.

    This is my favorite place ever. It has coffee and that’s all that matters.

    We walk into the café, ready to order.
    """
    show wren thinking at pos4 with moveinleft
    show kyran reg at pos1 with moveinleft

################################################################################
    $ shuffle_menu()
    menu:

        "Hmmm... what should I get?"

        "Hot coffee":
            $ somchai_points += 1

            "You can’t kill a dragon with fire, so: enjoy it hot, it’ll prepare me for hell."
            jump after_coffee1

        "Iced coffee":
            $ dominic_points +=1

            "When it’s cold I can drink it fast. Sippy sippy bitches let’s get caffeinated ASAP."
            jump after_coffee1

################################################################################

label after_coffee1:
    scene bg16
    show kyran reg at pos6
    show wren reg at pos3
    """
    After I ordered, Kyran ordered his coffee and we sat inside for a bit of sipping of the coffee.

    Watching people pass by through the window. Kyran stares at a guy.
    """
    pause 1
    show kyran happy
    pause 2
    k "He's totally gay."
    "Kyran points at a guy approaching the café."
    w "How could you possibly know that?"
    show wren surprised blush
    "He does kinda look gay..."
    k "I just know, I have these things called eyes, you know."
    show wren reg
    w "You didn’t even know I was gay when we first met."
    "I feel like I hid it well but at the same time it wasn’t a secret."
    show kyran thinking
    pause 3
    show kyran happy
    k "Because you’re...{w} you,{w} and I don’t pay attention to you like that."
    w "Excuses, you don’t know shit."
    "He knows everything about me yet he didn’t know I like dick. Surprising..."
    k "You should go talk to him."
    show wren surprised blush
    w "Ummm, no thanks."
    "I don't do face to face introductions...{w} Gross"
    k "Come on! Why not?"
    w "Because I don’t want to."
    "He is kind of cute though."
    k "But why not?"
    w "It’s too early for this. I’m trying to enjoy my coffee before having to deal with today."
    "I just don’t want to talk about boys with Kyran right now. I haven’t mentally prepared."
    k "Ugh. Fine. Ready for school now that you have some caffeine in your system?"
    show wren reg
    w "I’m ready to get to school and move on with my life, but just one more cup of coffee first… Please"
    "You don’t want to say no Kyran, I promise you."
    k "If we want to be on time we have to leave soon, we have to meet up with Tobias, remember?{w}
    But since you said please… hurry up."
    w "Sweet sweet Kyran… you don’t rush me with my coffee time, but for Tobias, I’ll get it to-go."
    stop sound fadeout 5.0
    scene blk with fade
    """
    Wren orders his second cup of coffee, relieved he will have caffeine to hold him off until lunch time.

    Kyran drives them to school and after finally finding a parking spot, they are surprisingly still on time.

    Off in the distance they see a familiar face.
    """
    #enters wren, kyran and tobias @ front of school
    scene bg05 with fade
    $ persistent.unlock_bg5_6 = True
    $ renpy.notify("New Background Unlocked")
    show tobias happy at pos2
    $ persistent.tobias = True
    $ renpy.notify("New Character Unlocked")
    show wren happy at pos6 with moveinright
    show kyran reg at pos8 with moveinright
    t "What took you guys so long?"
    w "Bean juice!"
    show wren happy at pos4 with move
    show kyran reg at pos6 with move
    "Dirty bean water. My one and only love."
    t "That’s your excuse for everything."
    "It gets ugly when I don’t have coffee, you don’t want to know."
    w "Do you want me to come here without my coffee?"
    t "I’d rather die first!"
    #hide tobias
    #hide wren
    #hide kyran
    #show cg01
    """
	Tobias. Sweet, sweet Tobias. Confused little Tobias.

    He’s smart but also not, if that makes sense.

    He’s a computer genius but doesn’t know how to interact with the general public.

    He is quiet but I have the best conversations with him.

    He taught me how to play Dungeons and Dragons, but I get bored easily.

    He is always there for me and is one of my friends that I can be weird with and relax.{w} He must be protected at all costs.
    """
    #hide cg01
    show tobias reg at pos2
    show kyran reg at pos6
    show wren happy at pos4
    k "Can I talk to you guys about something?"
    w "Never ask permission. Shoot!"
    k "So the tribe is asking about you again… Kinda demanding answers now."
    stop music
    show wren sad
    t "Well I’ll just be over here..."
    hide tobias reg with easeoutleft
    "Tobias awkwardly takes a step back to let Kyran and Wren have this conversation.
    Tobias wants nothing to do with this, but Wren needs him there."
    play music suspence
    show wren angry
    w "I’ve told them already; I’ve told them a hundred times."
    """
    What the fuck do they want from me?!

    I am not who they think I can be for them.
    I am not who they need or want.

    To make a long story short~{w}My grandpa died. He was kind of an important part of the tribe.
    My dad can’t take his place, for whatever reason, I guess he’s too old or something.

    My dad wants it, but the tribe says no, they want me. So, they are trying to force
    me out of all people to become the chief.
    I’m young and able to be molded into the person they want me to be. They just
    want to manipulate me and that's it.

    I want a different life, one that I can choose and be in charge of.
    I don’t want to be their puppet.
    So, I moved out of my family’s house and off the reservation.
    I separated myself from them. With the exception of Kyran.

    I’ve pretty much peeled myself away from them, but they keep trying to pull me back,
    my parents or older family members will call.

    I don’t want to lose my family.{w} I love them.

    But I can’t be the person they want me to be. They need to pick someone else.
    """

    w "You know I can’t do that, I just can’t."
    k "I know that, I do, and I support your decision 100 percent, but they are on my
    ass to get you to at least talk to them. They want to sit down and talk."
    w "About what?"
    "Probably to spew some bullshit to guilt trip me."
    k "I’m not sure, they just told me to tell you they want to talk and have some sort of meeting."
    w """
    I can’t go back, not with what they need me to do.

    I can’t give up my life to be something I’m not cut out to be.

    They need someone better. Someone that’s not me.
    """
    k "I know and I’m sorry for bringing this up. I just want you to think about it please. For me?"
    stop music fadeout 3.0
    show wren reg
    w "For you I’ll think about it."
    "You couldn’t have brought this up earlier, I would’ve spiked my coffee too."
    "I know this isn’t his fault. He’s just a messenger and not of his own volition."
    show tobias reg at pos2 with easeinleft
    t "This is kinda serious though, you should have a clear mind."
    w "I know, but I really wish I wasn’t fully conscious for this."
    k "We can talk more when I come over to your place later. I’ve gotta go."
    w "Bring a bottle of tequila, I’m gonna need it."
    play music theme1
    # wren and tobias in class, seated
    scene blk with fade
    pause 2
    scene bg13 with fade
    $ persistent.unlock_bg13_14 = True
    $ renpy.notify("New Background Unlocked")
    show wren thinking at pos3dwn
    show tobias reg at pos6dwn

    """
    Tobias and Wren are now in class; they take seats next to each other waiting
    for class to start.

    Wren is now on edge from the news Kyran spilled.

    Wren has his hands in fists and his head held lower with a look of frustration
    that Tobias can pick up on.
    """

    t "You seem tense."
    show wren reg
    w "You should be a detective."
    "How preceptive..."
    "I know it’s obvious, but fuck dude, don’t point it out"
    t "I’m just trying to make conversation, want to talk about it?"
    w "I want this to not be happening, but things could be worse, there could be a certain somebody involved."

    """
    This is the worst time to be thinking about this, but whenever my brain gets angry, I think of Somchai,{w} my ex.

    He makes me angry just thinking about him.{w} He just left.{w} Just straight up left.

    Everything was perfect,{w} well almost, and this fucker just leaves?!...

    Calm down Wren. You don’t want to start crying in class again. Think nice thoughts.

    Dogs{w}, cats{w}, bunnies{w}, blankets{w}, hot showers{w}, {b}coffee{/b}.

    *Sighs*{w} Better.
    """

    "Tobias responds in a very snappy, frustrated manner."
    show tobias thinking
    t "Would you stop thinking about him? I thought you were over him?!"
    w "I am! But I still remember him."
    "I’ll always remember my ex, he is kinda… my ex."
    show tobias happy
    t "Well forget about him, I’m here for you."
    w "I know you are, thanks for being such a good friend."
    "Tobias is always there for me, he keeps my thoughts collected and clear."
    "Tobias speaks in a soft tone, almost a whisper."
    show tobias sad
    t "{size=12}Yeah a good {i}friend{/i}{/size}."
    teach "Hello class, please take your seats and let's begin. Let’s pick up where we left off..."
    window hide
    scene blk with fade
    pause 2
    scene bg11 with fade
    $ persistent.unlock_bg11_12 = True
    window show
    #Class ends.
    "Once the professor ended the lecture, they walked out of the class into the hallway."
    #wren tobias in hallway1
    show bg07 with dissolve
    $ persistent.unlock_bg7_8 = True
    $ renpy.notify("New Background Unlocked")
    hide bg13
    show tobias reg at pos6 with easeinleft
    show wren reg at pos2 with moveinleft
    t "Are you gonna be alright without me?"
    "Sarcastically and with sass, I respond."
    show wren thinking
    w "{i}What ever shall I do without my precious Tobias, I cannot go one moment without thee by my side!{/i}"
    t "{i}Simmer down now, I shall see thee later my love, but for the next 2 hours myne
    body will be with computer design, how myne heart will yearn for thee!{/i}"
    w "Gross...{w} I’ll be having lunch with the girls, see ya later."
    show wren reg
    t "Lates my dude."
    show tobias sad
    #pause 3
    "Tobias looked at me with an expression I haven’t quite figured out yet."
    hide tobias with easeoutright
    "After Tobias turns and heads to his next class, I turn and walk the opposite
    direction to the school courtyard to meet up with some friends."
    hide wren reg with moveoutleft
    pause 1
    #hangout tree with Shaula and Evanora
    scene bg09
    $ persistent.unlock_bg9_10 = True
    $ renpy.notify("New Background Unlocked")
    show evanora happy at pos2
    $ persistent.evanora = True
    $ renpy.notify("New Character Unlocked")
    show shaula happy at pos4
    $ persistent.shaula = True
    $ renpy.notify("New Character Unlocked")
    "Wren walks up to the two standing waiting for him."
    show wren happy at pos7 with easeinright
    w "’Sup bitches."
    e "Look what the cat dragged in!"
    w "Can you fucking not?"
    #hide wren
    #hide shaula
    #hide evanora
    #show cg03 with fade
    """
    This is Evanora, she’s a lesbian without knowing it.

    She knows it... but it doesn’t sit right with her yet.

    She is a force to be reckoned with though. She is my guardian and will cut anyone if need be.

    I feel safer with her around. Evenora is the moral compass of our group.

    She is the dad of our friends. Responsible, protective, yet is quiet and reserved.

    Everyone needs a human like Evenora.
    """
    sh "Did someone wake up on the wrong side of the bed?!"
    w "I’m sorry, it’s just already been a day and it’s barley lunch time..."

    """
    This is Shaula. They are the most sexually confusing person among us.

    They are also a horny hopeless romantic.

    This is why we are best friends. Kyran knows me but Shaula {b}knows{/b} knows me.

    Shaula knows my dirty little secrets because they just happen to be in on them.

    They are also the loudest person I’ve ever met. But not in an annoying way.

    They say things with their heart, with no apologies.
    """
    scene bg09
    show evanora happy at pos2
    show shaula happy at pos4
    show wren happy at pos7
    w "Is it almost finals yet?"
    e_sh "I wish!"
    sh "Did you wanna talk about it? You know you can tell us anything
    and we’ll only judge you a little."
    e "Don’t listen to her, but we are here for you."
    w "Thanks, but I just want everything to be normal. I’m trying not to go
    back to the old days."
    "Only forwards steps from here on out. Never to turn back!"
    e  "You got it dude!"
    sh "I don’t even know what you’re talking about?"
    w "Thanks guys...{w} gals...{w} people???"

    "The three erupt into laughter."

    """
    What even is the gender neutral term? Like has anyone figured that out yet?

    Like calling someone a bitch or a dick have become gender neutral...
    """

    w "So where are all the hot people at? College is supposed to be full of
    hot people! This isn’t how I remember it."
    sh "Ass is ass to me!"
    e "School is a place for learning, not for doing the nasty."
    sh "That’s literally why you go to college, to get fucked and fucked up."
    w "¿Por qué no los dos?"
    show shaula surprised
    show wren surprised
    w_sh "-AT THE SAME TIME!"
    show shaula happy
    show wren happy
    "I look intently at Shaula."
    "We share the same mind.{w} Sometimes it’s scary."
    w "Jinx bitch, you owe me a coffee!"
    show shaula thinking
    sh "It’s a coke not coffee!"
    w "When have you ever seen me drink coke?"
    "What am I, straight?"
    show shaula happy
    sh "Want your regular?"
    w "Claro qué si!"
    "Shaula’s the best."
    stop music fadeout 5.0
    #Shaula leaves
    hide shaula with moveoutleft
    e "You sure everything is okay?"
    show evanora sad
    w """
    I’m not sure, but I hope it is.

    I just want this year to be semi-normal, no drama, no unneeded stress,
    and maybe a decent sleeping schedule.
    """
    show evanora happy
    e "You know I can take care of anyone that is bothering you.
    I know how to hide a body"
    "Evenora cracks her knuckles"
    w "That won’t be necessary but thank you. I’ll keep that in mind."
    "You never want to be on her bad side. I love having her on my side.
    She makes things easier to deal with."
    e "Just give me a call and I will be there, no questions asked."
    play music theme1 fadein 3.0
    #Shaula Enters
    show shaula happy behind evanora at pos4 with moveinleft
    sh "Here’s your coffee. Ready for class?"
    w "Arigato gozaimasu. And, no I'm not."
    e "Yeah let’s go. And Wren, don’t forget just give me a call."
    w "You got it..."
    "Wren turns and walks away down the hallway going towards his class,
    the only class he does not have with his friends."
    #wren in hallway2
    scene bg08
    show wren reg at pos2 with moveinright
    w """
    This better be worth it.

    I really want to get through college and start doing what I love. Teaching.

    All of this drama is just getting in the way of that. There has to be a way to make it stop.
    """
    hide wren with moveoutleft
    scene bg11
    #wren classroom
    teach "Good afternoon class, today we will be talking about the theory of teaching..."
    stop music fadeout 4.0
    "I’ve already forgotten everything this man has said. I should’ve maybe written notes. Oops."

    """
    30 more minutes...

    20 more minutes...

    15 more minutes...

    10 more minutes...

    5 more minutes...
    """
    "Come on! It's time to go. End lecture already. Please for the love of everyth-{w} 1:45 KTHNXBYE!!{nw}"
    play music theme1
    "Wren made it through the lecture.{fast} Quietly gathering his things, walks off into the hallway and
    makes his way out of the building."
    #wren in hallway2
    show bg08
    hide bg13
    show wren happy at pos8 with easeinleft
    "I want this semester to be the one that I look back on that I can say,
    this semester was the time I turned my life around. I really hope that for future me.
    I want to do that for them."
    hide wren with moveoutright
    #wren @ school front
    scene bg05 with fade
    show wren reg at pos5
    "Hmm I don’t see Kyran anywhere..."
    "I don’t mind walking home. Kyran can easily pick me up but walking home
    is my time to think about nothing. There Are noises and sights to keep my brain distracted.
    I can truly think about the void if I wanted to. It clears my mind after school
    and prepares me to be tired to actually relax at home."
    #street
    stop music fadeout 2.0
    scene blk
    play sound footsteps loop
    "After walking for a while Wren sees Kyran’s car parked in front of his place."
    "Until someone else intrudes. I can’t be mad though. I can’t cut off Kyran like that. He’s my better half."
    "Walking up to his building, Wren then opens the front door."
    stop sound
    #wren's livingroom with kyran
    show bg03
    show kyran reg at pos2
    show wren reg at left with moveinright
    hide wren
    play music theme1
    "Ignoring Kyran in the living room, he throws his backpack onto the couch and then heads straight for the fridge.
    There he grabs two beers then opens them. Kyran, upset that he hasn’t said a word yet, stares intently at Wren."
    play sound opencan
    show wren reg at pos5 with easeinleft
    k "I had a great day at school, thanks for asking."
    w "Sorry, I really need this before we talk about tribe stuff."
    k "I just don’t want you to be mad at me."
    w """
    I promise, I’m not mad at you. It’s them I’m upset with.
    You’re like the child whose parents just got a divorce and is being forced to choose which parent to go live with.

    Not that you’re a child... but it’s not your fault, you’re just caught in the middle of everything and I’m sorry for putting you in that position.
    """
    k "Thanks for reassuring me... So..."
    w "This makes no sense, why now?"
    k "I don’t know why now, but it’s happening. I’m sorry this is happening but i'll be there the whole way, promise."
    w "Thanks. This is going to be just another long drawn out semester."
    k "I’ll drink-to that!"
    scene bg04 with dissolve
    show wren reg at pos5dwn
    show kyran reg at pos2dwn
    """
    Kyran and I spent the rest of the night silently drinking and watching TV.

    This is how we hang out when one of us is upset and this is why we are such good friends.

    Not a word for hours but enjoy being with each other.

    It feels nice to know someone is there,
    even if we aren’t speaking.
    """
    k "I just realized how much we drank."
    w "Wait, how much?"
    "Kyran and Wren look at the table full of empty bottles then look back at each other."
    w "I just kept grabbing a new bottle for myself and then one for you."
    k "Wait...{w} I thought I was the one grabbing beers?"
    w "Were we both grabbing beers?"
    "I better not have run out of beer."
    stop music
    "Wren quickly stands up, finally understanding just how much he drank."
    #wren moves silghtly
    show wren at pos5 with move
    pause 1
    show wren embarrassed with hpunch
    show wren at pos5dwn with move
    "Holy shit. I didn’t even realize how drunk I was getting."
    k "Damn, how am I going to get home?"
    "Kyran gets up slowly and stumbles. Quickly returning to his seat."
    #Kyran moves slightly
    show kyran at pos2 with move
    show kyran embarrassed with hpunch
    show kyran behind wren at pos2dwn with move
    w "You are home. Mi casa es… whatever the rest is."
    "Kyran plops back down onto the couch, relieved he doesn’t have to wait to get some sleep."
    k "Giving you a ride to school tomorrow going to be easier at least,{w} if I’m not still drunk..."
    "Kyran is already starting to get ready for bed, taking the couch as his bed he lays down."
    w "Would you be mad if I sat here for a second. I’m scared to stand up."
    "If I didn’t know better, I would be convinced my legs don’t exist."
    k "Do what you want, just don’t fall on me when you fail at standing."
    "Both burst out in giggles."
    w "No promises… I seriously can’t feel my legs."
    "Kyran muffles his giggles."
    k "It’s okay. The feeling will come back, just keep wiggling your toes and then work your way up."
    "Wren takes 15 minutes to realize he still has legs."
    "Slowly and with a death grip on the arm of the couch slowly stands."
    #wren gets up
    show wren happy blush at pos5 with move
    "YESSS! I have functioning legs again!"
    w "HAHA!! They live! I was about to start crying."
    k "Congrats, now let’s go to bed, we forgot it’s only Monday,{w} well now Tuesday."
    w "’Night!"
    k "Goodnight, Wren."
    hide wren with easeoutleft
    show bg02
    hide bg04
    #wren in bedroom
    play music night
    show wren happy blush at pos8 with easeinleft
    "Wren makes his way to his room. Surprising even himself, he decided to just strip completely. Then he hears a familiar noise."
    play sound owl
    o "WHO~ WHO~"
    "Shit. Did I forget to feed him when I got home? He’s around here somewhere..."
    hide wren with moveoutleft
    show blk
    play sound fallen
    stop music
    "Wren runs into the door and knocks himself out."
    #wren falls
    "Waking up a few moments later to finish his final task before bed."
    scene blk
    jump day2
