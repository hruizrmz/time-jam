# The game starts here.
init:
    $ flash = Fade(.25, 0, .75, color="#fff")

    image white = "#fff"

label start:

    $ config.rollback_enabled = False

    call sc01_main from _call_sc01_main

    call sc02_main from _call_sc02_main

    # This ends the game.
    return
