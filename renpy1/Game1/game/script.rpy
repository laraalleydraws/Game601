# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Ole Reggie")
define g = Character("Tish")
define l = Character("Me")

# The game starts here.

label start:


    image home = "IMG_1449.png"
    image shopping = "IMG_1450.png"
    image art = "Untitled_Artwork 14 copy 2.png"
    image golf = "Untitled_Artwork 16.png"
    image double = "Untitled_Artwork 15.png"
    image car = "Untitled_Artwork 15 copy.png"
    image intro = "Untitled_Artwork 16 copy.png"
    image hotdog = "Untitled_Artwork 17.png"

    scene intro
    scene home

    image Ole Reggie = "IMG_1446.PNG"
    image Tish = "IMG_1441.PNG"
    image mad reg = "Untitled_Artwork 14.png"
    image mad tish = "Untitled_Artwork 14 copy.png"
    image dumb reg = "Untitled_Artwork 14 copy 3.png"

    show Ole Reggie

    # These display lines of dialogue.

    m "Hello. I'm Reginald Windbaugh III. Welcome to my city. New York City."
    m "I'm not gonna lie being rich is pretty freakin sweet."
    menu:
        "Wow. Okay.":
            jump wowdude
        "Word.":
            jump wordup
    label wowdude:
        m "haha, I know what you're thinking...How can I be rich like this guy? hmm?"
    label wordup:
        m "Anyway shall we get on with the tour?"
    scene shopping
    m "OOF what on earth is all of this..."
    menu:
        "Shopping bags?":
            jump shopbags
    label shopbags:
        m "Tish!!"

    show Tish at left
    g "Well hello I'm Tish!"
    hide Tish at left
    show mad reg at right
    m "What is the meaning of this... Haven't you shopped enough woman! I'm trying to give a tour here!"
    show mad tish
    g "Stop complaining you old fossil before I ground you..."
    show mad reg at right

    menu:
        "Can she really ground you?":
            jump grounded
        "Tish is my spirit animal...":
            jump spirit
    label grounded:
        m "In certain ways yes..."
    label spirit:
        m "Ahem...let us proceed"
    scene art
    show dumb reg
    m "THIS is our art gallery. This room displays our vast collection of abstract paintings we've collected throughout our travels across europe. Very exclusive and expensive."
    menu:
        "How expensive exactly?":
            jump exp
    label exp:
        m "More that you can ever dream of."
    menu:
        "How charming...":
            jump charm
    label charm:
        m "Yes isn't it. Money makes the world go round you know?"
        show mad tish
        g "People see what we have and are inspired by our fortune. Where is your family from dear?"
        l "Brooklyn."
        g "Oh..."
        hide dumb reg
        show mad reg
        m "My condolences. Shall we move on to see indoor golf range?"
        show mad tish
        g "A splendid idea!"
        l "..."
    menu:
        "Burn it to the ground.":
            jump burn
        "Go see the golf room thats pretty dope.":
            jump dope
    label burn:
        l "Okay you actually can't commit arson that's a felony just go to the damn golf room."
    label dope:
        l "Heaven help me."
    scene golf
    show dumb reg
    m "Behold our golf room!"
    hide dumb reg
    l "Is that an actual sky? I didn't even know that was possible.."
    show mad reg
    m "Why yes it is and thank you for noticing!"
    show mad tish
    g "What do people honestly do without golf rooms hahahah."
    hide mad tish
    m "hahahahahaha"
    show double
    g "hahahahahahahahahaha"
    m "Oh it's good to laugh like that sometimes. Shall we move on to the garage to see my luxury car collection?"
    menu:
        "Can't.Take.Anymore.":
            jump any
        "Please god let this be the last.":
            jump last
    label any:
        m "And last but not least...My car collection. Only the finest. Step right this way."
    label last:
        l "sure....."
    scene car
    l "Actually. You know what? No one cares about your stupid car collection. No one cares about a golf room either! How can you people live with yourselves?!"
    l "Yeah I'm from Brooklyn Okay? And no I don't have penthouse suite or fancy cars! But do you know what I DO have?"
    scene hotdog
    menu:
        "a dirty water hot dog.":
            jump dirty
    label dirty:
        l "The End."
    return
