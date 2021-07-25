# The game starts here.
init:
    $ flash = Fade(.25, 0, .75, color="#fff")

    image white = "#fff"

label start:

    $ config.rollback_enabled = False

    # add a choice to skip the prologue aka sc01 + sc02

    call sc01_main from _call_sc01_main

    call sc02_main from _call_sc02_main

    call sc03a_main from _call_sc03a_main

    # This ends the game.
    return
