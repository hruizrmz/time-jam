# Introductory scene

label sc01_main:
    # for backgrounds
    scene bg room
    with dissolve
    play music test

    # for character sprites
    show sprite at halfleft
    with moveinleft
    s "You've created a new Ren'Py game!"
    show mc happy at halfright
    with moveinright
    mc happy "Sure seems like it."

    return
