# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("???") 

$ password = null

default attempts = 0

default unlocked = False

# The game starts here.

label start:

    play music "audio/calm_bgm.mp3"
    scene entrance with dissolve

    mc "{i}zzz...grumble...grumble...zzz{/i}"

    mc "{i}zzz...{/i}"

    mc "...!"

    mc "Huh… W-what…"

    mc "What is this? Where am I?"

    "You look around the long hallway you mysteriously awoke in. Within the worn down hallway lie cobwebs
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

    play sound "audio/locked_door_sfx.mp3"
    "You grab the doorknob and attempt to twist, only to find it wedged in place."

    mc "What is this? It’s locked… I’m locked inside?"

    "You pull harder and harder until you’re sweating. Your brow furrows, face hot."

    play sound "audio/locked_door_sfx.mp3"
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

    play sound "audio/creaky_door_sfx.wav"
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
    "The silent and immobile clock hands really bother you for some reason. If the clock worked, you could have at least one clue of your surroundings."
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

    if attempts == 0:
        scene computer_locked
    if attempts == 1:
        scene computer_1incorrect
    if attempts == 2:
        scene computer_2incorrect

    "You take a closer look at the monitor and notice it’s asking for a 4 digit passcode to log in."
    "Enter in a code?"

    menu:
        "Yes":
            $ password = renpy.input("Enter a 4 digit code:", allow = "1234567890", length = 4)
            if password == "0245":
                stop music
                mc "Come on…"
                "LOGGING IN..."
                play music "audio/calm_bgm.mp3"
                "You release a sigh of relief."
                mc "Finally, some good news. Weird that the time of the murder specifically was the key. Does this office belong to a detective on the case?" 
                mc "Am I involved in this somehow? Well, before I dive down that rabbit hole let’s dig around on here."
                "Strangely, there exists only a single text file on the screen titled “BASTARD”. It’s feels deliberate, as no trace of any other application or file is present. 
                This text file is the PC’s only purpose."
                "Hesitantly, you click on the text file to open it."
                play sound "audio/click_sfx.wav"
                scene computer_unlocked
                "HAVE YOU HEARD OF “THE BASTARD’S CURSE?” THAT BOOK TALKS ABOUT BASTARDS LIKE YOU. ABOUT WHAT AWAITS SINNERS LIKE YOU. WHAT DO YOU THINK IT IS?"
                mc "“The Bastard’s Curse” huh?? Weird note."
                mc "All that work just to read that?? What a waste of time."
                $ unlocked = True
                call screen study_nav

            else:
                play sound "audio/incorrect_sfx.wav"
                $ attempts += 1
                if attempts == 1:
                    scene computer_1incorrect
                    "ERROR - WRONG PASSCODE"
                    mc "Shit, I can’t log in without that passcode… Maybe there’s some clues around this room. I’ll take a longer look."
                    call screen study_nav
                if attempts == 2:
                    scene computer_2incorrect
                    play music "audio/tense_bgm.mp3"
                    "ERROR - WRONG PASSCODE"
                    mc "Dammit, only one try left. I need to be more careful."
                    call screen study_nav
                if attempts == 3:
                    scene computer_3incorrect
                    "ERROR - WRONG PASSCODE"
                    mc "Fuck."
                    jump branch

        "No":
            "Let me look around the room some more first."

            call screen study_nav

label observe_newspaper:
    play sound "audio/paper_sfx.mp3"
    scene newspaper
    
    mc "Silus Graves…a serial killer huh…"
    "Why does this feel familiar? You feel a sense of unease."
    mc "So they caught this Silus guy then. If this newspaper is out here, this must be recent then."
    mc "I’m starting to wonder what my place in all of this is."
    mc "I feel a connection to this case, I should try looking around for more clues."

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

        play sound "audio/paper_sfx.mp3"
        scene book_key with dissolve

        "You flip through to the page marked by a bookmark. You find an antique key labeled “Master Bed.”"
        mc "Well look at that…Looks like that file wasn’t a waste of time after all."
        scene book_nokey
        "You twirl the cold brass key in your damp hands. You just now notice how sweaty you are. Your heart knocks violently against your chest."
        "This feeling… it’s…fear."
        mc "Am I seriously afraid right now? Surely I’m not the type of guy to get scared of an old run down house right? Haha…"
        "No, it’s not the house that scares you… it’s the secrets you feel that will be revealed as you explore. It’s… you. You are your own source of fear."
        mc "Shit. I should continue searching the house… right?"
        
        menu:
            "Yes":
                mc "That was a stupid question. I don’t have time to sit around pissing my pants."
                "You steel yourself for what you might find and press on ahead. Let’s see what awaits you in the master bedroom."
                scene to_be_continued with dissolve
                pause 5.0
                return
            "No":
                mc "Fuck man, I have a REALLY bad feeling about this. Why don’t I remember anything anyways. Maybe I don’t remember for a reason."
                mc "The past doesn’t matter anyways, what matters is just breaking out of this GODDAMN shithole!!"
                scene entrance with dissolve
                "Your heartbeat quickens, you’re now drenched in sweat. You rush back to the entrance you came from in a crazed frenzy."
                play sound "audio/bang_sfx.mp3"
                mc "LET ME OUT!! I’M NOT FUCKING AROUND!"
                "Your anger and anxiety make you dizzy. You lose yourself to emotion."
                "In a desperate attempt to escape, you punch and kick the door with all of your raw strength. The loud banging of your body against the wood echos throughout the empty hallway."
                play sound "audio/bang2_sfx.mp3"
                "{b}{i}BOOM...BOOM...{/i}{/b}"
                "But it isn’t enough. How can a door be so strong? After a futile display of resistance, you slump to the ground, depleted of energy. You begin to spiral."
                mc "{b}{i}Heavy panting{/i}{/b}"
                mc "N…N-No… No way"
                mc "I’m…g-going to die in this place - this hell."
                stop music
                play sound "audio/creaky_floor_sfx.wav"
                "After a few moments, you hear something scratching the floorboards down the hall. You would go check if you had the energy to stand."
                mc "W-What…"
                "It’s quick! Before you can finish registering the sound, you see a spider like abominating rushing towards you."
                scene entrance_monster
                mc "N-no fucking way, no fucking way!! GET THE HELL AWAY FROM ME MONSTER!!"
                "It’s too late. In mere seconds it races to you."
                scene entrance_monster2
                mc "NOO NOOO PLEASE, LEAVE ME ALONE!!!"
                play sound "audio/gore_sfx.mp3"
                "The monster tears apart at you, ripping apart your flesh. Your blood splatters over the old bloodstains of the hall."
                mc "ACK! G-GET AWAY!!! AGhhh"
                play sound "audio/jumpscare_sfx.wav"
                pause 0.3
                window hide
                scene monster_game_over
                pause 5.0
                return

label observe_lbookcase:
    scene study

    "You turn your attention to the bookcase lining the right wall. There’s mostly books covering historical and philosophical topics. Dust and dried blood cake the covers of the novels."
    mc "Doesn’t look like anything of importance here. I should keep looking around."

    call screen study_nav

label branch:
    stop music
    scene computer_off
    "Suddenly, the computer shut off and the lamp went out."
    mc "What the hell?"
    "Look up?"
    menu:
        "Yes":
            jump restart
        "No":
            play sound "audio/creaky_floor_sfx.wav"
            "You can hear footsteps outside the door."
    
    "LOOK UP!"
    menu:
        "Yes":
            jump too_late
        "No":
            play sound "audio/creaky_door_sfx.wav"
            "You hear the door open."
            play sound "audio/creaky_floor_sfx.wav"
            "The footsteps are getting louder, closer, but fear has you frozen in place."
            "As seconds pass you begin to feel the breath of something looming over you."
            "In that moment, you knew your fate was already set. You couldn't help but wonder if things might've turned out differently had you made better choices."
        "I'm scared":
            play sound "audio/creaky_door_sfx.wav"
            "You hear the door open."
            play sound "audio/creaky_floor_sfx.wav"
            "The footsteps are getting louder, closer, but fear has you frozen in place."
            "As seconds pass you begin to feel the breath of something looming over you."
            "In that moment, you knew your fate was already set. You couldn't help but wonder if things might've turned out differently had you made better choices."
    
    "look up."
    menu:
        "yes":
            jump death
        "yes":
            jump death

label restart:
    scene study_lights_off
    "You can just barely make out the furniture in the darkness."
    "As you take a look around, you can't shake this feeling of dread. You could sense something sinister approaching."

    "Hide?"
    menu:
        "Yes":
            scene desk_zoomin_dark
            "You quickly run and crouch behind the desk."
            play sound "audio/creaky_floor_sfx.wav"
            mc "..."
            "You begin holding your breath so as to not make any noises."
            play sound "audio/creaky_floor_sfx.wav"
            mc "..."
            "The seconds felt like hours. You didn't know if you could hold out much longer."
            play sound "audio/creaky_floor_sfx.wav"
            mc "..."
            "Finally, you hear the footsteps move away from the door. You're safe, for now."
            scene study
            "Suddenly, the computer and lamp turn back on. You let out a sigh of relief."
            mc "{b}{i}Sigh.{/i}{/b} Well, I guess I should get back to my search."
            $ attempts = 0
            play music "audio/calm_bgm.mp3"
            call screen study_nav

        "No":
            mc "I'm probably just imagining it."
            mc "I should focus on getting the power back on, I can't make any progress like this."
            "As you begin searching the room for a way to turn on the lights, you hear something."
            play sound "audio/creaky_floor_sfx.wav"
            jump too_late


label too_late:
    scene study_lights_off
    "You can sense something is right outside the door."
    "Hide?"
    menu:
        "Yes":
            scene desk_zoomin_dark
            "You quickly run and crouch behind the desk."
            play sound "audio/creaky_door_sfx.wav"
            mc "..."
            "You begin holding your breath so as to not make any noises."
            play sound "audio/creaky_floor_sfx.wav"
            mc "..."
            "The seconds felt like hours. You didn't know if you could hold out much longer."
            mc "..."
            "You are unsure of how much time has passed, but you hadn't heard any footsteps for a couple minutes."
            mc "I should be in the clear."
            "You slowly stand from where you were crouched behind the desk and take a look around."
            jump death

        "No":
            play sound "audio/creaky_door_sfx.wav"
            jump death

label death:
    scene monster
    window hide
    pause 3.0
    window show
    "..."
    "......"
    "........."
    play sound "audio/jumpscare_sfx.wav"
    pause 0.3
    window hide
    scene monster_game_over
    pause 5.0
    return