label rest:
    "You went to bed and rested untill the next day."
    $ current_day = current_day + 1
    python:
        
        for mission in allExpeditions:
            mission.updateDaysPassed()

        for expedition_id in expeditionsToDelete:
            delete_mission(expedition_id)

        creating_new_expeditions()

    jump resting_area