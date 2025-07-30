label base_travel_menu():
    menu:
        "Base of Operations":
            jump base_of_operations
        "Training Ground":
            jump training_ground
        "Resting Area":
            jump resting_area
    return

label base_of_operations():
    $ set_background("base-of-operations")
    "Base of Operations"
    mc "Here we are!"
    mc "What should I do here?"
    menu:
        "Check my missions":
            call check_my_missions()
        "Let's go to elsewhere":
            call base_travel_menu()
    jump base_of_operations

    
label training_ground():
    $ set_background("training-ground")
    "Training Ground"
    mc "Here we are!"
    mc "What should I do here?"
    menu:
        "Send a protector to train":
            call send_a_protector_to_train()
        "Let's go to elsewhere":
            call base_travel_menu()
    jump training_ground
    
label resting_area():
    $ set_background("resting-area")
    "Resting Area"
    mc "Here we are!"
    mc "What should I do here?"
    menu:
        "Rest":
            call rest()
        "Let's go to elsewhere":
            call base_travel_menu()
    jump resting_area


