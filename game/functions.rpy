init python:
    import os
    import json

    background_folder = "images/bg"
    valid_extensions = [".png", ".jpg", ".jpeg", ".webp"]

    dynamic_backgrounds = {}

    my_protectors_map = {}
    
    # showing disabled options
    config.menu_include_disabled = False

    folder_path = "game\images\protectors"
    full_path = os.path.join(config.basedir, folder_path)
    folder_map = {}

    protectors_base_information = {
        "ninja": {
            "health": 0.7,
            "damage": 1,
            "atack-speed": 1.3
        },
        "recruit": {
            "health": 1.1,
            "damage": 0.8,
            "atack-speed": 1.1
        },
        "robot": {
            "health": 1.5,
            "damage": 0.75,
            "atack-speed": 0.75
        },
        "samurai": {
            "health": 1.25,
            "damage": 1.25,
            "atack-speed": 0.5
        },
        "skeleton": {
            "health": 0.5,
            "damage": 1.5,
            "atack-speed": 1
        },
        "templar": {
            "health": 1.5,
            "damage": 1.2,
            "atack-speed": 0.3
        }
    }

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

    def add_new_protector(protector_name, stage = 0, level = 0):
        global my_protectors_map
        new_protector = {}
        new_protector["name"] = protector_name
        new_protector["bigLetterName"] = capitalize_first_letter(protector_name)
        new_protector["stage"] = stage
        new_protector["level"] = level
        my_protectors_map[protector_name] = new_protector
        return

    def get_protector_base_information(protector_name):
        global protectors_base_information
        protector_base_information_str = 'Health: ' + str(protectors_base_information[protector_name]['health'] * 300) + ' / ' + 'Damage: ' + str(protectors_base_information[protector_name]['damage'] * 30) + ' / ' + 'Atack-speed: ' + str(protectors_base_information[protector_name]['atack-speed'])
        return protector_base_information_str

    def get_count_of_my_protectors():
        global my_protectors_map
        # Parse JSON to Python dictionary
        return len(my_protectors_map)

    def get_current_status_from_my_protector(protector_name):
        global my_protectors_map
        global protectors_base_information
        my_protector_info = my_protectors_map[protector_name]
        my_protector_base_stats = protectors_base_information[protector_name]
        real_health = my_protector_base_stats['health'] + (my_protector_base_stats['health'] * my_protector_info['level'] * 0.1) + (my_protector_base_stats['health'] * my_protector_info['stage'] * 5)
        real_damage = my_protector_base_stats['damage'] + (my_protector_base_stats['damage'] * my_protector_info['level'] * 0.1) + (my_protector_base_stats['damage'] * my_protector_info['stage'] * 5)
        real_atack_speed = my_protector_base_stats['atack-speed'] + (my_protector_base_stats['atack-speed'] * my_protector_info['level'] * 0.1) + (my_protector_base_stats['atack-speed'] * my_protector_info['stage'] * 5)
        returning_string = str(real_health * 300) + " / " + str(real_damage * 30) + " / " + str(real_atack_speed)
        return returning_string

    def capitalize_first_letter(s):
        if not s:
            return s  # return empty string as is
        return s[0].upper() + s[1:]
