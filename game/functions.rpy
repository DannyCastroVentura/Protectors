default my_protectors_map = {}
default protectors_base_information = {}
default allMissions = []
define config.console = True

init python:
    import os
    import json
    

    if 'my_protectors_map' not in globals():
        my_protectors_map = {}

    if 'protectors_base_information' not in globals():
        protectors_base_information = {}
    
    if 'allMissions' not in globals():
        allMissions = []
    
    dynamic_backgrounds = {}

    background_folder = "images/bg"
    valid_extensions = [".png", ".jpg", ".jpeg", ".webp"]

    # creating basic multipliers for stat
    health_size = 30
    damage_size = 3
    atack_speed_size = 1
    xp_starter_size = 10
    xp_size = 20

    # multiplier per level
    level_factor_health = 0.05
    level_factor_damage = 0.05
    increasing_per_level_multiplier_xp = 0.5

    # multiplier per stage
    stage_factor_health = 1.5
    stage_factor_damage = 1.5
    increasing_per_stage_multiplier_xp = 10
    
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
        my_protectors_map[protector_name] = Protector(protector_name, capitalize_first_letter(protector_name), stage, level, "Available")
        return

    def get_count_of_my_protectors():
        global my_protectors_map
        # Parse JSON to Python dictionary
        return len(my_protectors_map)

    def capitalize_first_letter(s):
        if not s:
            return s  # return empty string as is
        return s[0].upper() + s[1:]

    def updating_wallet(incoming_money):
        global money
        money = money + incoming_money
        return

    def initializing_things():
        # creating protectors    
        protectors_base_information["ninja"] = BaseProtectorData(0.7, 1, 1.3)
        protectors_base_information["recruit"] = BaseProtectorData(1.1, 0.8, 1.1)
        protectors_base_information["robot"] = BaseProtectorData(1.5, 0.75, 0.75)
        protectors_base_information["samurai"] = BaseProtectorData(1.25, 1.25, 0.5)
        protectors_base_information["skeleton"] = BaseProtectorData(0.5, 1.5, 1)
        protectors_base_information["templar"] = BaseProtectorData(1.5, 1.2, 0.3)

        # Recreate missions
        allMissions.append(Mission("Training", "Send a protector to train in your facilities.", 0, 1, 1900, 0))
        return 