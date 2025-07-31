label rest:
    "You went to bed and rested untill the next day."
    $ current_day = current_day + 1
    
    python:
        for mission in (m for m in allMissions if m.status == "assigned"):
            mission.updateDaysPassed()

    "All assigned missions have been updated."
    jump resting_area