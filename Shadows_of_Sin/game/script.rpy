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

    # This ends the game.

    return
