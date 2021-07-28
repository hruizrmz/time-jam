##INVESTIGATION 1 - BENJI
label sc03b_main:
    scene sc_alley # later to be street scene
    with Dissolve(2)
    n "After signing some papers and doing a few calls, Benjamin set out to investigate with cane and coat in hand."
    n "He caught a taxi passing by his apartment just in time; he already knew the exact location to investigate."
    n "It had been about a year since his visit to one of England's best perfume stores, along with his now fiancée."
    nvl clear
    n "He was unable to enter the store with her due to an important client, who needed his assistance with a fraud allegation at the time."
    n "\nPart of being one of the best lawyers in town meant that he would have less time to spend with his beloved."
    n "No amount of money will ever buy time."
    n "Nevertheless, Benjamin remembered without a doubt the location of this store. After twenty minutes, he had arrived."
    #################
    # PERFUMERIAS EN INGLES???
    #################
    window hide
    nvl clear
    stop music fadeout 1.0
    $ renpy.pause (0.5, hard=False)
    $ quick_menu = True
    show ben at ctr
    b happy "Here, you can keep the change. Thank you for the ride."
    "Taxi driver" "Wow..! By all means, thank you, sir!"
    "Taxi driver" "Should I help you out of the car?"
    b "There's no need. That's what the cane is for. Enjoy the rest of your day."
    "Taxi driver" "Understood. You too, sir."
    play music inve fadein 1.0 volume 0.8
    # car driving away
    b conf "This place really is as big as I remembered, even from the outside."
    b -conf "I can already smell the perfumes too..."
    "{i}I wonder if the employees remember what fresh air is anymore.{/i}"
    "Greeter" "Welcome to 'Venus', sir. Let me open up the door for you."
    b conf "Oh, yes, thank you very much."
    "{i}Good thing I kept that to myself...{/i}"

    show sc_perfume
    with fade
    cl "Good day, gentleman. Welcome to Venus, where we awaken your senses!"
    show ben angry at ctr
    b angry "{i}Yes, I am aware of that already...{/i}"
    cl "Pardon?"
    b conf "Nothing! Just saying that my name is Benjamin Walker."
    b -conf "I was interested in learning about the 'Arbre Bleu' fragrance. I believe it is French."
    cl "Ah, yes, I definitely know the one you're referring to. "
    cl "I must let you know, however, that it is very hard to acquire. They are not affordable by just anybody."
    b "I see. With that said, do you have any information on anyone that might have bought it this week?"
    cl "Sir, here in 'Venus' we have a strict confidentiality protocole so I'm afraid I can't disclose-"
    b sad "Yes, of course, I completely understand that ma'am."
    "{i}But can she resist this free cash I'm handing over to her?{/i}"
    cl "...!"
    cl "Although... We could make an exception to a fair gentleman such as yourself."
    cl "I'll go get our sales history for you right away."
    b conf ". . ."
    cl "We keep track of everything in this book. As you can see, this is divided by month and week."
    cl "And... here. This is the current date. As you can see, there are no recent 'Arbre Bleu' purchases."
    b -conf "Hmm, would you mind if I took a closer look to confirm this?"
    cl "By all means, it's all yours."
    "{i}Alright, this week is definitely empty. Seems like the most recent sale was as far as four weeks ago.{/i}"
    "{i}... Interesting{/i}"
    b "Excuse me, the name 'John McKellen' shows up a lot in here."
    b "Not only is he the most recent buyer, but he's bought the same product every month for the past two years."
    b happy "Could you tell me more about him?"
    cl "Ah... He's certainly one of our most frequent clients."
    ### GABARDINA EN INGLES??
    cl "He's a middle-aged man that is always wearing a blue golf cap."
    cl "Lately it's more of a dark green if you ask me... With all the dirty rubbish it's been drenched in."
    b conf "I can only imagine..."
    b -conf "Would you happen to have a way of contacting him?"
    cl "I do apologize, Mr. Walker, but I have a terrible memory... People always point out my forgetfulness."
    b angry  "Ha ha... you don't say?"
    b -angry "Here, I can only hope this paper helps you remember."
    cl "Ah... You're certainly my favorite client now!"
    cl "I unfortunately have no direct way for yourself to reach him. However..."
    cl "That bloody hat always reeks of alcohol. Given his messy appearance as of late, I'd say you can find him at a bar."
    cl "Thinking about it, there was a flyer stuffed in his pockets last time from 'The Golden Hat'."
    b conf "'Golden drinks at the price of copper', eh? I am familiar with the place."
    b -conf "My brother and many others downtown frequent it due to its low prices."
    "{i}Talking about Arthur, I have not checked the time yet...{/i}"
    "{i}Huh..! I might actually be the one running late for once!{/i}"
    b angry "Damn, I won't have enough time to check out the bar before meeting up."
    cl "Sir, are you leaving already? It would make me very happy if you were to visit 'Venus' again sometime."
    b "I'm afraid I can't promise that, ma'am."
    ## MEMOROA DE PEZ EN INGLES?
    b happy "But worry not, with your memory you will soon forget me. Enjoy the rest of your day!"
    cl "Wha-! Hmph."
    hide arthur
    $ quick_menu = False

    scene sc_alley # later to be street scene
    with Dissolve(2)
    n "On the way out, Benjamin tipped the greeter and reminded him to never stop aspiring for better things."
    n "The young lawyer had always kept this mantra close to his heart, and had taken him thus far."
    n "With no time to lose, he hurried on over to the hotel where he would discuss the situation with Arthur."
    window hide
    nvl clear
    scene black
    with Dissolve(2)
    $ renpy.pause (4, hard=True)

    return
