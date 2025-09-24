
screen online_shop():
    
    # # Check if I already have the protector
    # #   -   if so, then it should not be available anymore
    $ online_shop_variable.checkIfProtectorStillAvailable()

    default selling_or_buying = None
    default online_shop_show = "main_menu"
    default rarity_selected = "S"
    $ online_shop_color = "#FFF"
    $ title_size = 60
    $ tittle_v_align = 0.1
    if online_shop_show != "main_menu":
        $ title_size = 40
        $ tittle_v_align = 0.01

    $ text_style_back_button = "rarity_navegation_text_online_shop"
    $ main_options_scale = 350
    $ items_scale = 400
    $ main_buttons_background = im.Scale("images/background_item.png", main_options_scale, main_options_scale)
    $ empty_scaled = im.Scale("images/background_item.png", items_scale, items_scale)
    frame:
        background Solid("#1a1a1a")
        fixed:
            xfill True
            yfill True
        xalign 0.5
        yalign 0.5
        xsize 1700
        
        ysize 925
        padding (20, 20)
        vbox:
            spacing 10
            xalign 1.0
            yalign 0                
            vbox:
                text "Next refresh: " + str(online_shop_refresh_in) + "d" size 20 color online_shop_color
        vbox:
            spacing 10
            xalign 0.5
            yalign tittle_v_align
            vbox:
                xalign 0.5
                if selling_or_buying == None:
                    vbox:
                        xalign 0.5
                        text "Online Shop" size title_size color online_shop_color
                elif selling_or_buying == "buying":
                    vbox:
                        xalign 0.5
                        text "Online Shop > Buy" size title_size color online_shop_color
                elif selling_or_buying == "selling":
                    vbox:
                        xalign 0.5
                        text "Online Shop > Sell" size title_size color online_shop_color

        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            if selling_or_buying == None:
                hbox:
                    spacing 50
                    xalign 0.5
                    yalign 0.5
                    $ show_buy_image = "images/menu/buy.png"
                    $ show_buy_scaled = im.Scale(show_buy_image, main_options_scale, main_options_scale)

                    fixed: 
                        xmaximum main_options_scale
                        ymaximum main_options_scale
                        button:
                            action SetScreenVariable("selling_or_buying", "buying")
                            style "option_button_online_shop"
                            frame:
                                add im.Composite(
                                    (main_options_scale, main_options_scale),
                                    (0, 0), main_buttons_background,
                                    (0, 0), show_buy_scaled
                                )
                        if online_shop_new_protectors == True or online_shop_new_equipments == True or online_shop_new_weapons == True:
                            frame:
                                background "#fff"  # white background
                                padding (5, 2)    # space around the "!"
                                xalign 1.0
                                yalign 0.0
                                text "!" size 30 color "#f00" bold True

                    $ show_sell_image = "images/menu/sell.png"
                    $ show_sell_scaled = im.Scale(show_sell_image, main_options_scale, main_options_scale)
                        
                    fixed: 
                        xmaximum main_options_scale
                        ymaximum main_options_scale
                        button:
                            action SetScreenVariable("selling_or_buying", "selling")
                            style "option_button_online_shop"
                            frame:
                                add im.Composite(
                                    (main_options_scale, main_options_scale),
                                    (0, 0), main_buttons_background,
                                    (0, 0), show_sell_scaled
                                )

            elif selling_or_buying == "buying":
                if online_shop_show == "main_menu":
                    hbox:
                        spacing 50
                        xalign 0.5
                        yalign 0.5
                        $ show_protectors_image = "images/menu/protectors.png"
                        $ show_protectors_scaled = im.Scale(show_protectors_image, main_options_scale, main_options_scale)
                            
                        fixed: 
                            xmaximum main_options_scale
                            ymaximum main_options_scale
                            button:
                                action [SetScreenVariable("online_shop_show", "show_protectors"), SetVariable("online_shop_new_protectors", False) ]
                                style "option_button_online_shop"
                                frame:
                                    add im.Composite(
                                        (main_options_scale, main_options_scale),
                                        (0, 0), main_buttons_background,
                                        (0, 0), show_protectors_scaled
                                    )
                            if online_shop_new_protectors == True:
                                frame:
                                    background "#fff"  # white background
                                    padding (5, 2)    # space around the "!"
                                    xalign 1.0
                                    yalign 0.0
                                    text "!" size 30 color "#f00" bold True

                        
                        $ show_weapons_image = "images/menu/weapons.png"
                        $ show_weapons_scaled = im.Scale(show_weapons_image, main_options_scale, main_options_scale)
                        
                        fixed: 
                            xmaximum main_options_scale
                            ymaximum main_options_scale
                            button:
                                action [SetScreenVariable("online_shop_show", "show_weapons"), SetVariable("online_shop_new_weapons", False)]
                                style "option_button_online_shop"
                                frame:
                                    add im.Composite(
                                        (main_options_scale, main_options_scale),
                                        (0, 0), main_buttons_background,
                                        (0, 0), show_weapons_scaled
                                    )
                            if online_shop_new_weapons == True:
                                frame:
                                    background "#fff"  # white background
                                    padding (5, 2)    # space around the "!"
                                    xalign 1.0
                                    yalign 0.0
                                    text "!" size 30 color "#f00" bold True
                                

                        $ show_equipment_image = "images/menu/equipments.png"
                        $ show_equipment_scaled = im.Scale(show_equipment_image, main_options_scale, main_options_scale)
                            
                        fixed: 
                            xmaximum main_options_scale
                            ymaximum main_options_scale
                            button:
                                action [SetScreenVariable("online_shop_show", "show_equipments"), SetVariable("online_shop_new_equipments", False)]
                                style "option_button_online_shop"
                                frame:
                                    add im.Composite(
                                        (main_options_scale, main_options_scale),
                                        (0, 0), main_buttons_background,
                                        (0, 0), show_equipment_scaled
                                    )
                            if online_shop_new_equipments == True:
                                frame:
                                    background "#fff"  # white background
                                    padding (5, 2)    # space around the "!"
                                    xalign 1.0
                                    yalign 0.0
                                    text "!" size 30 color "#f00" bold True

                if online_shop_show == "show_equipments":
                    
                    hbox:
                        spacing 50
                        xalign 0.5
                        yalign 0.5
                        for rarity, equipments in online_shop_variable.selling_equipments_list.items():
                            if rarity == rarity_selected:
                                for equipment in equipments:
                                    $ my_color = EClassColor
                                    $ rarity = equipment.rarity
                                    if equipment.rarity == "D":
                                        $ my_color = DClassColor
                                    if equipment.rarity == "C":
                                        $ my_color = CClassColor
                                    if equipment.rarity == "B":
                                        $ my_color = BClassColor
                                    if equipment.rarity == "A":
                                        $ my_color = AClassColor
                                    if equipment.rarity == "S":
                                        $ my_color = SClassColor
                                    
                                    $ equipment_img = "images/equipments/{}_{}.png".format(equipment.class_name, equipment.type)

                                    # Get original image size
                                    $ orig_width, orig_height = renpy.image_size(equipment_img)

                                    # Calculate proportional width
                                    $ new_width = int(orig_width * (items_scale / float(orig_height)))

                                    # Scale the image
                                    $ equipment_scaled = im.Scale(equipment_img, new_width, items_scale)

                                    $ button_action = Show("equipment_detail_screen", None, "e", equipment)
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        spacing 20
                                        vbox:
                                            xalign 0.5
                                            xminimum 700
                                            xmaximum 700
                                            vbox:
                                                xalign 0.5
                                                button:
                                                    action button_action
                                                    style "option_button_online_shop"
                                                    xpadding 4
                                                    ypadding 4
                                                    frame:                                            
                                                        background my_color
                                                        xalign 0.5 
                                                        add im.Composite(
                                                            (items_scale, items_scale),
                                                            (0, 0), empty_scaled,
                                                            ((items_scale - new_width) // 2, 0), equipment_scaled   
                                                        )

                                        text str(equipment.name) xalign 0.5 color online_shop_color

                                        text str(equipment.price) + " $" xalign 0.5 color online_shop_color

                                        $ online_shop_action = Function(notify_user_money_is_not_enough, equipment.name)
                                        if money >= equipment.price:
                                            $ online_shop_action = Function(buy_new_equipment, equipment)

                                        if equipment.stillAvailable:
                                            button:
                                                style "option_button_online_shop"
                                                xfill True
                                                xmaximum 500
                                                xalign 0.5
                                                frame:
                                                    xfill True
                                                    background "#444"
                                                    padding (10, 10)
                                                    vbox:
                                                        spacing 5
                                                        xalign 0.5
                                                        text "Buy" size 24 color "#fff" xalign 0.5
                                                action online_shop_action
                                        
                    hbox:
                        spacing 10
                        xalign 0.5
                        yalign 0.5
                        $ text_style_S = "rarity_navegation_text_online_shop"
                        $ text_style_A = "rarity_navegation_text_online_shop"
                        $ text_style_B = "rarity_navegation_text_online_shop"
                        $ text_style_C = "rarity_navegation_text_online_shop"
                        $ text_style_D = "rarity_navegation_text_online_shop"
                        $ text_style_E = "rarity_navegation_text_online_shop"
                        
                        if rarity_selected == "S": 
                            $ text_style_S = "rarity_navegation_text_online_shop_active"
                        elif rarity_selected == "A": 
                            $ text_style_A = "rarity_navegation_text_online_shop_active"
                        elif rarity_selected == "B": 
                            $ text_style_B = "rarity_navegation_text_online_shop_active"
                        elif rarity_selected == "C": 
                            $ text_style_C = "rarity_navegation_text_online_shop_active"
                        elif rarity_selected == "D": 
                            $ text_style_D = "rarity_navegation_text_online_shop_active"
                        elif rarity_selected == "E": 
                            $ text_style_E = "rarity_navegation_text_online_shop_active"
                        textbutton "S" action SetScreenVariable("rarity_selected", "S") yalign 0.9 xalign 0.5 text_style text_style_S
                        text "|"
                        textbutton "A" action SetScreenVariable("rarity_selected", "A") yalign 0.9 xalign 0.5 text_style text_style_A
                        text "|"
                        textbutton "B" action SetScreenVariable("rarity_selected", "B") yalign 0.9 xalign 0.5 text_style text_style_B
                        text "|"
                        textbutton "C" action SetScreenVariable("rarity_selected", "C") yalign 0.9 xalign 0.5 text_style text_style_C
                        text "|"
                        textbutton "D" action SetScreenVariable("rarity_selected", "D") yalign 0.9 xalign 0.5 text_style text_style_D
                        text "|"
                        textbutton "E" action SetScreenVariable("rarity_selected", "E") yalign 0.9 xalign 0.5 text_style text_style_E
                    textbutton "Back" action [SetScreenVariable("online_shop_show", "main_menu"), SetScreenVariable("rarity_selected", "S")] yalign 0.9 xalign 0.5 text_style text_style_back_button

                if online_shop_show == "show_weapons":

                    hbox:
                        spacing 50
                        xalign 0.5
                        yalign 0.5
                        for rarity, weapons in online_shop_variable.selling_weapons_list.items():
                            if rarity == rarity_selected:
                                for weapon in weapons:
                                    $ my_color = EClassColor
                                    $ rarity = weapon.rarity
                                    if weapon.rarity == "D":
                                        $ my_color = DClassColor
                                    if weapon.rarity == "C":
                                        $ my_color = CClassColor
                                    if weapon.rarity == "B":
                                        $ my_color = BClassColor
                                    if weapon.rarity == "A":
                                        $ my_color = AClassColor
                                    if weapon.rarity == "S":
                                        $ my_color = SClassColor
                                    
                                    $ weapon_img = "images/weapons/{}.png".format(weapon.class_name)

                                    # Get original image size
                                    $ orig_width, orig_height = renpy.image_size(weapon_img)

                                    # Calculate proportional width
                                    $ new_width = int(orig_width * (items_scale / float(orig_height)))

                                    # Scale the image
                                    $ weapon_scaled = im.Scale(weapon_img, new_width, items_scale)

                                    $ button_action = Show("equipment_detail_screen", None, "w", weapon)
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        spacing 20
                                        vbox:
                                            xalign 0.5
                                            xminimum 700
                                            xmaximum 700
                                            vbox:
                                                xalign 0.5
                                                button:
                                                    action button_action
                                                    style "option_button_online_shop"
                                                    xpadding 4
                                                    ypadding 4
                                                    frame:                                            
                                                        background my_color
                                                        xalign 0.5 
                                                        add im.Composite(
                                                            (items_scale, items_scale),
                                                            (0, 0), empty_scaled,
                                                            ((items_scale - new_width) // 2, 0), weapon_scaled   
                                                        )

                                        text str(weapon.name) xalign 0.5 color online_shop_color

                                        text str(weapon.price) + " $" xalign 0.5 color online_shop_color

                                        $ online_shop_action = Function(notify_user_money_is_not_enough, weapon.name)
                                        if money >= weapon.price:
                                            $ online_shop_action = Function(buy_new_weapon, weapon)

                                        if weapon.stillAvailable:
                                            button:
                                                style "option_button_online_shop"
                                                xfill True
                                                xmaximum 500
                                                xalign 0.5
                                                frame:
                                                    xfill True
                                                    background "#444"
                                                    padding (10, 10)
                                                    vbox:
                                                        spacing 5
                                                        xalign 0.5
                                                        text "Buy" size 24 color "#fff" xalign 0.5
                                                action online_shop_action
                    hbox:
                        spacing 10
                        xalign 0.5
                        yalign 0.5
                        $ text_style_S = "rarity_navegation_text_online_shop"
                        $ text_style_A = "rarity_navegation_text_online_shop"
                        $ text_style_B = "rarity_navegation_text_online_shop"
                        $ text_style_C = "rarity_navegation_text_online_shop"
                        $ text_style_D = "rarity_navegation_text_online_shop"
                        $ text_style_E = "rarity_navegation_text_online_shop"
                        
                        if rarity_selected == "S": 
                            $ text_style_S = "rarity_navegation_text_online_shop_active"
                        elif rarity_selected == "A": 
                            $ text_style_A = "rarity_navegation_text_online_shop_active"
                        elif rarity_selected == "B": 
                            $ text_style_B = "rarity_navegation_text_online_shop_active"
                        elif rarity_selected == "C": 
                            $ text_style_C = "rarity_navegation_text_online_shop_active"
                        elif rarity_selected == "D": 
                            $ text_style_D = "rarity_navegation_text_online_shop_active"
                        elif rarity_selected == "E": 
                            $ text_style_E = "rarity_navegation_text_online_shop_active"
                        textbutton "S" action SetScreenVariable("rarity_selected", "S") yalign 0.9 xalign 0.5 text_style text_style_S
                        text "|"
                        textbutton "A" action SetScreenVariable("rarity_selected", "A") yalign 0.9 xalign 0.5 text_style text_style_A
                        text "|"
                        textbutton "B" action SetScreenVariable("rarity_selected", "B") yalign 0.9 xalign 0.5 text_style text_style_B
                        text "|"
                        textbutton "C" action SetScreenVariable("rarity_selected", "C") yalign 0.9 xalign 0.5 text_style text_style_C
                        text "|"
                        textbutton "D" action SetScreenVariable("rarity_selected", "D") yalign 0.9 xalign 0.5 text_style text_style_D
                        text "|"
                        textbutton "E" action SetScreenVariable("rarity_selected", "E") yalign 0.9 xalign 0.5 text_style text_style_E
                    textbutton "Back" action [SetScreenVariable("online_shop_show", "main_menu"), SetScreenVariable("rarity_selected", "S")] yalign 0.9 xalign 0.5 text_style text_style_back_button

                if online_shop_show == "show_protectors":
                    
                    hbox:
                        spacing 50
                        xalign 0.5
                        yalign 0.5
                        for protector_to_sell in online_shop_variable.selling_protectors_list:

                            $ image_name = protector_to_sell.stage

                            # Path to the image
                            $ show_protectors_image = "images/protectors/{}/{}.png".format(protector_to_sell.name, image_name)

                            # Get original image size
                            $ orig_width, orig_height = renpy.image_size(show_protectors_image)

                            # Calculate proportional width
                            $ new_width = int(orig_width * (items_scale / float(orig_height)))

                            # Scale the image
                            $ show_protectors_scaled = im.Scale(show_protectors_image, new_width, items_scale)

                            $ button_action = Show("protector_detail_screen", my_protector=protector_to_sell)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 20
                                vbox:
                                    xalign 0.5
                                    xminimum 700
                                    xmaximum 700
                                    vbox:
                                        xalign 0.5
                                        button:
                                            action button_action
                                            style "option_button_online_shop"
                                            xpadding 4
                                            ypadding 4
                                            frame:
                                                xalign 0.5 
                                                add im.Composite(
                                                    (items_scale, items_scale),
                                                    (0, 0), empty_scaled,
                                                    ((items_scale - new_width) // 2, 0), show_protectors_scaled   
                                                )

                                text str(protector_to_sell.name) xalign 0.5 color online_shop_color

                                text str(protector_to_sell.price) + " $" xalign 0.5 color online_shop_color

                                $ online_shop_action = Function(notify_user_money_is_not_enough, protector_to_sell.name)
                                if money >= protector_to_sell.price:
                                    $ online_shop_action = Function(buy_new_protector, protector_to_sell)

                                if protector_to_sell.stillAvailable:
                                    button:
                                        style "option_button_online_shop"
                                        xfill True
                                        xmaximum 500
                                        xalign 0.5
                                        frame:
                                            xfill True
                                            background "#444"
                                            padding (10, 10)
                                            vbox:
                                                spacing 5
                                                xalign 0.5
                                                text "Buy" size 24 color "#fff" xalign 0.5
                                        action online_shop_action
                    textbutton "Back" action [SetScreenVariable("online_shop_show", "main_menu"), SetScreenVariable("rarity_selected", "S")] yalign 0.9 xalign 0.5 text_style text_style_back_button
                        
            elif selling_or_buying == "selling":
                
                if online_shop_show == "main_menu":
                    hbox:
                        spacing 50
                        xalign 0.5
                        yalign 0.5
                        
                        $ show_weapons_image = "images/menu/weapons.png"
                        $ show_weapons_scaled = im.Scale(show_weapons_image, main_options_scale, main_options_scale)
                        
                        fixed: 
                            xmaximum main_options_scale
                            ymaximum main_options_scale
                            button:
                                action [SetScreenVariable("online_shop_show", "show_weapons"), SetVariable("online_shop_new_weapons", False)]
                                style "option_button_online_shop"
                                frame:
                                    add im.Composite(
                                        (main_options_scale, main_options_scale),
                                        (0, 0), main_buttons_background,
                                        (0, 0), show_weapons_scaled
                                    )
                            if online_shop_new_weapons == True:
                                frame:
                                    background "#fff"  # white background
                                    padding (5, 2)    # space around the "!"
                                    xalign 1.0
                                    yalign 0.0
                                    text "!" size 30 color "#f00" bold True
                                

                        $ show_equipment_image = "images/menu/equipments.png"
                        $ show_equipment_scaled = im.Scale(show_equipment_image, main_options_scale, main_options_scale)
                            
                        fixed: 
                            xmaximum main_options_scale
                            ymaximum main_options_scale
                            button:
                                action [SetScreenVariable("online_shop_show", "show_equipments"), SetVariable("online_shop_new_equipments", False)]
                                style "option_button_online_shop"
                                frame:
                                    add im.Composite(
                                        (main_options_scale, main_options_scale),
                                        (0, 0), main_buttons_background,
                                        (0, 0), show_equipment_scaled
                                    )
                            if online_shop_new_equipments == True:
                                frame:
                                    background "#fff"  # white background
                                    padding (5, 2)    # space around the "!"
                                    xalign 1.0
                                    yalign 0.0
                                    text "!" size 30 color "#f00" bold True

                if online_shop_show == "show_equipments":
                    
                    hbox:
                        spacing 50
                        xalign 0.5
                        yalign 0.5
                        for equipment in myEquipments:
                            $ price = get_value_for_item_of_this_rarity(equipment.rarity)
                            $ my_color = EClassColor
                            $ rarity = equipment.rarity
                            if equipment.rarity == "D":
                                $ my_color = DClassColor
                            if equipment.rarity == "C":
                                $ my_color = CClassColor
                            if equipment.rarity == "B":
                                $ my_color = BClassColor
                            if equipment.rarity == "A":
                                $ my_color = AClassColor
                            if equipment.rarity == "S":
                                $ my_color = SClassColor
                            
                            $ equipment_img = "images/equipments/{}_{}.png".format(equipment.class_name, equipment.type)

                            # Get original image size
                            $ orig_width, orig_height = renpy.image_size(equipment_img)

                            # Calculate proportional width
                            $ new_width = int(orig_width * (items_scale / float(orig_height)))

                            # Scale the image
                            $ equipment_scaled = im.Scale(equipment_img, new_width, items_scale)

                            $ button_action = Show("equipment_detail_screen", None, "e", equipment)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 20
                                vbox:
                                    xalign 0.5
                                    xminimum 700
                                    xmaximum 700
                                    vbox:
                                        xalign 0.5
                                        button:
                                            action button_action
                                            style "option_button_online_shop"
                                            xpadding 4
                                            ypadding 4
                                            frame:                                            
                                                background my_color
                                                xalign 0.5 
                                                add im.Composite(
                                                    (items_scale, items_scale),
                                                    (0, 0), empty_scaled,
                                                    ((items_scale - new_width) // 2, 0), equipment_scaled   
                                                )

                                text str(equipment.name) xalign 0.5 color online_shop_color

                                text str(price) + " $" xalign 0.5 color online_shop_color

                                $ online_shop_action = Function(sell_new_equipment, equipment)

                                button:
                                    style "option_button_online_shop"
                                    xfill True
                                    xmaximum 500
                                    xalign 0.5
                                    frame:
                                        xfill True
                                        background "#444"
                                        padding (10, 10)
                                        vbox:
                                            spacing 5
                                            xalign 0.5
                                            text "Sell" size 24 color "#fff" xalign 0.5
                                    action online_shop_action
                    textbutton "Back" action [SetScreenVariable("online_shop_show", "main_menu"), SetScreenVariable("rarity_selected", "S")] yalign 0.9 xalign 0.5 text_style text_style_back_button

                if online_shop_show == "show_weapons":

                    hbox:
                        spacing 50
                        xalign 0.5
                        yalign 0.5
                        
                        for weapon in myWeapons:
                            $ price = get_value_for_item_of_this_rarity(weapon.rarity)
                            $ my_color = EClassColor
                            $ rarity = weapon.rarity
                            if weapon.rarity == "D":
                                $ my_color = DClassColor
                            if weapon.rarity == "C":
                                $ my_color = CClassColor
                            if weapon.rarity == "B":
                                $ my_color = BClassColor
                            if weapon.rarity == "A":
                                $ my_color = AClassColor
                            if weapon.rarity == "S":
                                $ my_color = SClassColor
                            
                            $ weapon_img = "images/weapons/{}.png".format(weapon.class_name)

                            # Get original image size
                            $ orig_width, orig_height = renpy.image_size(weapon_img)

                            # Calculate proportional width
                            $ new_width = int(orig_width * (items_scale / float(orig_height)))

                            # Scale the image
                            $ weapon_scaled = im.Scale(weapon_img, new_width, items_scale)

                            $ button_action = Show("equipment_detail_screen", None, "w", weapon)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 20
                                vbox:
                                    xalign 0.5
                                    xminimum 700
                                    xmaximum 700
                                    vbox:
                                        xalign 0.5
                                        button:
                                            action button_action
                                            style "option_button_online_shop"
                                            xpadding 4
                                            ypadding 4
                                            frame:                                            
                                                background my_color
                                                xalign 0.5 
                                                add im.Composite(
                                                    (items_scale, items_scale),
                                                    (0, 0), empty_scaled,
                                                    ((items_scale - new_width) // 2, 0), weapon_scaled   
                                                )

                                text str(weapon.name) xalign 0.5 color online_shop_color

                                text str(price) + " $" xalign 0.5 color online_shop_color

                                $ online_shop_action = Function(sell_new_weapon, weapon)

                                button:
                                    style "option_button_online_shop"
                                    xfill True
                                    xmaximum 500
                                    xalign 0.5
                                    frame:
                                        xfill True
                                        background "#444"
                                        padding (10, 10)
                                        vbox:
                                            spacing 5
                                            xalign 0.5
                                            text "Sell" size 24 color "#fff" xalign 0.5
                                    action online_shop_action

                    textbutton "Back" action [SetScreenVariable("online_shop_show", "main_menu"), SetScreenVariable("rarity_selected", "S")] yalign 0.9 xalign 0.5 text_style text_style_back_button
        if selling_or_buying == None:
            hbox:
                spacing 20
                xalign 0.5
                yalign 0.99
                textbutton "Return" action Return() xalign 0.5 text_style text_style_back_button
        else:            
            hbox:
                spacing 20
                xalign 0.5
                yalign 0.99
                textbutton "Return" action SetScreenVariable("selling_or_buying", None) xalign 0.5 text_style text_style_back_button
