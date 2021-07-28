# The game starts here.
init -2:
    # ---------- CTC blinking arrow -------------------
    image ctc_blink:
        xpos 1.5 # Across from right
        ypos 1.0 # Up from bottom
        xanchor 1.0  # On Right
        yanchor 1.0   # On Bottom
        alpha 1.0 # visible
        "gui/ctc.png"
        0.4
        alpha 0.0 # invisible
        0.3
        repeat

    $ flash = Fade(.25, 0, .75, color="#fff")

    image white = "#fff"

    # $ config.rollback_enabled = False


label start:
    # add a choice to skip the prologue aka sc01 + sc02

    #call sc01_main from _call_sc01_main

    #call sc02_main from _call_sc02_main

    #call sc03a_main from _call_sc03a_main

    call sc03b_main from _call_sc03b_main

    #call sc04_main from _call_sc04_main

    # This ends the game.
    return
