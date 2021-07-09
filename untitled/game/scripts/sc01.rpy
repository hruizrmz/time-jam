## INTRO SCENE
label sc01_main:
    $ quick_menu = False
    scene black
    with fade
    $ renpy.pause (1, hard=True)

    show scene1_alley
    with Dissolve(2)
    play music calm
    window show
    n """
    The Moon Bar's a nice small place, adorned by a yellow light

    A shelf at the back displays bottles of all sizes

    And there's a noticeable lack of cleaning...

    But the cozy and calm ambience make up for it
    """
    window hide
    nvl clear

    # dialogue starts
    $ quick_menu = True
    a "I'm sorry, what did you say?"
    bm "The time, sir... It's past 2 a.m. You've been asleep for a while."
    bm "We are about to close for the evening so I humbly ask for you to leave."
    a "Of course..."
    a "Here, have this. I apologize for the inconvenience."
    bm "Oh, it's alright, sir."
    a "I insist."
    bm "Well, thank you very much! Should I help you to the exit?"
    a "That won't be necessary. I can manage on my own."
    "I say that and yet I almost fell on my ass as I stood up..."

    # scene transition here, fuera del bar
    window show
    n """
    Arthur lit up a cigar and observed the dark sky for a moment

    The night was illuminated by stars and flickering street lamps

    Perfect for walking a couple blocks and showing the way back home
    """
    window hide
    nvl clear
    stop music fadeout 1.0
    scene black
    with fade
    # secuencia/animacion aqui?

    # scene transition, negro o fuera del apartamento
    a "Damn it... I hate being on the third floor."
    a "The rent is not worth tripping on all these stairs"
    $ renpy.pause (0.5, hard=False)
    # sfx de llave abriendo un candado
    # sfx de puerta rechinando
    # scene transition, apartamento oscuro
    a "Huh, it's quiet in here... What happened to that annoying leak?"
    a "The chairs are out of place too. Was I already drunk before getting to the bar?"
    $ quick_menu = False
    # show clickable lamp to turn on the lights
    # immediate scene change to apt with body
    $ quick_menu = True
    a ". . ."
    # show scared arthur sprite, sfx of loud thud
    $ quick_menu = False
    play music som
    window show
    n """
    As Arthur fell to the ground, he lost his composure

    A scream that carried both fright and pain rang through the hallway

    This was reality; he had found a corpse inside his apartment
    """
    window hide
    nvl clear
    $ renpy.pause (0.5, hard=False)
    $ quick_menu = True
    a "God..."
    "I can hardly breathe. This is just insane."
    "... Get it together. I should take a closer look."

    $ quick_menu = False
    # close up of body
    # show clickable bag
    # transition bag image to opened
    # show clickable plush
    $ quick_menu = True
    # plush: 'The tag says "Doorbell Toys".'
    a "... Who is this person?"
    $ renpy.pause (0.5, hard=True)
    "Neighbor" "What do you think you're doing!? You're going to wake up the whole damn building..!"
    "Neighbor" "Don't even get me started on the ti-- Oh, Christ!"
    "Shit, she noticed the body. I probably shouldn't be holding this bloody purse either."
    "What's she running to the window for..?"
    "Neighbor" "Help! Police! There's been a murder!"
    # sfx whistle
    "Policeman" "Quick, go call for some backup!"
    a "Ah..."
    "I can't really blame her. I'm scared to death myself."
    "Quick, focus! Are there any other clues?"
    # show clickable perfume
    # perfume: the odd shape and smell match its extravagant name, "Arbre Bleu"

    "This is all useless! There has to be some sort of identification here."
    # sfx de policias acercandose

    return
