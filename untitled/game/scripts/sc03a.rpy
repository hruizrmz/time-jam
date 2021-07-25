##INVESTIGATION 1 - ARTHUR
label sc03a_main:
    play music inve fadein 1.5 volume 0.8
    scene sc_toys # later to be street scene
    with Dissolve(2)
    n "After hanging up the phone, Arthur headed downtown, where one could find all kinds of shops."
    n "A couple hours went by as he searched 5 different toystores. No one seemed to have heard of the brand 'Doorbell Toys'. It was as if it didn't even exist."
    n "\nAs he went into yet another store, someone approached him from the back."
    window hide
    nvl clear
    $ renpy.pause (0.5, hard=False)
    $ quick_menu = True
    "???" "Excuse me, are you the one that's been going around asking about a lion plush?"
    show arthur at ctr
    a "That's correct. Would you happen to know anything about 'Doorbell Toys'?"
    "???" "Of course I do, sonny! It was quite a popular brand before the war."
    "???" "Unfortunately, that moment of fame was brief. People had to prioritize survival over toys."
    "???" "With no more clients, they eventually went bankrupt and stopped producing toys since then."
    a sad "I see... The war was hard on all of us."
    a "I can't imagine a child having to worry about living another day instead of just... being a kid."
    "???" "Times change. I can only hope that today's youth will never have to experience that."
    a "Hopefully..."
    a -sad "If you'd allow me to bring back the lion toy, do you know anyone that might still sell it?"
    "???" "I happen to know just the man. Please, follow me through here."
    $ quick_menu = False
    $ renpy.pause (0.5, hard=True)

    # play sound PPL WALKING volume 0.7
    hide arthur
    scene black
    with Dissolve(1)
    $ renpy.pause (0.5, hard=True)
    window show
    n """
    Both of them walked into an alley, where a green wooden door with a crystal window awaited them.

    There was a sign that read 'We Are Open!'. So, they went in as a small bell announced their entrance.

    The entire place was decked with toys from tin cars and soldiers, to puppets hanging from the ceiling.

    Near the entrance, there was a long glass case filled with toys that looked even more antique.
    """
    window hide
    nvl clear
    play sound s06 volume 0.6
    scene sc_toys
    with Dissolve(2)
    $ quick_menu = True
    tmn "Good evening, gentlemen."
    "???" "How's it going, John?"
    tm "It's a bit slow, Charles... Just about the usual."
    "Charles" "Well, this will surely brighten up your day. This kid is interested in your relics! He is, um..."
    show arthur at ctr
    a "Arthur... Arthur Walker, sir."
    tm "Very well, Mr. Walker. How may I help you today?"
    a "I'm looking for a lion plush from the brand 'Doorbell Toys'. I was hoping you could show me one."
    tm "Hmm, that's definitely a rare one."
    tm "Let me go see if there's anything on the back..."
    ". . ."
    tm "I must apologize, Mr. Walker. I recently sold the last model to a pretty lady; three hours ago as a matter of fact."
    tm "She seemed quite keen on it too. She shared that she would repay a friend for gifting it to her at a fair once."
    a happy "A fair, eh? It's been so long since I've been to one."
    a "Not since..."
    $ quick_menu = False
    stop music fadeout 1.5
    hide arthur
    play sound s09 volume 0.8
    scene white
    with flash
    $ renpy.pause (2, hard=True)
    play music nostb fadein 1.5 volume 1.0
    "{i}...What is this feeling?{/i}"
    call screen mem_01 with Dissolve(1)

label sc03a_mem:
    show cat mem at ctr
    with flash
    # play sound CAT LAUGHING volume 0.8
    $ renpy.pause (1.5, hard=True)
    window show
    n """
    A flashing memory of a day at the fair with a girl came back to Arthur after the Toymaker's remark.

    He recalled a promise involving a big teddy bear wearing a blue ribbon; but with whom?

    The promise was never fulfilled, as Arthur recalls winning something else instead.
    """
    window hide
    nvl clear
    cn "Arthur! This little guy is adorable, hehe~"
    cn "Thank you, truly."
    cn ". . ."
    cn "I... love you."
    stop music
    scene sc_toys
    with flash
    $ renpy.pause (1.5, hard=True)

    show arthur conf at ctr
    $ quick_menu = True
    "{i}The fair...{/i}"
    play music inve fadein 1.5 volume 0.8
    a happy "That's it!"
    a -happy "I'd like to stay and chat but I have to go, immediately."
    "Charles" "Must you leave so soon?"
    a "Yes, I'm afraid I can't explain why. Although it was nice meeting you two."
    tm "In that case, I hope you find what you are looking for, Mr. Walker."
    a "So do I, John... Thanks again."
    $ quick_menu = False
    hide arthur
    scene black
    with fade
    $ renpy.pause (4, hard=True)

    return