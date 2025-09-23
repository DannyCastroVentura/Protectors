default my_protectors_map = {}
default expeditions_enemies_base_data = {}
default expeditions_bosses_base_data = {}
default protectors_base_information = {}
default allExpeditions = []
default bossExpeditions = []
default weapons = []
default myWeapons = []
default equipments = []
default myEquipments = []
default expeditionsToDelete = []
define config.console = True
# define config.keymap["hide_windows"] = []
default allExpeditionTemplates = []

init python:
    import os
    import json
    import random

    my_protectors_map = {}
    expeditions_enemies_base_data = {}
    expeditions_bosses_base_data = {}
    protectors_base_information = {}
    allExpeditions = []
    bossExpeditions = []
    weapons = []
    myWeapons = []
    equipments = []
    myEquipments = []
    expeditionsToDelete = []
    allExpeditionTemplates = []
    stats_increment_map = {
        "Dexterity": {
            "prio1": "Dexterity",
            "prio2": "Strength"
        },
        "Strength": {
            "prio1": "Strength",
            "prio2": "Dexterity"
        },
        "Magic": {
            "prio1": "Intelligence",
            "prio2": "Wisdom"
        },
        "Tank": {
            "prio1": "Constitution",
            "prio2": "Strength"
        },
        "Shield": {
            "prio1": "Constitution",
            "prio2": "Dexterity"
        },
        "Evasion": {
            "prio1": "Dexterity",
            "prio2": "Luck"
        },
        "Critical": {
            "prio1": "Luck",
            "prio2": "Dexterity"
        },
        "Speed": {
            "prio1": "Speed",
            "prio2": "Dexterity"
        },
        "Political":{
            "prio1": "Charisma",
            "prio2": "Wisdom"
        },
        "Miracle":{
            "prio1": "Wisdom",
            "prio2": "Charisma"
        }
    }
    evolution_increment_map = {
        "DAM": {  # Physical damage dealer
            "increase": [ "Strength", "Dexterity" ],
            "decrease": [ "Intelligence", "Wisdom" ]
        },
        "DAM_SPE": {  # Damage + Speed
            "increase": [ "Strength", "Dexterity", "Speed" ],
            "decrease": [ "Intelligence", "Wisdom" ]
        },
        "DEX": {  # High crit + accuracy
            "increase": [ "Dexterity", "Dexterity", "Luck", "Speed" ],
            "decrease": [ "Intelligence", "Wisdom" ]
        },
        "DEX_TAN": {  # Agile tank
            "increase": [ "Dexterity", "Dexterity", "Constitution" ],
            "decrease": [ "Intelligence", "Wisdom" ]
        },
        "STR": {  # Balanced strength build
            "increase": [ "Strength", "Strength", "Constitution" ],
            "decrease": [ "Intelligence", "Wisdom" ]
        },
        "STR_CON": {  # Balanced strength build
            "increase": [ "Strength", "Constitution" ],
            "decrease": [ "Intelligence", "Wisdom" ]
        },
        "STR_ONLY": {  # Glass cannon
            "increase": [ "Strength" ],
            "decrease": [ "Intelligence", "Wisdom", "Luck" ]
        },
        "STR_STR_STR_CON_SPE": {  # Pure bruiser
            "increase": [ "Strength", "Strength", "Strength", "Constitution", "Speed" ],
            "decrease": [ "Intelligence", "Wisdom", "Luck" ]
        },
        "INT": {  # Pure caster
            "increase": [ "Intelligence", "Intelligence", "Wisdom" ],
            "decrease": [ "Strength", "Dexterity" ]
        },
        "INT_TAN": {  # Battle-mage tank
            "increase": [ "Intelligence", "Wisdom", "Constitution", "Constitution" ],
            "decrease": [ "Strength", "Dexterity" ]
        },
        "INT_EVA": {  # Trickster mage
            "increase": [ "Intelligence", "Wisdom", "Dexterity", "Luck" ],
            "decrease": [ "Strength", "Constitution" ]
        },
        "TAN": {  # Tanky build
            "increase": [ "Constitution", "Constitution", "Strength" ],
            "decrease": [ "Intelligence", "Luck" ]
        },
        "MIR_CON": {  # Spiritual tank
            "increase": [ "Wisdom", "Wisdom", "Constitution" ],
            "decrease": [ "Dexterity", "Intelligence" ]
        },
        "MIR_TAN": {  # Paladin style
            "increase": [ "Wisdom", "Strength", "Constitution" ],
            "decrease": [ "Intelligence" ]
        },
        "MIR_STR_STR": {  # War cleric
            "increase": [ "Wisdom", "Strength", "Strength" ],
            "decrease": [ "Intelligence", "Luck" ]
        },
        "MIR_MIR_DEX": {  # Agile priest
            "increase": [ "Wisdom", "Wisdom", "Dexterity" ],
            "decrease": [ "Strength", "Constitution" ]
        },
        "SHI": {  # Shield-focused
            "increase": [ "Constitution", "Constitution", "Dexterity" ],
            "decrease": [ "Luck", "Speed" ]
        },
        "CON_DEX": {  # constitution and dexterity
            "increase": [ "Constitution", "Dexterity" ],
            "decrease": [ "Intelligence", "Wisdom" ]
        },
        "HP": {  # Health-obsessed
            "increase": [ "Constitution" ],
            "decrease": [ "Dexterity", "Luck" ]
        },
        "EVA": {  # Evasion build
            "increase": [ "Dexterity", "Dexterity", "Dexterity", "Speed", "Speed", "Constitution", "Luck" ],
            "decrease": [ "Strength", "Wisdom", "Intelligence" ]
        },
        "CRI": {  # Critical strike build
            "increase": [ "Dexterity", "Luck", "Luck" ],
            "decrease": [ "Strength", "Constitution", "Wisdom" ]
        },
        "CHA_WIS": {  # Charisma and wisdom
            "increase": [ "Charisma", "Wisdom" ],
            "decrease": [ "Strength", "Constitution", "Speed" ]
        },
        "CHA": {  # Charisma
            "increase": [ "Charisma" ],
            "decrease": [ "Strength", "Constitution", "Speed" ]
        }
    }
    
    percentage_for_increasing_on_evolutions = 0.50
    percentage_for_decreasing_on_evolutions = 0.50
    
    expeditions_needed_for_boss_expedition = 2

    dynamic_backgrounds = {}

    expeditionsListSize = 51
    maxDifficulty = 200
    maxNeededDaysToFinish = 5
    maxDisapearingInThisDays = 10

    background_folder = "images/bg"
    valid_extensions = [".png", ".jpg", ".jpeg", ".webp"]

    xp_starter_size = 10
    xp_size = 20
    increasing_per_level_multiplier_xp = 2

    folder_path = "game\images\protectors"
    full_path = os.path.join(config.basedir, folder_path)
    folder_map = {}

    # Scan and define backgrounds
    for f in renpy.list_files():
        if f.startswith(background_folder + "/") and any(f.endswith(ext) for ext in valid_extensions):
            name = f[len(background_folder) + 1:].rsplit(".", 1)[0]  # Extract filename without folder or extension
            tag_name = "bg " + name  # Prefix the image name with "bg"
            dynamic_backgrounds[name] = tag_name
            renpy.image(tag_name, f)  # Define as a Ren'Py image

    if os.path.isdir(full_path):
        for name in os.listdir(full_path):
            subfolder_path = os.path.join(full_path, name)
            if os.path.isdir(subfolder_path):
                relative_path = os.path.join(folder_path, name).replace("\\", "/")
                folder_map[name] = "/".join(relative_path.split("/")[1:])

    def getImage(path):
        for ext in valid_extensions:
            if renpy.loadable(path + ext):
                return path + ext
        return None

    def set_background(name):
        if name in dynamic_backgrounds:
            tag = dynamic_backgrounds[name]
            
            # Show the background and apply the matrix transformation for night mode
            renpy.scene()
            renpy.show(tag, at_list=[stretch_fullscreen])
        
        else:
            renpy.say("System", f"Background '{name}' not found.")

    def get_folder_from_map(key):
        global folder_map
        """
        Retrieves the path associated with a folder name (key) from the map.
        """
        return folder_map.get(key, None)

    def add_new_protector(protector_name, stage = 1, level = 1):
        global my_protectors_map
        global protectors_base_information
        new_protector = Protector(protector_name, stage, level, "Available", protectors_base_information)
        can_new_protector_use_weapons = new_protector.basePoints.can_it_use_weapons
        if can_new_protector_use_weapons:
            default_weapon_name = new_protector.basePoints.default_weapon
            # get the weapon id
            default_weapon_id = get_weapon_by_name(default_weapon_name).weapon_id

            # add the weapon to our bag
            add_new_weapon_to_our_bag(default_weapon_id)

            # add the weapon to the protector
            new_protector.equip_weapon(default_weapon_id)
        my_protectors_map[protector_name] = new_protector
        return

    def get_count_of_my_protectors():
        global my_protectors_map
        # Parse JSON to Python dictionary
        return len(my_protectors_map)

    def capitalize_first_letter(s):
        if not s:
            return s  # return empty string as is
        return s[0].upper() + s[1:]

    def update_menu_disable_options(value):
        config.menu_include_disabled = value

    def updating_wallet(incoming_money):
        global money
        money = money + incoming_money
        return

    def creating_new_expeditions():
        global allExpeditions
        global expeditionsListSize
        global maxDifficulty
        global maxNeededDaysToFinish
        global maxDisapearingInThisDays
        global allExpeditionTemplates

        for expeditionNumber in range(len(allExpeditions), expeditionsListSize):
            randomNumber = int(random.uniform(1, maxDifficulty))
            neededDaysToFinish = int(random.uniform(1, maxNeededDaysToFinish))
            disapearingInThisDays = int(random.uniform(1, maxDisapearingInThisDays))
            randomExpedition = int(random.uniform(1, len(allExpeditionTemplates) - 1))
            expedition = allExpeditionTemplates[randomExpedition]

            allExpeditions.append(
                Expedition(
                    expedition.title,
                    expedition.description,
                    randomNumber,  # difficulty
                    neededDaysToFinish,
                    disapearingInThisDays,
                    expedition.expedition_type
                )
            )

        # ✅ Sort expeditions by difficulty (ascending)
        allExpeditions.sort(key=lambda m: m.difficulty)
        return


    def marking_expeditions_to_be_deleted(expedition_id):
        global expeditionsToDelete
        expeditionsToDelete.append(expedition_id)
        return

    def delete_expedition(chosen_expedition_id):
        global allExpeditions
        allExpeditions = [e for e in allExpeditions if e.expedition_id != chosen_expedition_id]
        return

    def testing_things():
        # global allExpeditions
        # for mission in allExpeditions:
        #     renpy.say(None, str(mission.title))
        return

    def resetAssignmentsForThisProtectorName(protectorName):
        global allExpeditions
        for expedition in allExpeditions:
            if expedition.assignedProtectorName == protectorName and expedition.status != "started":
                expedition.assignedProtectorName = None
                expedition.status = "not assigned"
        return

    def show_weapons(protector):
        renpy.show_screen("weapon_select", protector)

    def get_weapon_by_id(weapon_id):
        global weapons
        return next(w for w in weapons if w.weapon_id == weapon_id)

    def get_my_protector(protector_name):
        global my_protectors_map
        if protector_name in my_protectors_map.keys():
            return my_protectors_map[protector_name]

    def get_weapon_by_name(weapon_name):
        global weapons
        return next(w for w in weapons if w.name == weapon_name)

    def add_new_weapon_to_our_bag(weapon_id):
        global weapons
        global myWeapons
        weapon = get_weapon_by_id(weapon_id)
        myWeapons.append(weapon)
        return

    def show_equipments(protector, equipment_type):
        renpy.show_screen("equipment_select", protector, equipment_type)
        return

    def send_not_available_notification(protector, additional_message = None):
        if additional_message == None:
            renpy.notify(f"Protector unavailable: {protector.name}")
        else:
            renpy.notify(f"Protector unavailable: {protector.name} - {additional_message}")
        return

    def send_custom_notification(message):
        renpy.notify(f"{message}")
        return
        
    def get_equipment_by_id(equipment_id):
        global equipments
        return next(e for e in equipments if e.equipment_id == equipment_id)

    def add_new_equipment_to_our_bag(equipment_id):
        global equipments
        global myEquipments
        equipment = next(e for e in equipments if e.equipment_id == equipment_id)
        myEquipments.append(equipment)
        return

    def update_evolution_for_protector(protector, option):
        protector.choose_evolution(option)
        protector.promote()
        return

    def open_protectors_box():
        global my_protectors_map
        global protectors_base_information

        all_protectors_array = list(protectors_base_information.keys())
        my_protectors_array = list(my_protectors_map.keys())

        # remove the options on the new array for the protectors we have
        all_protectors_array = [p for p in all_protectors_array if p not in my_protectors_array]

        # randomly get a protector name
        randomProtectorName = all_protectors_array[int(random.uniform(0, len(all_protectors_array)))]

        # and get the protector
        add_new_protector(randomProtectorName)
        return randomProtectorName

    def notify_user_money_is_not_enough(item_name):
        renpy.notify(f"Can't afford to buy {item_name}")
        return

    def buy_new_equipment(equipment):
        add_new_equipment_to_our_bag(equipment.equipment_id)
        updating_wallet(int(0 - equipment.price))
        renpy.notify(f"You’ve purchased a new equipment: {equipment.name}")
        equipment.stillAvailable = False
        return

    def buy_new_weapon(weapon):
        add_new_weapon_to_our_bag(weapon.weapon_id)
        updating_wallet(int(0 - weapon.price))
        renpy.notify(f"You’ve purchased a new weapon: {weapon.name}")
        weapon.stillAvailable = False
        return

    def buy_new_protector(protector):
        add_new_protector(protector.name, protector.stage, protector.level)
        updating_wallet(int(0 - protector.price))
        renpy.notify(f"You’ve purchased a new protector: {protector.name}")
        protector.stillAvailable = False
        return

    def enemy_equip_weapon(enemy, rarity_number):
        if rarity_number >= 0:
            # getting the letter for the rarity
            rank_multipliers_array = {v: k for k, v in rank_multipliers.items()}
            rarity_letter = rank_multipliers_array[rarity_number]
        else:
            rarity_letter = "E"

        # Getting a weapon for the weapon
        #   -   it needs to be of the type that the enemy can use
        #   -   also needs to be according to the rarity he should use
        weapon = next(
            w for w in weapons 
                if w.class_name == enemy.basePoints.usable_weapon_types[0]
                if w.rarity == rarity_letter 
        )

        enemy.set_weapon(weapon)
        return enemy


    def enemy_equip_equipments(enemy, rarity_number, target_class_name):
        rank_multipliers_array = {v: k for k, v in rank_multipliers.items()}
        rarity_letter = rank_multipliers_array[rarity_number]
        # Getting a helmet
        helmet = next(
            e for e in equipments 
                if e.type == "helmet"
                if e.rarity == rarity_letter
                if e.class_name == target_class_name
        )

        # Getting a body armor
        body = next(
            e for e in equipments 
                if e.type == "body"
                if e.rarity == rarity_letter
                if e.class_name == target_class_name
        )

        # Getting pants
        pants = next(
            e for e in equipments 
                if e.type == "pants"
                if e.rarity == rarity_letter
                if e.class_name == target_class_name
        )
        
        # Getting boots
        boots = next(
            e for e in equipments 
                if e.type == "boots"
                if e.rarity == rarity_letter
                if e.class_name == target_class_name
        )

        enemy.set_helmet(helmet)
        enemy.set_body(body)
        enemy.set_pants(pants)
        enemy.set_boots(boots)
        return enemy

    def unlockingExpeditionStage(number):
        global regions_variable
        expedition_stage_names = list(regions_variable.object.keys())
        name = expedition_stage_names[number]
        regions_variable.object[name]['unlocked'] = True
        
        # on finishing the first region we unlock the online shop!
        if number == 1:
            renpy.notify("OnlineStore unlocked!")
            regions_variable.object['OnlineStore']['unlocked'] = True
        return