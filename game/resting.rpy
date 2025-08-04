label rest:
    "You went to bed and rested untill the next day."
    $ current_day = current_day + 1
    
    python:
        for mission in (m for m in allMissions if m.status == "assigned"):
            mission.updateDaysPassed()

        # TODO:
        # also loop for all the missions which are not assigned, 
        # and update the days to dissapear to minus 1, if this is 0, 
        # then we should delete the mission, and once every deletion is concluded, 
        # we should create new missions untill the max count we should have is reached.
        # if mission.title not "training"

    "All assigned missions have been updated."
    jump resting_area