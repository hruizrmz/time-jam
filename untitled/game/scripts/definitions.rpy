## Backgrounds #############################################################
image bg room = "bgs/bg room.png"
############################################################################

## Characters ##############################################################
#define mc = Character("MC", image = "mc/default.png")
define mc = Character("MC")
#####################################################################

## Character Sprites #######################################################
image sprite = "charas/sprite happy.png"

image mc happy = "charas/komaeda/happy.png"
image mc sad = "charas/komaeda/sad.png"
image mc scared = "charas/komaeda/scared.png"
#####################################################################

## BGM #####################################################################
define audio.test = "<from 5 loop 0>audio/bgm/test.mp3"
#####################################################################

## SFX #####################################################################

#####################################################################

## Screens #################################################################
screen omg:
    frame:
        xpos 20
        ypos 20
        text "omg is that a sprite":
            size 40

screen sprite:
    imagebutton:
        xpos 150
        ypos 150
        idle "charas/sprite.png"
        at custom_zoom
        # hover "a different picture"
        action [ Hide("omg"), Jump("sc02_sprite") ]

#####################################################################

## Transforms #############################################################
transform halfleft:
    xalign 0.25 yalign 0.25

transform halfright:
    xalign 0.75 yalign 0.25

transform ctr:
    xalign 0.5 yalign 0.25

transform custom_zoom:
    zoom 0.3

transform close_up:
    zoom 1.7
#####################################################################
