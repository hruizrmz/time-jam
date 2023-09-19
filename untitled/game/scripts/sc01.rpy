## INTRO SCENE
label sc01_main:
    $ quick_menu = False
    scene black
    with Dissolve(2)
    $ renpy.pause (1, hard=True)

    play music som fadein 1.0
    scene sc_bar
    with Dissolve(2)
    n """
    The Golden Hat Bar is a nice small place, adorned by a yellow light.

    The shelf on the back displays bottles of all kinds.

    And there's a noticeable lack of cleaning...

    But the cozy and calm ambience make up for it.
    """
    window hide
    nvl clear

    # dialogue starts
    $ quick_menu = True
    show barman at rightNPC
    with Dissolve(0.4)
    bm "Sir, please get up. Do you know what time it is?"
    show arthur at halfleft
    with Dissolve(0.4)
    a "I'm sorry, what did you say?"
    bm "The time, sir... It's past 2 a.m. You've been asleep for a while."
    bm "We are about to close for the evening so I humbly ask for you to leave."
    dm "You want him to go? But we're just getting started!"
    dm "Such a killjoy... just leave my friend here alone."
    bm "Don't think I've forgotten about you, you're next!"
    bm "Bloody fat drunkard..."
    bm "Hey you, are you able to stand?"
    a "Yeah, I'm fine..."
    a "Here, have this. I apologize for the inconvenience."
    bm "Oh, it's alright, sir."
    a happy "I insist."
    bm "Well, thank you very much! Should I walk you to the exit?"
    a -happy "That won't be necessary. I can manage on my own."
    "{i}I say that and yet I almost fell on my ass as I stood up...{/i}"
    hide arthur
    hide barman

    scene sc_alley
    with Dissolve(2)
    n "Arthur lit up a cigar and observed the dark sky for a moment."
    n "The night was illuminated by stars and flickering street lamps."
    n "Perfect for walking a couple blocks and showing the way back home."
    a "Ah... I guess it's time to go back."
    window hide
    nvl clear
    stop music fadeout 1.0
    $ renpy.pause (1, hard=False)

    scene black
    with Dissolve(2)
    show arthur at ctr
    with Dissolve(0.1)
    a "Damn it... I hate being on the third floor."
    a angry "The rent is not worth tripping on all these stairs"
    hide arthur
    with Dissolve(0.1)
    play sound s01
    queue sound s02
    $ renpy.pause (2, hard=True)
    scene sc_apt_night
    with Dissolve(2)
    show arthur at ctr
    with Dissolve(0.1)
    a conf "Huh, it's quiet in here... What happened to that annoying leak?"
    a "The chairs are out of place too. Was I already drunk before getting to the bar?"
    hide arthur
    scene sc_body
    with Dissolve(0.2)
    play sound s03
    a ". . ."
    $ quick_menu = False
    n "As Arthur fell to the ground, he lost his composure."
    n "A scream that carried both fright and pain rang through the hallway."
    n "This was reality; he had found a woman's corpse inside his apartment."
    play music pan volume 0.6
    window hide
    nvl clear
    $ renpy.pause (0.5, hard=False)
    $ quick_menu = True
    a "God..."
    "{i}I can hardly breathe. This is just insane.{/i}"
    "{i}... Get it together. I need to take a closer look and figure this out.{/i}"
    $ quick_menu = False
    call screen bag_01

label sc01_toy:
    show screen toy
    "This seems interesting, but why was she carrying a plush toy?"
    "The tag says it's from 'Doorbell Toys'."
    "... Other than that I only see a bunch of makeup and keys here."
    hide screen toy
    scene sc_apt_night
    with Dissolve(0.5)
    $ renpy.pause (0.5, hard=False)
    $ quick_menu = True
    la "What do you think you're doing!? You're going to wake up the whole damn building..!"
    la "Don't even get me started on the ti-- Oh, Christ!"
    show arthur sad at ctr
    with Dissolve(0.1)
    "{i}Shit, she noticed the body... I probably shouldn't be holding this bloody purse either.{/i}"
    show arthur conf
    "{i}What's she running to the window for..?{/i}"
    la "Help! Police! There's been a murder!"
    play sound s04 volume 0.5
    "Policeman" "Quick, go call for some backup!"
    a angry "Ah..!"
    "{i}I can't really blame her. I'm scared to death myself.{/i}"
    "{i}Quick, get a grip! Are there any other clues?{/i}"
    hide arthur
    $ quick_menu = False
    scene sc_body
    with Dissolve(0.2)
    call screen bag_02

label sc01_perfume:
    show screen perfume
    "Wait, there's a perfume bottle at the very bottom of the bag. Was she keeping it hidden?"
    "Looks like it's called 'Arbre Bleu'. Surely this can't be from England."
    hide screen perfume
    call screen bag_03

label sc01_ticket:
    show screen ticket
    stop music fadeout 1.0
    "There's nothing else here besides a train ticket and some coins."
    "This is all useless! This can't be everything..."
    hide screen ticket
    scene sc_apt_night
    with Dissolve(0.2)
    play music ten volume 0.7
    $ quick_menu = True
    show arthur angry at ctr
    with Dissolve(0.1)
    "{i}I just need to keep looking! There has to be an ID somewhere.{/i}"
    play sound s05 volume 0.8
    "Policeman" "Get ready to arrest the suspect! Beware of any weapons!"
    la "Quick, he's in here!"
    $ quick_menu = False
    "{i}I can't stay here, my life will be over.{/i}"
    show arthur
    "{i}... I can only think of one thing.{/i}"
    "{i}I swore to never do this again, but I have no choice here.{/i}"
    stop music fadeout 0.3
    a angry "Come on, focus.... it's now or never!"
    play sound s06
    hide arthur
    scene white
    with flash
    $ renpy.pause (3, hard=True)

    return
