## LUNCHTIME
label sc04_main:
    play sound rest fadein 0.5 volume 0.1
    play music calm fadein 1.5 volume 0.8
    scene sc_cafe
    with Dissolve(2)
    $ renpy.pause (1, hard=True)

    show ben at halfright
    show arthur at halfleft
    with Dissolve(0.4)
    $ quick_menu = True
    b sad "I saw you drinking through the window, Arthur. I apologize for taking so long."
    a conf "No worries. I just hope you don't mind I decided to order without you."
    b "No, that's fine by me."
    b -sad "Excuse me, waiter? I'll have what he's having. Thank you."
    a -conf "... Well then, did you find out anything?"
    b "Nothing of much relevance yet."
    b "I was able to look through the boutique's records and found a possible lead for the perfume."
    b angry "...Unfortuntely, they won't be easy to deal with."
    b -angry "Surely you had more luck than I did?"
    a sad "Not exactly... The toy is from before the war, so the company doesn't exist anymore."
    a -sad "A man that collected toys had just sold the last one to a woman shortly before my arrival..."
    b sad "You don't suppose it was that same woman..?"
    a angry "Who else could it be? I was just too late..."
    b -conf "Why not travel back again, to before she's able to buy it?"
    a conf "It's not that simple, Ben."
    a "I can't risk losing my memory now. The line between the past and present would become a blur."
    a "This... This is the only shot I've got."
    a -conf  "You just wouldn't understand, even if you wanted to..."
    stop music fadeout 0.5
    b angry "Seriously?"
    b "I apologize for not being knowledgeable on the complex metaphysics of your body."
    play music som fadein 1.5 volume 0.8
    b "Even more so for not knowing the abilities of an opportunist bloke such as yourself."
    a angry "What are you on about? You can't imagine what I've been through!"
    a happy "While I risked my life during the war, all you had to worry about were your 'studies of grandeur'."
    b "You know very well this blasted leg of mine forced me to stay. Did you {i}forget{/i} who did this to me?"
    a -happy "Christ, it was just an accident! We were nothing but children playing around-"
    b angry "'Playing around'?!"
    b -sad "Arthur... You must be joking. What you did was driven by rage."
    b "Your explosive emotions have always gotten the best of you. Especially after that curse was given to you."
    b "The weight of such a thing, on top of losing all those bets you were so sure of winning... They broke you."
    b sad "My leg isn't what hurts me the most. It doesn't come close to the pain of losing my brother."
    b "Your body may have returned from the war, but a part of your soul died in it."
    a "... I see, now. Why didn't I think of it before?"
    a angry "The woman I entrusted you with back then... She seems to have turned you into an emotional man."
    a "What with all the company you two kept each other, it makes perfect sense."
    b angry "... I should let you rot in prison."
    b -angry "Do you know why I'm helping you? Because you used to be the one to protect me from the horrors of the world."
    b "Whether it was inside or outside the household, you were there for me..."
    b "So, I am only doing this to repay my debt from our younger days."
    b angry "There is no affection left in me for you."
    a -angry "Your speech doesn't fool me. "
    a "This heroic act of yours is driven by the guilt of robbing me the only thing that I cared about."
    a "Being the pride of the family wasn't enough for you; being the most intelligent or gentle out of the two."
    a happy "You had to take the love of my life right from my hands..."
    b -angry ". . ."
    b "I wish you would let me explain. You've always refused to listen to me or her."
    a angry "There's no need to explain, I already understood you two take me for a fool."
    a -angry "I'm leaving now. Unlike you, I have an innocent woman to save and I'm running out of time to find her."
    a "Meet me in my apartment by 6 p.m. if you still want to help me stop a murder..."
    hide arthur
    with Dissolve(0.4)
    b sad "... I think I'm getting a migraine after this."
    "Waiter" "Excuse me... Here's your drink, sir."
    b -sad "Just in time. Thank you."
    "{i}Never in my life have I had such a long and bitter glass of whisky...{/i}"
    $ quick_menu = False
    stop sound fadeout 1.0
    stop music fadeout 1.0
    hide ben

    scene white
    with fade
    $ renpy.pause (1, hard=True)
    n """
    Hello once again. Thank you for playing the next part of MURDRUM!

    Things are heating up between the Walker brothers. How will this affect the investigation?

    Next update will include the reveal and the final part. Please keep an eye out for it! :)
    """
    window hide
    nvl clear
    with fade
    $ renpy.pause (2, hard=True)

    return
