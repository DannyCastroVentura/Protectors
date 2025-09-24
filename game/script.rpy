default mc_name = "Daniel"
default show_things = False
default show_equipment = False
default current_day = 1
default online_shop_refresh_in = 7
default money = 0
default online_shop_new_protectors = True
default online_shop_new_weapons = True
default online_shop_new_equipments = True
default SClassColor = "#DC143C"
default AClassColor = "#FFD700"
default BClassColor = "#9370DB"
default CClassColor = "#1E90FF"
default DClassColor = "#32CD32"
default EClassColor = "#A9A9A9"
default black_see_through_color = "#000000f8"
default black_color = "#000000ff"

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
    $ update_menu_disable_options(True)
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
    nova "Let’s begin by finding your first ally."
    nova "The Alliance is offering you a Protectors Lucky Box!"
    nova "Open it!"
    window hide
    $ protector_name = renpy.call_screen("lucky_box_screen", "protector")
    show nova at center, fit_to_screen_height
    nova "Great! You have your first protector!"
    nova "Your first protector is: [protector_name]"
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
    # TODO: [ PRIO 1 ] also have the possibility to unequip and equip an equipment / weapon in the equipment and weapon detail
    # 
    # TODO: check the level we go to the next - because on level 80 we are already in stage 5, and stage 10 is at 180
    # 
    # TODO: on boss final expeditions, we should give the player a equipment/weapon box, depending on the rarity of the box, different drops will be achieved!
    # 
    # TODO: on completing stages rewareds:
    #   -   2 we start to get raids, every 8 to 12 days (randomly)
    #   -   3 we receive another protector lucky box - as good work rewards (only the first time)
    #   -   4 we unlock the Battles
    #   -   5 we unlock the tournament    
    #   -   -   its like battles agaisnt enemys of level > 100 , we can make like every 50 levels -> 100 / 150 / 200 / 250 / 300 and so on infinite
    #   -   6
    #   -   7
    #   -   8
    #   -   9
    #   -   10  we receive an S Weapon lucky box - as good work rewards (only the first time)
    # 
    # TODO: battles:
    #   -   the level of the enemy is random from 100 to 200
    #   -   the oponent should be random
    #   -   -   as I will leave examples for: dexterity build, strength build, speed build, tank, etc and then randomly will chose of of them and create a enemy for the battle
    #   -   the name is autogenerated
    #   -   the image will be automatically choosen - as I will leave them in specific folder to be used as examples - strength / dexterity and so on
    # 
    # TODO: [ PRIO 1 ] update the names for evolutions and descriptions for the other characters (even create the other characters)
    #   -   skeleton - dexterity based
    #   -   priest - this will use miracles
    #   -   lawyer - this will be good for charisma and political missions
    # 
    # TODO: the finish expedition is finishing the wrong one OR when we are assigning a mission, we are assigning it to the wrong one. - after I added the number in the name, never got this error again - once I deleted the renpy.notify , the issue started again - let's add it again?
    # 
    # TODO: test all the bosses
    # 
    # TODO: also make an option to send the protectors to help the organization
    #   -   this would make us earn weekly money
    #   -   and they would also win xp (not much)
    # 
    # TODO: create the screen for the time based combat
    #   -   what to show in the report?
    #   -   -   what equipments we also got - in case of victory
    #   -   -   -   final boss drops!
    #   -   -   -   -   Region 10 - 2 A Equipment or Weapon
    #   -   -   -   -   Region 9 - 1 A Equipment or Weapon
    #   -   -   -   -   Region 8 - 2 B Equipment or Weapon
    #   -   -   -   -   Region 7 - 1 B Equipment or Weapon
    #   -   -   -   -   Region 6 - 2 C Equipment or Weapon
    #   -   -   -   -   Region 5 - 1 C Equipment or Weapon
    #   -   -   -   -   Region 4 - 2 D Equipment or Weapon
    #   -   -   -   -   Region 3 - 1 D Equipment or Weapon
    #   -   -   -   -   Region 2 - 2 E Equipment or Weapon
    #   -   -   -   -   Region 1 - 1 E Equipment or Weapon
    #   -   once the stage 1 is killed:
    #   -   -   unlock battles
    #
    # TODO: Improve the fight experience
    #   -   add the option for spell
    # 
    # TODO: [ PRIO 1 ] ADD DROP CHANCE FOR BATTLES AND EXPEDITIONS
    #   -   item drop chance
    #   -   -   at the end of each expedition mission, we should have a percentage of item drop -> 5% + luck attributes
    #   -   -   depending on the difficulty of the mission, this change get's ligther -> we should divide the total chance by the number per each rank of the equipment/weapon
    #
    # TODO: [ PRIO 1 ] test all the protectors 
    # 
    # TODO: [ PRIO 3 ] add a way to see the statistics for this protector ( maybe I can add a link to the name of the protector, and when clicked, it shows the statistics )
    #   -   for now the statistics are expeditions_succeeded / expeditions_failed / expeditions_went -> I can also create a bar
    #   -   in case a evolution was already specified, we can also show the description once again
    # 
    # TODO: [ PRIO 4 ] as we are having good results the resitance will provide some other new protectors or items (in here weapons are a possibility)
    # 
    # TODO: [ IDEA ] another idea, maybe we could even get other forces, not protectors, but some army guys, which we could send on different expeditions?
    # 
    # TODO: [ IDEA ] each one of the protectors should have a unique passive
    #   -   ideas:
    #   -   -   increase 10% gold from expeditions
    #   -   -   increase 10% luck on expeditions
    #   -   -   increase 10% xp
    #   -   -   increase 10% more damage
    #   -   -   and so on and so forth
    # 
    return


label showFirst3Protectors(): 
    # hiding the 3 protectors before showing
    hide templar_starting
    hide wizard_starting
    hide ninja_starting

    # showing Ninja
    image ninja_starting = getImage(f"{get_folder_from_map("Ninja")}/1")
    show ninja_starting at fit_to_screen_height, farLeft
    
    # showing Templar
    
    image templar_starting = getImage(f"{get_folder_from_map("Templar")}/1")
    show templar_starting at fit_to_screen_height, center

    # showing wizard
    image wizard_starting = getImage(f"{get_folder_from_map("Wizard")}/1")
    show wizard_starting at fit_to_screen_height, farRight

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
    hide nova
    show nova at fit_to_screen_height, right
    nova "Here we are!"
    nova "You can use your base of operations to: \n- Check your expeditions list \n- Train you protectors\n- Rest area"
    nova "Check your expeditions list: \nIn here you can see what expeditions you have received."
    nova "Check your expeditions list: \nNote that there will be some expeditions very hard to handle - I recommend to start with the basic ones first!"
    nova "Check your expeditions list: \nIf the mission is to difficult for the experience of the protector, he might be unable from escape - and if this happens, he'll die and you'll lose this protector."
    nova "Check your expeditions list: \nIf all of your protectors die - you'll lose the game."
    nova "Check your expeditions list: \nBe careful when assinging protectors to expeditions."

    $ set_background("training-ground")
    hide nova
    show nova at fit_to_screen_height, right
    nova "Training ground: \nThis is the a place we have built for helping you make new protectors stronger."
    nova "Training ground: \nTraining ground should be very helpful for inexperienced protectors."
    nova "Training ground: \nBut as they become stronger - the training ground start to be less effective."
    
    $ set_background("resting-area")
    hide nova
    show nova at fit_to_screen_height, right
    nova "Resting area: \nYou can also go to the bedrooms to rest!"
    nova "Resting area: \nResting is very important, as your protectors also need to recover when they are back from their expeditions."
    nova "Resting area: \nResting is also very helpful when you need to advance the time."
    nova "Resting area: \nAdvancing time can be helpful for a lot of things, including - to get new expeditions."
    nova "Resting area: \nNew expeditions appear every day, but be careful! Old expeditions might disapear when you rest."
    nova "Resting area: \nEvery mission have a time to be started. If a mission was not yet initiated and this time finished, then this mission is closed as ignored."
    return

label get_help_from_nova():
    hide nova
    show nova at center, fit_to_screen_height
    call nova_explains_tutorial()
    hide nova
    show nova at center, fit_to_screen_height
    nova "Hope you understood everything!"
    nova "If not, just ask me again!"
    nova "Bye bye!"
    jump base_of_operations

label show_my_available_protectors(isThisExpedition):
    call screen protector_selection(isThisExpedition)
    return
