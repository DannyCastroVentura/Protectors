init python:
    # CLASSES
    class BaseProtectorData:
        def __init__(self, health, damage, atack_speed):
            self.health = health
            self.damage = damage
            self.atack_speed = atack_speed
            
        def get_base_information(self):
            return 'Health: ' + str(self.health * health_size) + ' / ' + 'Damage: ' + str(self.damage * damage_size) + ' / ' + 'Atack-speed: ' + str(self.atack_speed * atack_speed_size)

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

    class Mission:
        _id_counter = 0
        def __init__(self, title, description, difficulty, neededDaysToFinish, xp_received = None, gold_received = None):
            self.mission_id = Mission._id_counter
            Mission._id_counter += 1
            self.title = title
            self.description = description
            self.difficulty = difficulty
            self.neededDaysToFinish = neededDaysToFinish
            self.daysPassed = 0 # this will going to be updated every time a day passes and this mission is assigned # this needs to be reseted once this mission is finished
            self.status = "hidden" # possible values: hidden / visible / assigned # this needs to be reseted once this mission is finished
            self.assignedProtectorName = None # on assigning the protector to a specific mission, this variable is going to be updated accordingly # this needs to be reseted once this mission is finished
            if xp_received == None or gold_received == None:
                randomNumber = renpy.random.randint(1, difficulty)
                self.xp_received = (randomNumber) * 10
                self.gold_received = (difficulty - randomNumber) * 10
            else:
                self.xp_received = xp_received
                self.gold_received = gold_received
        
        def startMission(self, protectorName):
            self.assignedProtectorName = protectorName
            self.status = "assigned"
        
        def updateDaysPassed(self):
            if self.status == "assigned":
                self.daysPassed += 1
            
            if self.daysPassed == self.neededDaysToFinish:
                self.finishMission()
        
        def finishMission(self):
            self.daysPassed = 0
            self.status = "hidden"
            my_protectors_map[self.assignedProtectorName].status = "Available"
            my_protectors_map[self.assignedProtectorName].increasing_xp(self.xp_received)
            self.assignedProtectorName = None
    