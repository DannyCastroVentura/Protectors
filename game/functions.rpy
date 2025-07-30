default my_protectors_map = {}

init python:
    import os
    import json
    
    if 'my_protectors_map' not in globals():
        my_protectors_map = {}
    
    dynamic_backgrounds = {}

    background_folder = "images/bg"
    valid_extensions = [".png", ".jpg", ".jpeg", ".webp"]

    # creating basic multipliers for stat
    health_size = 300
    damage_size = 30
    atack_speed_size = 1
    xp_size = 10

    # multiplier per level
    increasing_per_level_multiplier_health = 0.1
    increasing_per_level_multiplier_damage = 0.1
    increasing_per_level_multiplier_atack_speed = 0.1
    increasing_per_level_multiplier_xp = 0.5

    # multiplier per stage
    increasing_per_stage_multiplier_health = 5
    increasing_per_stage_multiplier_damage = 5
    increasing_per_stage_multiplier_atack_speed = 5
    increasing_per_stage_multiplier_xp = 0.5  

    
    
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

    def add_new_protector(protector_name, stage = 0, level = 0):
        global my_protectors_map
        my_protectors_map[protector_name] = Protector(protector_name, capitalize_first_letter(protector_name), stage, level, "Available")
        return

    def get_count_of_my_protectors():
        global my_protectors_map
        # Parse JSON to Python dictionary
        return len(my_protectors_map)

    def get_current_status_from_my_protector(protector_name):
        global my_protectors_map
        returning_string = my_protectors_map[protector_name].get_current_status()
        return returning_string

    def capitalize_first_letter(s):
        if not s:
            return s  # return empty string as is
        return s[0].upper() + s[1:]
