## INVESTIGATION 2 - ARTHUR
label sc05a_main:
    play sound train fadein 0.5 volume 0.1
    $ renpy.pause (1.5, hard=True)
    n "After storming out the Black Royal Cat Hotel, Arthur got on the closest train."
    n "He decided to sleep for a while as he traveled across the city to the carnival."
    n "\nAs he fell into deep slumber, Arthur dreamt about his previous flashback with more clarity."
    window hide
    nvl clear

    stop sound fadeout 0.6
    play music nostb fadein 1.5 volume 1.0
    scene white
    with flash
    play sound s13 volume 0.6
    show cat mem at ctr
    with Dissolve(0.8)
    $ renpy.pause (1.5, hard=True)
    n "It was a memory of the last night with his beloved before the war began."
    n "\nHe remembered how he failed to win Catherine the big teddy bear with the blue ribbon."
    n "Instead, his prize at the shooting gallery was just a small stuffed lion."
    n "\nCatherine, however, did not seem to care much about what type of gift she received."
    n "She moved to Arthur's side, and hugged him lovingly as she whispered into his ear."
    window hide
    nvl clear
    cn "Being by your side is the best reward I could ever get."
    cn "I... love{nw}"
    stop music
    scene black
    play sound s14
    $ renpy.pause (0.8, hard=True)
    n "The loud tremors of the station interrupted Arthur's serene rest."
    n "The commotion of children and adults, were enough to wake Arthur up and catch him disoriented."
    n "\nHe started to look around as he got off the train, seemingly lost as to what year this currently was..."
    window hide
    nvl clear

    play sound carnival fadein 0.5 volume 0.1
    play music inve fadein 1.5 volume 0.8
    scene sc_carnival
    with Dissolve(2)
    $ renpy.pause (0.5, hard=False)
    $ quick_menu = True
    show arthur at ctr
    with Dissolve(0.1)
    a "Well... Here I am. Now what?"
    n "Arthur began to meander through the carnival. There was something for everyone here."
    n "Food stalls, a High Striker, balloon darts, and other games of chance..."
    n "Those last ones reminded him of a time in his past that he wished to forget."
    n "\nHis actions back then almost cost him his mental health."
    nvl clear
    n "He grabbed a nearby chair and slowly moved it towards the dealer."
    n "However, Arthur stopped in his tracks when he saw the shooting range."
    n "\nIt looked very much like the very same one that had been there years ago."
    n "He left the cards table behind and made his way to shoot some targets."
    window hide
    nvl clear

    "Clerk" "Good afternoon, gentleman! Would you like to try your luck at winning a prize?"
    "Clerk" "You seem like someone with a good eye for aiming."
    

    return