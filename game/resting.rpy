label rest:
    "You went to bed and rested untill the next day."
    $ current_day += 1
    $ online_shop_refresh_in -= 1
    python:
        
        # handling expeditions
        for expedition in allExpeditions:
            expedition.updateDaysPassed()

        for expedition_id in expeditionsToDelete:
            delete_expedition(expedition_id)

        creating_new_expeditions()

        # handling online shop new items
        if online_shop_refresh_in == 0:
            online_shop_refresh_in = 7
            online_shop_variable.update_store()

    jump resting_area