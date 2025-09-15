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


        # checking if the protector is much time not available
        for my_protector_name in my_protectors_map.keys():
            my_protectors_map[my_protector_name].refresh_stats()
            if my_protectors_map[my_protector_name].status != "Available":
                my_protectors_map[my_protector_name].adding_not_available_counter()

    jump resting_area