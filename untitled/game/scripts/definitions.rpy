## Characters ##############################################################
define n = Character(None, kind=nvl, who_color="F9F9F9", ctc="ctc_blink")
define narrator = Character(None, what_italic=True, who_color="C0C0C0", ctc="ctc_blink")

define a = Character("Arthur", who_color="#D82626", image="arthur", ctc="ctc_blink")
define b = Character("Benjamin", who_color="#1375D7", image ="ben", ctc="ctc_blink")
define c = Character("Catherine", who_color="#16C3C3", image="cat", ctc="ctc_blink")
define cn = Character("???", who_color="#16C3C3", ctc="ctc_blink")

define bm = Character("Barman", who_color="#E1C615", ctc="ctc_blink") #choose a diff color
define dm = Character("Drunkard", ctc="ctc_blink")
define dj = Character("John McKellen", who_color="#109010", ctc="ctc_blink")
define la = Character("Landlady", ctc="ctc_blink")
define tmn = Character("???", who_color="#78CD2F", ctc="ctc_blink")
define tm = Character("John the Toymaker", who_color="#78CD2F", ctc="ctc_blink")
define cl = Character("Claire the Manager", who_color="#800E47", ctc="ctc_blink")
#####################################################################

## Character Sprites #######################################################
image arthur = ConditionSwitch(
            "_last_say_who == 'a'", "charas/arthur/a1.png",
            "not _last_say_who == 'a'", im.MatrixColor("charas/arthur/a1.png", im.matrix.brightness(-0.08)))
image arthur happy = ConditionSwitch(
            "_last_say_who == 'a'", "charas/arthur/a2.png",
            "not _last_say_who == 'a'", im.MatrixColor("charas/arthur/a2.png", im.matrix.brightness(-0.08)))
image arthur angry = ConditionSwitch(
            "_last_say_who == 'a'", "charas/arthur/a3.png",
            "not _last_say_who == 'a'", im.MatrixColor("charas/arthur/a3.png", im.matrix.brightness(-0.08)))
image arthur sad = ConditionSwitch(
            "_last_say_who == 'a'", "charas/arthur/a4.png",
            "not _last_say_who == 'a'", im.MatrixColor("charas/arthur/a4.png", im.matrix.brightness(-0.08)))
image arthur conf = ConditionSwitch(
            "_last_say_who == 'a'", "charas/arthur/a5.png",
            "not _last_say_who == 'a'", im.MatrixColor("charas/arthur/a5.png", im.matrix.brightness(-0.08)))
image arthur mem = ConditionSwitch(
            "_last_say_who == 'a'", "charas/arthur/a6.png",
            "not _last_say_who == 'a'", im.MatrixColor("charas/arthur/a6.png", im.matrix.brightness(-0.08)))
#image arthur = "charas/arthur/a1.png"

image ben = ConditionSwitch(
            "_last_say_who == 'b'", "charas/ben/b1.png",
            "not _last_say_who == 'b'", im.MatrixColor("charas/ben/b1.png", im.matrix.brightness(-0.23)))
image ben happy = ConditionSwitch(
            "_last_say_who == 'b'", "charas/ben/b2.png",
            "not _last_say_who == 'b'", im.MatrixColor("charas/ben/b2.png", im.matrix.brightness(-0.23)))
image ben angry = ConditionSwitch(
            "_last_say_who == 'b'", "charas/ben/b3.png",
            "not _last_say_who == 'b'", im.MatrixColor("charas/ben/b3.png", im.matrix.brightness(-0.23)))
image ben sad = ConditionSwitch(
            "_last_say_who == 'b'", "charas/ben/b4.png",
            "not _last_say_who == 'b'", im.MatrixColor("charas/ben/b4.png", im.matrix.brightness(-0.23)))
image ben conf = ConditionSwitch(
            "_last_say_who == 'b'", "charas/ben/b5.png",
            "not _last_say_who == 'b'", im.MatrixColor("charas/ben/b5.png", im.matrix.brightness(-0.23)))
#image ben = "charas/ben/b1.png"

image cat = "charas/cat/c1.png"
image cat happy = "charas/cat/c2.png"
image cat angry = "charas/cat/c3.png"
image cat sad = "charas/cat/c4.png"
image cat conf = "charas/cat/c5.png"
image cat mem = "charas/cat/c6.png"

image barman = ConditionSwitch(
            "_last_say_who == 'bm'", "charas/bm.png",
            "not _last_say_who == 'bm'", im.MatrixColor("charas/bm.png", im.matrix.brightness(-0.23)))
image toymaker = ConditionSwitch(
            "_last_say_who == 'tm'", "charas/tm.png",
            "not _last_say_who == 'tm'", im.MatrixColor("charas/tm.png", im.matrix.brightness(-0.23)))
image claire = ConditionSwitch(
            "_last_say_who == 'cl'", "charas/cl.png",
            "not _last_say_who == 'cl'", im.MatrixColor("charas/cl.png", im.matrix.brightness(-0.23)))
#####################################################################

## BGM #####################################################################
define audio.calm = "<loop 0>audio/bgm/calm.wav"
define audio.inv = "<loop 0>audio/bgm/inv.wav"
define audio.pan = "<loop 2 to 79>audio/bgm/pan.wav"
define audio.ten = "<loop 0>audio/bgm/ten.wav"
define audio.nosta = "<loop 0>audio/bgm/nost_a.mp3"
define audio.nostb = "<loop 0>audio/bgm/nost_b.wav"
define audio.som = "<from 2 loop 0>audio/bgm/som.mp3"
#####################################################################

## SFX #####################################################################
define audio.s01 = "audio/sfx/01.mp3"
define audio.s02 = "audio/sfx/02.mp3"
define audio.s03 = "audio/sfx/03.mp3"
define audio.s04 = "audio/sfx/04.mp3"
define audio.s05 = "<from 0 to 2>audio/sfx/05.mp3"
define audio.s06 = "audio/sfx/06.mp3"

define audio.s07 = "<from 0 to 3>audio/sfx/07.mp3"
define audio.s08 = "<from 0 to 3>audio/sfx/08.mp3"
define audio.s09 = "audio/sfx/09.mp3"
define audio.s10 = "audio/sfx/10.mp3"
define audio.s11 = "<from 2>audio/sfx/11.mp3"
define audio.s12 = "audio/sfx/12.mp3"
define audio.s13 = "<from 0 to 2>audio/sfx/13.mp3"
define audio.s14 = "audio/sfx/14.mp3"
define audio.s15 = "audio/sfx/15.mp3"
define audio.s16 = "audio/sfx/16.mp3"
define audio.s17 = "audio/sfx/17.mp3"
define audio.s18 = "audio/sfx/18.mp3"

define audio.rest = "<loop 0>audio/sfx/rest.mp3"
define audio.train = "<loop 0>audio/sfx/train.mp3"
define audio.carnival = "<loop 0>audio/sfx/carnival.mp3"
#####################################################################

## Transforms #############################################################
#transform focus:
#    yoffset 20
#    easein 0.20 zoom 1.050

#transform unfocus:
#    yoffset 20
#    easeout 0.20 zoom 1.0

transform halfleft:
    zoom 0.35
    xalign -0.2 yalign 0.1

transform halfright:
    zoom 0.35
    xalign 1.2 yalign 0.1

transform rightNPC:
    zoom 0.35
    xalign 0.95 yalign -0.08

transform leftNPC:
    zoom 0.35
    xalign 0.15 yalign -0.08

transform ctr:
    zoom 0.4
    xalign 0.5 yalign 0.1

transform custom_zoom:
    zoom 0.4

transform close_up:
    zoom 1.7
#####################################################################
