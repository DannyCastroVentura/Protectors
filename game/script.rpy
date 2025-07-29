default mc_name = "Daniel"
default show_my_protectors = False
default show_my_protector_specific_info = False

init python:
    mc = Character("TEMP")
    ninja_path = get_folder_from_map("ninja")
    templar_path = get_folder_from_map("templar")
    samurai_path = get_folder_from_map("samurai")
    config.overlay_screens.append("my_protectors_screen")

define nova = Character("Nova", color="#00a2ff")
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

    hide nova
    # TODO: change the first 3 protectors, so we remove the samurai, and add the recruit
    call showFirst3Protectors()

    nova "These are the candidates.."
    
    $ while_aux = 0
    while while_aux == 0:
        call showFirst3Protectors()

        nova "You have the Ninja, the Templar and the Samurai."

        nova "You can choose only one.."
        nova "Who will that be?"
        menu:
            "Ninja \n([get_protector_base_information('ninja')])":
                hide templar_starting
                hide samurai_starting
                show ninja_starting at fit_to_screen_height, center
                nova "Are you sure you want to choose the Ninja for your first protector?"
                menu:
                    "Yes!":
                        $ while_aux = 1
                        nova "Great!"
                        nova "I'm adding Ninja to your list of protectors!"
                        $ add_new_protector("ninja")
                        nova "Ninja added!"
                    "What were the other ones?":
                        nova "Let's recap."
            "Templar \n([get_protector_base_information('templar')])":
                hide ninja_starting
                hide samurai_starting
                show templar_starting at fit_to_screen_height, center
                nova "Are you sure you want to choose the Templar for your first protector?"
                menu:
                    "Yes!":
                        $ while_aux = 1
                        nova "Great!"
                        nova "I'm adding Templar to your list of protectors!"
                        $ add_new_protector("templar")
                        nova "Templar added!"
                    "What were the other ones?":
                        nova "Let's recap."
            "Samurai \n([get_protector_base_information('samurai')])":
                hide ninja_starting
                hide templar_starting
                show samurai_starting at fit_to_screen_height, center
                nova "Are you sure you want to choose the Samurai for your first protector?"
                menu:
                    "Yes!":
                        $ while_aux = 1
                        nova "Great!"
                        nova "I'm adding Samurai to your list of protectors!"
                        $ add_new_protector("samurai")
                        nova "Samurai added!"
                    "What were the other ones?":
                        nova "Let's recap."

    hide templar_starting
    hide samurai_starting
    hide ninja_starting
    show nova at center, fit_to_screen_height
    nova "Great! Now you have your first protector!"
    nova "You can check your protectors by clicking in the button \"My Protectors\""
    nova "So we can now continue!!"
    nova "So we can now continue!"
    nova "So we can now continue!!"
    return


label showFirst3Protectors(): 
    # hiding the 3 protectors before showing
    hide templar_starting
    hide samurai_starting
    hide ninja_starting

    # showing ninja
    image ninja_starting = getImage(f"{ninja_path}/1")
    show ninja_starting at fit_to_screen_height, farLeft
    
    # showing templar
    
    image templar_starting = getImage(f"{templar_path}/1")
    show templar_starting at fit_to_screen_height, center

    # showing samurai
    image samurai_starting = getImage(f"{samurai_path}/1")
    show samurai_starting at fit_to_screen_height, farRight
    return

label novaShowingProtector():
    nova "Going back"
    return