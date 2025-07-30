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


    # CLASSES    
    class BaseProtectorData:
        def __init__(self, health, damage, atack_speed):
            self.health = health
            self.damage = damage
            self.atack_speed = atack_speed
            
        def get_base_information(self):
            return 'Health: ' + str(self.health * health_size) + ' / ' + 'Damage: ' + str(self.damage * damage_size) + ' / ' + 'Atack-speed: ' + str(self.atack_speed * atack_speed_size)
    
    protectors_base_information = {
        "ninja": BaseProtectorData(0.7, 1, 1.3),
        "recruit": BaseProtectorData(1.1, 0.8, 1.1),
        "robot": BaseProtectorData(1.5, 0.75, 0.75),
        "samurai": BaseProtectorData(1.25, 1.25, 0.5),
        "skeleton": BaseProtectorData(0.5, 1.5, 1),
        "templar": BaseProtectorData(1.5, 1.2, 0.3)
    }

    class Protector:
        def __init__(self, name, bigLetterName, stage, level, status, xp = 0):
            self.name = name
            self.bigLetterName = bigLetterName
            self.stage = stage
            self.level = level
            self.status = status
            self.xp = xp
            self.basePoints = protectors_base_information[name]
        
        def increasing_xp(self, incoming_xp):
            self.xp += incoming_xp

            while True:
                xp_needed = (
                    xp_size * increasing_per_level_multiplier_xp * self.level +
                    xp_size * self.stage * increasing_per_stage_multiplier_xp
                )

                if self.xp >= xp_needed:
                    self.xp -= xp_needed
                    self.level += 1

                    # Check for stage-up
                    if self.level >= 20:
                        self.level = 0
                        self.stage += 1

                else:
                    break


        def get_current_status(self):
            my_protector_base_stats = self.basePoints
            real_health = my_protector_base_stats.health + (my_protector_base_stats.health * self.level * increasing_per_level_multiplier_health) + (my_protector_base_stats.health * self.stage * increasing_per_stage_multiplier_health)
            real_damage = my_protector_base_stats.damage + (my_protector_base_stats.damage * self.level * increasing_per_level_multiplier_damage) + (my_protector_base_stats.damage * self.stage * increasing_per_stage_multiplier_damage)
            real_atack_speed = my_protector_base_stats.atack_speed + (my_protector_base_stats.atack_speed * self.level * increasing_per_level_multiplier_atack_speed) + (my_protector_base_stats.atack_speed * self.stage * increasing_per_stage_multiplier_atack_speed)
            returning_string = str(real_health * health_size) + " / " + str(real_damage * damage_size) + " / " + str(real_atack_speed * atack_speed_size)
            return returning_string

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
