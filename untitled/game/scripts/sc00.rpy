# Test scene
define s = Character("Sprite")
define mc = Character("MC", image = "komaeda/mc.png")

label sc00_main:
    # for backgrounds
    $ quick_menu = False
    scene black
    with fade
    $ renpy.pause (2, hard=True)

    scene bg_room
    with fade
    play music test
    $ renpy.pause (1, hard=True)

    # for character sprites
    $ quick_menu = True
    show s at halfleft
    with moveinleft
    s "You've created a new Ren'Py game!"
    show mc happy at halfright
    with moveinright
    mc happy "Sure seems like it."
    s "Once you add a story, pictures, and music, you can release it to the world."
    s "cya"
    hide sprite
    with moveoutleft

    show mc sad at ctr
    with move
    mc "But wait..."
    show mc scared
    mc "Why am I in space!?"
    show mc with dissolve
    mc "...I need to explore. Where should I go?"
    menu:
        "Go to the right.":
            jump right
        "Go to the left.":
            jump left

label right:
    show mc happy with dissolve
    mc "Hey, I think I see another person in the distance!"
    "{b}HAPPY END{/b}"
    return

label left:
    show mc scared with dissolve
    "The MC fell into a crater and died."
    "{b}BAD END{/b}"
    return
