label base_of_operations():
    $ set_background("base-of-operations")
    menu:
        "Go to computer":
            call go_to_computer()
    jump base_of_operations

label training_ground():
    $ set_background("training-ground")
    menu:
        "Send a protector to train":
            call show_my_available_protectors(False)
    jump training_ground
    
label resting_area():    
    $ set_background("resting-area")
    menu:
        "Rest":
            call rest()
    jump resting_area