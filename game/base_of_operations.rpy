label go_to_computer:
    $ set_background("computer")
    menu:
        "Expeditions":
            call see_expeditions(1)
        "Check online shop" if regions_variable.object['OnlineStore']['unlocked']:
            call check_online_shop()
        "Go back":
            jump base_of_operations
    jump go_to_computer

label see_expeditions(page):
    $ set_background("computer")
    if page == 1:
        $ update_menu_disable_options(True)
        $ expedition_names = list(regions_variable.object.keys())
        $ region_1_name = expedition_names[0]
        $ region_2_name = expedition_names[1]
        $ region_3_name = expedition_names[2]
        $ region_4_name = expedition_names[3]
        $ region_5_name = expedition_names[4]
        $ region_6_name = expedition_names[5]
        $ region_7_name = expedition_names[6]
        $ region_8_name = expedition_names[7]
        $ region_9_name = expedition_names[8]
        $ region_10_name = expedition_names[9]

        
        menu:
            "[region_1_name]":
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(1)
            "[region_2_name]" if regions_variable.object[region_2_name]['unlocked']:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(2)
            "[region_3_name]" if regions_variable.object[region_3_name]['unlocked']:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(3)
            "[region_4_name]" if regions_variable.object[region_4_name]['unlocked']:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(4)
            "[region_5_name]" if regions_variable.object[region_5_name]['unlocked']:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(5)
            ">> Check next regions >>":
                $ update_menu_disable_options(False)
                call see_expeditions(2)
            "Go back":
                jump go_to_computer
    elif page == 2:
        $ update_menu_disable_options(True)
        menu:
            "[region_6_name]" if regions_variable.object[region_6_name]['unlocked']:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(6)
            "[region_7_name]" if regions_variable.object[region_7_name]['unlocked']:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(7)
            "[region_8_name]" if regions_variable.object[region_8_name]['unlocked']:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(8)
            "[region_9_name]" if regions_variable.object[region_9_name]['unlocked']:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(9)
            "[region_10_name]" if regions_variable.object[region_10_name]['unlocked']:
                $ update_menu_disable_options(False)
                call see_expeditions_for_region(10)
            "<< Check previous regions <<":
                $ update_menu_disable_options(False)
                call see_expeditions(1)
            "Go back":
                jump go_to_computer
    call see_expeditions(1)

label see_expeditions_for_region(regionNumber):
    $ set_background(f"regions/{regionNumber}")
    call screen expedition_screen(regionNumber)
    return

label check_online_shop():
    call screen online_shop()
    return
