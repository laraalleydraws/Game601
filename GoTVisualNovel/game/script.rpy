# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Dani")
define j = Character("Jon")
define s = Character("Jon")
define k = Character("Dani")
define n = Character("nightking")
define c = Character("cersei")
define y = Character("jaime")
define b = Character("bran")
define a = Character("Arya")
define m = Character("mountain")
define r = Character("Red Woman")
define z = Character("Gendry")
define t = Character("Samwell")
define w = Character("Tormund")
define f = Character("Sansa")
define l = Character("tyrion")
define x = Character("Jon")
define u = Character("Mel")
define g = Character("Theon")
define e = Character("Brienne")
define audio.tavernmusic = "music/got.mp3"


# The game starts here.

label start:

    image Dani = "dannyrl.png"
    image jon = "jon.png"
    image snow = "jonrl.png"
    image Jon and Dani = "jondanny.png"
    image Daenerys = "danny.png"
    image nightking = "nightking.png"
    image cersei = "cersei.png"
    image jaime = "jaime.png"
    image bran = "bran.png"
    image arya = "arya.png"
    image mountain = "mountain.png"
    image redwoman = "redwoman.png"
    image hound = "hound.png"
    image jorah = "jorah.png"
    image samwell = "samwell.png"
    image tormund = "bane.png"
    image sansa = "sansa.PNG"
    image tyrion = "tyrion.PNG"
    image Winterfell = "Winterfell.png"
    image Kings Landing = "kingslanding.PNG"
    image The Wall = "thewall.png"
    image Mel = "mel.png"
    image Warp = "time.png"
    image night = "night.png"
    image battle = "battle.png"
    image theon = "theon.png"
    image meeting = "meeting.png"
    image tdeath = "tdeath.png"
    image aryanight = "aryanight.jpg"
    image daniface = "dannyface.png"
    image stables = "stables.png"
    image genrya = "genrya.png"
    image brienne = "brienne.png"
    image torbri = "Tormund-Flirting-for-3-Minutes-Straight-.png"
    image bigwoman = "maxresdefault.jpg"
    image britor = "Game-Of-Thrones-Season-7-Romance-Brienne-Tormund.jpg"
    image ending = "3000.png"
    image title = "title.png"
    image starbucks = "starbucks.png"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

play music tavernmusic
scene title
menu:
    "PLAY GAME":
        jump Winterfell



label Winterfell:
    scene Winterfell
    show Dani

    d "Jon...have you heard about the backlash over Season 8? We really need to repair the damage. This is a PR nightmare."

    show snow with dissolve


    x "You are my queen."
    hide snow
    show Dani

    d "Great. Glad you're on board with this. Alrighty well I have Melisandre here and she's going perform a little spell for us and uh we should fix this up in no time."
    hide Dani
    show snow

    s "I don't want it."

    show Dani

    d "Okay whatevs. Anyway here she is! Hi Mel!"

    show mel

    u "Death is coming for everyone."

    hide snow
    hide mel
    show Dani

    d "WHOAAA talk about a buzz kill haha"
    d "Anywho we were wondering if you knew of a spell to change Season 8?"

    hide Dani
    show mel

    u "The darkness..."
    u "I know of a spell."
    u "But it is not as it seems..."

    hide mel
    show Dani

    d "eh we'll take it. How bad can it be?"

    show snow
    show mel

    menu:
        "Praise the lord of light":
            jump light
        "Ask Mel?":
            jump dark

label light:
    u "you have chosen well. Allow me to prepare the spell."

    scene Winterfell
    show Dani

    d "Noice. Well we will just sit back here and let you do your thi-"
    u "Valar morghūlis."

label dark:

    scene Warp
    show mel
    hide snow

    u "Āeksios Ōño, aōhos ōñoso īlōn jehikās! Āeksios Ōño, īlōn mīsās! Kesrio syt bantis zōbrie issa se ossȳngnoti lēdys!"

    show Dani with dissolve

    d "What is happening!?"

    show snow

    x "You are my queeeeeeen."

    d "DO YOU HAVE ANY OTHER VOCABULARYYYYY?!"

    "WAAAaaaaaRRRRpppppPPPP"

    hide snow with dissolve
    hide mel with dissolve
    hide Dani with dissolve
    scene Winterfell

    d "Oh my god...what just happened..."
    d "look at me!?!?"

    show Daenerys with dissolve

    d "Sweet Jesus...why am I all pixelated??"
    show jon at center with dissolve
    x "I dont want it."
    d "*Eyeroll* Well at least that's normal..."
    d "Mel what the hell is going on here? I thought you were helping us!"

    show redwoman with dissolve

    u "Lord of Light, protect us..."
    u "It appears as if we got pixelated while traveling through space and time..."
    u "I told you it is not as it seems."

    show Daenerys
    d "Oh christ what the devil do we do now?"
    show jon
    x "You are my-"
    d "please don't."
    d "hmm I guess we should get started..."
    d "Where to first Mel?"
    hide jon
    hide Daenerys
    show redwoman with dissolve

    u "The Battle of Winterfell."

    scene night

    d "what fresh hell is this."
    u "The battle of Winterfell."
    d "Why is it so dark?"
    u "...No one knows."
    d "What a poor judgement choice. Let's start by brightening the screen."

    scene battle

    d "That is much better isn't it."
    show Daenerys
    d "Now we can actually see!"
    show redwoman
    u "Well done young queen."
    show jon
    x "..."
    d "Just say it."
    x "You are MY queen."
    u "The Army of the dead are coming."
    d "Yes we must hurry!"
    d "Wait who is that?"
    u "Theon Greyjoy."
    d "I think I know a Greyjoy..."

    menu:
        "Talk to Theon":
            jump theon
        "Try to remember the last time you met him...":
            jump ignore

label theon:
    d "Theon Greyjoy?"

    hide jon with dissolve
    show theon with dissolve

    g "Yes? Oh my queen."
    g "'bowing'"

label ignore:
    d "ah yes now I remember you..."

    scene meeting
    show theon with dissolve
    show Daenerys with dissolve
    d "This is where we formed a treaty. You swore your loyalty to me..."
    g "Yes..."
    d "Where are you off to now?"
    g "To defend Bran. The army of the dead are approaching!"
    d "Defend Bran...Oh no."
    d "Theon you shouldn't defend Bran! It's uh bad news."
    g "What? But I swore to defend the Starks!"

    menu:
        "Stop Theon from Defending Bran":
            jump defend
        "Let him meet his untimely death":
            jump death

label defend:
    d "Yes well about that...I am your queen! You will do as I command!"

    show theon

    g "Okay...well I will be off then."
    d "Yes, off you trot!"
    d "I just saved his life...I am the best queen EVER."

jump thebattle

label death:
    d "Good-bye Theon Greyjoy..."
    show tdeath
    d "Damn RIP tho."

label thebattle:
    scene battle
    hide theon
    show jon
    show redwoman
    show Daenerys

    u "Where shall we go next..."
    d "Let me think...Wait who is that walking towards Jon?"
    u "It appears to be Samwell Tarley."
    d "what."
    d "Oh no...oh god"
    u "Something wrong?"
    d "I may have...killed his father and brother. This is going to be AWKWARD."
    show samwell
    t "helloooo Jon! I have very interesting news about you that I found in the Citadellll!"
    d "'NOOOOOOOOOOO that big buffoon is going to take away my throne!'"
    t "Oh hello Dani I didn't see you there!"
    d "Samwell! uh Jon can't speak anymore he...lost his tongue in the battle of the bastards"
    t "Oh that's dreadful..."
    d "Tragic."
    t "Yes...Good thing I learned sign langage in the Citadel!"
    "walks over to jon"
    d "'UGHHHH I must do something...'"
    d "Sam wait! I killed your whole family!"
    t "WHAT?!"
    d "Okay not all of them but for sure your father and brother. They wouldn't bend the knee!"
    t "'sniffles' But how could you!?!?"
    t "'sniffles instensifies'"
    d "I'm very sorry Sam. I did what had to be done."
    "Sam walks away"
    hide samwell
    d "Can we please get out of here?"
    u "I figured you'd want to see Arya defeat the nightking..."

    menu:
        "Go see Arya":
            jump arya
        "Eh you've seen it":
            jump mainmenu
label arya:
    scene aryanight
    show Daenerys
    show redwoman
    d "yasssss meeee(queen)!!"
    u "Never gets old."
    d "Right? SO feminist."
    f "Did someone say feminist..."
    show sansa with dissolve
    u "Sansa Fierce!"
    d "Sansa..."
    scene daniface
    d "lol."
    hide redwoman with dissolve
    scene Winterfell
    f "Winterfell is yours your grace."
    show sansa with dissolve
    show Daenerys with dissolve
    d "Yes... still not reconizing me as queen tho?"
    f "no."
    d "dammit."
    f "I just spoke to Jon..."
    d "...what?"
    f "He seems to have an interesting family back story..."
    d "...oh...does he?"
    f "I believe he has a legitimate claim to the throne."
    d "'clutches fists'"
    d "HAHAHAHA sounds like fake news to me."
    f "We'll see..."
    f "'sansa walks away'"
    hide sansa with dissolve
    show Daenerys
    show redwoman
    d "Note to self: Kill her by dragon fire later."
    u "You would kill one of your strongest ally's without any hesitation?"
    d "Hold. my. beer."
    d "Did you see 'The Bell's' episode? I decimated an entire city!"
    d "Anyway, where to next?"
jump mainmenu

label mainmenu:
    menu:
        "The Stables":
            jump bangsesh
        "Tormunds Reckoning":
            jump tor
label bangsesh:
    scene stables
    hide redwoman
    show Daenerys
    d "Are we in the stables? What could possibly be going on-"
    show genrya
    a "TAKE YOUR BLOODY PANTS OFF!"
    z "AHHH!"
    d "Oh my god. Aren't you like 12?!"
    a "Oh it's the queen..."
    d "You listen missy. I am your quee-"
    a "'rolls eyes'"
    d "Put clothes on AT ONCE."
    d "This is so inappropiate."
    d "I need outta here. Where's my starbucks cup?"
    show starbucks
    d "sippppppp"
    hide genrya
label tor:
    scene Winterfell
    show Daenerys with dissolve
    show tormund
    d "Oh? What's this? Are we witnessing a romance here?"
    w "What light through yonder window breaks..."
    show brienne
    e "Oh god."
    w "That thou her maid art far more fair than she."
    e "Look Tormund I really appreciate the gesture but my heart is with Jaime."
    w "Jaime Lannister? Oh he left he a little while ago."
    e "What."
    w "Yeah I heard him run off. Probs going to go do his sister."
    e "you sure?"
    w "Would I lie to an angel?"
    hide Daenerys
    hide starbucks
label tormundslife:
    menu:
        "Slap him-Your loyalty is with Jaime":
            jump slap
        "Embrace the Love":
            jump love
label slap:
    e "Tormund this is very inappropriate."
    e "I will ask you no more to leave me alone!"
    w "..."
    w "Oh, won't you stay with me?"
    w "Cause you're all I need"
    e "Sam Smith? Really?"
    w "This ain't love, it's clear to see."
    show Daenerys
    e "Dani. Starbucks?"
    d "Way ahead of you."
    hide Daenerys with dissolve
    hide brienne with dissolve
    w "But darling, stay with me..."
    scene britor
jump end
label love:
    e "I really appreciate that Tormund."
    e "You know. You've always been there for me..."
    scene torbri
    e "Always watching over me..."
    scene bigwoman
    e "Asking about my well-being..."
    scene Winterfell
    show brienne
    show tormund
    e "You know what. We may die tomorrow..."
    e "This battle will be harsh. Let's give love a shot."
    scene britor
jump end
label end:
    scene ending
    d "Well that was beautiful. I think our work is done here."
    u "Where to next young queen?"
    d "I guess we are off to King's Landing for some PR damage control..."
    return
