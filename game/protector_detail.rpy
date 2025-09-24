  
screen protector_detail_screen(my_protector):
    $ scale = 125
    $ action_button = None
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)

        fixed:
            xfill True
            yfill True

            # Adding protector image
            python:
                image_name = my_protector.stage
                if my_protector.stage >= 5:
                    image_name = str(my_protector.stage) + "_" + str(my_protector.chosen_evolution)
                image_path = getImage(str(get_folder_from_map(my_protector.name)) + '/' + str(image_name))
                if image_path:
                    ui.at(center)
                    ui.at(fit_to_screen_height)
                    ui.add(image_path)

            # Close button - top right
            textbutton "Back" action Hide("protector_detail_screen"):
                text_style "hover_white"
                xalign 1.0
                yalign 0.0
                padding (10, 5)
            
            vbox:
                yalign 0.05
                xalign 0.5
                
                if my_protector.chosen_evolution != 0:
                    $ evolution_name = my_protector.basePoints.evolution_name_1
                    if my_protector.chosen_evolution == 2:
                        $ evolution_name = my_protector.basePoints.evolution_name_2
                    text "[evolution_name] ([my_protector.status])" size 50 color "#FFF" xalign 0.5
                    
                else:
                    text "[my_protector.name] ([my_protector.status])" size 50 color "#FFF" xalign 0.5
                
                if my_protector.status != "Available" and my_protector.status != "To sell":
                    $ day_or_days = "day"
                    if my_protector.not_available_counter > 1:
                        $ day_or_days = "days"
                    text "Away for [my_protector.not_available_counter] [day_or_days]." size 25 color "#FFF" xalign 0.5

            hbox:
                xalign 0.5
                yalign 0.95
                spacing 20
                text "Level: [my_protector.level]" size 25 color "#DDD"
                text "Stage: [my_protector.stage]" size 25 color "#DDD"
                    
            # Text block - vertically centered on left side
            vbox:
                spacing 20
                xalign 0.0000000000001
                yalign 0.5
                xmaximum 500
                xfill True
                hbox:
                    xalign 0.5
                    spacing 20
                    $ empty_scaled = im.Scale("images/background_item.png", scale, scale)
                    if my_protector.equipedWeapon == None:
                        $ weapon_img = "images/weapons/default_weapon.png"

                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(weapon_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ weapon_scaled = im.Scale(weapon_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Show("weapon_select", None, my_protector)
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")
                        
                        if my_protector.basePoints.can_it_use_weapons == True:
                            $ action_button = Show("weapon_select", None, my_protector)
                        else: 
                            $ action_button = Function(send_custom_notification, my_protector.name + " cannot equip weapons.")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background "#ffffff"
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_scaled,
                                    ((scale - new_width) // 2, 0), weapon_scaled   
                                )
                    else:
                        $ weapon_img = "images/weapons/{}.png".format(my_protector.equipedWeapon.class_name)
                        $ background_color_style = EClassColor
                        if my_protector.equipedWeapon.rarity == "D":
                            $ background_color_style = DClassColor
                        if my_protector.equipedWeapon.rarity == "C":
                            $ background_color_style = CClassColor
                        if my_protector.equipedWeapon.rarity == "B":
                            $ background_color_style = BClassColor
                        if my_protector.equipedWeapon.rarity == "A":
                            $ background_color_style = AClassColor
                        if my_protector.equipedWeapon.rarity == "S":
                            $ background_color_style = SClassColor
                            
                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(weapon_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ weapon_scaled = im.Scale(weapon_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Show("protector_detail_weapon_click", None, my_protector)
                            
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background background_color_style
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_scaled,
                                    ((scale - new_width) // 2, 0), weapon_scaled   
                                )


                    
                    $ helmet_img = "images/equipments/no_helmet.png"
                    $ empty_helmet_scaled = im.Scale("images/background_item.png", scale, scale)
                    
                    $ body_img = "images/equipments/no_body.png"
                    $ empty_body_scaled = im.Scale("images/background_item.png", scale, scale)
                    
                    $ pants_img = "images/equipments/no_pants.png"
                    $ empty_pants_scaled = im.Scale("images/background_item.png", scale, scale)
                    
                    $ boots_img = "images/equipments/no_boots.png"
                    $ empty_boots_scaled = im.Scale("images/background_item.png", scale, scale)
                        

                    if my_protector.equipedHelmet == None:
                        $ helmet_img = "images/equipments/no_helmet.png"

                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(helmet_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ helmet_scaled = im.Scale(helmet_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Show("equipment_select", None, my_protector, "helmet")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background "#ffffff"
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_scaled,
                                    ((scale - new_width) // 2, 0), helmet_scaled
                                )
                    else:
                        $ helmet_img = "images/equipments/{}_{}.png".format(my_protector.equipedHelmet.class_name, my_protector.equipedHelmet.type)
                        $ helmet_scaled = im.Scale(helmet_img, 200, 200)
                        $ background_color_style = EClassColor
                        if my_protector.equipedHelmet.rarity == "D":
                            $ background_color_style = DClassColor
                        elif my_protector.equipedHelmet.rarity == "C":
                            $ background_color_style = CClassColor
                        elif my_protector.equipedHelmet.rarity == "B":
                            $ background_color_style = BClassColor
                        elif my_protector.equipedHelmet.rarity == "A":
                            $ background_color_style = AClassColor
                        elif my_protector.equipedHelmet.rarity == "S":
                            $ background_color_style = SClassColor
                        
                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(helmet_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ helmet_scaled = im.Scale(helmet_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Show("protector_detail_equipment_click", None, my_protector, "Helmet")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background background_color_style
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_scaled,
                                    ((scale - new_width) // 2, 0), helmet_scaled
                                )
                    if my_protector.equipedBodyArmor == None:
                        $ body_img = "images/equipments/no_body.png"

                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(body_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ body_scaled = im.Scale(body_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Show("equipment_select", None, my_protector, "body")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background "#ffffff"
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_body_scaled,
                                    ((scale - new_width) // 2, 0), body_scaled
                                )
                    else:
                        $ body_img = "images/equipments/{}_{}.png".format(my_protector.equipedBodyArmor.class_name, my_protector.equipedBodyArmor.type)
                        $ body_scaled = im.Scale(body_img, 200, 200)
                        $ background_color_style = EClassColor
                        if my_protector.equipedBodyArmor.rarity == "D":
                            $ background_color_style = DClassColor
                        if my_protector.equipedBodyArmor.rarity == "C":
                            $ background_color_style = CClassColor
                        if my_protector.equipedBodyArmor.rarity == "B":
                            $ background_color_style = BClassColor
                        if my_protector.equipedBodyArmor.rarity == "A":
                            $ background_color_style = AClassColor
                        if my_protector.equipedBodyArmor.rarity == "S":
                            $ background_color_style = SClassColor
                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(body_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ body_scaled = im.Scale(body_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Show("protector_detail_equipment_click", None, my_protector, "Body")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background background_color_style
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_body_scaled,
                                    ((scale - new_width) // 2, 0), body_scaled
                                )
                
                hbox:
                    xalign 0.5
                    spacing 20
                    if my_protector.equipedPants == None:
                        $ pants_img = "images/equipments/no_pants.png"

                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(pants_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ pants_scaled = im.Scale(pants_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Show("equipment_select", None, my_protector, "pants")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background "#ffffff"
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_pants_scaled,
                                    ((scale - new_width) // 2, 0), pants_scaled
                                )
                    else:
                        $ pants_img = "images/equipments/{}_{}.png".format(my_protector.equipedPants.class_name, my_protector.equipedPants.type)
                        $ pants_scaled = im.Scale(pants_img, 200, 200)
                        $ background_color_style = EClassColor
                        if my_protector.equipedPants.rarity == "D":
                            $ background_color_style = DClassColor
                        if my_protector.equipedPants.rarity == "C":
                            $ background_color_style = CClassColor
                        if my_protector.equipedPants.rarity == "B":
                            $ background_color_style = BClassColor
                        if my_protector.equipedPants.rarity == "A":
                            $ background_color_style = AClassColor
                        if my_protector.equipedPants.rarity == "S":
                            $ background_color_style = SClassColor
                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(pants_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ pants_scaled = im.Scale(pants_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Show("protector_detail_equipment_click", None, my_protector, "Pants")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background background_color_style
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_pants_scaled,
                                    ((scale - new_width) // 2, 0), pants_scaled
                                )

                    if my_protector.equipedBoots == None:
                        $ boots_img = "images/equipments/no_boots.png"

                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(boots_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ boots_scaled = im.Scale(boots_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Show("equipment_select", None, my_protector, "boots")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background "#ffffff"
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_boots_scaled,
                                    ((scale - new_width) // 2, 0), boots_scaled
                                )
                    else:
                        $ boots_img = "images/equipments/{}_{}.png".format(my_protector.equipedBoots.class_name, my_protector.equipedBoots.type)
                        $ boots_scaled = im.Scale(boots_img, 200, 200)
                        $ background_color_style = EClassColor
                        if my_protector.equipedBoots.rarity == "D":
                            $ background_color_style = DClassColor
                        if my_protector.equipedBoots.rarity == "C":
                            $ background_color_style = CClassColor
                        if my_protector.equipedBoots.rarity == "B":
                            $ background_color_style = BClassColor
                        if my_protector.equipedBoots.rarity == "A":
                            $ background_color_style = AClassColor
                        if my_protector.equipedBoots.rarity == "S":
                            $ background_color_style = SClassColor
                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(boots_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ boots_scaled = im.Scale(boots_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Show("protector_detail_equipment_click", None, my_protector, "Boots")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background background_color_style
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_boots_scaled,
                                    ((scale - new_width) // 2, 0), boots_scaled
                                )
                
                # Text block - vertically centered on left side
                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5
                    null height 10  # This adds 40 pixels of vertical space at the top
                    $ current_status = my_protector.get_current_stats()
                    hbox:
                        xalign 0.5
                        spacing 20
                        xfill True
                        vbox:
                            xalign 0.3
                            text "Strength:" size 22 color "#EEE" xalign 0.0000001
                            text "Dexterity:" size 22 color "#EEE" xalign 0.0000001
                            text "Constitution:" size 22 color "#EEE" xalign 0.0000001
                            text "Intelligence:" size 22 color "#EEE" xalign 0.0000001
                            text "Wisdom:" size 22 color "#EEE" xalign 0.0000001
                            text "Charisma:" size 22 color "#EEE" xalign 0.0000001
                            text "Speed:" size 22 color "#EEE" xalign 0.0000001
                            text "Luck:" size 22 color "#EEE" xalign 0.0000001
                        vbox:
                            xalign 0.7
                            text "[str(current_status['strength'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['dexterity'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['constitution'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['intelligence'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['wisdom'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['charisma'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['speed'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['luck'])]" size 22 color "#EEE" xalign 0.9999


                if my_protector.basePoints.can_it_use_weapons == True:
                    $ possible_weapons = my_protector.basePoints.usable_weapon_types
                    if my_protector.chosen_evolution == 1:
                        $ possible_weapons = my_protector.basePoints.usable_weapon_types_evolution_1
                    elif my_protector.chosen_evolution == 2:
                        $ possible_weapons = my_protector.basePoints.usable_weapon_types_evolution_2
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 20
                        null height 10  # This adds 40 pixels of vertical space at the top
                        text "Usable weapon types:" size 23 color "#EEE" xalign 0.5
                        for i in range(0, len(possible_weapons), 4):
                            hbox:
                                xalign 0.5
                                spacing 20
                                for weapon_type in possible_weapons[i:i+4]:
                                    text "[weapon_type]" size 22 color "#EEE" xalign 0.5

                
                $ range_for_the_moment = my_protector.basePoints.unarmed_range
                if my_protector.chosen_evolution == 1:
                    $ range_for_the_moment = my_protector.basePoints.unarmed_range_evo_1
                elif my_protector.chosen_evolution == 2:
                    $ range_for_the_moment = my_protector.basePoints.unarmed_range_evo_2
                
                if my_protector.equipedWeapon != None:
                    $ range_for_the_moment = my_protector.equipedWeapon.range
                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 20
                    null height 10  # This adds 40 pixels of vertical space at the top
                    hbox:
                        xalign 0.5
                        spacing 20
                        text "Atack range:" size 23 color "#EEE" xalign 0.5
                        text range_for_the_moment size 23 color "#EEE" xalign 0.5
            vbox:
                spacing 20
                xalign 0.99999999999
                yalign 0.5
                xmaximum 500
                xfill True
                vbox:
                    xalign 0.5
                    spacing 20
                    bar value my_protector.hp range my_protector.get_health_points() style "hp_bar"
                    text "[my_protector.hp] / [my_protector.get_health_points()]" size 20 color "#DDD" xalign 1.0
                    bar value my_protector.get_mana_points() range my_protector.get_mana_points() style "mana_bar"
                    text "[my_protector.get_mana_points()] / [my_protector.get_mana_points()]" size 20 color "#DDD" xalign 1.0
                    bar value my_protector.xp range my_protector.get_amount_of_xp_needed_for_leveling_up() style "xp_bar"
                    text "[my_protector.xp] / [my_protector.get_amount_of_xp_needed_for_leveling_up()]" size 20 color "#DDD" xalign 1.0
                    null height 10  # This adds 40 pixels of vertical space at the top

                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5
                    null height 10  # This adds 40 pixels of vertical space at the top
                    hbox:
                        xalign 0.5
                        spacing 20
                        xfill True
                        vbox:
                            xalign 0.3
                            text "Attack speed:" size 22 color "#EEE" xalign 0.0000001
                            text "Defense:" size 22 color "#EEE" xalign 0.0000001
                            text "Evasion:" size 22 color "#EEE" xalign 0.0000001
                            text "Morality:" size 22 color "#EEE" xalign 0.0000001
                            text "Cooldown reduction:" size 22 color "#EEE" xalign 0.0000001
                            text "Critical Damage:" size 22 color "#EEE" xalign 0.0000001
                            text "Critical chance:" size 22 color "#EEE" xalign 0.0000001
                        vbox:
                            xalign 0.7
                            text "[str(round(current_status['attack_speed'], 2))] a/s" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['defense'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['evasion'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['morality'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['cooldown_reduction'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(round(current_status['critical_damage'] * 100, 2))] %" size 22 color "#EEE" xalign 0.9999
                            text "[str(round(current_status['critical_chance'] * 100, 2))] %" size 22 color "#EEE" xalign 0.9999
                vbox:
                    xalign 0.5
                    spacing 70
                    null height 10  # This adds 40 pixels of vertical space at the top
                    hbox:
                        xalign 0.5
                        spacing 25
                        vbox:
                            xalign 0.5
                            text "Real Damage:" size 30 color "#EEE"
                        vbox:
                            xalign 0.5
                            text "[str(my_protector.get_damage_points())]" size 30 color "#EEE"
                    hbox:
                        xalign 0.5
                        spacing 25
                        vbox:
                            xalign 0.5
                            text "Damage Type:" size 30 color "#EEE"
                        vbox:
                            xalign 0.5
                            text "[str(my_protector.get_damage_type())]" size 30 color "#EEE"

            if my_protector.readyForPromotion == True and my_protector.status == "Available":

                vbox:
                    xalign 0.5
                    yalign 0.8
                    text "Do you want to promote [my_protector.name]?" size 30 color "#FFF" xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 150
                        vbox:
                            xalign 0.5
                            $ action_button = Function(my_protector.promote)
                            if my_protector.stage == 4:
                                $ action_button = Show("protector_evolution_choosing_screen", None, my_protector) 
                            textbutton "Yes" action action_button:
                                text_size 25
                                text_style "button_in_black_background"

                        vbox:
                            xalign 0.5
                            textbutton "No" action Hide("protector_detail_screen"):
                                text_size 25
                                text_style "button_in_black_background"



screen protector_detail_weapon_click(my_protector):

    tag menu  # so the player can't open other menus while this is open

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20

        vbox:
            spacing 10
            xalign 0.5
            text "Menu" size 30 xalign 0.5
            textbutton "More information":
                action [Show("equipment_detail_screen", None, "w", my_protector.equipedWeapon), Hide("protector_detail_weapon_click")]
                ypadding 10
                xalign 0.5
                
            textbutton "Unequip":
                action [Function(my_protector.unequip_weapon), Hide("protector_detail_weapon_click")]
                ypadding 10
                xalign 0.5

            textbutton "Cancel":
                action Hide("protector_detail_weapon_click")
                xalign 0.5
                ypadding 10

screen protector_detail_equipment_click(my_protector, equipment_type):

    
    $ equipment = my_protector.equipedHelmet
    if equipment_type == "Body":
        $ equipment = my_protector.equipedBodyArmor
    elif equipment_type == "Pants":
        $ equipment = my_protector.equipedPants
    if equipment_type == "Boots":
        $ equipment = my_protector.equipedBoots

    tag menu  # so the player can't open other menus while this is open

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20

        vbox:
            spacing 10
            xalign 0.5
            text "Menu" size 30 xalign 0.5
            textbutton "More information":
                action [Show("equipment_detail_screen", None, "e", equipment), Hide("protector_detail_equipment_click")]
                ypadding 10
                xalign 0.5
                
            textbutton "Unequip":
                action [Function(my_protector.unequip_equipment, equipment.type), Hide("protector_detail_equipment_click")]
                ypadding 10
                xalign 0.5

            textbutton "Cancel":
                action Hide("protector_detail_equipment_click")
                xalign 0.5
                ypadding 10


screen weapon_select(protector):

    tag menu  # so the player can't open other menus while this is open

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20

        vbox:
            spacing 10
            xalign 0.5
            text "Select your weapon:" size 30 xalign 0.5

            # For each available weapon, create a button
            $ filtered_weapons = sorted(
                [weapon for weapon in myWeapons if weapon.class_name in protector.basePoints.usable_weapon_types],
                key=lambda weapon: (weapon.rarity, weapon.name.lower())
            )
            for weapon in filtered_weapons:
                textbutton "[weapon.name] - [weapon.type] ([weapon.rarity])":
                    action [Function(protector.equip_weapon, weapon.weapon_id), Hide("weapon_select")]
                    ypadding 10
                    xalign 0.5

            textbutton "Cancel":
                action Hide("weapon_select")
                xalign 0.5
                ypadding 10


screen equipment_select(protector, equipment_type):

    tag menu  # so the player can't open other menus while this is open

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20

        vbox:
            spacing 10
            xalign 0.5

            text "Select your equipment:" size 30 xalign 0.5

            # For each available weapon, create a button
            $ filtered_equipments = sorted(
                [equipment for equipment in myEquipments if equipment.type == equipment_type],
                key=lambda equipment: (equipment.rarity, equipment.name.lower())
            )

            for equipment in filtered_equipments:
                textbutton "[equipment.name] - [equipment.class_name] ([equipment.rarity])":
                    action [Function(protector.equip_equipment, equipment.equipment_id), Hide("equipment_select")]
                    xalign 0.5
                    ypadding 10

            textbutton "Cancel":
                action Hide("equipment_select")
                ypadding 10
                xalign 0.5
