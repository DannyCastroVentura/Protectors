default mc_name = "Daniel"
default show_my_protectors = False
default show_my_protector_specific_info = False
default show_whole_functionality_for_seeing_my_protectors = False
default show_current_day = False
default show_wallet = False
default current_day = 1
default money = 0

init python:
    if 'mc_name' not in globals():
        mc_name = "Daniel"
    mc = Character([mc_name])
    ninja_path = get_folder_from_map("ninja")
    templar_path = get_folder_from_map("templar")
    samurai_path = get_folder_from_map("samurai")
    config.overlay_screens.append("my_protectors_screen")
    config.overlay_screens.append("current_day_screen")
    config.overlay_screens.append("wallet_screen")
    
    

define nova = Character("Nova", color="#00a2ff")
define anonymous_yet = Character("??")
define selected_protector = None


label start:
    $ initializing_things()
    $ testing_things()
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
            "Ninja \n([protectors_base_information['ninja'].get_base_information()])":
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
            "Templar \n([protectors_base_information['templar'].get_base_information()])":
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
            "Samurai \n([protectors_base_information['samurai'].get_base_information()])":
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
    $ show_whole_functionality_for_seeing_my_protectors = True
    nova "You can check your protectors by clicking in the button \"My Protectors\""
    nova "Once you click, you'll see all your protectors - for now, you have only one!"
    nova "If you click on your protector, you'll see more information about him."
    nova "Great! Now let's continue!"    
    $ while_aux = 0
    while while_aux == 0:        
        call nova_explains_tutorial()
        $ set_background("base-of-operations")
        nova "Then that would be all!"
        nova "Did you understood everything so far?"
        menu:
            "Yes, I understood everything!":
                $ while_aux = 1
                mc "I think I understood everything!"
                nova "Great!"
                nova "In any case you can alsways call me!"
            "No, could you please repeat?":
                mc "I'm not sure if I understood.."
                mc "Could you repeat please?"
                nova "Sure!"
    $ show_wallet = True
    $ show_current_day = True
    jump base_of_operations

    # TODO: missions
    #   we need to create the different regions to check for the specific mission
    #   also when we click on a mission title, we should get the detail for that mission, and then click on "Send a protector for this mission?"
    #   We can send the protector for any mission - if he have the right stats -> need to think a bit better - maybe depending on the type of the mission, different stats are needed?
    #   for the stage missions, our protector can be killed, we need to be careful
    #   stage missions only appear after we successfully do 15 (?number still to figure?) missions for that stage)
    #   once stage mission is completed, we can go to the next region - and everything should be the same
    # 
    # TODO: make it possible to call nova
    #
    # TODO: if the protector have 20 of level and 10 of stage, when showing the max level I should show (+oo)
    #
    # TODO: create the new frame for the stage 5 - as he should choose which one should he get, and depending on the one he chose, he will get some advantages
    # 
    # TODO: create a way to buy items or item drop chang? Still need to think about it
    # 
    # TODO: while we are having good results the resitance will provide some other new protectors

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

label nova_explains_tutorial():
    nova "Let me take you to your base of operations!"
    $ set_background("base-of-operations")
    nova "Here we are!"
    nova "You can use your base of operations to: \n- Check your missions list \n- Train you protectors\n- Rest area"
    nova "Check your missions list: \nIn here you can see what missions you have received."
    nova "Check your missions list: \nNote that there will be some missions very hard to handle - I recommend to start with the basic ones first!"
    nova "Check your missions list: \nIf the mission is to difficult for the experience of the protector, he might be unable from escape - and if this happens, he'll die and you'll lose this protector."
    nova "Check your missions list: \nIf all of your protectors die - you'll lose the game."
    nova "Check your missions list: \nBe careful when assinging protectors to missions."

    $ set_background("training-ground")
    nova "Training ground: \nThis is the a place we have built for helping you make new protectors stronger."
    nova "Training ground: \nTraining ground should be very helpful for inexperienced protectors."
    nova "Training ground: \nBut as they become stronger - the training ground start to be less effective."
    
    $ set_background("resting-area")
    nova "Resting area: \nYou can also go to the bedrooms to rest!"
    nova "Resting area: \nResting is very important, as your protectors also need to recover when they are back from their missions."
    nova "Resting area: \nResting is also very helpful when you need to advance the time."
    nova "Resting area: \nAdvancing time can be helpful for a lot of things, including - to get new missions."
    nova "Resting area: \nNew missions appear every day, but be careful! Old missions might disapear when you rest."
    nova "Resting area: \nEvery mission have a time to be started. If a mission was not yet initiated and this time finished, then this mission is closed as ignored."
    return

label show_my_available_protectors(isThisMission):
    call screen protector_selection(isThisMission)
    return
