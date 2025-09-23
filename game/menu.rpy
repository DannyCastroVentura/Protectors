screen menu_button_for_protectors_game():
    if show_things:
        $ button_style = "hover_white"
        textbutton "Menu":
            text_style button_style
            background "#4448"
            xalign 0.5
            yalign 0.0
            padding (20, 10)
            text_size 40
            action Show("menu_for_protectors_game")

screen menu_for_protectors_game():
    frame:
        modal True
        background Solid(black_see_through_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 150
        xfill True
        yfill True

        $ buttons_background = im.Scale("images/background_item.png", scale, scale)
        
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            xfill True
            yfill True

            # Close button - top right
            textbutton "Close" action Hide("menu_for_protectors_game"):
                text_style "hover_white"
                xalign 1.0
                yalign 0.0
                padding (10, 5)
                
            vbox:
                yalign 0.0
                xalign 0.5
                spacing 75
                vbox:
                    yalign 0.5
                    xalign 0.5
                    spacing 40
                    null height 30
                    text "Menu" size 50 color "#FFF" xalign 0.5
                    text "Map" xalign 0.5 size 40 color "#FFF"
                    hbox:
                        yalign 0.5
                        xalign 0.5
                        spacing 100
                        
                        
                        vbox:
                            spacing 20
                            xminimum 250
                            $ show_protectors_image = "images/menu/base_of_operations.png"
                            $ show_protectors_scaled = im.Scale(show_protectors_image, scale, scale)
                                
                            button:
                                action [Hide("menu_for_protectors_game"), Jump("base_of_operations")]  # show possible weapons to use
                                background "#ffffff"
                                xalign 0.5
                                frame:
                                    add im.Composite(
                                        (scale, scale),
                                        (0, 0), buttons_background,
                                        (0, 0), show_protectors_scaled
                                    )
                            text "Operations" color "#FFF" xalign 0.5
                        
                        vbox:
                            spacing 20
                            xminimum 250
                            $ show_weapons_image = "images/menu/training.png"
                            $ show_weapons_scaled = im.Scale(show_weapons_image, scale, scale)
                                
                            button:
                                action [Hide("menu_for_protectors_game"), Jump("training_ground")]  # show possible weapons to use
                                background "#ffffff"
                                xalign 0.5
                                frame:
                                    add im.Composite(
                                        (scale, scale),
                                        (0, 0), buttons_background,
                                        (0, 0), show_weapons_scaled
                                    )
                            text "Training" color "#FFF" xalign 0.5
                        
                        vbox:
                            spacing 20
                            xminimum 250
                            $ show_equipment_image = "images/menu/rest.png"
                            $ show_equipment_scaled = im.Scale(show_equipment_image, scale, scale)
                                
                            button:
                                action [Hide("menu_for_protectors_game"), Jump("resting_area")]  # show possible weapons to use
                                background "#ffffff"
                                xalign 0.5
                                frame:
                                    add im.Composite(
                                        (scale, scale),
                                        (0, 0), buttons_background,
                                        (0, 0), show_equipment_scaled
                                    )
                            text "Resting" color "#FFF" xalign 0.5
                
                vbox:
                    yalign 0.5
                    xalign 0.5
                    spacing 50
                    text "Inventory" xalign 0.5 size 40 color "#FFF"
                    hbox:
                        yalign 0.5
                        xalign 0.5
                        spacing 100
                        vbox:
                            spacing 20
                            xminimum 250
                            $ show_protectors_image = "images/menu/protectors.png"
                            $ show_protectors_scaled = im.Scale(show_protectors_image, scale, scale)
                                
                            button:
                                action Show("my_protectors_screen")  # show possible weapons to use
                                background "#ffffff"
                                xalign 0.5
                                frame:
                                    add im.Composite(
                                        (scale, scale),
                                        (0, 0), buttons_background,
                                        (0, 0), show_protectors_scaled
                                    )
                            text "Protectors" color "#FFF" xalign 0.5
                        
                        vbox:
                            spacing 20
                            xminimum 250
                            $ show_weapons_image = "images/menu/weapons.png"
                            $ show_weapons_scaled = im.Scale(show_weapons_image, scale, scale)
                                
                            button:
                                action Show("my_weapons_screen")  # show possible weapons to use
                                background "#ffffff"
                                xalign 0.5
                                frame:
                                    add im.Composite(
                                        (scale, scale),
                                        (0, 0), buttons_background,
                                        (0, 0), show_weapons_scaled
                                    )
                            text "Weapons" color "#FFF" xalign 0.5
                        
                        vbox:
                            spacing 20
                            xminimum 250
                            $ show_equipment_image = "images/menu/equipments.png"
                            $ show_equipment_scaled = im.Scale(show_equipment_image, scale, scale)
                                
                            button:
                                action Show("my_equipments_screen")  # show possible weapons to use
                                background "#ffffff"
                                xalign 0.5
                                frame:
                                    add im.Composite(
                                        (scale, scale),
                                        (0, 0), buttons_background,
                                        (0, 0), show_equipment_scaled
                                    )
                            text "Equipments" color "#FFF" xalign 0.5
                vbox:
                    yalign 0.5
                    xalign 0.5
                    spacing 50
                    text "Nova" xalign 0.5 size 40 color "#FFF"
                    hbox:
                        yalign 0.5
                        xalign 0.5
                        spacing 100
                        vbox:
                            spacing 20
                            xminimum 250
                            $ show_protectors_image = "images/menu/nova.png"
                            $ show_protectors_scaled = im.Scale(show_protectors_image, scale, scale)
                                
                            button:
                                action [Hide("menu_for_protectors_game"), Jump("get_help_from_nova")]  # show possible weapons to use
                                background "#ffffff"
                                xalign 0.5
                                frame:
                                    add im.Composite(
                                        (scale, scale),
                                        (0, 0), buttons_background,
                                        (0, 0), show_protectors_scaled
                                    )
                            text "Call Nova" color "#FFF" xalign 0.5
