default mc_name = "Daniel"

init python:
    mc = Character("TEMP")

define nova = Character("Nova")
define anonymous_yet = Character("??")

label start:

    anonymous_yet "Greetings, human."    
    anonymous_yet "Can you ear me?"
    anonymous_yet "Please try to open your eyes."


    $ set_background("dream")
    image nova = getImage("images/nova")

    show nova at center, fit_to_screen_height

    anonymous_yet "Is it better now?"

    anonymous_yet "I'm Nova — your new assistant and guide through this unfamiliar world."

    nova "There’s much to discover, but before we begin..."

    nova "I’d like to know what to call you."

    $ mc_name = renpy.input("What’s your name?")
    $ mc_name = mc_name.strip()
    if not mc_name:
        $ mc_name = "Daniel"

    $ mc.name = mc_name

    nova "Ah, [mc.name]."
    nova "That's a lovely name."

    nova "Alright then, [mc.name] — let’s dive in."

    mc "I'm ready. Lead the way, Nova."

    return
