## Interactive Scenes & Objects

screen bag_01:
    imagebutton:
        xpos 0
        ypos 0
        idle "items/bagID.png"
        hover "items/bagHOV.png"
        action [Hide("bag_01"), Jump("sc01_toy")]

screen toy:
    frame:
        xpos 140
        ypos 85
        add "items/01.png"

screen bag_02:
    imagebutton:
        xpos 0
        ypos 0
        idle "items/bagID.png"
        hover "items/bagHOV.png"
        action [Hide("bag_02"), Jump("sc01_perfume")]

screen perfume:
    frame:
        xpos 140
        ypos 85
        add "items/02.png"

screen bag_03:
    imagebutton:
        xpos 0
        ypos 0
        idle "items/bagID.png"
        hover "items/bagHOV.png"
        action [Hide("bag_03"), Jump("sc01_ticket")]

screen ticket:
    frame:
        xpos 140
        ypos 85
        add "items/03.png"
