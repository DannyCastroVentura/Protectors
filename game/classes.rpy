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

        def get_base_information(self):
            return {
                "strength": self.strength,
                "dexterity": self.dexterity,
                "constitution": self.constitution,
                "intelligence": self.intelligence,
                "wisdom": self.wisdom,
                "charisma": self.charisma,
                "luck": self.luck
            }

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
            return

        def increasing_xp(self, incoming_xp):
            if self.level / 20 > (self.stage):
                self.readyForPromotion = True
            # renpy.say(mc, f"the incoming_xp is: {incoming_xp}")

            self.xp += incoming_xp

            while True:
                xp_needed = self.get_amount_of_xp_needed_for_leveling_up()
                if self.xp >= xp_needed:
                    # Then we are going to level up!
                    self.xp -= xp_needed
                    self.level += 1
                    # check if level is ready for promotion
                    if self.level / 20 > (self.stage):
                        # we need to increase the stage
                        # check if stage is already at 10
                        if self.stage != 10:
                            self.readyForPromotion = True
                else:
                    break
            return

        def get_amount_of_xp_needed_for_leveling_up(self):
            return ( 
                round(( xp_starter_size + 
                    (xp_size * increasing_per_level_multiplier_xp * (self.level - 1))
                ), 2)
            )

        # TODO: Think on a way to make the protector stronger depending on the stage level

        def get_strength(self):
            return int(self.basePoints.strength + (self.level * self.basePoints.incrementing_strength))
        
        def get_dexterity(self):
            return int(self.basePoints.dexterity + (self.level * self.basePoints.incrementing_dexterity))
        
        def get_constitution(self):
            return int(self.basePoints.constitution + (self.level * self.basePoints.incrementing_constitution))
        
        def get_intelligence(self):
            return int(self.basePoints.intelligence + (self.level * self.basePoints.incrementing_intelligence))
        
        def get_wisdom(self):
            return int(self.basePoints.wisdom + (self.level * self.basePoints.incrementing_wisdom))
        
        def get_charisma(self):
            return int(self.basePoints.charisma + (self.level * self.basePoints.incrementing_charisma))
        
        def get_luck(self):
            return int(self.basePoints.luck + (self.level * self.basePoints.incrementing_luck))

        def get_current_stats(self):
            return {
                "strength": self.get_strength(),
                "dexterity": self.get_dexterity(),
                "constitution": self.get_constitution(),
                "intelligence": self.get_intelligence(),
                "wisdom": self.get_wisdom(),
                "charisma": self.get_charisma(),
                "luck": self.get_luck()
            }
    
        def promote(self):
            self.stage += 1
            self.readyForPromotion = False
            self.increasing_xp(0)
            return

        def get_health_points(self):
            return int(50 + self.get_constitution() * 10 + self.get_strength() * 2)

        def get_mana_points(self):
            return int(20 + self.get_intelligence() * 5 + self.get_wisdom() * 3)

        # TODO: complete these final stats
        # Physical weapon: Damage = WeaponBaseDamage + Strength * 2 + Dexterity * 1
        # Dexterity weapon: Damage = WeaponBaseDamage + Dexterity * 2 + Strength * 1
        # Magic weapon: MagicDamage = WeaponBaseDamage + Intelligence * 2 + Wisdom * 1
        def get_damage_points(self):
            return 0 

        def get_defense(self):
            return int(self.get_constitution() * 1.5 + self.get_dexterity() * 0.5)
        
        def get_critical_change(self):
            return int(5 + self.get_luck() * 0.5 + self.get_dexterity() * 0.2)

        def get_evasion(self):
            return inf(self.get_dexterity() * 0.4 + self.get_luck() * 0.2)

        def cooldown_reduction(self):
            return int(self.get_wisdom() * 0.05)

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
            if self.mission_id != 0:
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