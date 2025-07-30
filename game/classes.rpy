init python:
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

    class missions:
        def __init__(self, mission_id, name, description, difficulty, xp_received, gold_received):
            self.mission_id = mission_id
            self.name = name
            self.description = description
            self.difficulty = difficulty
            self.status = status
            self.xp = xp
            self.basePoints = protectors_base_information[name]