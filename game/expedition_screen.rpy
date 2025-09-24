
screen expedition_screen(regionNumber):
    $ min_level = (regionNumber - 1) * 20
    $ max_level = regionNumber * 20
    default page = 0
    default page_size = 5
    default filtered_expeditions = [m for m in allExpeditions if min_level <= m.difficulty <= max_level and m.expedition_id != 0]
    default max_pages = max((len(filtered_expeditions) - 1) // page_size, 0)
    default mode = "list"
    default selected_expedition = None
    default selected_boss_expedition = None
    
    # List of available protectors
    $ available_protectors = [p for p in my_protectors_map.values() if p.status == "Available"]
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        
        ysize 925
        padding (20, 20)
        vbox:
            xsize 700
            xalign 0.5  # center content inside the frame
            if mode == "list":
                vbox:
                    spacing 10
                    xalign 0.5
                    yalign 0.0
                    vbox:
                        xalign 0.5
                        vbox:
                            xalign 0.5
                            text "Expeditions" size 40
                        
                        vbox:
                            xalign 0.5
                            $ bossExpedition = next((m for m in bossExpeditions if m.regionNumber == regionNumber), None)
                            vbox:
                                xalign 0.5
                                yminimum 75
                                if bossExpedition.successfulMinorExpeditions >= bossExpedition.successfulMinorExpeditionsRequired:
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        spacing 5
                                        textbutton "❗Boss Fight❗" text_size 27 action [SetScreenVariable("mode", "boss_fight_detail"), SetScreenVariable("selected_boss_expedition", bossExpedition)] style "background_boss_expedition_button" text_style "text_boss_expedition_button"
                                else:
                                    bar value bossExpedition.successfulMinorExpeditions range bossExpedition.successfulMinorExpeditionsRequired:
                                        xmaximum 400
                                        ymaximum 30

                                    vbox:
                                        xalign 0.5
                                        text "[bossExpedition.successfulMinorExpeditions] / [bossExpedition.successfulMinorExpeditionsRequired]" size 24

                    for i in range(page * page_size, min((page + 1) * page_size, len(filtered_expeditions))):
                        $ expedition = filtered_expeditions[i]
                        button:
                            xfill True
                            frame:
                                xfill True
                                style "background_expedition_button"
                                padding (10, 10)
                                vbox:
                                    spacing 5
                                    text "[expedition.title] ([expedition.expedition_type])" size 24 color "#fff"
                                    text expedition.description size 16 color "#ccc"
                                    text "Difficulty: [expedition.difficulty]" size 14 color "#aaa"
                            action [SetScreenVariable("mode", "detail"), SetScreenVariable("selected_expedition", expedition)]

                    hbox:
                        spacing 20
                        xalign 0.5

                        if page > 0:
                            textbutton "Previous" action SetScreenVariable("page", page - 1) text_size 25
                        else:
                            textbutton "Previous" action NullAction() sensitive False text_size 25

                        if page < max_pages:
                            textbutton "Next" action SetScreenVariable("page", page + 1) text_size 25
                        else:
                            textbutton "Next" action NullAction() sensitive False text_size 25

                    textbutton "Return" action Return() xalign 0.5 text_size 25

            elif mode == "detail" and selected_expedition is not None:
                vbox:
                    yalign 0.0
                    xalign 0.5
                    spacing 20
                    xsize 700
                    null height 40  # This adds 40 pixels of vertical space at the top
                    
                    vbox:
                        xalign 0.5
                        text "[selected_expedition.title]" size 40 color "#000000"
                        
                        vbox:
                            xalign 0.5
                            spacing 20
                            text "([selected_expedition.expedition_type])" size 30 color "#000000"
                        
                            vbox:
                                xalign 0.5
                                text "Difficulty: [selected_expedition.difficulty]" size 20 color "#5a5a5a"

                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    text selected_expedition.description size 20 color "#5a5a5a" xalign 0.5

                    $ neededDaysToFinish_day_name = "day"
                    $ disapearingInThisDays_day_name = "day"
                    if selected_expedition.neededDaysToFinish > 1:
                        $ neededDaysToFinish_day_name = "days"
                    if selected_expedition.disapearingInThisDays > 1:
                        $ disapearingInThisDays_day_name = "days"
                        
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top
                    hbox:
                        xsize 700
                        spacing 20

                        vbox:
                            xalign 0.2  # force to left
                            spacing 20

                            hbox:
                                text "Payment:" size 18 color "#5a5a5a"
                            hbox:
                                text "Time it takes to complete:" size 18 color "#5a5a5a"
                            if selected_expedition.status != "started":
                                hbox:
                                    text "Will disappear in:" size 18 color "#5a5a5a"
                            if selected_expedition.status == "assigned":
                                hbox:
                                    text "Assigned protector:" size 18 color "#5a5a5a"

                        vbox:
                            xalign 0.8  # force to right
                            spacing 20

                            hbox:
                                xalign 1.0  # force to right
                                text "[selected_expedition.gold_received] $" size 18 color "#5a5a5a"
                            hbox:
                                xalign 1.0  # force to right
                                text "[selected_expedition.neededDaysToFinish] [neededDaysToFinish_day_name]" size 18 color "#5a5a5a"
                            if selected_expedition.status != "started":
                                hbox:
                                    xalign 1.0  # force to right
                                    text "[selected_expedition.disapearingInThisDays] [disapearingInThisDays_day_name]" size 18 color "#5a5a5a"
                            if selected_expedition.status == "assigned":
                                hbox:
                                    xalign 1.0  # force to right
                                    text "[selected_expedition.assignedProtectorName]" size 18 color "#5a5a5a"
                
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    if selected_expedition.status == "assigned":
                        $ success_rate = selected_expedition.get_success_rate(my_protectors_map[selected_expedition.assignedProtectorName])
                        if success_rate > 100:
                            $ success_rate = 100
                        vbox: 
                            xalign 0.5
                            spacing 10
                            bar value success_rate range 100 style "success_rate_bar"
                            text "Success rate: [success_rate] %" size 20 xalign 0.5
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    if selected_expedition.status != "started":
                        if selected_expedition.assignedProtectorName == None:
                            hbox:
                                xalign 0.5
                                spacing 10
                                for protector in available_protectors:
                                    $ select_protector_button_style = "button_small_text"
                                    if protector.name == selected_expedition.assignedProtectorName:
                                        $ select_protector_button_style = "button_small_text_selected"
                                    textbutton protector.name style str(select_protector_button_style) action Function(selected_expedition.assignProtector, protector.name) text_size 20

                                
                                if len(available_protectors) == 0:
                                    text "There are no available protectors." size 15 color "#5a5a5a" xmaximum 640
                        else:
                            hbox:
                                xalign 0.5
                                spacing 10
                                textbutton "Unassign [selected_expedition.assignedProtectorName]" action Function(selected_expedition.unassignProtector) text_size 20

                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top
                    null ysize 1  # This adds 40 pixels of vertical space at the top
                    
                    hbox:
                        xalign 0.5
                        spacing 20
                        if selected_expedition.status != "started" and selected_expedition.assignedProtectorName != None:
                            textbutton "Start Expedition" action Function(selected_expedition.startExpedition, success_rate) text_size 25
                        textbutton "Back" action SetScreenVariable("mode", "list") text_size 25
            
            elif mode == "boss_fight_detail" and selected_boss_expedition is not None:
                vbox:
                    yalign 0.0
                    xalign 0.5
                    spacing 20
                    xsize 700
                    null height 40  # This adds 40 pixels of vertical space at the top
                    
                    vbox:
                        xalign 0.5
                        text "[selected_boss_expedition.title]" size 40 color "#000000" xalign 0.5

                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    text selected_boss_expedition.description size 20 color "#5a5a5a" xalign 0.5 text_align 0.5

                    hbox:
                        xsize 700
                        spacing 20
                        vbox:
                            xalign 0.2  # force to left
                            spacing 20

                            hbox:
                                text "Payment:" size 18 color "#5a5a5a"
                            if selected_boss_expedition.status == "assigned":
                                hbox:
                                    text "Assigned protector:" size 18 color "#5a5a5a"

                        vbox:
                            xalign 0.8  # force to right
                            spacing 20

                            hbox:
                                xalign 1.0  # force to right
                                text "[selected_boss_expedition.gold_received] $" size 18 color "#5a5a5a"
                            if selected_boss_expedition.status == "assigned":
                                hbox:
                                    xalign 1.0  # force to right
                                    text "[selected_boss_expedition.assignedProtectorName]" size 18 color "#5a5a5a"

                    if selected_boss_expedition.assignedProtectorName == None:
                        hbox:
                            xalign 0.5
                            spacing 10
                            for protector in available_protectors:
                                $ select_protector_button_style = "button_small_text"
                                if protector.name == selected_boss_expedition.assignedProtectorName:
                                    $ select_protector_button_style = "button_small_text_selected"
                                textbutton protector.name style str(select_protector_button_style) action Function(selected_boss_expedition.assignProtector, protector.name) text_size 20

                            
                            if len(available_protectors) == 0:
                                text "There are no available protectors." size 15 color "#5a5a5a" xmaximum 640
                    else:
                        hbox:
                            xalign 0.5
                            spacing 10
                            textbutton "Unassign [selected_boss_expedition.assignedProtectorName]" action Function(selected_boss_expedition.unassignProtector) text_size 20
                        
                    hbox:
                        xalign 0.5
                        spacing 20
                        if selected_boss_expedition.assignedProtectorName != None:
                            textbutton "Start Boss Fight" action Function(selected_boss_expedition.startBossExpedition) text_size 25 
                        textbutton "Back" action SetScreenVariable("mode", "list") text_size 25
