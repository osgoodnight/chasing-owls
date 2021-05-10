label day3:
    scene nightmare with flash2
    $ persistent.unlock_nightmare = True
    $ renpy.notify("New Background Unlocked")
    play music suspense
    "{i}Where am I?{/i}"
    "{i}The last thing I remember was...{/i}"

    uv "{size=30}วเรน์...นะ...{/size}"

    w "{i}What? Who's that? Is that thai?{/i}"
    show somchai sad at pos5 with dissolve
    s "{size=30}ขอโทษ...วเรน์...{/size}"

    w "{i}Somchai what are you doing here?{/i}"

    s "{size=30}สมฉาย...เป็น...ขอโทษ...{/size}"
    s "{size=30}มากแลว...นะกรับ...{/size}"

    w "{i}Somchai you're worrying me.{/i}"
    "{i}I see something out of the corner of my eye and look over to the left.{/i}"
    hide somchai with flash1
    "{i}When I look back, Somchai is gone.{/i}"
    w "{i}Somchai? Somchai, where'd you go?{/i}"
    show blk with flash1
    show figure with dissolve
    $ persistent.figure = True
    $ renpy.notify("New Character Unlocked")
    "{i}Infront of me a strange being appears in front of me. Dark from top to bottom.{/i}"
    "{i}I couldn't see his face but he has to have one...{w} right?{/i}"
    w "{i}Who..What are you?{/i}"
    f "{i}Do you want history to repeat?{/i}"
    w "{i}What do you mean \"repeat\". What happened in my past?{/i}"
    f "{i}Do you want the pain again?{/i}"
    w "{i}Of course I don't, what type of question is that?
    If I had it my way I would never hurt again.{/i}"
    f "{i}The boys aren't your main problem. Be wary.{/i}"
    hide figure with flash1
    w "{i}Wait! Don't leave! Who are you? Who else should I be watching?{/i}"
    show blk with flash1
    show somchai reg at pos3
    show dominic reg at pos7
    "{i}Somchai and Dominic stand before Wren.{/i}"
    w "{i}What are you guys doing here?{/i}"
    stop music fadeout 2.5
    show bg02 with flash2
    hide somchai
    hide dominic
    show wren surprised at pos5 with moveinbottom
    $ day +=1
    "Wren wakes up in a cold sweat in his bed."
    "Damn, that was the worse nightmare I've had recently."
    "I thought I was done having nightmares since I left the tribe…"
    "Ugh~ what time is it?"
    pause 2.0
    with hpunch
    "5 AM?!??!"

    """
    Ugh am I going to have a repeat of yesterday?{w} Wait…{w} \"repeat\"...{w}
    That figure said that…

    What does he mean by that?

    And what are these other problems that I have…{w} or will have.

    UGH~! I’m having a headache again. Today is going to be worse
    than yesterday isn’t it? Well I better try and go back to sleep… hopefully.
    """
    hide wren
    hide bg02 with fade
    show blk


    """
    Wren tosses and turns for the next hour thinking of nothing but what that figure has said.

    \"Do you want history to repeat?\"...{w}
    \"Do you want the pain again?\"...

    Wren finally gives up and accepts his fate.
    """
    show bg02 with hpunch
    show wren angry at pos5 with moveinbottom
    w  "AH!!! I GIVE UP! FINE!!! Be like that life. I guess I’ll just go cry in
    the shower for a bit until I feel better."
    hide wren
    hide bg02
    play sound shower loop

    """
    When I was still living with my parents on the reservation, I was having nightmares all the time.

    At the time I knew Somchai so he already knew about them once we started seeing each other.
    Once I talked with my parents they suggested I see the tribe's Shaman.

    I was describing my dreams to them as much as I could and when they suddenly stared in shock.
    From what I understand, the \"dreams\" I had weren’t dreams, but memories.

    Everything I described were things that happened in the tribe to my family in the past.
    From that point on, the shaman told my father and that set this whole
    \"you’re the next chief\" thing in motion.

    Also, it probably doesn’t help that I'm a two-spirit, too... Originally, I was hoping to get out of the tribe for a
    bit to do many things I wanted to do in life. That’s why I wanted to go to
    school off the reservation.

    I’m not saying I hate my culture or where I come from.
    It just isn’t the life I want to live. The people are great and I love my family,
    however I just don’t want to be told how to live my life.
    """
    stop sound fadeout 2.5
    scene bg03
    show wren sad at pos4dwn
    "Several moments, and some tears later, Wren sits in his living room waiting for Kyran to come get him."
    "Even though I don’t have any classes today, I still spend my time at the school to get some work done.
    Also later… I have some dates."
    show kyran reg at pos7 with easeinright
    play music theme1
    k "Wow you look like hell. Did you sleep?"
    w "Only just enough..."
    k "What happened?"
################################################################################
    $ shuffle_menu()
    menu:
        "Should I tell him about my nightmare?"

        "Don't tell him.":
            $ somchai_points += 1

            w "It’s fine I just couldn’t sleep from the stress of yesterday."
            jump day3morn

        "Tell him.":
            $ dominic_points += 1

            w "Well, I had a nightmare and was woken up in a cold sweat…"
            "Wren spends the next few minutes explaining his nightmare to Kyran.
            Kyran fights the urge to fight the imaginary figure Wren was talking about."
            jump day3morn

################################################################################
label day3morn:

    k "Well, you know what will make everything better? Coffee."
    w "Sounds good."
    show wren reg at pos4 with ease
    hide kyran with easeoutright
    hide wren with easeoutright
    "Kyran and Wren both get up and head out the door."
    scene bg05
    "After heading to school. Wren and Kyran go their separate ways."
    show wren reg at pos7 with dissolve
    show kyran reg at pos4 with dissolve
    k "I’ll see you after class Wren. Try not to do anything I wouldn’t do."
    w "No promises."
    "Damn, and I was totally planning on doing all the bad things..."
    hide kyran with easeoutleft
    "Wren watches as Kyran walks off into the distance. He goes to the school’s
    cafe to study and do some of his assignments for his classes."
    stop music
    hide wren
    show bg16 with fade
    play music cafe fadein 3.0
    hide bg05
    show wren reg at pos7dwn
    "Ugh~ Why do teachers have to give us so many assignments?"
    pause 1.0
    play sound sms
    pause 1.0
    "Who would be calling this early in the morning?...{w} Oh it’s Dominic."
    "Wren opens his messages and reads it."
    d "\"Good Morning you adorable human you.\""
    "Wow… I was not expecting that."
    w "\"Good Morning to you too, sexy.\""
    "I wonder why he wants to talk to me this early?"
    pause 1.0
    play sound sms
    pause 1.0
    d "\"What are you doing today?\""
    "I think he wants to hangout with me before dinner."
    w "\"Nothing much. I’m just at the school’s cafe doing some homework until lunch.\""
    "Ugh lunch, how could I forget. I’m not looking forward to that."
    pause 1.0
    play sound sms
    pause 1.0
    d "\"Well, I was wondering if you wouldn’t mind that I hang out with you for a bit before my first class.\""
    "Called it."
    w "\"Yeah, sure, why not.\""
    "I hope Somchai doesn’t notice me this time. How did he even know…"
    pause 1.0
    play sound sms
    pause 1.0
    d "\"Perfect, because I’m already here.\""
    stop music
    show wren surprised
    "What? He’s already here?"
    "Wren looks up to see that big beautiful himbo who is chasing his heart"
    show dominic happy at pos1 with easeinleft
    d "Is this seat taken?"
    w "How did you get here so fast?"
    show dominic at pos3dwn with move
    d "Good. I was hoping you’d be alone."
    "He didn’t answer my question…"
    w "Sorry, let me rephrase that. How did you get here so fast?"
    play music theme1
    d "Actually, I was thinking about you last night and when I woke up I really
    wanted to see you. So, I came here earlier than I usually do hoping that I could see you."
    show wren happy blush
    w "Oh, that’s sweet...{w} and kind of creepy…{w} but in a cute way."
    "I dropped the pencil I was holding and put my hand flat on the table."
    w "So, what made you want to talk to me? I’m not exactly most guys’ first choice in general."
    "Dominic looks down at my hand and grabs it gently."
    d "I’m not quite sure honestly… I looked at you from across the field and
    suddenly wanted to talk to you. And when I got closer and looked into your
    eyes I knew at that moment I needed you in my life."
    w "Where the hell did you learn how to speak like that?"
    show dominic thinking
    pause 1.0
    show dominic happy
    d "High school english class... or was it in a show I saw?"
    w "Also, Why are you holding my hand?"
    show dominic happy blush
    d "Because I want everyone here to know that you are the one my heart wants."
    w "Gosh, please stop talking like that you’re giving me goosebumps. You can’t
    be telling the truth. Did someone put you up to this? Am I being Pranked?"
    show wren thinking
    "I quickly look around the room for hidden cameras..."
    show dominic reg
    pause 1.0
    d "What are you doing?"
    show wren reg
    w "Is Ashton Kutcher or Jason Goldberg hiding behind those bushes outside?"
    show dominic happy blush
    d "What? No, I’m not the type of guy who jokes around with love. A man who
    doesn’t tell his feelings and doesn’t stay true to his heart is a coward.
    Undeserving of the title \"MAN\"."
    show wren happy blush
    w "That is very… chivalrous of you. But, I have enough problems going on in my
    life and I just don’t need another."
    d "Well lucky for you because I come with no baggage. At Least none that will bother you."
    w "That doesn’t sound too reassuring."
    d "Well that’s all I can offer at the moment."
    "Without noticing it, Wren feels Dominic’s thumb caressing his hand."
    show wren embarrassed
    w "Can you not do that? It tickles and you haven’t even bought me coffee or
    food yet. I’m not a hussy."
    d "I’ll get you whatever you want! Even if it’s just to hold your hand."
    "Wren pauses for a moment and smiles."
    show wren happy blush
    "What a huge dork… I like it."
    w "Sure, just get me a caramel macchiato with an extra shot of espresso."
    d "Uhhh~ could you repeat that one more time?"
    show wren happy
    w "Just go up to the counter and tell the cashier that you want to buy me a drink.
    She knows my order."
    d "Anything for you Wren."
    show dominic at pos2 with ease
    hide dominic with easeoutleft
    pause 1.0
    show wren thinking
    "Oh God, did I just get a new pet? Do I smell extra nice today or something?
    I feel like shit so probably not. And how has he not seen the bags under my eyes?
    Maybe he has eye problems..."
    show wren reg
    show dominic happy at pos2 with easeinleft
    d "Here’s your drink, Wren."
    show dominic at pos3dwn with ease
    show wren happy
    w "Thank you, Dominic."
    "Wren takes a sip from his fresh hot drink."
    w "Oh fuck me that’s good."
    show dominic surprised
    d "YOU REALLY MEAN IT?!"
    show wren embarrassed
    w "What? No, not you... At least not yet."
    d "So you’ll give me a chance?"
    show wren thinking
    w "What makes you think I wouldn’t?"
    show dominic embarrassed
    d "I don’t know… I’m confident about many things but with guys not so much."
    show wren happy
    w "Awe that’s so cute. You do have a weakness."
    show dominic reg
    d "What was that?"
    w "Aww~ you’re so cute."
    show dominic happy
    d "Thank you? Anyway, what type of food do you like?"
    w "Well..."

################################################################################
    $ shuffle_menu()
    menu:
        "What food do I like?"

        "Tamales":
            $ dominic_points += 1

            w "I like Tamales."
            d "Those are amazing! I know a really good mexican restaurant near my
            house if you wanna go with me sometime."
            w "You better be right or I’ll never forgive you."
            hide wren with dissolve
            hide dominic with dissolve

        "Burgers":
            $ dominic_points += 1

            w "I like Burgers."
            d "Those are amazing! I know a really good restaurant near my house if you
            wanna try it out with me. Their burgers will melt in your mouth."
            w "You better be telling or I’ll never forgive you for getting my hopes up."
            hide wren with dissolve
            hide dominic with dissolve

        "{size=30}ข้าวไข่เจียว{/size}":
            $ somchai_points += 1

            w "{size=30}ผมชอบข้าวไข่เจียวนะ{/size}"
            show dominic reg
            d "I don’t have the slightest clue on what that could be."
            w "\"{i}Khao khai chiao{/i}\" It’s a thai dish. It’s an omelet on top of rice."
            show dominic happy
            d "Wow I didn't know you could speak squiggly lines."
            pause 1.0
            show wren reg
            w "It’s thai..."
            d "Well I could probably make that for you if you wanted."
            show wren happy
            w "Maybe..."
            hide wren with dissolve
            hide dominic with dissolve

        #"Anything edible" if somchai_points >= dominic_points:
            #$ somchai_points += 1

            #[only if unlocked]
            #(Includes a secret scene)
            #stop music fadeout 2.0
            jump flashback_1

################################################################################
label day3dom:

    stop music
    """
    Dominic and I sit and just casually talk while doing our homework together.
    He’s actually a really sweet guy. Very loud but sweet. He plays for the college’s
    basketball team and does... something important I think.

    I don’t really pay attention to guys running around with balls...{w}
    Wait not those kinds of balls...{w}the other ones.

    You have a dirty mind.
    """
    "After about an hour Dominic had to leave to do something with… nevermind."
    "I stayed there and continued my classwork."
    scene bg05
    show wren reg at pos5
    """
    After another hour had passed Wren walked to the front of school to wait for
    Somchai to pick him up.

    There’s a lot of people getting out and going to class.
    That’s the one thing I never understood about University: Why did they schedule
    afternoon classes like this?

    There’s never any parking and when you do get parking
    it’s a 30 minute walk to your class.
    """
    "After about 10 minutes, Wren spots a familiar car pulling up. The driver side
    door opens and it’s Somchai."
    show somchai happy at pos8 with easeinright
    s "You decided to hear me out. I’m happy."
    w "Well~ let's get this over with you have a lotta explaining to do."
    show somchai reg
    "Somchai squints a little bit to the left of Wren. Pausing. Saying nothing."
    w "What are you looking at?"
    s "Oh nothing I guess I just saw an interesting looking squirrel or something."
    show somchai happy
    "Somchai smiles at Wren and gets back in his car."
    w "Well, let's hope this isn’t a trainwreck."
    hide somchai with easeoutright
    hide wren with easeoutright
    "Wren opens the passenger side door and hopes in. Once Wren buckles up the car
    heads towards the coffee shop."
    stop music fadeout 1.0
    scene blk
    show text "{size=50}Meanwhile...{/size}" at truecenter with fade
    pause 3.0
    hide text with fade
    scene bg05
    show dominic reg at pos5 with easeinleft
    play music awkward

    "As Dominic walks towards his class all sweaty from playing ball with the boys
    something familiar catches his eye. He stops and hides behind the corner."
    show dominic happy
    d "Is that...Wren? Oh, he’s so cute. Just look at that cute butt. Wait! Who’s
    that man he’s with? Damn, he’s cute too. Ugh, what am I saying I haven’t seen that
    guy around Wren recently. I hope he’s not trying to steal my future husband."
    "The guy notices Dominic. Making Dominic hide behind the wall."
    show dominic embarrassed at pos3 with move
    d "Shit! I hope he didn’t see me."
    "After a moment, Dominic looks back around the wall and sees Wren getting into the man's car."
    d "Wren what are you doing? Don’t let him take you away from me. I need you."
    "The car slowly speeds off towards the exit of campus."
    show dominic reg at pos5 with move
    d "Dammit, I guess I can’t go to class today. Well, it’s not like it's an important class.
    Well, Wren, here I come to save the day! Ooh~ I can be his knight in shining armour.
    Yes, that’s a good plan."
    hide dominic with moveoutright
    show blk
    "Dominic runs towards his bike and unlocks it. He hops on and rides after the two in the car..."
    d "You can’t have him. Not on my watch!"
    stop music
    scene bg15
    play sound cafe fadein 3.0 loop
    show wren reg at pos4 with easeinleft
    show somchai reg at pos2 with easeinleft
    "Somchai and Wren pull up to the cafe and walk inside to order their drinks."

################################################################################
    $ shuffle_menu()
    menu:
        "What should I get this time?"

        "Caramel Macchiato":
            $ dominic_points += 1

            "Sometimes I just want to be covered in caramel sauce and live happily."
            w "I’ll have a caramel macchiato."
            s "Interesting… I guess a lot has changed since I’ve been gone."
            w "You have no idea."
            jump day3som

        "Cappuccino":
            $ somchai_points += 1

            "I’ve had enough sweets for today. I’ll just order something simple."
            w "I’ll have a cappuccino, please."
            s "I see things haven’t changed much."
            w "Well that’s not entirely true."
            jump day3som

################################################################################
label day3som:

    scene bg16
    show wren reg at pos3dwn
    show somchai sad at pos7dwn
    "After we order, we go find a place to sit to start the dreaded conversation
    I haven’t been looking forward to since yesterday."
    s "Are you okay Wren? You look like you haven’t gotten enough sleep. Did you
    have a nightmare again?"
    w "Yeah, but that’s not why we’re here. How are you going to make this better
    Somchai? How are you going to make me forgive you?"
    s "...I didn’t want to leave you. But, I had to."
    w "Why didn’t you tell me in the first place?"
    s "I thought you would get upset?"
    show wren angry
    w "I’m upset now!"
    "Wren accidentally says that a bit too loud in the cafe. It goes quiet for a moment."
    s "I’m sorry Wren. I just thought-"
    w "That’s exactly why. You thought but didn’t say it. That’s your problem Somchai,
    You always keep everything to yourself. You know I loved you. You could tell me anything...
    and yet you didn’t. You know that pissed me off."
    s "I know, and I’ve learned my lesson. But, I missed you everyday that I was gone."
    w "So... tell me why you left me alone."
    s "Well, remember the night I took you to the park to have a picnic date?"
    w "Yeah?"
    stop sound
    #show cg06_2
    play music sweet
    s """
    Well that night I was supposed to tell you, but I was too scared to say anything.

    The week leading up to that night, my parents had told me that we had to move back to Pattaya.
    And I didn’t know if I was going to ever see you again.

    They told me that my grandparents needed us to move back and so I had to go at the time because we
    were still in high school. I couldn’t go against my parents and you know that.

    There wasn’t a day I wished I could have stayed to be with you.
    """
    "This whole time he left because his parents needed to move back. Goddamn it
    Somchai! You should have told me this. It would have saved me so many tears
    and sleepless nights. You asshole."
    #show cg06_1
    #hide cg06_2
    w """
    I’m so pissed you couldn’t tell me this. You know I would have been fine
    if you just told me like you should.

    Maybe, we could have worked through this, together.

    You destroyed me Somchai, I always thought I was just not good enough.
    You made me think that I wasn’t worth it. Wasn’t worth anything to anyone.
    """
    #show cg06_2
    #hide cg06_1
    s """
    Wren, I’m so sorry I did this to you. I regretted my decision every single day.

    When I left I missed you so much that I wanted to go against my parents and come back to you.
    I would have even proposed to you if it meant I could always be with you.
    """
    "Propose?{w} Did he just say what I think he said? I thought for a moment what
    my life could have been like if he had just told me or was able to stay."
    s "Wren please don’t cry."
    "Once Somchai said that I saw tears on the lid of my coffee cup. I was crying and I didn’t even notice."
    stop music fadeout 1.5

    scene blk
    show text "{size=50}Meanwhile...{/size}" at truecenter with fade
    pause 3.0
    hide text with fade
    scene bg15
    play music awkward

    "After biking for about a mile or so, Dominic sees the car pull into the
    cafe parking lot and stops behind a building next to the cafe."
    d "Finally, I thought I was going to have to do extra exercising today before practice."
    "Dominic sees Wren and the other guy walk into the cafe. Once he locks his bike up,
    he sits outside the cafe and watches the two chatting at a table."
    show dominic thinking at pos2 with easeinleft
    d "Who is that guy? Also, Wren looks pissed off. He’s kinda cute when he’s mad."
    "Dominic hears Wren shout from outside the cafe clearly."
    d "Wow he’s really pissed. Should I do something? No, I better wait for a bit
    and if something happens I'll swoop in and save him like the knight that I am."
    "Dominic sits there for about five minutes trying to not bring attention to
    himself while staring at the two inside. He looks closely at Wren and notices a few tears on his face."
    show dominic angry
    d "Oh, that son of a bitch. Making Wren cry is unforgivable. I will make you pay!"
    "Dominic stands up and enters the cafe."
    show bg16 with dissolve
    hide dominic
    show wren reg at pos3dwn
    show somchai sad at pos7dwn
    #show cg06_2
    #hide dominic
    s "Wren please don’t cry."
    "A moment later Dominic shows up out of nowhere."
    #show cg06_3
    stop music
    show dominic angry at pos1 with moveinleft
    d "What did you do to my Wren?"
    play music suspence
    w "Dominic?!"
    s "Who’s that?"
    "Wren, completely flabbergasted, doesn’t have time to respond before Dominic does."
    d "I’m his boyfriend. The names Dominic."
    "Dominic puts his arm around Wren. Wrens eyes go wide as he looks up at the himbo currently touching him."
    s "Oh~, nice to meet you Dominic. I’m Somchai."
    d "What’s your relation to my Wren?"
    "\"My Wren\"? Are you kidding me? I’m getting ready to throw hands."
    s "I’m his… former boyfriend."
    "Wren’s eyes shoot back to Somchai’s."
    "\"Former boyfriend\"? That is the first time he’s ever said the word \"boyfriend\"
    while referring to me. What is going on? Someone get me out of here!"
    d "Former boyfriend? How could you let such an adorable and smart guy get away from you?"
    s "Well, I had family issues and had to move away."
    d "Oh that’s too bad. Well it’s nice that you’re still friends with him, right?"
    s "I mean, I was..."
    d "Don’t tell me you were going to try and get back together with him."
    "Oh gosh, I can sense the tension in the air. This isn’t going to end well...if it ends."
    s "Actually, I came here to apologize."
    d "Well, I hope it won’t take too long because we have another date later. And I have a lot planned for us."
    "Dominic ruffles Wren’s head a little then proceeds to caress his cheek."
    s "Oh~, well, it shouldn’t..."
    "I know that look in his eye. That’s the look of the precursor to an atomic
    bomb dropping. This definitely won’t end well."
    d "Well after yesterday’s date I needed more of him. And, after all this isn’t a date."
    s "Well, I was hoping to go on a date with him myself, but it seems that some
    jock has taken what is rightfully mine."
    "Oh no. Shit, shit, shit, shit, shit! I don’t think I can handle this right now."
    "The two lovers begin to try and one up each other. Getting louder and louder in the cafe.
    Most of it Wren isn’t paying attention to until Somchai’s voice is heard over the fight."
    s "YEAH? WELL AT LEAST I’VE HAD SEX WITH HIM!!!  AND HE TOLD ME IT WAS THE BEST NIGHT OF HIS LIFE."
    "Oh hell no. I have to do something. People are staring. I don’t want to get kicked out of my favourite place."

################################################################################
label recall_1:
    $ shuffle_menu()
    menu:

        "Oh hell no. I have to do something. People are staring. I don’t want to get kicked out of my favourite place."

        "Yell at Somchai to stop":
            $ dominic_points += 1

            jump day3a

        "Yell at Dominic to shut up":
            $ somchai_points += 1

            jump day3b

        #"EJECT!" if somchai_points >= dominic_points:
            #"Being tired of this, Wren gets up and walks out of the Café."
            #[only if unlocked]
            #(Includes a sex scene)
            #jump day3c

################################################################################
