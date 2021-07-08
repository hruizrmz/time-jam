# Testing point & click
label sc02_main:
    scene black
    show mc sad at ctr, close_up
    mc "Man, I sure am thirsty!"
    show screen omg
    call screen sprite

label sc02_sprite:
    show mc
    mc "Ayo, what's a Sprite doing here?"
    show mc happy at close_up
    mc "Today must be my lucky day!"

    "END OF TEST"
    return
