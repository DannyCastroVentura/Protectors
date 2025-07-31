label rest:
    "You went to bed and rested untill the next day."
    $ current_day = current_day + 1
    
    python:
        for mission in allMissions:
            if mission.status == "assigned":
                mission.updateDaysPassed()

    "All assigned missions have been updated."
    jump resting_area