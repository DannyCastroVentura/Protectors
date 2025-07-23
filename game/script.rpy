default mc_name = "Daniel"

init python:
    mc = Character("TEMP")
    ninja_path = get_folder_from_map("ninja")    
    templar_path = get_folder_from_map("templar")
    samurai_path = get_folder_from_map("samurai")

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
    nova "That's a beautiful name."

    nova "Alright, [mc.name] — let’s get started."
    mc "Okay... What's going on, exactly?"
    nova "The moment you launched this 'game', you stepped into a different world."
    mc "Wait — you mean this isn’t just a game?"
    nova "Not anymore. You’ve crossed into a world scarred by endless wars — each one destroying pieces of ancient knowledge and lost technology."
    mc "That sounds... serious. Like post-apocalyptic serious."
    nova "Very much so. No one even knows what year it is anymore. Wars reset the calendar, shaped by the chaos and shifting religions that follow."
    mc "So there's no real history? Just... fragments?"
    nova "Exactly. And it’s in that chaos where your purpose lies."
    nova "Your mission is simple in words, but not in action: restore peace and equality to this broken world."
    mc "Peace and equality? That’s... a pretty big ask for one person."
    nova "You won’t be alone. You’ll have help — from powerful allies known as the 'Protectors'. The Alliance has chosen to trust you."
    mc "The Alliance? Is that like... a government or something?"
    nova "A resistance. One of the last coalitions fighting for balance, not power."
    nova "Any questions so far?"
    mc "*pauses* Honestly? A thousand. But mostly... why me?"
    nova "That answer will come with time, [mc.name]. For now, know that you’ve been chosen for a reason."
    mc "Right. No pressure or anything."
    nova "I understand it’s overwhelming."
    mc "It is. But... I don’t want to walk away, either. If I can help, I want to try."
    nova "Good. You’ll need that spirit where you’re going."
    nova "Let’s begin by finding your first ally. The Alliance is offering you three Protector candidates."
    nova "Each brings something unique to your team."
    mc "Alright. Let’s see who they are."

    # TODO: improve the image dispersion - they are stuck at the limits as they should
    # showing ninja
    image ninja_starting = getImage(f"{ninja_path}/1")
    show ninja_starting at fit_to_screen_height, farLeft
    
    # showing templar
    
    image templar_starting = getImage(f"{templar_path}/1")
    show templar_starting at fit_to_screen_height, center

    # showing samurai
    image samurai_starting = getImage(f"{samurai_path}/1")
    show samurai_starting at fit_to_screen_height, farRight

    nova "Okay, so you can choose only one.."
    nova "Who will that be?"

    menu:
        "Ninja (stats)":
            # TODO: choose ninja, and add it to the bag of protectors
            mc ""
        "Templar (stats)":
            # TODO: choose Templar, and add it to the bag of protectors
            mc ""
        "Samurai (stats)":
            # TODO: choose Samurai, and add it to the bag of protectors
            mc ""

    return
