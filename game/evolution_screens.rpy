screen protector_evolution_choosing_screen(my_protector):
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 500
        $ buttons_background = im.Scale("images/background_item.png", scale, scale)
        fixed:
            xfill True
            yfill True

            # Close button - top right
            textbutton "Back" action Hide("protector_evolution_choosing_screen"):
                text_style "hover_white"
                xalign 1.0
                yalign 0.0
                padding (10, 5)
            vbox:
                yalign 0.1
                xalign 0.5
                text "[my_protector.name]" size 50 color "#FFF" xalign 0.5
            hbox:
                xfill True
                xalign 0.5
                yalign 0.5
                vbox:
                    spacing 20
                    xalign 0.5
                    text str(my_protector.basePoints.evolution_name_1):
                        xalign 0.5
                    $ image_name = "5_1"

                    # Path to the image
                    $ show_protectors_image = "images/protectors/{}/{}.png".format(my_protector.name, image_name)

                    # Get original image size
                    $ orig_width, orig_height = renpy.image_size(show_protectors_image)

                    # Calculate proportional width
                    $ new_width = int(orig_width * (scale / float(orig_height)))

                    # Scale the image
                    $ show_protectors_scaled = im.Scale(show_protectors_image, new_width, scale)
                    button:
                        frame:
                            xalign 0.5 
                            add im.Composite(
                                (scale, scale),
                                (0, 0), buttons_background,
                                ((scale - new_width) // 2, 0), im.Flip(show_protectors_scaled, horizontal=True)
                            )
                    text str(my_protector.basePoints.evolution_description_1):
                        xmaximum scale
                        size 25
                        xalign 0.5
                        text_align 0.5
                    textbutton str(my_protector.basePoints.evolution_name_1):
                        action Show("protector_evolution_detail_screen", None, my_protector, 1) 
                        text_style "button_in_black_background"
                        padding (10, 5)
                        xalign 0.5
                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5
                    text "Choose wisely!":
                        color "#FFF"
                        size 30
                        xalign 0.5
                    text "You may only choose one":
                        color "#FFF"
                        size 25
                        xalign 0.5
                vbox:
                    spacing 20
                    xalign 0.5
                    text str(my_protector.basePoints.evolution_name_2):
                        xalign 0.5
                    $ image_name = "5_2"

                    # Path to the image
                    $ show_protectors_image = "images/protectors/{}/{}.png".format(my_protector.name, image_name)

                    # Get original image size
                    $ orig_width, orig_height = renpy.image_size(show_protectors_image)

                    # Calculate proportional width
                    $ new_width = int(orig_width * (scale / float(orig_height)))

                    # Scale the image
                    $ show_protectors_scaled = im.Scale(show_protectors_image, new_width, scale)
                    button:
                        frame:
                            xalign 0.5 
                            add im.Composite(
                                (scale, scale),
                                (0, 0), buttons_background,
                                ((scale - new_width) // 2, 0), show_protectors_scaled
                                
                            )
                    text str(my_protector.basePoints.evolution_description_2):
                        xmaximum scale
                        size 25
                        xalign 0.5
                        text_align 0.5
                    textbutton str(my_protector.basePoints.evolution_name_2):
                        action Show("protector_evolution_detail_screen", None, my_protector, 2) 
                        text_style "button_in_black_background"
                        padding (10, 5)
                        xalign 0.5

screen protector_evolution_detail_screen(my_protector, evolution):
    $ protector_evolution_name = my_protector.basePoints.evolution_name_1
    if evolution == 2:
        $ protector_evolution_name = my_protector.basePoints.evolution_name_2
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 500
        fixed:
            xfill True
            yfill True

            # Close button - top right
            textbutton "Back" action Hide("protector_evolution_detail_screen"):
                text_style "hover_white"
                xalign 1.0
                yalign 0.0
                padding (10, 5)
            vbox:
                yalign 0.1
                xalign 0.5
                text "[my_protector.name]" size 50 color "#FFF" xalign 0.5
            hbox:
                xfill True
                xalign 0.5
                yalign 0.5

                # getting the improvements array
                $ evolution_parameter_key = "evolution_1"
                $ possible_future_weapons_array = my_protector.basePoints.usable_weapon_types_evolution_1
                if evolution == 2:
                    $ evolution_parameter_key = "evolution_2"
                    $ possible_future_weapons_array = my_protector.basePoints.usable_weapon_types_evolution_2

                $ str_t_color = "#EEE"
                $ con_t_color = "#EEE"
                $ wis_t_color = "#EEE"
                $ spe_t_color = "#EEE"
                $ dex_t_color = "#EEE"
                $ int_t_color = "#EEE"
                $ luc_t_color = "#EEE"

                $ current_stats = my_protector.get_current_stats(4, None)
                $ evolution_stats = my_protector.get_current_stats(5, evolution)
                
                $ str_text = str(current_stats['strength'])
                $ con_text = str(current_stats['constitution'])
                $ wis_text = str(current_stats['wisdom'])
                $ spe_text = str(current_stats['speed'])
                $ dex_text = str(current_stats['dexterity'])
                $ int_text = str(current_stats['intelligence'])
                $ luc_text = str(current_stats['luck'])

                if int(current_stats['strength']) < int(evolution_stats['strength']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(evolution_stats['strength']) * 100 / int(current_stats['strength'])) - 100
                    $ str_t_color = "#4CAF50"
                    $ str_text = str(current_stats['strength']) + " → " + str(evolution_stats['strength']) + " (+" + str(percentage_change) + "%)"
                elif int(current_stats['strength']) > int(evolution_stats['strength']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(current_stats['strength']) * 100 / int(evolution_stats['strength'])) - 100
                    $ str_t_color = "#F44336"
                    $ str_text = str(current_stats['strength']) + " → " + str(evolution_stats['strength']) + " (-" + str(percentage_change) + "%)"
                if int(current_stats['constitution']) < int(evolution_stats['constitution']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(evolution_stats['constitution']) * 100 / int(current_stats['constitution'])) - 100
                    $ con_t_color = "#4CAF50"
                    $ con_text = str(current_stats['constitution']) + " → " + str(evolution_stats['constitution']) + " (+" + str(percentage_change) + "%)"
                elif int(current_stats['constitution']) > int(evolution_stats['constitution']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(current_stats['constitution']) * 100 / int(evolution_stats['constitution'])) - 100
                    $ con_t_color = "#F44336"
                    $ con_text = str(current_stats['constitution']) + " → " + str(evolution_stats['constitution']) + " (-" + str(percentage_change) + "%)"
                if int(current_stats['wisdom']) < int(evolution_stats['wisdom']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(evolution_stats['wisdom']) * 100 / int(current_stats['wisdom'])) - 100
                    $ wis_t_color = "#4CAF50"
                    $ wis_text = str(current_stats['wisdom']) + " → " + str(evolution_stats['wisdom']) + " (+" + str(percentage_change) + "%)"
                elif int(current_stats['wisdom']) > int(evolution_stats['wisdom']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(current_stats['wisdom']) * 100 / int(evolution_stats['wisdom'])) - 100
                    $ wis_t_color = "#F44336"
                    $ wis_text = str(current_stats['wisdom']) + " → " + str(evolution_stats['wisdom']) + " (-" + str(percentage_change) + "%)"
                if int(current_stats['speed']) < int(evolution_stats['speed']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(evolution_stats['speed']) * 100 / int(current_stats['speed'])) - 100
                    $ spe_t_color = "#4CAF50"
                    $ spe_text = str(current_stats['speed']) + " → " + str(evolution_stats['speed']) + " (+" + str(percentage_change) + "%)"
                elif int(current_stats['speed']) > int(evolution_stats['speed']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(current_stats['speed']) * 100 / int(evolution_stats['speed'])) - 100
                    $ spe_t_color = "#F44336"
                    $ spe_text = str(current_stats['speed']) + " → " + str(evolution_stats['speed']) + " (-" + str(percentage_change) + "%)"
                if int(current_stats['dexterity']) < int(evolution_stats['dexterity']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(evolution_stats['dexterity']) * 100 / int(current_stats['dexterity'])) - 100
                    $ dex_t_color = "#4CAF50"
                    $ dex_text = str(current_stats['dexterity']) + " → " + str(evolution_stats['dexterity']) + " (+" + str(percentage_change) + "%)"
                elif int(current_stats['dexterity']) > int(evolution_stats['dexterity']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(current_stats['dexterity']) * 100 / int(evolution_stats['dexterity'])) - 100
                    $ dex_t_color = "#F44336"
                    $ dex_text = str(current_stats['dexterity']) + " → " + str(evolution_stats['dexterity']) + " (-" + str(percentage_change) + "%)"
                if int(current_stats['intelligence']) < int(evolution_stats['intelligence']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(evolution_stats['intelligence']) * 100 / int(current_stats['intelligence'])) - 100
                    $ int_t_color = "#4CAF50"
                    $ int_text = str(current_stats['intelligence']) + " → " + str(evolution_stats['intelligence']) + " (+" + str(percentage_change) + "%)"
                elif int(current_stats['intelligence']) > int(evolution_stats['intelligence']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(current_stats['intelligence']) * 100 / int(evolution_stats['intelligence'])) - 100
                    $ int_t_color = "#F44336"
                    $ int_text = str(current_stats['intelligence']) + " → " + str(evolution_stats['intelligence']) + " (-" + str(percentage_change) + "%)"
                if int(current_stats['luck']) < int(evolution_stats['luck']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(evolution_stats['luck']) * 100 / int(current_stats['luck'])) - 100
                    $ luc_t_color = "#4CAF50"
                    $ luc_text = str(current_stats['luck']) + " → " + str(evolution_stats['luck']) + " (+" + str(percentage_change) + "%)"
                elif int(current_stats['luck']) > int(evolution_stats['luck']):
                    # always need to have the bigger number first
                    $ percentage_change = int(int(current_stats['luck']) * 100 / int(evolution_stats['luck'])) - 100
                    $ luc_t_color = "#F44336"
                    $ luc_text = str(current_stats['luck']) + " → " + str(evolution_stats['luck']) + " (-" + str(percentage_change) + "%)"

                vbox:
                    xalign 0.2
                    yalign 0.5
                    spacing 45
                    text str(protector_evolution_name):
                        xalign 0.5
                        size 40
                        color "#EEE"
                    vbox:
                        spacing 20
                        xalign 0.5
                        text "Final attributes:":
                            xalign 0.5
                        hbox:
                            xalign 0.5
                            spacing 20
                            $ size_letter = 25
                            vbox:
                                xalign 0.5
                                text "Strength:" size size_letter color str_t_color
                                text "Constitution:" size size_letter color con_t_color
                                text "Wisdom:" size size_letter color wis_t_color
                                text "Speed:" size size_letter color spe_t_color
                            vbox:
                                xalign 0.5
                                text "[str_text]" size size_letter color str_t_color
                                text "[con_text]" size size_letter color con_t_color
                                text "[wis_text]" size size_letter color wis_t_color
                                text "[spe_text]" size size_letter color spe_t_color
                            vbox:
                                null width 40  # This adds 40 pixels of vertical space at the top
                            vbox:
                                xalign 0.5
                                text "Dexterity:" size size_letter color dex_t_color
                                text "Intelligence:" size size_letter color int_t_color
                                text "Luck:" size size_letter color luc_t_color
                            vbox:
                                xalign 0.5
                                text "[dex_text]" size size_letter color dex_t_color
                                text "[int_text]" size size_letter color int_t_color
                                text "[luc_text]" size size_letter color luc_t_color
                    vbox:
                        spacing 20
                        xalign 0.5
                        text "Usable weapons:":
                            xalign 0.5
                        vbox:
                            xalign 0.5
                            spacing 20
                            for i in range(0, len(possible_future_weapons_array), 6):
                                hbox:
                                    xalign 0.5
                                    spacing 20
                                    for weapon_type in possible_future_weapons_array[i:i+6]:
                                        text [weapon_type] size 25 color "#EEE" xalign 0.5
                            if my_protector.equipedWeapon != None:                                        
                                if my_protector.equipedWeapon.class_name not in possible_future_weapons_array:
                                    text "Warning: Current weapon will be removed from the protector.\n It will be stored in your inventory." size 22 color "#FFD700" xalign 0.5 text_align 0.5
                            

            $ image_name = "5_" + str(evolution)

            python:
                image_name = "5_" + str(evolution)
                image_path = getImage(str(get_folder_from_map(my_protector.name)) + '/' + str(image_name))
                if image_path:
                    ui.at(right)
                    ui.at(fit_to_screen_height)
                    ui.add(image_path)
                            
            vbox:
                yalign 0.9
                xalign 0.5
                textbutton "Choose: " + str(protector_evolution_name):
                    action [Function(update_evolution_for_protector, my_protector, evolution), 
                            Hide("protector_evolution_detail_screen"), Hide("protector_evolution_choosing_screen")] 
                    text_style "button_in_black_background"
                    padding (10, 5)
                    xalign 0.5
