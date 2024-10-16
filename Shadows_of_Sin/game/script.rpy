# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("???")


# The game starts here.

label start:

    scene interior_entrance_night with dissolve

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
    try to collect your thoughts into something coherent, but you draw only blanks. This leads to an even 
    more concerning realization. Who… are you?"

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

    mc "this looks familiar"
    call screen study_nav

label observe_clock:
    scene clock_zoomin

    mc "the hands arent moving"
    call screen study_nav

label observe_chair:
    scene study
    mc "looks uncomfortable"
    call screen study_nav

label observe_computer:
    scene study
    mc "looks like it needs a passcode"
    call screen study_nav

label observe_lamp:
    scene study
    mc "should i turn it off?"
    call screen study_nav

label observe_newspaper:
    scene study
    mc "i aint reading allat"
    call screen study_nav

label observe_rbookcase:
    scene study
    mc "i dont want to touch the books with blood on them"
    call screen study_nav

label observe_lbookcase:
    scene study
    mc "just looks like books"
    call screen study_nav

# This ends the game.

return
