# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("???") 

$ password = null

default unlocked = False

# The game starts here.

label start:

    scene entrance with dissolve

    mc "{i}zzz...grumble...grumble...zzz{/i}"

    mc "{i}zzz...{/i}"

    mc "...!"

    mc "Huh… W-what…"

    mc "What is this? Where am I?"

    "You look around the long hallway you mysteriously awoke in. Within the worn down hallway lies cobwebs
    lined in the corners and the floor is caked in dust. This place appears to be from a forgotten time."

    mc "What is this place? It looks like a Halloween prop. Why is it so run down?"

    mc "Hello? Is anyone there?"

    "..."

    mc "Hello? Can anyone hear me? HELLO?"

    "No response. You can only hear the sound of your own voice echoing through the hallowed halls."

    "The resounding silence turns your thoughts introspective. Why were you here in the first place? You 
    try to collect your thoughts into something coherent, but you draw only blanks."
    
    "This leads to an even more concerning realization. Who… are you?"

    mc "Why can’t I remember anything? Fuck I don’t even know my name. Is this some sort of sick joke?"

    "As concerning as this discovery is, you don’t have time to waste."

    mc "Well I’d better get out of here first, I’ll figure out the rest later."

    "You turn around and notice a large door behind you, equipped with an antique doorknob with a keyhole. 
    It looms over you like it’s trying to intimidate you to turn back around. It’s as if it‘s telling you 
    “You don’t belong outside this place, go back.”"
    
    "You feel your gut sink, but you push through it."

    mc "This is no time to fool around, let’s go."

    "You grab the doorknob and attempt to twist, only to find it wedged in place."

    mc "What is this? It’s locked… I’m locked inside?"

    "You pull harder and harder until you’re sweating. Your brow furrows, face hot."

    mc "Fuck, OPEN!!"

    "You’re banging on the door with your fists, and start kicking it out of frustration. 
    After a few minutes of futile resistance, you accept your fate. You are stuck here."

    mc "{b}{i}pant pant{/i}{/b}"

    mc "I’m gonna have to find another way. Shit."

    mc "It has a keyhole, there must be a key inside somewhere. Or someone who has it."

    mc "Hell, maybe I’ll find someone who can fill me in on what’s happening. Or better yet, my name."

    "You look around closer at your surroundings. You notice 3 other doors you haven’t tried opening yet. 
    You approach the one closest to you and decide to try your luck."

    mc "Please, please open."

    "You turn the knob slowly, anticipating the worst. To your surprise, it opens. You let out a sigh of relief."

    mc "Ok…it opened. Let’s find out what’s happening."

    scene study with dissolve

    "You scan the dimly lit room, carefully taking in your surroundings."

    "Books line the vintage wallpapered walls. A PC desk placed in the middle of the room demands your attention."

    scene desk_zoomin with dissolve

    "As you creep closer to the desk you notice something sinister. Blood. Everywhere."

    mc "Blood? What the hell?"

    "Upon closer inspection, the blood is thoroughly caked on the wood of the desk. Whatever happened here, it wasn’t recent."

    "Without thinking, you touch the bloodstained wood with your hands. You don’t know what possessed you to touch it."

    mc "..."

    "There’s something drawing you in. You feel strangely calm, or maybe even comforted? You feel that you should be more frightened than you are."

    mc "Just what kind of life was I leading?"

    scene study with dissolve

    "You back away from the desk, taking in the room in its entirety again. You have work to do."

    mc "Right, a key. There’s gotta be one somewhere. Now… where to look first?"

    call screen study_nav

    screen study_nav():
        add "study"
        modal True

        imagebutton auto "painting_%s":
            focus_mask True
            action Jump("observe_painting")

        imagebutton auto "clock_%s":
            focus_mask True
            action Jump("observe_clock")

        imagebutton auto "computer_%s":
            focus_mask True
            action Jump("observe_computer")

        imagebutton auto "lamp_%s":
            focus_mask True
            action Jump("observe_lamp")

        imagebutton auto "newspaper_%s":
            focus_mask True
            action Jump("observe_newspaper")

        imagebutton auto "chair_%s":
            focus_mask True
            action Jump("observe_chair")

        imagebutton auto "rbookcase_%s":
            focus_mask True
            action Jump("observe_rbookcase")

        imagebutton auto "lbookcase_%s":
            focus_mask True
            action Jump("observe_lbookcase")

label observe_painting:
    scene painting_zoomin

    mc "Hmm this artwork looks familiar for some reason, but I can’t quite put my finger on it."
    mc "I wonder if there’s anything behind it?"
    "You lift the painting to look behind the frame."
    mc "..."
    mc "Nothing. Well, it was worth a shot."
    
    call screen study_nav

label observe_clock:
    scene clock_zoomin

    "An old antique grandfather clock firmly placed and towers over you. Like the rest of the house, it’s covered in dust and is worn down."
    "It’s too silent. There’s no clicking of time. You notice the hands are frozen in place."
    mc "It must be broken. No surprise really, I think this clock might be older than me."
    "You make note of the time it froze on, 2:25. Whether its AM or PM remains a mystery."
    "The silent and immobile clock hands really bother you for some reason. If at least the clock worked, you could have at least one clue of your surroundings."
    "Your thoughts start to wander. Is the clock broken, or is time itself stuck in place with you? You almost laugh at the absurdity of the idea."
    mc "Frozen huh… Get a grip man. I need to focus on clues, not old shitty clocks."

    call screen study_nav

label observe_chair:
    scene study

    "An antique chair sits behind the desk. Deep red velvet lines the cushion. You feel an urge to sit in it."
    mc "It would be nice to sit for a second."
    "You rest your feet and take a short breather."
    "The cushions are dusty but soft."
    mc "Well, I should get back to it."

    call screen study_nav

label observe_lamp:
    scene study
    
    "A green desk lamp sits on the desk, illuminating the room with a soft glow."

    call screen study_nav

label observe_computer:
    scene study
    
    "A soft blue light is radiating from the PC."
    mc "I’m shocked this rundown place even has power. But that must mean someone turned it on…"

    scene computer_locked with dissolve

    "You take a closer look at the monitor and notice it’s asking for a 4 digit passcode to log in."
    "Enter in a code?"

    menu:
        "Yes":
            $ password = renpy.input("Enter a 4 digit code:", allow = "1234567890", length = 4)
            if password == "0225":
                mc "Come on…"
                "LOGGING IN..."
                "You release a sigh of relief."
                mc "Finally, some good news. Weird that the time of the murder specifically was the key. Does this office belong to a detective on the case?" 
                mc "Am I involved in this somehow? Well, before I dive down that rabbit hole let’s dig around on here."
                "Strangely, there exists only a single text file on the screen titled “BASTARD”. It’s feels deliberate, as no trace of any other application or file is present. 
                This text file is the PC’s only purpose."
                "Hesitantly, you click on the text file to open it."
                scene computer_unlocked
                "HAVE YOU HEARD OF “THE BASTARD’S CURSE?” THAT BOOK TALKS ABOUT BASTARDS LIKE YOU. ABOUT WHAT AWAITS SINNERS LIKE YOU. WHAT DO YOU THINK IT IS?"
                mc "“The Bastard’s Curse” huh?? Weird note."
                mc "All that work just to read that?? What a waste of time."
                $ unlocked = True

                call screen study_nav

            else:
                "ERROR - WRONG PASSCODE"
                mc "Shit, I can’t log in without that passcode… Maybe there’s some clues around this room. I’ll take a longer look."

                call screen study_nav

        "No":
            "Let me look around the room some more first."

            call screen study_nav

label observe_newspaper:
    scene newspaper
    
    mc "Wow, what a tragedy..."
    mc "Good thing that guy was caught."

    call screen study_nav

label observe_rbookcase:
    scene study
    
    if not unlocked:
        "You turn your attention to the bookcase lining the right wall. There’s mostly books covering historical and philosophical topics. Dust and dried blood cake the covers of the novels."
        mc "Doesn’t look like anything of importance here. I should keep looking around."

        call screen study_nav
    else:
        "You turn your attention to the bookcase lining the right wall. There’s mostly books covering historical and philosophical topics. Dust and dried blood cake the covers of the novels."
        mc "Wait..."
        "You notice a book titled “The Bastard’s Curse.”"
        mc "...That’s the book mentioned in the computer file. Maybe I should take a quick look."
        "You pick up the book, ignoring the blood stains as you flip through the pages."
        mc "Looks like there’s something sticking out in the middle."

        scene book_key with dissolve

        "You flip through to the page marked by a bookmark. You find an antique key labeled “Master Bed.”"
        mc "Well look at that…Looks like that file wasn’t a waste of time after all."
        "Grab the key?"

        menu:
            "Yes":
                jump good_end
            "No":
                mc "placeholder text"
                window hide
                show game_over with dissolve
                pause 5.0
                return

label observe_lbookcase:
    scene study

    "You turn your attention to the bookcase lining the right wall. There’s mostly books covering historical and philosophical topics. Dust and dried blood cake the covers of the novels."
    mc "Doesn’t look like anything of importance here. I should keep looking around."

    call screen study_nav

label good_end:
    # This ends the game. 
    scene book_nokey
    mc "“Master Bed…” must be one of the rooms out in the hall. Let’s go check it out."
    #scene to_be_continued with dissolve
    return
