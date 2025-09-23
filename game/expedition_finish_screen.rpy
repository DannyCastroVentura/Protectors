screen expedition_finish_screen(expedition, result):
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 650

        $ buttons_background = im.Scale("images/background_item.png", scale, scale)
        $ my_protector_name = expedition.assignedProtectorName

        fixed:
            xfill True
            yfill True

            vbox:
                yalign 0.15
                xalign 0.5
                spacing 100
                text "[expedition.title]" size 30 color "#FFF" xalign 0.5
                text "[result]" size 50 color "#FFF" xalign 0.5

            vbox:
                yalign 0.5
                xalign 0.5
                spacing 20
                if result == "Success!":
                    text "Victory! [my_protector_name] successfully finalized the expedition!" size 20 color "#FFF" xalign 0.5
                elif result == "Failed!":
                    text "It seems [my_protector_name] did not finalized the expedition as it should." size 25 color "#FFF" xalign 0.5
                    text "Make him to take on more missions, gain experience, level up, and try again!" size 25 color "#FFF" xalign 0.5
                    text "You might also find better equipment in the shop." size 25 color "#FFF" xalign 0.5
                
                
            vbox:
                yalign 0.9
                xalign 0.5
                button:
                        frame:
                            style "rectangle_button"
                            padding (10, 10)
                            vbox:
                                xalign 0.5  # horizontal center
                                yalign 0.5  # vertical center
                                spacing 5
                                text "Continue"
                        action Return(0)