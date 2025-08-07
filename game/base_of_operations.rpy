label go_to_computer:
    $ set_background("computer")
    menu:
        "See all missions":
            call see_all_missions(1)
        "Check online shop":
            # TODO: make this work -> online shop for some items
            #   -   for this we would need to create a couple of items
            #   -   and think of what could these items do :\
            #   -   implement the logic
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
    $ set_background(f"regions/{regionNumber}")
    call screen mission_screen(regionNumber)
    # TODO: 
    #   -   create the boss mission so I can unlock the next region
    #   -   but first, I'll need to conclude the minor missions
    return
