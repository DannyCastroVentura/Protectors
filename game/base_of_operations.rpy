label go_to_computer:
    $ set_background("computer")
    menu:
        "Expeditions":
            call see_expeditions(1)
        "Check online shop":
            call check_online_shop()
        "Go back":
            jump base_of_operations
        "Let's go to elsewhere":
            call base_travel_menu()
    jump go_to_computer

label see_expeditions(page):
    $ set_background("computer")
    if page == 1:
        $ update_menu_disable_options(True)
        menu:
            "Region 1":
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(1)
            "Region 2" if False:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(2)
            "Region 3" if False:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(3)
            "Region 4" if False:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(4)
            "Region 5" if False:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(5)
            ">> Check next regions >>":
                $ update_menu_disable_options(False)
                call see_expeditions(2)
            "Go back":
                jump go_to_computer
            "Let's go to elsewhere":
                call base_travel_menu()
    elif page == 2:
        $ update_menu_disable_options(True)
        menu:
            "Region 6" if False:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(6)
            "Region 7" if False:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(7)
            "Region 8" if False:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(8)
            "Region 9" if False:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(9)
            "Region 10" if False:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(10)
            "<< Check previous regions <<":
                $ update_menu_disable_options(False)
                call see_expeditions(1)
            "Go back":
                jump go_to_computer
            "Let's go to elsewhere":
                call base_travel_menu()
    call see_expeditions(1)

label see_expeditions_for_region(regionNumber):
    $ set_background(f"regions/{regionNumber}")
    call screen expedition_screen(regionNumber)
    return

label check_online_shop():
    call screen online_shop()
    return
