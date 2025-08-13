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
            self.equipedWeapon = None
            self.equipedHelmet = None
            self.equipedBodyArmor = None
            self.equipedPants = None
            self.equipedBoots = None
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

        def equip_weapon(self, weapon_id):
            global myWeapons
            weapon = next(w for w in myWeapons if w.weapon_id == weapon_id)
            if self.equipedWeapon == None:
                self.equipedWeapon = weapon
            else:
                return
            myWeapons.remove(weapon)
            return

        def equip_equipment(self, equipment_id):
            global myEquipments
            equipment = next(e for e in myEquipments if e.equipment_id == equipment_id)
            if equipment.type == "helmet":
                if self.equipedHelmet == None:
                    self.equipedHelmet = equipment
                else:
                    return
                myEquipments.remove(equipment)
            elif equipment.type == "body armor":
                if self.equipedBodyArmor == None:
                    self.equipedBodyArmor = equipment
                else:
                    return
                myEquipments.remove(equipment)
            elif equipment.type == "pants":
                if self.equipedPants == None:
                    self.equipedPants = equipment
                else:
                    return
                myEquipments.remove(equipment)
            elif equipment.type == "boots":
                if self.equipedBoots == None:
                    self.equipedBoots = equipment
                else:
                    return
                myEquipments.remove(equipment)
            return

        def unequip_weapon(self):
            global myWeapons
            myWeapons.append(self.equipedWeapon)
            self.equipedWeapon = None            
            return

        def unequip_equipment(self, type_equipment):
            global myEquipments
            if type_equipment == "helmet":
                myEquipments.append(self.equipedHelmet)
                self.equipedHelmet = None
            if type_equipment == "body armor":
                myEquipments.append(self.equipedBodyArmor)
                self.equipedBodyArmor = None
            if type_equipment == "pants":
                myEquipments.append(self.equipedPants)
                self.equipedPants = None
            if type_equipment == "boots":
                myEquipments.append(self.equipedBoots)
                self.equipedBoots = None
            return

        def get_amount_of_xp_needed_for_leveling_up(self):
            return ( 
                round(( xp_starter_size + 
                    (xp_size * increasing_per_level_multiplier_xp * (self.level - 1))
                ), 2)
            )

        # dexterity -> prio1 -> dexterity
        #           -> prio2 -> strength
        # Strength  -> prio1 -> strength
        #           -> prio2 -> dexterity
        # magic     -> prio1 -> intelligence
        #           -> prio2 -> wisdom
        # tank      -> prio1 -> constitution
        #           -> prio2 -> strength
        # shield    -> prio1 -> constitution
        #           -> prio2 -> dexterity
        # Evasion   -> prio1 -> dexterity
        #           -> prio2 -> luck
        # Critical  -> prio1 -> luck
        #           -> prio2 -> dexterity

        def get_strength(self):
            return int((self.basePoints.strength + (self.level * self.basePoints.incrementing_strength + ((self.stage - 1) * self.level * self.basePoints.incrementing_strength))) * self.get_strength_increments())
        
        def get_dexterity(self):
            return int((self.basePoints.dexterity + (self.level * self.basePoints.incrementing_dexterity + ((self.stage - 1) * self.level * self.basePoints.incrementing_dexterity))) * self.get_dexterity_increments())
        
        def get_constitution(self):
            return int((self.basePoints.constitution + (self.level * self.basePoints.incrementing_constitution + ((self.stage - 1) * self.level * self.basePoints.incrementing_constitution))) * self.get_constitution_increments())
        
        def get_intelligence(self):
            return int((self.basePoints.intelligence + (self.level * self.basePoints.incrementing_intelligence + ((self.stage - 1) * self.level * self.basePoints.incrementing_intelligence))) * self.get_intelligence_increments())
        
        def get_wisdom(self):
            return int((self.basePoints.wisdom + (self.level * self.basePoints.incrementing_wisdom + ((self.stage - 1) * self.level * self.basePoints.incrementing_wisdom))) * self.get_wisdom_increments())
        
        def get_charisma(self):
            return int((self.basePoints.charisma + (self.level * self.basePoints.incrementing_charisma + ((self.stage - 1) * self.level * self.basePoints.incrementing_charisma))) * self.get_charisma_increments())
        
        def get_luck(self):
            return int((self.basePoints.luck + (self.level * self.basePoints.incrementing_luck + ((self.stage - 1) * self.level * self.basePoints.incrementing_luck))) * self.get_luck_increments())
        
        def get_health_points(self):
            return int(50 + self.get_constitution() * 10 + self.get_strength() * 2)

        def get_mana_points(self):
            return int(20 + self.get_intelligence() * 5 + self.get_wisdom() * 3)

        # TODO: make the weapon to also scale, to have a multiplier
        def get_damage_points(self):
            if self.equipedWeapon == None:
                return 3 + self.get_strength() * 2 + self.get_dexterity()
            elif self.equipedWeapon.class_name == "Strength weapon":
                return self.equipedWeapon.base_damage + self.get_strength() * 2 + self.get_dexterity()
            elif self.equipedWeapon.class_name == "Dexterity weapon":
                return self.equipedWeapon.base_damage + self.get_dexterity() * 2 + self.get_strength()
            elif self.equipedWeapon.class_name == "Magic weapon":
                return self.equipedWeapon.base_damage + self.get_intelligence() * 2 + self.get_wisdom()
            return 0 

        def get_defense(self):
            return int(self.get_constitution() * 1.5 + self.get_dexterity() * 0.5)
        
        def get_critical_change(self):
            return int(5 + self.get_luck() * 0.5 + self.get_dexterity() * 0.2)

        def get_evasion(self):
            return inf(self.get_dexterity() * 0.4 + self.get_luck() * 0.2)

        def cooldown_reduction(self):
            return int(self.get_wisdom() * 0.05)

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

        def get_strength_increments(self):
            totalIncrement = 1
            if self.equipedHelmet != None:
                if self.equipedHelmet.class_name == "Strength":
                    totalIncrement += self.equipedHelmet.prio1
                if self.equipedHelmet.class_name == "Dexterity":
                    totalIncrement += self.equipedHelmet.prio2
                if self.equipedHelmet.class_name == "Tank":
                    totalIncrement += self.equipedHelmet.prio2
            if self.equipedBodyArmor != None:
                if self.equipedBodyArmor.class_name == "Strength":
                    totalIncrement += self.equipedBodyArmor.prio1
                if self.equipedBodyArmor.class_name == "Dexterity":
                    totalIncrement += self.equipedBodyArmor.prio2
                if self.equipedBodyArmor.class_name == "Tank":
                    totalIncrement += self.equipedBodyArmor.prio2
            if self.equipedPants != None:
                if self.equipedPants.class_name == "Strength":
                    totalIncrement += self.equipedPants.prio1
                if self.equipedPants.class_name == "Dexterity":
                    totalIncrement += self.equipedPants.prio2
                if self.equipedPants.class_name == "Tank":
                    totalIncrement += self.equipedPants.prio2
            if self.equipedBoots != None:
                if self.equipedBoots.class_name == "Strength":
                    totalIncrement += self.equipedBoots.prio1
                if self.equipedBoots.class_name == "Dexterity":
                    totalIncrement += self.equipedBoots.prio2
                if self.equipedBoots.class_name == "Tank":
                    totalIncrement += self.equipedBoots.prio2
            return totalIncrement
        
        def get_dexterity_increments(self):
            totalIncrement = 1
            if self.equipedHelmet != None:
                if self.equipedHelmet.class_name == "Dexterity":
                    totalIncrement += self.equipedHelmet.prio1
                if self.equipedHelmet.class_name == "Strength":
                    totalIncrement += self.equipedHelmet.prio2
                if self.equipedHelmet.class_name == "Shield":
                    totalIncrement += self.equipedHelmet.prio2
                if self.equipedHelmet.class_name == "Evasion":
                    totalIncrement += self.equipedHelmet.prio1
                if self.equipedHelmet.class_name == "Critical":
                    totalIncrement += self.equipedHelmet.prio1
            if self.equipedBodyArmor != None:
                if self.equipedBodyArmor.class_name == "Dexterity":
                    totalIncrement += self.equipedBodyArmor.prio1
                if self.equipedBodyArmor.class_name == "Strength":
                    totalIncrement += self.equipedBodyArmor.prio2
                if self.equipedBodyArmor.class_name == "Shield":
                    totalIncrement += self.equipedBodyArmor.prio2
                if self.equipedBodyArmor.class_name == "Evasion":
                    totalIncrement += self.equipedBodyArmor.prio1
                if self.equipedBodyArmor.class_name == "Critical":
                    totalIncrement += self.equipedBodyArmor.prio1
            if self.equipedPants != None:
                if self.equipedPants.class_name == "Dexterity":
                    totalIncrement += self.equipedPants.prio1
                if self.equipedPants.class_name == "Strength":
                    totalIncrement += self.equipedPants.prio2
                if self.equipedPants.class_name == "Shield":
                    totalIncrement += self.equipedPants.prio2
                if self.equipedPants.class_name == "Evasion":
                    totalIncrement += self.equipedPants.prio1
                if self.equipedPants.class_name == "Critical":
                    totalIncrement += self.equipedPants.prio1
            if self.equipedBoots != None:
                if self.equipedBoots.class_name == "Dexterity":
                    totalIncrement += self.equipedBoots.prio1
                if self.equipedBoots.class_name == "Strength":
                    totalIncrement += self.equipedBoots.prio2
                if self.equipedBoots.class_name == "Shield":
                    totalIncrement += self.equipedBoots.prio2
                if self.equipedBoots.class_name == "Evasion":
                    totalIncrement += self.equipedBoots.prio1
                if self.equipedBoots.class_name == "Critical":
                    totalIncrement += self.equipedBoots.prio1
            return totalIncrement

        def get_constitution_increments(self):
            totalIncrement = 1
            if self.equipedHelmet != None:
                if self.equipedHelmet.class_name == "Tank":
                    totalIncrement += self.equipedHelmet.prio1
                if self.equipedHelmet.class_name == "Shield":
                    totalIncrement += self.equipedHelmet.prio1
            if self.equipedBodyArmor != None:
                if self.equipedBodyArmor.class_name == "Tank":
                    totalIncrement += self.equipedBodyArmor.prio1
                if self.equipedBodyArmor.class_name == "Shield":
                    totalIncrement += self.equipedBodyArmor.prio1
            if self.equipedPants != None:
                if self.equipedPants.class_name == "Tank":
                    totalIncrement += self.equipedPants.prio1
                if self.equipedPants.class_name == "Shield":
                    totalIncrement += self.equipedPants.prio1
            if self.equipedBoots != None:
                if self.equipedBoots.class_name == "Tank":
                    totalIncrement += self.equipedBoots.prio1
                if self.equipedBoots.class_name == "Shield":
                    totalIncrement += self.equipedBoots.prio1
            return totalIncrement

        def get_intelligence_increments(self):
            totalIncrement = 1
            if self.equipedHelmet != None:
                if self.equipedHelmet.class_name == "Magic":
                    totalIncrement += self.equipedHelmet.prio1
            if self.equipedBodyArmor != None:
                if self.equipedBodyArmor.class_name == "Magic":
                    totalIncrement += self.equipedBodyArmor.prio1
            if self.equipedPants != None:
                if self.equipedPants.class_name == "Magic":
                    totalIncrement += self.equipedPants.prio1
            if self.equipedBoots != None:
                if self.equipedBoots.class_name == "Magic":
                    totalIncrement += self.equipedBoots.prio1
            return totalIncrement

        def get_wisdom_increments(self):
            totalIncrement = 1
            if self.equipedHelmet != None:
                if self.equipedHelmet.class_name == "Magic":
                    totalIncrement += self.equipedHelmet.prio2
            if self.equipedBodyArmor != None:
                if self.equipedBodyArmor.class_name == "Magic":
                    totalIncrement += self.equipedBodyArmor.prio2
            if self.equipedPants != None:
                if self.equipedPants.class_name == "Magic":
                    totalIncrement += self.equipedPants.prio2
            if self.equipedBoots != None:
                if self.equipedBoots.class_name == "Magic":
                    totalIncrement += self.equipedBoots.prio2
            return totalIncrement

        # TODO: create a new class for charisma as well
        def get_charisma_increments(self):
            totalIncrement = 1
            # TODO: add here the increments
            return totalIncrement

        def get_luck_increments(self):
            totalIncrement = 1
            if self.equipedHelmet != None:
                if self.equipedHelmet.class_name == "Evasion":
                    totalIncrement += self.equipedHelmet.prio2
                if self.equipedHelmet.class_name == "Critical":
                    totalIncrement += self.equipedHelmet.prio1
            if self.equipedBodyArmor != None:
                if self.equipedBodyArmor.class_name == "Evasion":
                    totalIncrement += self.equipedBodyArmor.prio2
                if self.equipedBodyArmor.class_name == "Critical":
                    totalIncrement += self.equipedBodyArmor.prio1
            if self.equipedPants != None:
                if self.equipedPants.class_name == "Evasion":
                    totalIncrement += self.equipedPants.prio2
                if self.equipedPants.class_name == "Critical":
                    totalIncrement += self.equipedPants.prio1
            if self.equipedBoots != None:
                if self.equipedBoots.class_name == "Evasion":
                    totalIncrement += self.equipedBoots.prio2
                if self.equipedBoots.class_name == "Critical":
                    totalIncrement += self.equipedBoots.prio1
            return totalIncrement

    
        def promote(self):
            self.stage += 1
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
                self.xp_received = difficulty * 20
                self.gold_received = difficulty * 10
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


    # RARITY COLORS:
    #   S   Crimson Red #DC143C
    #   A   Gold        #FFD700
    #   B   Purple      #9370DB
    #   C   Blue        #1E90FF
    #   D   Green       #32CD32
    #   E   Gray        #A9A9A9
    class Weapon:
        _id_counter = 0
        def __init__(self, name, description, weapon_type, class_name, base_damage, rarity):
            self.weapon_id = Weapon._id_counter
            Weapon._id_counter += 1
            self.name = name # name of the weapon
            self.description = description # a small description for the weapon, it also can have a story of the weapon
            self.type = weapon_type # the type (knife, sword, axe, lance, etc..)
            self.class_name = class_name # dexterity weapon / strength weapon / magic weapon
            self.base_damage = base_damage # damage
            self.rarity = rarity

    class Equipment:
        _id_counter = 0
        def __init__(self, name, description, equipment_type, class_name, prio1, prio2, rarity):
            self.equipment_id = Equipment._id_counter
            Equipment._id_counter += 1
            self.name = name # name of the equipment
            self.description = description # a small description for the equipment, it also can have a story of the equipment
            self.type = equipment_type # the type (helmet, pants, boots, body armor)
            self.class_name = class_name # Dexterity / Strength / Magic / Tank / Shield / Evasion / Critical
            self.prio1 = prio1 # prio1 improvement (str, dex, con, int, wis, cha, luc)
            self.prio2 = prio2 # prio1 improvement (str, dex, con, int, wis, cha, luc)
            self.rarity = rarity