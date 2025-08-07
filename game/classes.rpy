init python:
    # CLASSES
    class BaseProtectorData:
        def __init__(self, strength, dexterity, constitution, 
            intelligence, wisdom, charisma, luck, incrementing_strength, 
            incrementing_dexterity, incrementing_constitution, 
            incrementing_intelligence, incrementing_wisdom, 
            incrementing_charisma, incrementing_luck):
            self.strength = strength
            self.dexterity = dexterity
            self.constitution = constitution
            self.intelligence = intelligence
            self.wisdom = wisdom
            self.charisma = charisma
            self.luck = luck
            self.incrementing_strength = incrementing_strength
            self.incrementing_dexterity = incrementing_dexterity
            self.incrementing_constitution = incrementing_constitution
            self.incrementing_intelligence = incrementing_intelligence
            self.incrementing_wisdom = incrementing_wisdom
            self.incrementing_charisma = incrementing_charisma
            self.incrementing_luck = incrementing_luck
            return
            
        def get_base_strength(self):
            return self.strength
            
        def get_base_dexterity(self):
            return self.dexterity
            
        def get_base_constitution(self):
            return self.constitution
            
        def get_base_intelligence(self):
            return self.intelligence
            
        def get_base_wisdom(self):
            return self.wisdom
            
        def get_base_charisma(self):
            return self.charisma
            
        def get_base_luck(self):
            return self.luck

        def get_base_information(self):
            return 'Strength: ' + str(self.get_base_strength()) + '\n\
                    Dexterity: ' + str(self.get_base_dexterity()) + '\n\
                    Constitution: ' + str(self.get_base_constitution()) + '\n\
                    Intelligence: ' + str(self.get_base_intelligence()) + '\n\
                    Wisdom: ' + str(self.get_base_wisdom()) + '\n\
                    Charisma: ' + str(self.get_base_charisma()) + '\n\
                    Luck: ' + str(self.get_base_luck())

    class Protector:
        # TODO: REFACTOR ALL THIS
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
            global my_protectors_map
            global bossMissions
            
            # TODO: Evaluate if the mission is going to pass or not
            #   -   depending on the type of the mission, different things on the protector would be evaluated

            # getting the show off name for the protector
            bigLetterName = my_protectors_map[self.assignedProtectorName].bigLetterName

            # notifying that the mission was completed
            renpy.notify(f"{bigLetterName} has successfully completed {self.title}.")

            # updating the protector status and xp
            my_protectors_map[self.assignedProtectorName].status = "Available"
            my_protectors_map[self.assignedProtectorName].increasing_xp(self.xp_received * self.daysPassed)

            # Updating wallet
            updating_wallet(self.gold_received)
            
            # updating the boss mission for this stage
            mission_stage = min(((self.difficulty - 1) // 20) + 1, 10)
            bossMission = next((m for m in bossMissions if m.regionNumber == mission_stage), None)
            bossMission.successfulMinorMissions += 1

            # deleting the mission if not training
            if self.mission_id != 0:
                delete_mission(self.mission_id)

            # if training            
            self.neededDaysToFinish = 1
            self.status = "not assigned"
            self.assignedProtectorName = None
            return
    
    class MissionTemplate:
        def __init__(self, title, description, mission_type):
            self.title = title
            self.description = description
            self.mission_type = mission_type
            return

    class BossMission:
        def __init__(self, regionNumber, title, description, successfulMinorMissionsRequired):
            self.regionNumber = regionNumber
            self.title = title
            self.description = description
            self.successfulMinorMissionsRequired = successfulMinorMissionsRequired
            self.successfulMinorMissions = 0
            return