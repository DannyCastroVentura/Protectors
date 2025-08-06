label rest:
    "You went to bed and rested untill the next day."
    $ current_day = current_day + 1
    python:
        
        for mission in allMissions:
            mission.updateDaysPassed()

        for mission_id in missionsToDelete:
            delete_mission(mission_id)

        creating_new_missions()

    jump resting_area