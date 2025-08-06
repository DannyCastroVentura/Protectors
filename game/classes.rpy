init python:
    # CLASSES
    class BaseProtectorData:
        def __init__(self, health, damage, atack_speed):
            self.health = health
            self.damage = damage
            self.atack_speed = atack_speed
            return
            
        def get_base_health_information(self):
            return round(self.health * health_size, 2)
        
        def get_base_damage_information(self):
            return round(self.damage * damage_size, 2)
        
        def get_base_atack_speed_information(self):
            return round(self.atack_speed * atack_speed_size, 2)
        
        def get_base_information(self):
            return 'Health: ' + str(self.get_base_health_information()) + ' / ' + 'Damage: ' + str(self.get_base_damage_information()) + ' / ' + 'Atack-speed: ' + str(self.get_base_atack_speed_information())

    class Protector:
        def __init__(self, name, bigLetterName, stage, level, status, xp = 0):
            self.name = name
            self.bigLetterName = bigLetterName
            self.stage = stage
            self.level = level
            self.status = status
            self.xp = xp
            self.readyForPromotion = False
            self.basePoints = protectors_base_information[name]
            self.stats = self.get_current_stats()
            return
        
        def increasing_xp(self, incoming_xp):
            # renpy.say(mc, f"the incoming_xp is: {incoming_xp}")
            self.xp += incoming_xp

            while True:
                xp_needed = self.get_amount_of_xp_needed_for_leveling_up()
                if self.xp >= xp_needed:
                    if self.level == 20 and self.stage == 10:
                        break
                    # Then we are going to level up!
                    self.xp -= xp_needed
                    self.level += 1
                    # check if level is already at 20
                    if self.level == 20:
                        # we need to increase the stage
                        # check if stage is already at 10
                        if self.stage != 10:
                            self.readyForPromotion = True
                            self.stats = self.get_current_stats()
                            break
                        else:
                            self.level = 20
                            self.stage = 10
                            self.readyForPromotion = False
                else:
                    self.stats = self.get_current_stats()
                    break
            return

        def get_amount_of_xp_needed_for_leveling_up(self):
            return ( 
                        round(( xp_starter_size + 
                            (xp_size * increasing_per_level_multiplier_xp * (self.level - 1)) +
                            (xp_size * increasing_per_stage_multiplier_xp * (self.stage - 1)) 
                        ), 2)
                    )

        def get_health_stat(self):
            return round((self.basePoints.health + (self.basePoints.health * (self.level - 1) * level_factor_health * (self.level - 1) * level_factor_health) + 
                        (self.basePoints.health * (self.stage - 1) * stage_factor_health * (self.stage - 1) * stage_factor_health)) * health_size, 2)

        def get_damage_stat(self):
            return round((self.basePoints.damage + (self.basePoints.damage * (self.level - 1) * level_factor_damage * (self.level - 1) * level_factor_damage) + 
                        (self.basePoints.damage * (self.stage - 1) * stage_factor_damage * (self.stage - 1) * stage_factor_damage)) * damage_size, 2)

        def get_atack_speed_stat(self):                        
            return round(self.basePoints.atack_speed, 2)

        def get_current_stats(self):
            return str(
                        self.get_health_stat()
                    ) + " / " + str(
                        self.get_damage_stat()
                    ) + " / " + str(
                        self.get_atack_speed_stat()
                    )
    
        def promote(self):
            self.stage += 1
            self.level = 1
            self.readyForPromotion = False
            self.increasing_xp(0)
            return



    class Mission:
        _id_counter = 0
        def __init__(self, title, description, difficulty, neededDaysToFinish, disapearingInThisDays, mission_type, status = "not assigned", xp_received = None, gold_received = None):
            self.mission_id = Mission._id_counter
            Mission._id_counter += 1
            self.title = title
            self.description = description
            self.difficulty = difficulty
            self.neededDaysToFinish = neededDaysToFinish 
            self.disapearingInThisDays = disapearingInThisDays # this will going to be updated every time a day passes and this mission is assigned #if this reaches 0 and mission title is not "training", then the mission is deleted
            self.mission_type = mission_type
            self.daysPassed = 0 # days passed since the mission started, this will be updated every day passed while the mission is running -> we should multiple the xp received per day worked.
            self.status = status # possible values: not assigned / assigned / started # if the mission title is not training, once this is concluded, this mission needs to be deleted, if not, this needs to be reseted
            self.assignedProtectorName = None # on assigning the protector to a specific mission, this variable is going to be updated accordingly # this needs to be reseted once this mission is finished
            if xp_received == None or gold_received == None:
                randomNumber = renpy.random.randint(0, difficulty)
                self.xp_received = (randomNumber) * 20
                self.gold_received = (difficulty - randomNumber) * 10
            else:
                self.xp_received = xp_received
                self.gold_received = gold_received
            return
        
        def startMission(self, protectorName):
            self.assignedProtectorName = protectorName
            self.status = "started"
            resetAssignmentsForThisProtectorName(protectorName)
            return

        def updateDaysPassed(self):
            if self.status == "started":
                self.neededDaysToFinish -= 1
                self.daysPassed += 1
                if self.neededDaysToFinish <= 0:
                    self.finishMission()
            elif self.mission_id != 0:
                self.disapearingInThisDays -= 1
                if self.disapearingInThisDays <= 0:
                    marking_missions_to_be_deleted(self.mission_id)
            

            return
        
        def finishMission(self):
            # TODO: Evaluate if the mission is going to pass or not
            #   -   depending on the type of the mission, different things on the protector would be evaluated
            bigLetterName = my_protectors_map[self.assignedProtectorName].bigLetterName
            renpy.notify(f"{bigLetterName} has successfully completed {self.title}.")
            self.status = "hidden"
            my_protectors_map[self.assignedProtectorName].status = "Available"
            my_protectors_map[self.assignedProtectorName].increasing_xp(self.xp_received * self.daysPassed)
            self.assignedProtectorName = None
            updating_wallet(self.gold_received)
            self.neededDaysToFinish = 1
            if self.mission_id != 0:
                delete_mission(self.mission_id)
            return
    
    class MissionTemplate:
        def __init__(self, title, description, mission_type):
            self.title = title
            self.description = description
            self.mission_type = mission_type
            return