label send_to_training:
    "You selected [selected_protector.name] to be trained."
    $ selected_protector.status = "Training"
    $ allExpeditions[0].assignProtector(selected_protector.name)
    $ allExpeditions[0].startExpedition()
    jump training_ground