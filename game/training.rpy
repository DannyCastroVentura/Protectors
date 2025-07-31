label send_to_training:
    "You selected [selected_protector.name] to be trained."
    $ selected_protector.status = "Training"
    $ allMissions[0].startMission(selected_protector.name)
    jump training_ground