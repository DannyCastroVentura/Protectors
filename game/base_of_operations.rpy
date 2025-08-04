label go_to_computer:
    $ set_background("computer")
    "Computer"
    mc "Here we are! What should I do here?"
    menu:
        "See all missions":
            call see_all_missions(1)
        "Check online shop":
            call check_my_missions()
        "Go back":
            jump base_of_operations
    jump go_to_computer

label see_all_missions(page):
    $ set_background("computer")
    if page == 1:
        $ update_menu_disable_options(True)
        menu:
            "Region 1":
                $ update_menu_disable_options(False)
                call see_missions_for_region(1)
            "Region 2" if False:
                $ update_menu_disable_options(False)
                call see_missions_for_region(2)
            "Region 3" if False:
                $ update_menu_disable_options(False)
                call see_missions_for_region(3)
            "Region 4" if False:
                $ update_menu_disable_options(False)
                call see_missions_for_region(4)
            "Region 5" if False:
                $ update_menu_disable_options(False)
                call see_missions_for_region(5)
            ">> Check next regions >>":
                $ update_menu_disable_options(False)
                call see_all_missions(2)
            "Go back":
                jump go_to_computer
    elif page == 2:
        $ update_menu_disable_options(True)
        menu:
            "Region 6" if False:
                $ update_menu_disable_options(False)
                call see_missions_for_region(6)
            "Region 7" if False:
                $ update_menu_disable_options(False)
                call see_missions_for_region(7)
            "Region 8" if False:
                $ update_menu_disable_options(False)
                call see_missions_for_region(8)
            "Region 9" if False:
                $ update_menu_disable_options(False)
                call see_missions_for_region(9)
            "Region 10" if False:
                $ update_menu_disable_options(False)
                call see_missions_for_region(10)
            "<< Check previous regions <<":
                $ update_menu_disable_options(False)
                call see_all_missions(1)
            "Go back":
                jump go_to_computer
    call see_all_missions(1)

label see_missions_for_region(regionNumber):
    $ min_level = (regionNumber - 1) * 20
    $ max_level = regionNumber * 20
    $ set_background("regions/1")
    call screen mission_screen(min_level, max_level)
    # TODO: 
    #   -   I'll also need to add the number of missions remaining until I can face the boss for this region 
    #   -   (maybe I could use a chart? this would be dope.)
    return

label show_mission_detail(mission):
    call screen mission_detail_screen(mission)
    $ result = _return

    if result == "start":
        "You chose to start [mission.title]."
        # TODO: Start mission logic here
    return

