## LUNCHTIME
label sc04_main:
    scene sc_cafe
    with Dissolve(2)

    show ben at halfright
    show arthur at halfleft
    with Dissolve(0.4)
    b sad "I saw you drinking through the window, Arthur. I apologize for taking so long."
    a conf "No worries. I just hope you don't mind I decided to order without you."
    b "No, that's fine by me."
    b -sad "Excuse me, waiter? I'll have what he's having. Thank you."
    a -conf "... Well then, did you find out anything?"

    return
