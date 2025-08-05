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
    menu:
        "Go to computer":
            call go_to_computer()
        "Let's go to elsewhere":
            call base_travel_menu()
    jump base_of_operations

label training_ground():
    $ set_background("training-ground")
    "Training Ground"
    menu:
        "Send a protector to train":
            call show_my_available_protectors(False)
        "Let's go to elsewhere":
            call base_travel_menu()
    jump training_ground
    
label resting_area():    
    $ set_background("resting-area")
    "Resting Area"
    menu:
        "Rest":
            call rest()
        "Let's go to elsewhere":
            call base_travel_menu()
    jump resting_area