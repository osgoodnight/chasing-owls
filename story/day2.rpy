label day2:

    $ day += 1
    #[wren’s bedroom]
    scene bg01
    play music theme
    "As the sun peeks through the curtains, wren wakes up on the floor."
    w """
    *groans* What the fuck happened?

    I remember trying to get off the couch... and then nothing. I know I was drunk but I didn’t know I was that drunk.
    """
    show wren reg at pos2 with easeinbottom

    "Off in the other room wren hears a familiar sound"
    play sound owl
    o "*owl noises*"
    "There’s a sharp pain on the front of his head from hitting the door last
    night, stinging as he gets up quickly"
    show wren surprised
    w "Shit! Now I remember!"
    o "*Louder owl noises*"
    show wren reg
    w "Okay! Okay! I’m coming! I’m sorry!"
    hide wren with easeoutleft
    #[blk]
    scene blk
    """
    Wren walks to the fridge and takes out an opaque container, he takes out a
    few slices of red meat, bare handed. He does this every day and doesn’t get fazed
    by raw meat anymore, then makes his way back to his secret room.
    """

    #[show owl]
    show owl at owlcenter

    """
    This owl is the most spoiled thing in the world. I’m a butler of sorts.
    I clean, feed and entertain them… with no thank you, I might add.

    Ungrateful turd.

    Given, they are super cool to have, and I love them to bits, but it sometimes
    feels like a one-sided relationship.
    """
    show wren reg at pos7 with easeinright
    play sound owl
    o "*owl noises*"
    w "I love you too, buddy."
    "Okay maybe not one sided, but I do all the work still."
    "Kyran emerges from his ‘couch slumber’ and drags his body to the bathroom.
    He yells from the hallway."
    k "{b}I call dibs on shower first!{/b}"
    w "Guests first."
    k "{b}I’m going to take all the hot water on purpose!{/b}"
    "Why is he so spicy today?"
    w "You’ll die before you do."
    "I would never but I would think about it for just a second."
    k "{b}Try me bitch!{/b}"
    w "You’re saucy when you’re hung over."
    k "{b}I need coffee!{/b}"
    "I am, honestly, a dead sack of potatoes right now, too."
    w "Demanding… Fine I’ll put the kettle on."
    hide wren with easeoutright
    hide owl
    #[livingroom]
    show bg03 with fade
    """
    I was going to do that anyway, but I’ll let him feel like it was his decision.

    Even though, physically, I feel ill. Mentally I feel kind of okay...{w=1.0}
    something's up…{w=1.0} I’m dying. I’m sure of it.

    While wren is making coffee, there’s music starting to come from the bathroom.
    Getting louder and louder with the song now distinguishable.

    Oh god… I know what song this is now. Why did it take me so long to realize it?
    """
    show wren happy at pos5 with easeinleft
    k "NOW GET A BUCKET AND A MOP, THAT’S SOME WET ASS ~"
    "Holy hell I can’t with this man… but this song is a bop."
    k_w "I’M TALKIN’ WAP, WAP, WAP, THAT’S SOME WET ASS PUSSY!"
    "This is why we are friends."
    hide wren with easeoutright
    "After a few short minutes the music stops, and the shower turns off. Kyran
    comes out now fresh and clean."
    show kyran reg at pos4 with easeinleft
    k "Coffee smells good."
    show wren reg at pos7 with easeinright
    k "Your turn… I did save you some hot water, I promise."
    "Kyran gestures towards the bathroom. wren hands kyran a cup of coffee
    prepared exactly how he likes it."
    k "You know me so well, this is why I keep you around."
    w "That’s the only reason?"
    "Not because of our beautiful duets?"
    k "No… but one of them, our duets are immaculate."
    "There it is!"
    w "I mean we ‘aight."
    k "Go shower ya’ nasty, we have to get to class soon."
    w "So bossy. You know how I like it."
    #[blk]#
    scene blk with fade
    play sound shower loop
    """
    While in the shower, I started to plan how my day should be.

    Best route to get the most sleep: After my first class, I have to meet with
    tobias for our second class, then he goes to do his nerd shit while I eat with
    my girls.

    Next, I go to my last class, which means I can get home to do some homework,
    feed my child, and then can reunite with my sweet bed. Pretty straight forward,
    I can do this no problem…{w} right?

    As the hot water drenched him and runs down his naked body, wren begins to
    feel the effects of the events of the night before.

    I can do this. Everything is fine. deep breaths.

    Wren fights through the nausea and finishes his shower.
    """
    stop sound
    #[Bedroom]#
    show bg01 with fade
    show wren reg at pos5 with easeinright
    "Walking out of the room, he is hit with the smell of coffee once more."
    "Now that’s some good shit. Instantly better. Coffee is the cure to everything.{w}
    I solved it."
    "From the other room a yell crashes into his ears."
    with vpunch
    k "{b}10 MINUTES TILL LIFT OFF!!!{/b}"
    w "You don’t have to YELL!!!"
    k "Yes I do, because you don’t listen and if I don’t yell then later you’re
    going to say \"WeLL I dIdN’t HeAr YoU sAY iT\"… I know you better than that. Go get ready."
    w "Okay MOM~."
    #[livingroom]
    hide wren
    hide bg01
    show bg03 with fade
    show kyran reg at pos8
    show wren reg at pos3 with easeinleft
    "Kyran responds in a high pitch voice."
    k "Were you going to come eat breakfast sweetie?"
    w "Okay honestly that scares me, stop… but yes I’ll have some food."
    scene blk
    "After a quick breakfast of toast and eggs; the boys head off for school.
    kyran drives them both and pulls into the parking lot."
    #[front of school]
    show bg05
    show wren reg at pos3 with moveinright
    show kyran reg at pos6 with moveinright
    "They quickly make their way to class."
    k "We left on time, how are we running late?"
    w "The universe hates us~"
    k "I know but still, I did everything right."
    w "It’s okay we aren’t even that late."
    k "If you are early you are on time, if you are on time you are late,
    if you are late you are dead."
    w "well okay DAD~!"
    "kyran imitating a fatherly voice"
    k "Now son you have to push yourself or you’ll fall behind everyone else and
    fail? do you want to fail?"
    "Jesus I’m triggering myself saying that."
    w "Let’s just get to class DAD."
    k "I totally prefer daddy."
    w "No."
    k "Fine, dad it is. It gives me an excuse to have a dad bod."
    "Kyran hates kids, but I know he’d be an amazing dad one day.
    Me and kyran make our way to our first class. I look off into the distance by a tree."
    show wren thinking
    """
    That person looks familiar...No. It can’t be him. that’s impossible. He left.
    It was just some guy that kinda looked like him… a lot like him... but either way.

    It couldn’t possibly be him.
    """
    show wren surprised
    k "What are you looking at?"
    show wren reg
    w "Nothing…"
    k "I think you need more coffee."
    #[hallway]
    show bg07 with fade
    hide bg05
    hide wren
    hide kyran
    "Kyran and wren continue their trek to class. They make a quick detour for some coffee and continue to class.
    A few minutes before the lecture starts."
    show bg08
    hide bg07
    show kyran reg at pos3 with moveinright
    show wren reg at pos5 with moveinright
    w "Told you. Just on time"
    k "We cut it close, though."
    w "And I thought I was the stressed one here."
    "A timid, soft voice eases its way into wrens ear from behind."
    stop music
    s "Um… wren?"
    show wren surprised
    """
    Wren freezes at the sound of this voice. Knowing the owner of the voice his
    body refuses to turn around and he freezes in place.

    Fuck. Fuck. Fuck. Fuck.{fast} Fuck. Fuck. Fuck. Fuck. I knew it, I fucking knew it.
    Of course it would be him. This is the worst day of my life.
    """
    show somchai surprised at pos8 with moveinright
    show wren angry
    s "ummm… hello Wren."
    "If I move, I’ll die."
    show cg06 with fade
    k "What are you doing here, Somchai?"
    "Please tell me this is a joke...{w}a cruel joke."
    show cg05
    hide cg06
    s "I came to talk to Wren"
    "I’m about to scream and run away at the same time right now. this can’t be happening."
    s "Wren? Can we have a second?"
    "I don’t have control of my body right now"
    show cg06
    hide cg05
    k "You had plenty of seconds before now buzz off!"
    "Kyran always coming in clutch"
    show cg05
    hide cg06
    s "I’m just trying to talk to him for a bit. I want to explain myself."
    "EXPLAIN?! NOW YOU DECIDE IT’S TIME TO EXPLAIN?!"
    show cg06
    hide cg05
    k "You had your chance and you blew it."
    show cg05
    hide cg06
    s "ky. Listen."
    show cg06
    hide cg05
    k "Don’t call me that. It’s kyran… not ky."
    "He hates the nickname ‘ky’"
    show cg05
    hide cg06
    s "Sorry. Kyran, I really just want to explain myself. I can see he’s...{w} broken...{w=0.5} right now-{nw}"
    show cg04
    hide cg05
    w "I’m not broken. I’m pissed there’s a difference."
    "It took me lots of time and hard work to realize that."
    show cg06
    k "He speaks!"
    show cg05
    hide cg04
    s "Please. Let me explain everything. Please."
    show cg04
    hide cg05
    w "I’m busy."
    show cg05
    hide cg04
    s "Can I see you after class?"
    show cg04
    hide cg05
    w "Can’t."
    "I don’t think I physically can..."
    show cg05
    hide cg04
    s "Later today maybe? After you’re done with school."
    show cg04
    hide cg05
    w "I’m Busy."
    show cg05
    hide cg04
    s "Please. I’m begging you. Just let me explain.{w} I can do all the talking-"
    show cg04
    hide cg06
    w "As you usually do."
    show cg06
    k "Ooo~ burn."
    show cg05
    s "I’m sorry, but please. I just want to give you an explanation. There’s a reason I had to leave. I swear. I will tell you everything!"
    hide cg04 with dissolve
    hide cg05 with dissolve
    hide cg06 with dissolve
    "Maybe I should hear him out? He never was the one to do things on a whim. There has to be a reason he walked away."
    w "Tomorrow. Around lunch. Café. 15 minutes. that’s all you get."
    s "That’s perfect. Thank you. I’ll see you tomorrow. I missed you wren."
    k "I swear somchai if wren wasn’t here I’d smite you right where you stand."
    "WTF. It was going fine until you ruined it, som."
    w "k."
    s "Later."
    #[somchai leaves]
    hide somchai with easeoutright
    show kyran happy
    k "Damn. Hit you with the verbal ‘k.’, see you never som."
    show wren sad
    w "I can’t do this."
    show kyran sad
    k "Can you specify what exactly you can’t do?"
    w "Everything… this lecture, this day, this life. I can’t sit for 2 hours after that."
    "I cannot function properly right now. I’m feeling nauseous. "
    k"""
    It’s gonna be okay. I know you can do this, but if you really can’t...
    you can have my keys and have some time to yourself in the car.

    But I will say; don’t let him get to you. You became better without him. I know you can do it!
    """
################################################################################
    menu:

        "Ugh~ what should I do?"

        "Go to the lecture with kyran":
            $ dominic_points += 1
            "I can do this. I’ll try and take my mind off it."
            k "I’m here for you my dude"
            w "You’re the best ky."
            k "Don’t do me dirty like that."
            hide kyran with easeoutleft
            hide wren with easeoutleft
            scene blk
            jump after_som

        "Have some time alone in the car":
            $ somchai_points += 1
            w "Keys please. I’ll see you after class."
            k "Text me if you need anything."
            w "Thanks ky."
            k "I hate you."
            hide wren with easeoutright
            scene blk
            "Wren walks back to the car alone."
            "Happy thoughts. It’s gonna be okay. Everything is fine."
            pause 2.0
            show text "Later..." at truecenter with fade
            pause 3.0
            hide text with fade
            "After about 30 minutes of meditating, wren takes a walk to enjoy the
            scenery at school and get some nice fresh air."
            show bg19 with dissolve
            pause 3.0
            show bg05 with dissolve
            pause 2.0
            show bg08 with dissolve
            "He then makes his way back to the hall to meet kyran outside the class he was supposed to go to."
            jump after_som

################################################################################
label after_som:

    #[front of school]#
    scene bg05
    "Kyran and Wren walk to the front of the school together to meet with tobias."
    show wren reg at pos3 with dissolve
    show kyran reg at pos5 with dissolve
    show tobias reg at pos8 with dissolve
    k "You'll never guess what just happened."
    w "UGH~!"
    t "Cut to the chase."
    k "Somchai is back!"
    show tobias angry
    t "WHAT?! WHY?! WHEN?!"
    w "Where, how and who? He showed up before class. He wanted to explain himself. No big deal. There’s not fuss.
    Now can we stop talking about this? Please."
    "Tobias looks visibly upset for some reason."
    show wren thinking
    t "This is a big deal. What the fuck happened? What did he say to you?"
    show wren surprised
    w "Nothing happened. He begged me to let him explain himself and I agreed to talk with him tomorrow over coffee.
    That’s it. Now please, let it go."
    show kyran surprised
    t "But why would you agree to this? Do you not remember what he did to you? All the pain you suffered because of him? Are you stupid?"
    k "Woah there, buddy. Calm yourself. Not right now."
    show wren angry
    w "I’m not stupid…{w} completely. This conversation is over, if you continue talking about it, I’m leaving."
    t "Fine."
    show wren reg
    show tobias sad
    show kyran reg
    pause 4.0
    "Awkward silence"
    k "How about that sports game last night, huh?"
    w "It was fantastic. Let’s go to class."
    #[hallway]
    scene bg07
    show wren angry at pos8 with easeinleft
    "Wren, still upset, begins to walk towards class.
    Tobias and Kyran stay behind Wren to talk to each other."
    hide wren with moveoutright
    show tobias reg at pos7 with easeinleft
    show kyran reg at pos5 with easeinleft
    t "Was it something I said?"
    k "WaS iT sOmEthInG I sAiD? ARE YOU STUPID? Bro, just shut up and let it go.
    You’ll only make it worse with your ‘feelings’"
    t "I’m allowed to be upset and have feelings."
    k """
    Just because you have this little boy crush on wren, doesn’t mean you can
    dictate what he does and criticize what he wants.

    If you truly like him, you would let him be his own person and love him
    unconditionally, like a true friend should.
    """
    t "I care about him.{w=1.0} That’s all."
    k """
    Then let him have his time to think. Act like nothing is happening. That’s
    how you can be there for Wren. Be there for him and reassure him, not
    criticize him and call him stupid.
    """
    t "Well Sorry. I’m not an expert in \"Wren\"."
    k "You don’t have to be an expert to know how to be a good friend. Let’s go, it's time for class."
    hide tobias with moveoutright
    hide kyran with moveoutright
    show blk
    """
    With tension high. The two catch up to Wren and head to class. Wren in deep thought not paying attention.

    Today can’t get any worse. I just need to vent to my girls. Vent, then finish this horrible day and sleep it off.
    """
    #[class]
    scene bg11
    """
    The three friends get to class and sit down together.

    After an hour Wren is staring into the void.

    I listened to every word this teacher has said and yet I’ve learned absolutely nothing…{w} another successful day in college I suppose.

    Lecture finally ends. kyran, tobias, and wren exit.
    """
    show bg07
    hide bg11
    show wren reg at pos7 with easeinleft
    show kyran reg at pos4 with moveinleft
    show tobias reg at pos2 with moveinleft
    "Before anyone else can speak"
    w "Alright see you guys later gonna go to lunch~{w} KTHXBYE!{nw}"
    hide wren with moveoutright
    "Wren quickly turns,{fast} not waiting for a response to walk toward the lunch area."
    show kyran thinking
    show tobias thinking
    "Kyran and tobias look at each other. Kyran just stared at tobias then back to wren."
    k "Bye friend! See you later!"
    show tobias angry
    t "How is this okay?"
    show kyran reg
    k "Stop being a little bitch."
    t "What the fuck bro, you’re being a dick."
    k "Stop being a bitch and I’ll stop being a dick."
    t "Hmph~"
    show kyran happy
    k "Calladito se ve mas bonito."
    show tobias thinking
    t "What does that even mean?"
    k "You’re prettier when you don’t speak."
    show tobias angry
    t "You’re a dick."
    k "I know."
    "Kyran and Tobias go their separate ways. "
    #[tree hangout]
    scene bg09
    show evanora happy at pos3
    show shaula happy at pos5
    "Wren approaches shaula and Evanora sitting outside under some light tree shade.
    It is nice outside so a lot of students are enjoying the sun and hanging out outside."
    show wren sad at pos7 with easeinright
    w "Thank Satan you guys are here."
    show shaula sad
    show evanora reg
    sh "Always! Is everything okay, no offense but you seem tense."
    e "You look like you’re about to cry."
    w "I just might…{w} Somchai is back."
    pause 3.0
    "Cricket noises"
    show evanora surprised
    show shaula surprised
    pause 1.0
    sh "I’m sorry I was just waiting for you to say ‘sike’ or atleast a guy coming
    around the corner with a camera saying \"It’s just a prank bro\"."
    w "He came to see me this morning before class."
    show evanora angry
    e "Well what did the fucker want? TO DIE? Because I will grant him his wish."
    w "He wants to explain himself."
    show shaula angry
    sh "The fucking nerves of that guy. What is wrong with him?"
    w "I agreed to get coffee with I’m tomorrow..."
    show shaula sad
    sh "Do you want us to go with you?"
    w "No. I can do this, I’m just... scared."
    show evanora reg
    e "Oh no. About what? He’s not very scary. I can take him. Easily."
    "Evanora cracks her knuckles."
    w "I’m scared that my feelings for him will come back. I’m scared I’m gonna go back."
    show evanora sad
    show shaula angry
    sh "I won’t let that happen. You worked too hard to get where you are now for you to just go back."
    w "I know, that’s why I wanted to talk to you guys instead of Kyran and Tobias.
    You guys are better at this than them. They hide their feelings because they’re \"men\"."
    "I like to think I am a man without being a \"man\"."
    show shaula reg
    sh "Well, you have to get coffee with him. So, you have to show him you’re better without his weak ass."
    show evanora reg
    e """
    You just have to listen to him. You barely even need to speak.

    Just let him talk and then once he’s done, ask \"Are ya done?\" and then just leave.

    Ooh~{w=1.0} that'll make you look so badass.
    """
    show evanora happy
    show shaula angry
    sh "And like an asshole..."
    show evanora sad
    w """
    I’m gonna let him talk, get it out of his system and then he’s gonna get a piece of my mind.

    I’m gonna tell him how much what he did hurt me, and how I’m better that I don’t need him.
    I don’t need any man to make me happy.
    """
    "I mean I would like a life partner, but{w} I don’t need one. Especially not now.{w=1.0}"

    "Suddenly, there’s a whooshing sound and a frisbee comes out of nowhere hitting
    Wren in the back of his head."

    show wren embarrassed with vpunch

    "The strike scared him more than hurt him."
    show evanora surprised
    show shaula surprised
    "A large gorgeous man jogs towards the trio."
    show evanora angry
    show shaula happy
    d "My bad, I was only hoping to get your attention, not hit you. I’m really sorry."
    w "That’s your version of flirting? I think you need to work on that."
    show dominic happy at pos9 with easeinright
    pause 2.0
    show cg08
    """
    After rubbing the back of his head he turns to look at the culprit.

    There, next to him, stands this tall man in a sports tee and basketball shorts.

    His bright brown eyes look like they’re trying to peer into my soul.

    His bushy brown eyebrows look like a caterpillar and its brother crawled onto
    his face while he was sleeping on the grass or something.

    His freckles stand out from the rest of his skin tone.
    """

    d "Oh, um, let me try again. Uh~.{w} Hi.{w=1.0} My name is dominic, and I really like your face…{w} Better?"
    "He’s hot. He doesn’t even need to flirt, honestly."
    show cg07
    w "A little, but still… you might need to work on that."
    "Holy hell, dominic is a hot name."
    show cg08
    d "I really am sorry. I wasn’t trying to hit you but I was hoping for an excuse to come talk to you."
    show cg07
    w "That’s a little better."
    w "I’m Wren."
    "Please. take me right now. Scoop me up in those manly arms and save me from this day."
    show cg08
    d "Wren! Cute. Well it’s very nice to meet you. Can I take you out tomorrow?"
    hide cg07 with dissolve
    hide cg08 with dissolve
    show wren happy blush
    show shaula surprised
    show evanora surprised
    w "Like…{w} a date?"
    "Evanora and Shaula are silenced by the confidence of this strange man. Shaula interjects very quickly."
    show shaula happy
    show evanora happy
    sh "He would love to! He has a \"lunch\" thing but he’s free for dinner in the evening?"
    d  "Are you his assistant or something?"
    e "We are just his friends trying to help our guy get some ass."
    show dominic happy blush
    sh "Evanora! You saucy girl."
    show wren surprised blush
    w "Guys, this is my conversation. Please, stop!?"
    d "So~ dinner tomorrow?"
    show wren happy blush
    w "Can I at least get your number first?"
    show dominic surprised blush
    d "Oh shit yeah. Sure! I forgot that part."
    show dominic happy blush

    """
    Dominic pulls his phone out of his pocket and hands it to wren.

    Wren puts his phone number in and saves it as \"Wren\" with the car, heart eyes, and target emoji.

    He hands the phone back to dominic.
    """

    d "Cute. I like it."
    "Dominic calls the number, so Wren has it in his phone as well."
    "Dominic puts his hand out gesturing towards the phone. He saves it as \"Dominic\" with the eggplant emoji."
    show wren embarrassed
    d "Gives you something to think about."
    "Cocky little son of a bitch. I like it."
    d "I’ve gotta go. I’ll see you tomorrow."
    hide dominic with moveoutright
    "Dominic jogs off. With his huge ass bouncing in his shorts, leaving nothing to the imagination."
    show wren happy blush
    w "I’ve spoken 5 sentences to this man and I already want to have his children."
    e "You can’t birth children."
    show wren reg
    w "I can try, though."
    show wren sad
    "Holy shit. To think today was supposed to be normal and easy. Ugh~{w} I have a lot to think about."
    show wren reg
    w "Shit, I might just pass out, that was so stressful. How did I do?"
    sh "You scored a date and a phone number with a super-hot and well-hung man in less than 5 minutes. You did amazing!"
    show evanora thinking
    e "I’m impressed."
    show wren surprised
    w "AAAHHHH~. And I still have to meet up with somchai tomorrow too. Shit."
    sh "At least it’s your off day and you don’t start school until late the next day so you can get it on with the hot guy."
    show wren happy
    w "I’m not going to get it on with Dominic. It’s just dinner."
    show evanora reg
    e "He put an eggplant emoji next to his name. He wants you."
    show wren happy blush
    sh "Trust us. That man wants a piece of wren’s ‘sweet cream’. If not the whole damn barrel."
    w "Stop it guys. It’s too much. I’m already blushing, my face is so hot."
    e "Yes, we can easily tell. We have to get going anyway. "
    show evanora angry
    e "You better give us {b}EVERY SINGLE DETAIL OF YOUR DATES OR I WILL FIND YOU AND FORCE IT OUT OF YOU.{/b}"
    w "I won’t leave out any details. I’ll let you guys know if he’s circumcised or not."
    show evanora reg
    e "Ew. Not that far. that’s too much detail."
    show shaula surprised
    sh "YES PLEASE!... It’s for research purposes."
    w "You two are seriously the best. Lates my dudes."
    #[front of school]
    scene bg05 with fade
    show wren reg at pos5
    """
    Wren decides to skip his last lecture and texts a classmate to record the lecture for him.
    After he gets the confirmation that he is covered, he walks home.

    He lets kyran know what is going on. On his way home wren is blasting music in his earbuds.

    Today has been a whirlwind. Waking up hungover. Seeing somchai and now this new guy, dominic.
    I would never in a million years think something like this would happen. Stuff like this only happens in movies{w} and BL visual novels.
    """
    #[Cafe]
    scene bg15 with fade
    pause 2.0
    show blk with fade
    hide bg15
    """
    Wren makes a stop at the café, and then at the dog park to watch the puppers run around playing.

    He takes in the sights of his city and makes his way in the general direction of his house.

    Wren arrives at his place. Time having slipped away from him.
    """
    #[wren’s living room]
    show bg04 with fade
    hide blk
    show wren reg at pos7 with easeinright
    "He enters his living room and hears his owl making a ruckus in the room."
    play sound owl loop
    hide wren with moveoutleft
    show blk with fade
    """
    Wren grabs the food and makes his way to the owl’s locked room{w}, or so he thought.

    The door…

    He always locks that door before leaving every morning. Panicking he runs into the room.

    Kyran is there feeding the owl.
    """
    stop sound
    show owl at owlcenter with dissolve
    show kyran reg at pos3 with dissolve
    show wren surprised at pos8 with moveinright
    k """
    Oh hey! You’re finally home.

    I came to pick up my stuff I left here last night and saw that you weren’t here yet.
    Your owl was making noise, so I thought you haven’t fed them yet.
    """
    show wren reg
    w "You scared the living shit out of me! I thought someone broke in or he got out because I didn’t lock his room or something."
    show kyran sad
    k "Sorry. I should’ve texted you."
    w "No it’s okay now that I know it’s you. I’m glad you came and took care of him."
    "Kyran is actually extremely thoughtful and really cares about me. He’s the epitome of the best friend."
    show kyran happy
    k "Sure thing. You know I’ve got your back."
    show wren happy
    w "Thanks for everything."
    "Kyran was slightly confused, thinking all he did was feed his carnivorous bird."
    show kyran thinking
    pause 3.0
    show wren reg
    k "Umm you’re welcome~?"
    show wren happy
    w "Not just for feeding my bird, but for being there for me and being a really great best friend."
    "Because he really is."
    show kyran happy
    k "You too my guy. We are in this life together and we have to be there for each other no matter what. You’re my soul-brother."
    w "Whatever that means. Sure."
    k "I love you man."
    w "I love you too soul-bro."
    k "Alright I gotta go. See you tomorrow maybe? If not, see you next day for school."
    w "See ya’."
    hide kyran with easeoutright
    """
    I’ve made it so I have a day off in the middle of the week.
    I know it’s weird but people owed me favors that I cashed in.
    Gotta make sure mental health is in check and a day off in between the chaos helps a lot.

    I walked over to my owl child and looked at the cage.
    """
    show wren at pos6 with ease
    w "You’re so dirty and gross but I love you so much."
    play sound owl
    o "WHO~!"
    #[wren’s Bedroom]
    scene bg02
    stop sound
    play music night
    show wren reg at pos7 with easeinleft
    "Wren quickly finishes his routine and gets ready for bed."
    hide wren with easeoutbottom
    "Moments getting into bed he receives a SMS."
    play sound sms
    w "Oh, it’s dominic."
    d "\"Excited for dinner tomorrow?  If you have anything in mind for dessert just let me know.\""
    "Wren takes a few seconds to contemplate."
    w "\"Red velvet cupcakes sound amazing.\""
    pause 2.0
    play sound sms
    d "\"I can arrange that. See you tomorrow. Dream sweet dreams about me.\""
    w "\"Maybe~ ;). sleep tight, don’t let the bed bugs bite.\""
    pause 2.0
    play sound sms
    d "\"But what if I like the pain?\""
    pause 2.0
    play sound sms
    d "\"I’m sorry that was really bad.\""
    play sound sms
    d "\"I’m gonna go cry now.\""
    pause 2.0
    play sound sms
    d "\"Good night. Mr. adorable.\""
    w "\"lol Good night. :3\""
    """
    That was a surprisingly short interaction but I kinda loved it.

    He’s confident, yet awkward. He’s funny and hot.

    Something definitely is wrong with him.
    I just don’t know it yet. No one can be that hot AND that perfect.

    Wren put his phone on the side table and tried to get comfortable.

    After tossing and turning for a while, his exhaustion finally catches up. Wren eventually finds sleep.
    """
    show blk with fade
    stop music fadeout 1.0
    #day 2 ends.#
    jump day3
