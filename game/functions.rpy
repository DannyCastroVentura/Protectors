default my_protectors_map = {}
default protectors_base_information = {}
default allMissions = []
default bossMissions = []
default weapons = []
default myWeapons = []
default equipments = []
default myEquipments = []
default initial_weapons_choice = []
default missionsToDelete = []
define config.console = True
# define config.keymap["hide_windows"] = []
default allMissionTemplates = []
default stats_increment_map = {
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
    }
}

default evolution_increment_map = {
    "DAM": [ "Dexterity", "Strength" ],
    "DEX": [ "Dexterity", "Strength", "Luck" ],
    "STR": [ "Strength", "Dexterity", "Constitution" ],
    "INT": [ "Intelligence", "Wisdom" ],
    "INT_TAN": [ "Intelligence", "Wisdom", "Constitution" ],
    "INT_EVA": [ "Intelligence", "Wisdom", "Constitution", "Luck", "Dexterity" ],
    "TAN": [ "Constitution", "Strength" ],
    "SHI": [ "Constitution", "Dexterity" ],
    "EVA": [ "Dexterity", "Luck", "Constitution" ],
    "CRI": [ "Dexterity", "Luck" ]
}

init python:
    import os
    import json
    import random

    if 'my_protectors_map' not in globals():
        my_protectors_map = {}

    if 'protectors_base_information' not in globals():
        protectors_base_information = {}
    
    if 'allMissions' not in globals():
        allMissions = []

    if 'bossMissions' not in globals():
        bossMissions = []

    if 'weapons' not in globals():
        weapons = []

    if 'myWeapons' not in globals():
        myWeapons = []

    if 'equipments' not in globals():
        equipments = []
    
    if 'myEquipments' not in globals():
        myEquipments = []

    if 'initial_weapons_choice' not in globals():
        initial_weapons_choice = []

    if 'missionsToDelete' not in globals():
        missionsToDelete = []

    if 'allMissionTemplates' not in globals():
        allMissionTemplates = []

    if 'stats_increment_map' not in globals():
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
            }
        }

    if 'evolution_increment_map' not in globals():
        evolution_increment_map = {
            "DAM": [ "Dexterity", "Strength" ],
            "DEX": [ "Dexterity", "Strength", "Luck" ],
            "STR": [ "Strength", "Dexterity", "Constitution" ],
            "INT": [ "Intelligence", "Wisdom" ],
            "INT_TAN": [ "Intelligence", "Wisdom", "Constitution" ],
            "INT_EVA": [ "Intelligence", "Wisdom", "Constitution", "Luck", "Dexterity" ],
            "TAN": [ "Constitution", "Strength" ],
            "SHI": [ "Constitution", "Dexterity" ],
            "HP": [ "Constitution" ],
            "EVA": [ "Dexterity", "Luck", "Constitution" ],
            "CRI": [ "Dexterity", "Luck" ]
        }

    
    dynamic_backgrounds = {}

    missionsListSize = 51
    maxDifficulty = 200
    maxNeededDaysToFinish = 5
    maxDisapearingInThisDays = 10

    background_folder = "images/bg"
    valid_extensions = [".png", ".jpg", ".jpeg", ".webp"]

    xp_starter_size = 10
    xp_size = 20
    increasing_per_level_multiplier_xp = 2
    
    # showing disabled options
    config.menu_include_disabled = False    

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
        my_protectors_map[protector_name] = Protector(protector_name, stage, level, "Available")
        return my_protectors_map[protector_name]

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

    def creating_new_missions():
        global allMissions
        global missionsListSize
        global maxDifficulty
        global maxNeededDaysToFinish
        global maxDisapearingInThisDays
        global allMissionTemplates

        for missionNumber in range(len(allMissions), missionsListSize):
            randomNumber = int(random.uniform(1, maxDifficulty))
            neededDaysToFinish = int(random.uniform(1, maxNeededDaysToFinish))
            disapearingInThisDays = int(random.uniform(1, maxDisapearingInThisDays))
            randomMission = int(random.uniform(1, len(allMissionTemplates) - 1))
            mission = allMissionTemplates[randomMission]

            allMissions.append(
                Mission(
                    mission.title,
                    mission.description,
                    randomNumber,  # difficulty
                    neededDaysToFinish,
                    disapearingInThisDays,
                    mission.mission_type
                )
            )

        # ✅ Sort missions by difficulty (ascending)
        allMissions.sort(key=lambda m: m.difficulty)
        return


    def marking_missions_to_be_deleted(mission_id):
        global missionsToDelete
        missionsToDelete.append(mission_id)
        return

    def delete_mission(chosen_mission_id):
        global allMissions
        allMissions = [m for m in allMissions if m.mission_id != chosen_mission_id]
        return

    def testing_things():
        # global allMissions
        # for mission in allMissions:
        #     renpy.say(None, str(mission.title))
        return

    def assign_protector(target_mission_id, protectorName):
        global allMissions

        mission_index = next((i for i, m in enumerate(allMissions) if m.mission_id == target_mission_id), -1)

        # assigning protector to the mission
        allMissions[mission_index].assignedProtectorName = protectorName
        allMissions[mission_index].status = "assigned"
        renpy.restart_interaction()
        
        return

    def start_mission(mission, protectorName, success_rate):
        global allMissions
        
        target_mission_id = mission.mission_id
        mission = next(m for m in allMissions if m.mission_id == target_mission_id)
        
        mission.startMission(protectorName, success_rate)

        my_protectors_map[protectorName].status = "In a mission"
        return

    def resetAssignmentsForThisProtectorName(protectorName):
        global allMissions
        for mission in allMissions:
            if mission.assignedProtectorName == protectorName and mission.status != "started":
                mission.assignedProtectorName = None
                mission.status = "not assigned"
        return

    def show_weapons(protector):
        renpy.show_screen("weapon_select", protector)

    def get_weapon_by_id(weapon_id):
        global weapons
        return next(w for w in weapons if w.weapon_id == weapon_id)

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
        
    def get_equipment_by_id(equipment_id):
        global equipments
        return next(e for e in equipments if e.equipment_id == equipment_id)

    def add_new_equipment_to_our_bag(equipment_id):
        global equipments
        global myEquipments
        equipment = next(e for e in equipments if e.equipment_id == equipment_id)
        myEquipments.append(equipment)
        return