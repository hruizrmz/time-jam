## INVESTIGATION 2 - ARTHUR
label sc05a_main:
    play music inve fadein 1.5 volume 0.8
    scene sc_alley # later to be street scene
    with Dissolve(2)
    n ""
    window hide
    nvl clear
    $ renpy.pause (0.5, hard=False)
    $ quick_menu = True

    return
