default mc_name = "Daniel"
default show_things = False
default show_equipment = False
default current_day = 1
default money = 0
default SClassColor = "#DC143C"
default AClassColor = "#FFD700"
default BClassColor = "#9370DB"
default CClassColor = "#1E90FF"
default DClassColor = "#32CD32"
default EClassColor = "#A9A9A9"

init python:
    if 'mc_name' not in globals():
        mc_name = "Daniel"
    mc = Character([mc_name])
    config.overlay_screens.append("menu_button_for_protectors_game")
    config.overlay_screens.append("current_day_screen")
    config.overlay_screens.append("money_screen")

    # button_small_text
    # Button box styling (background, padding, etc.)
    style.button_small_text = Style("button")
    style.button_small_text.background = "#444444"
    style.button_small_text.hover_background = "#666666"
    style.button_small_text.xpadding = 10
    style.button_small_text.ypadding = 5

    # Text styling
    style.button_small_text_text = Style("button_text")
    style.button_small_text_text.color = "#FFFFFF"
    style.button_small_text_text.hover_color = "#FFCC00"
    style.button_small_text_text.size = 18
    style.button_small_text_text.bold = True

    # button_small_text_selected
    # Button box styling (background, padding, etc.)
    style.button_small_text_selected = Style("button")
    style.button_small_text_selected.background = "#ffffff"
    style.button_small_text_selected.hover_background = "#666666"
    style.button_small_text_selected.xpadding = 10
    style.button_small_text_selected.ypadding = 5

    # Text styling
    style.button_small_text_selected_text = Style("button_text")
    style.button_small_text_selected_text.color = "#444444"
    style.button_small_text_selected_text.hover_color = "#FFCC00"
    style.button_small_text_selected_text.size = 18
    style.button_small_text_selected_text.bold = True

    
    

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
    # TODO: add a magic protector
    # TODO: change the first 3 protectors, so we remove the Samurai, and add a sorcerer
    call showFirst3Protectors()

    nova "These are the candidates.."
    $ first_protector_selected = ""
    $ while_aux = 0
    while while_aux == 0:
        call showFirst3Protectors()
        hide screen base_stats
        nova "You have the Ninja, the Templar and the Samurai."

        nova "You can choose only one.."
        nova "Who will that be?"
        menu:
            "Ninja":
                hide templar_starting
                hide samurai_starting
                show ninja_starting at fit_to_screen_height, farMidRight
                show screen base_stats(protectors_base_information['Ninja'])
                nova "Are you sure you want to choose the Ninja for your first protector?"
                menu(screen="custom_menu"):
                    "Yes!":
                        $ while_aux = 1
                        $ first_protector_selected = "Ninja"
                        nova "Great!"
                        nova "I'm adding Ninja to your list of protectors!"
                        $ firstProtector = add_new_protector("Ninja")
                        nova "Ninja added!"
                    "What were the other ones?":
                        nova "Let's recap."
            "Templar":
                hide ninja_starting
                hide samurai_starting
                show templar_starting at fit_to_screen_height, farMidRight
                show screen base_stats(protectors_base_information['Templar'])
                nova "Are you sure you want to choose the Templar for your first protector?"
                menu(screen="custom_menu"):
                    "Yes!":
                        $ while_aux = 1
                        $ first_protector_selected = "Templar"
                        nova "Great!"
                        nova "I'm adding Templar to your list of protectors!"
                        $ firstProtector = add_new_protector("Templar")
                        nova "Templar added!"
                    "What were the other ones?":
                        nova "Let's recap."
            "Samurai":
                hide ninja_starting
                hide templar_starting
                show samurai_starting at fit_to_screen_height, farMidRight
                show screen base_stats(protectors_base_information['Samurai'])
                nova "Are you sure you want to choose the Samurai for your first protector?"
                menu(screen="custom_menu"):
                    "Yes!":
                        $ while_aux = 1
                        $ first_protector_selected = "Samurai"
                        nova "Great!"
                        nova "I'm adding Samurai to your list of protectors!"
                        $ firstProtector = add_new_protector("Samurai")
                        nova "Samurai added!"
                    "What were the other ones?":
                        nova "Let's recap."

    hide templar_starting
    hide screen base_stats
    hide samurai_starting
    hide ninja_starting
    show nova at center, fit_to_screen_height
    nova "Great! Now you have your first protector!"
    nova "Now let's choose the weapon you want him to start with!"
    
    hide nova
    $ while_aux = 0
    while while_aux == 0:
        call showFirst3Weapons()
        hide screen weapon_base_stats
        nova "You can choose one of these weapons."
        nova "Maybe its a good thing you consider what might be better for your protector."
        nova "Which will you choose?"
        $ firstWeaponName = get_weapon_by_id(0).name
        $ secondWeaponName = get_weapon_by_id(1).name
        $ thirdWeaponName = get_weapon_by_id(2).name
        menu:
            "[firstWeaponName]":
                hide ironcladMace_starting
                hide elderwoodStaff_starting
                show thievesKnife_starting at fit_to_screen_height, farMidRight
                $ weapon = next(w for w in weapons if w.name == firstWeaponName)
                show screen weapon_base_stats(weapon)
                nova "Are you sure you want to choose the [firstWeaponName] for your first protector to use?"
                menu(screen="custom_menu"):
                    "Yes!":
                        $ while_aux = 1
                        nova "Great!"
                        nova "I'm adding [firstWeaponName] to your protector!"
                        $ add_new_weapon_to_our_bag(0)
                        $ firstProtector.equip_weapon(0)
                        nova "[firstWeaponName] added!"
                    "What were the other ones?":
                        nova "Let's recap."
            "[secondWeaponName]":
                hide elderwoodStaff_starting
                hide thievesKnife_starting
                show ironcladMace_starting at fit_to_screen_height, farMidRight
                $ weapon = next(w for w in weapons if w.name == secondWeaponName)
                show screen weapon_base_stats(weapon)
                nova "Are you sure you want to choose the [secondWeaponName] for your first protector to use?"
                menu(screen="custom_menu"):
                    "Yes!":
                        $ while_aux = 1
                        nova "Great!"
                        nova "I'm adding [secondWeaponName] to your protector!"
                        $ add_new_weapon_to_our_bag(1)
                        $ firstProtector.equip_weapon(1)
                        nova "[secondWeaponName] added!"
                    "What were the other ones?":
                        nova "Let's recap."
            "[thirdWeaponName]":
                hide ironcladMace_starting
                hide thievesKnife_starting
                show elderwoodStaff_starting at fit_to_screen_height, farMidRight
                $ weapon = next(w for w in weapons if w.name == thirdWeaponName)
                show screen weapon_base_stats(weapon)
                nova "Are you sure you want to choose the [thirdWeaponName] for your first protector to use?"
                menu(screen="custom_menu"):
                    "Yes!":
                        $ while_aux = 1
                        nova "Great!"
                        nova "I'm adding [thirdWeaponName] to your protector!"
                        $ add_new_weapon_to_our_bag(2)
                        $ firstProtector.equip_weapon(2)
                        nova "[thirdWeaponName] added!"
                    "What were the other ones?":
                        nova "Let's recap."

    hide ironcladMace_starting
    hide screen weapon_base_stats
    hide thievesKnife_starting
    hide elderwoodStaff_starting
    show nova at center, fit_to_screen_height
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
    $ show_things = True
    jump base_of_operations
    
    #
    # TODOS:
    # 
    # TODO:
    #   -   normal missions sould be always possible to send our protectors, at the end, it will say if it was successful or not.
    #   -   for the normal missions, or protector is not in life danger
    #   -   for the stage missions, our protector can be killed, we need to be careful
    #   -   once stage mission is completed, we can go to the next region - and everything should be the same
    # 
    # TODO: make it possible to call nova
    #
    # TODO: create the new frame for the stage 5 - as he should choose which one should he get, and depending on the one he chose, he will get some advantages
    # 
    # TODO: create a way to buy items or item drop chang? Still need to think about it
    # 
    # TODO: while we are having good results the resitance will provide some other new protectors or items (in here weapons are a possibility)
    # 
    # TODO: once the mission is finished we should show a report? saying "This missions was completed, the protector got this xp and this money"
    #   -   or if it was successful or not -> maybe also the reason?
    # 
    # TODO: in case the user is clicking the armor or weapon and protector is not available, we should send a notification saying "cannot change the equipment because protector is [status]"
    #
    # TODO: update the weapons and equipments list as I did for the protectors, so it shows the pictures
    #
    # TODO: add the description on the equipments and weapons to be out of the box.
    #
    # TODO: drops!
    #   -   Region 10 - 2 A Equipment or Weapon
    #   -   Region 9 - 1 A Equipment or Weapon
    #   -   Region 8 - 2 B Equipment or Weapon
    #   -   Region 7 - 1 B Equipment or Weapon
    #   -   Region 6 - 2 C Equipment or Weapon
    #   -   Region 5 - 1 C Equipment or Weapon
    #   -   Region 4 - 2 D Equipment or Weapon
    #   -   Region 3 - 1 D Equipment or Weapon
    #   -   Region 2 - 2 E Equipment or Weapon
    #   -   Region 1 - 1 E Equipment or Weapon
    #
    # TODO: [BUG] if ready for promotion, it allows us to change the equipment, fix it
    # 
    # TODO: make the listing, not a column only - protectors, equipments, weapons
    #   -   vbox
    #   -   -   hbox
    #   -   -   count = 1, per item, we add 1
    #   -   -   if count = 5 -> we close the hbox, and add a new hbox -> and count = 1
    #   -   -   -    I nneed to check this better, as I'm not sure how can I close hbox and open other in code..
    #
    # TODO: have images for each type of equipment
    #   -   ex:     helmet for tank, helmet for evasion, and so on
    #
    # TODO: I want to show a percentage of successfully the mission will be, and this should depend on the attributes, I can also ask chatgpt for help
    return


label showFirst3Protectors(): 
    # hiding the 3 protectors before showing
    hide templar_starting
    hide samurai_starting
    hide ninja_starting

    # showing Ninja
    image ninja_starting = getImage(f"{get_folder_from_map("Ninja")}/1")
    show ninja_starting at fit_to_screen_height, farLeft
    
    # showing Templar
    
    image templar_starting = getImage(f"{get_folder_from_map("Templar")}/1")
    show templar_starting at fit_to_screen_height, center

    # showing Samurai
    image samurai_starting = getImage(f"{get_folder_from_map("Samurai")}/1")
    show samurai_starting at fit_to_screen_height, farRight

    return

label showFirst3Weapons(): 
    # hiding the 3 protectors before showing
    hide thievesKnife_starting
    hide ironcladMace_starting
    hide elderwoodStaff_starting
    
    # showing [firstWeaponName]
    image thievesKnife_starting = getImage("images/weapons/knife")
    show thievesKnife_starting at fit_to_screen_height, farLeft

    # showing [secondWeaponName]
    image ironcladMace_starting = getImage("images/weapons/mace")
    show ironcladMace_starting at fit_to_screen_height, center
    
    # showing [thirdWeaponName]
    image elderwoodStaff_starting = getImage("images/weapons/staff")
    show elderwoodStaff_starting at fit_to_screen_height, farRight

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
