screen equipment_detail_screen(weaponOrEquipment_type, equipment_or_weapon, protector = None):
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 600

        fixed:
            xfill True
            yfill True

            # Close button - top right
            textbutton "Back" action Hide("equipment_detail_screen"):
                text_style "hover_white"
                xalign 1.0
                yalign 0.0
                padding (10, 5)
            vbox:
                yalign 0.1
                xalign 0.5
                text "[equipment_or_weapon.name] ([equipment_or_weapon.rarity])" size 50 color "#FFF" xalign 0.5
            vbox:
                spacing 20
                xalign 0.9
                yalign 0.5
                $ background = im.Scale("images/background_item.png", scale, scale)

                
                if weaponOrEquipment_type == "w":
                    $ e_or_w_image = "images/weapons/{}.png".format(equipment_or_weapon.class_name)
                elif weaponOrEquipment_type == "e":
                    $ e_or_w_image = "images/equipments/{}_{}.png".format(equipment_or_weapon.class_name, equipment_or_weapon.type)

                # Get original image size
                $ orig_width, orig_height = renpy.image_size(e_or_w_image)

                # Calculate proportional width
                $ new_width = int(orig_width * (scale / float(orig_height)))

                # Scale the image
                $ e_or_w_scaled = im.Scale(e_or_w_image, new_width, scale)

                $ my_color = EClassColor
                $ rarity = equipment_or_weapon.rarity
                if equipment_or_weapon.rarity == "D":
                    $ my_color = DClassColor
                if equipment_or_weapon.rarity == "C":
                    $ my_color = CClassColor
                if equipment_or_weapon.rarity == "B":
                    $ my_color = BClassColor
                if equipment_or_weapon.rarity == "A":
                    $ my_color = AClassColor
                if equipment_or_weapon.rarity == "S":
                    $ my_color = SClassColor
                frame:                           
                    background my_color
                    xalign 0.5 
                    add im.Composite(
                        (scale, scale),
                        (0, 0), background,
                        ((scale - new_width) // 2, 0), e_or_w_scaled
                        
                    )
            vbox:
                spacing 20
                xalign 0.1
                yalign 0.5
                xmaximum 800
                text "[equipment_or_weapon.name] ([equipment_or_weapon.rarity])" size 25 color "#FFF" 
                text "[str(equipment_or_weapon.description)]" size 22 color "#EEE"
                null height 20
                hbox:
                    xalign 0.5
                    spacing 20
                    
                    
                    vbox:
                        xminimum 300
                        xalign 0.5
                        if protector is not None:
                            text "Equiped on:" size 22 color "#EEE"
                        text "Type:" size 22 color "#EEE"
                        text "Class:" size 22 color "#EEE"
                        if weaponOrEquipment_type == "w":
                            text "Base damage:" size 22 color "#EEE"
                            text "Range type:" size 22 color "#EEE"

                        elif weaponOrEquipment_type == "e":
                            text "Defense value:" size 22 color "#EEE"
                            text "[str(stats_increment_map[equipment_or_weapon.class_name]['prio1'])]:" size 22 color "#EEE"
                            text "[str(stats_increment_map[equipment_or_weapon.class_name]['prio2'])]:" size 22 color "#EEE"

                        text "Rarity:" size 22 color "#EEE"
                        
                    vbox:
                        xminimum 300
                        xalign 0.5
                        if protector is not None:
                            text protector.name size 22 color "#EEE" xalign 1.0
                        text "[str(equipment_or_weapon.type)]" size 22 color "#EEE" xalign 1.0
                        text "[str(equipment_or_weapon.class_name)]" size 22 color "#EEE" xalign 1.0
                        if weaponOrEquipment_type == "w":
                            text "[str(int(equipment_or_weapon.base_damage))]" size 22 color "#EEE" xalign 1.0
                            text "[str(equipment_or_weapon.range)]" size 22 color "#EEE" xalign 1.0
                        elif weaponOrEquipment_type == "e":
                            text "[str(int(equipment_or_weapon.base_defense))]" size 22 color "#EEE" xalign 1.0
                            text "+[str(equipment_or_weapon.prio1)]%" size 22 color "#EEE" xalign 1.0
                            text "+[str(equipment_or_weapon.prio2)]%" size 22 color "#EEE" xalign 1.0
                        
                        text "[str(equipment_or_weapon.rarity)]" size 22 color "#EEE" xalign 1.0
    