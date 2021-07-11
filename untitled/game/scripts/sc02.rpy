## MEETING BEN
label sc02_main:
    scene sc_apt_day
    with flash
    play music calm fadein 1.5 volume 0.8
    window show
    n """
    Time suddenly moved backwards as Arthur arrived at his apartment

    Everything was silent, and a dim light shone through the curtains

    He stared at the bloodless carpet as he laid in bed

    While his head was spinning, the clues he found remained present
    """
    window hide
    nvl clear
    $ renpy.pause (0.5, hard=False)
    $ quick_menu = True
    a "..."
    show arthur conf at ctr
    a "Did I make it?"
    a sad "I feel exhausted..."
    a "Jumping takes a lot of energy, not to mention I can only go back 24 hours at a time."
    a angry "Ah, shit! I can't believe I fell asleep!"
    a "It's already 7am. I need to find the culprit before the murder happens again."
    a -angry "... The only person who can help me in a situation like this is my brother. I have to call him."
    $ quick_menu = False
    hide arthur

    scene black
    with fade
    $ renpy.pause (1, hard=True)
    $ quick_menu = True
    "Operator" "Good day, who shall I connect you to?"
    a "Hey, connect me to Mr. Benjamin Walker, please."
    "Operator" "Sure thing, please hold."
    play sound s08 volume 0.7
    scene sc_phone
    with fade
    $ renpy.pause (0.5, hard=False)
    show arthur at halfleft
    a "... Hello?"
    show ben at halfright
    $ renpy.pause (0.5, hard=False)
    b "Hello, how may I help you?"
    a sad "It's me, Ben."
    b angry "Arthur? I've told you not to call me! Especially on a day like this."
    b "I have to meet a client during the afternoon, so I won't deal with-"
    a "Please, wait! You know I wouldn't do this if it weren't important..."
    b -angry "Ahh, this is ridiculous. What do you want?"
    a -sad "I need your help, but, it's just... It's hard to explain."
    b "Why? What have you done this time?"
    a sad "It's not what I did, but what I didn't do. No one else is going to believe me."
    a -sad "There was a woman thrown over the floor of my apartment, and-"
    b angry "Please, Arthur. Spare me your sex life..."
    a angry "What? It's not that! I just... can't bring myself to say it."
    b angry "Out with it!"
    a "Alright, alright!"
    a -angry "I found a woman on my apartment, and she was..."
    a sad "She was dead, Ben."
    b conf "Seriously? You killed someone?!"
    a "Of course not! I would never do something like that, not after the war..."
    a -sad "Someone must've tried to incriminate me."
    b sad "Arthur... just what have you gotten yourself into?"
    a "I know it's hard to believe, but I need your help on this."
    b -sad "And what exactly do you expect me to do?"
    b conf "Are you trying to make me help you hide a murder? To go bury a body somewhere?"
    a "No, Ben... Even if I wanted to, I can't do it yet."
    b -conf "What do you mean 'not yet'?"
    a sad ". . ."
    b "You jumped again, didn't you."
    b angry "Did you forget about what happened last time?! You could barely even remember your name!"
    a -sad "I am aware, but I had no other choice."
    a sad "There was a huge pool of blood, and the police were about to arrest me."
    a "Trying to talk myself out of it would only make things worse."
    b sad "... Ah, Christ."
    b -sad "What's your plan then? To find the culprit before he gets to your apartment?"
    a -sad "Something among those lines."
    a sad "I just can't do this alone. Please, I beg you to trust me..."
    a "I am asking you this as your brother."
    b conf ". . ."
    b -conf "Alright, you can count on me."
    a happy "..!"
    b "What'll be our first course of action?"
    a -happy "Ahem, right."
    a "I found two clues yesterday, or rather... There were two important clues at that moment."
    a "They could tell us more about the woman and her relationships."
    a "Hopefully it'll be enough to find a suspect and stop him on time."
    b happy "So you don't even know who she was? You can't be serious! Ahaha."
    a angry "I couldn't catch a proper look. It was dark and papers were covering her face."
    a "She wasn't carrying any sort of ID either. On top of that, the police were pressuring me..."
    a -angry "Either way, what I found was a stuffed lion toy and a blue glass perfume."
    b -happy "How do you reckon that's going to help us prove your innocence?"
    a "I'm convinced that we can discover this woman's identity, and determine where she was seen last."
    a "If luck is on our side, we'll get to her before the murderer does."
    b "Very well, then. We should each go investigate one of the leads."
    b sad "We need to use whatever time we have left... For your sake."
    b -sad "Where will you go investigate?"
    a "I'll go check out the toy store and find any information on the lion."
    a "You go ask about the 'Arbre Bleu' perfume at that popular store."
    a "Let's meet at Black Royal Cat Hotel by 2:00 p.m. Got it?"
    b "Yes, I'm just writing down the name of the perfume."
    a "Alright, I'll hang up then."
    a sad "... Thank you again, Ben. Truly."
    b happy "... Go on. I'll meet you later."
    b angry "Do NOT be late."
    hide arthur
    hide ben
    $ quick_menu = False
    stop music fadeout 1.0
    scene black
    with fade
    $ renpy.pause (2, hard=False)

    return
