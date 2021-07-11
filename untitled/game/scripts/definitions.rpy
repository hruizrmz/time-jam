## Characters ##############################################################
#define mc = Character("MC", image = "mc/default.png")
define n = Character(None, kind=nvl)
define narrator = Character(None, what_italic=True, who_color="DFDFDF")

define a = Character("Arthur", who_color="#ff3333", image="arthur")
define b = Character("Benjamin", who_color="#004C99", image ="ben")
define c = Character("Catherine", who_color="#CCFFFF", image="cat")

define bm = Character("Barman")
define dm = Character("Drunkard")
define dj = Character("John McKellen", who_color="#009900")
define la = Character("Landlady")
#####################################################################

## Character Sprites #######################################################
#image sprite = "charas/sprite.png"

image arthur = "charas/arthur/a1.png"
image arthur happy = "charas/arthur/a2.png"
image arthur angry = "charas/arthur/a3.png"
image arthur sad = "charas/arthur/a4.png"
image arthur conf = "charas/arthur/a5.png"

image ben = "charas/ben/b1.png"
image ben happy = "charas/ben/b2.png"
image ben angry = "charas/ben/b3.png"
image ben sad = "charas/ben/b4.png"
image ben conf = "charas/ben/b5.png"

image cat = "charas/cat/c1.png"
image cat happy = "charas/cat/c2.png"
image cat angry = "charas/cat/c3.png"
image cat sad = "charas/cat/c4.png"
image cat conf = "charas/cat/c5.png"
#####################################################################

## BGM #####################################################################
define audio.calm = "<loop 0>audio/bgm/calm.wav"
define audio.inv = "<loop 0>audio/bgm/inv.wav"
define audio.pan = "<loop 2 to 79>audio/bgm/pan.wav"
define audio.ten = "<loop 0>audio/bgm/ten.wav"
define audio.nost = "<loop 0>audio/bgm/nost.wav"
define audio.som = "<from 2 loop 0>audio/bgm/som.mp3"
#####################################################################

## SFX #####################################################################
define audio.s01 = "audio/sfx/01.mp3"
define audio.s02 = "audio/sfx/02.mp3"
define audio.s03 = "audio/sfx/03.mp3"
define audio.s04 = "audio/sfx/04.mp3"
define audio.s05 = "<from 0 to 2>audio/sfx/05.mp3"
define audio.s06 = "<from 0 to 2>audio/sfx/06.mp3"
define audio.s07 = "audio/sfx/07.mp3"
define audio.s08 = "<from 0 to 5>audio/sfx/08.mp3"
#####################################################################

## Transforms #############################################################
transform halfleft:
    xalign 0.25 yalign 0.25

transform halfright:
    xalign 0.75 yalign 0.25

transform ctr:
    zoom 0.6
    xalign 0.5 yalign 0.1

transform custom_zoom:
    zoom 0.3

transform close_up:
    zoom 1.7
#####################################################################
