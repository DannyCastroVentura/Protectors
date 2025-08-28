init python:
    import random
    # CLASSES
    class BaseProtectorData:
        def __init__(self, strength, dexterity, constitution, 
            intelligence, wisdom, charisma, luck, incrementing_strength, 
            incrementing_dexterity, incrementing_constitution, 
            incrementing_intelligence, incrementing_wisdom, 
            incrementing_charisma, incrementing_luck, evolution_1, 
            evolution_2, evolution_name_1, evolution_description_1,
            evolution_name_2, evolution_description_2, prefered_weapon_types, unarmed_range):
            self.strength = strength
            self.dexterity = dexterity
            self.constitution = constitution
            self.intelligence = intelligence
            self.wisdom = wisdom
            self.charisma = charisma
            self.morality = int(charisma * 0.6 + wisdom * 0.4)
            self.luck = luck
            self.evolution_1 = evolution_1
            self.evolution_2 = evolution_2
            self.evolution_name_1 = evolution_name_1
            self.evolution_description_1 = evolution_description_1
            self.evolution_name_2 = evolution_name_2
            self.evolution_description_2 = evolution_description_2
            self.incrementing_strength = incrementing_strength
            self.incrementing_dexterity = incrementing_dexterity
            self.incrementing_constitution = incrementing_constitution
            self.incrementing_intelligence = incrementing_intelligence
            self.incrementing_wisdom = incrementing_wisdom
            self.incrementing_charisma = incrementing_charisma
            self.incrementing_luck = incrementing_luck
            self.prefered_weapon_types = prefered_weapon_types.split(",")
            self.unarmed_range = unarmed_range
            self.can_it_use_weapons = True
            if prefered_weapon_types == "":
                self.can_it_use_weapons = False
            return

        def get_base_information(self):
            return {
                "strength": self.strength,
                "dexterity": self.dexterity,
                "constitution": self.constitution,
                "intelligence": self.intelligence,
                "wisdom": self.wisdom,
                "charisma": self.charisma,
                "morality": self.morality,
                "luck": self.luck
            }

    class Protector:
        def __init__(self, name, stage, level, status):
            self.name = name
            self.stage = stage
            self.level = level
            self.status = status
            self.xp = 0
            self.readyForPromotion = False
            self.equipedWeapon = None
            self.equipedHelmet = None
            self.equipedBodyArmor = None
            self.equipedPants = None
            self.equipedBoots = None
            self.basePoints = protectors_base_information[name]
            self.missions_succeeded = 0
            self.missions_failed = 0
            self.missions_went = 0
            self.chosen_evolution = 0
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
            elif equipment.type == "body":
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
            if type_equipment == "body":
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

        def get_strength(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int((self.basePoints.strength + (self.level * self.basePoints.incrementing_strength + ((used_stage - 1) * self.level * self.basePoints.incrementing_strength))) * self.get_increments("Strength") * self.get_evolution_increments("Strength", fake_evolution))
        
        def get_dexterity(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int((self.basePoints.dexterity + (self.level * self.basePoints.incrementing_dexterity + ((used_stage - 1) * self.level * self.basePoints.incrementing_dexterity))) * self.get_increments("Dexterity") * self.get_evolution_increments("Dexterity", fake_evolution))
        
        def get_constitution(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int((self.basePoints.constitution + (self.level * self.basePoints.incrementing_constitution + ((used_stage - 1) * self.level * self.basePoints.incrementing_constitution))) * self.get_increments("Constitution") * self.get_evolution_increments("Constitution", fake_evolution))
        
        def get_intelligence(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int((self.basePoints.intelligence + (self.level * self.basePoints.incrementing_intelligence + ((used_stage - 1) * self.level * self.basePoints.incrementing_intelligence))) * self.get_increments("Intelligence") * self.get_evolution_increments("Intelligence", fake_evolution))
        
        def get_wisdom(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int((self.basePoints.wisdom + (self.level * self.basePoints.incrementing_wisdom + ((used_stage - 1) * self.level * self.basePoints.incrementing_wisdom))) * self.get_increments("Wisdom") * self.get_evolution_increments("Wisdom", fake_evolution))
        
        # TODO: add things to increment charisma attribute
        def get_charisma(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int((self.basePoints.charisma + (self.level * self.basePoints.incrementing_charisma + ((used_stage - 1) * self.level * self.basePoints.incrementing_charisma))) * self.get_increments("Charisma") * self.get_evolution_increments("Charisma", fake_evolution))
        
        def get_luck(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int((self.basePoints.luck + (self.level * self.basePoints.incrementing_luck + ((used_stage - 1) * self.level * self.basePoints.incrementing_luck))) * self.get_increments("Luck") * self.get_evolution_increments("Luck", fake_evolution))
        
        def get_health_points(self):
            return int(50 + self.get_constitution() * 10 + self.get_strength() * 2)

        def get_mana_points(self):
            return int(20 + self.get_intelligence() * 5 + self.get_wisdom() * 3)

        def get_damage_points(self):
            if self.equipedWeapon == None:
                return 3 + self.get_strength() * 2 + self.get_dexterity()
            elif self.equipedWeapon.class_name == "Strength":
                return self.equipedWeapon.base_damage + self.get_strength() * 2 + self.get_dexterity()
            elif self.equipedWeapon.class_name == "Dexterity":
                return self.equipedWeapon.base_damage + self.get_dexterity() * 2 + self.get_strength()
            elif self.equipedWeapon.class_name == "Magic":
                return self.equipedWeapon.base_damage + self.get_intelligence() * 2 + self.get_wisdom()
            return 0 

        def get_critical_change(self):
            return int(5 + self.get_luck() * 0.5 + self.get_dexterity() * 0.5)

        def get_evasion(self):
            return int(self.get_dexterity() * 0.5 + self.get_luck() * 0.5)
        
        def get_defense(self):
            return int(self.get_constitution() * 0.5 + self.get_evasion() * 0.5)
        
        def get_morality(self, fake_stage = None, fake_evolution = None):
            return int(self.get_charisma(fake_stage, fake_evolution) * 0.6 + self.get_wisdom(fake_stage, fake_evolution) * 0.4)

        def cooldown_reduction(self):
            return int(self.get_wisdom() * 0.05)

        def get_current_stats(self, fake_stage = None, fake_evolution = None):
            return {
                "strength": self.get_strength(fake_stage, fake_evolution),
                "dexterity": self.get_dexterity(fake_stage, fake_evolution),
                "constitution": self.get_constitution(fake_stage, fake_evolution),
                "intelligence": self.get_intelligence(fake_stage, fake_evolution),
                "wisdom": self.get_wisdom(fake_stage, fake_evolution),
                "charisma": self.get_charisma(fake_stage, fake_evolution),
                "morality": self.get_morality(fake_stage, fake_evolution),
                "luck": self.get_luck(fake_stage, fake_evolution)
            }
        
        def get_increments(self, searchingClassName):
            totalIncrement = 1
            for className, prios in stats_increment_map.items():
                # helmet
                if self.equipedHelmet is not None:
                    if self.equipedHelmet.class_name == className:
                        if prios["prio1"] == searchingClassName:
                            totalIncrement += self.equipedHelmet.prio1
                        if prios["prio2"] == searchingClassName:
                            totalIncrement += self.equipedHelmet.prio2
                # body
                if self.equipedBodyArmor is not None:
                    if self.equipedBodyArmor.class_name == className:
                        if prios["prio1"] == searchingClassName:
                            totalIncrement += self.equipedBodyArmor.prio1
                        if prios["prio2"] == searchingClassName:
                            totalIncrement += self.equipedBodyArmor.prio2
                # pants
                if self.equipedPants is not None:
                    if self.equipedPants.class_name == className:
                        if prios["prio1"] == searchingClassName:
                            totalIncrement += self.equipedPants.prio1
                        if prios["prio2"] == searchingClassName:
                            totalIncrement += self.equipedPants.prio2
                # boots
                if self.equipedBoots is not None:
                    if self.equipedBoots.class_name == className:
                        if prios["prio1"] == searchingClassName:
                            totalIncrement += self.equipedBoots.prio1
                        if prios["prio2"] == searchingClassName:
                            totalIncrement += self.equipedBoots.prio2
            return totalIncrement

        def get_evolution_increments(self, searchingClassName, fake_evolution = None):
            used_chosen_evolution = self.chosen_evolution
            if fake_evolution != None:
                used_chosen_evolution = fake_evolution
            totalIncrement = 1

            # get what incrementation are we going to add
            if used_chosen_evolution != 0:
                choose_evolution = self.basePoints.evolution_1
                if used_chosen_evolution == 2:
                    choose_evolution = self.basePoints.evolution_2
                # check if this attribute is one of the attributes which will get that incrementation
                if searchingClassName in evolution_increment_map[choose_evolution]:
                    # check how much increment are we going to add to this attribute
                    totalIncrement += total_evolution_increment / len(evolution_increment_map[choose_evolution])
            
            return totalIncrement
    
        def promote(self):
            self.stage += 1
            self.readyForPromotion = False
            self.increasing_xp(0)
            return

        def choose_evolution(self, evolution):
            self.chosen_evolution = evolution
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
            self.success_rate = None # This will have a value once the mission starts
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
        
        def startMission(self, protectorName, success_rate = 100):
            self.assignedProtectorName = protectorName
            self.status = "started"
            self.success_rate = success_rate
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
        
        def get_success_rate(self, protector):
            mission_type = self.mission_type
            protector_stat = 0
            if mission_type == "Rescue":
                protector_stat = protector.get_defense()
            if mission_type == "Recon":
                protector_stat = protector.get_evasion()
            if mission_type == "Political":
                protector_stat = protector.get_charisma()
            if mission_type == "Moral":
                protector_stat = protector.get_morality()
            if mission_type == "Combat":
                protector_stat = protector.get_damage_points() * 0.2
            difficulty = self.difficulty
            needed_stat_value = 10 + difficulty * 3

            return int((protector_stat * 100 / needed_stat_value) + protector.get_luck() * 0.15)

        def finishMission(self):
            global my_protectors_map
            global bossMissions

            # Evaluate if the mission was a success
            success_rate = self.success_rate  # already in percentage (0–100)

            roll = int(random.uniform(0, 100))  # get a random float between 0 and 100

            if success_rate >= roll:
                mission_success = True
                renpy.notify(f"Mission success ✅ (rolled {roll:.2f} vs rate {success_rate}%)")

                # updating xp
                my_protectors_map[self.assignedProtectorName].increasing_xp(self.xp_received * self.daysPassed)

                # updating the missions succeeded on this protector
                my_protectors_map[self.assignedProtectorName].missions_succeeded += 1

                # Updating wallet
                updating_wallet(self.gold_received)
                
                # updating the boss mission for this stage
                mission_stage = min(((self.difficulty - 1) // 20) + 1, 10)

                # if not training, update the bossMission
                if self.mission_id != 0:
                    bossMission = next((m for m in bossMissions if m.regionNumber == mission_stage), None)
                    bossMission.successfulMinorMissions += 1
            else:
                mission_success = False
                renpy.notify(f"Mission failed ❌ (rolled {roll:.2f} vs rate {success_rate}%)")
                
                # updating the missions failed on this protector
                my_protectors_map[self.assignedProtectorName].missions_failed += 1

            
            # updating the protector status and xp
            my_protectors_map[self.assignedProtectorName].status = "Available"
            
            # updating the missions went on this protector
            my_protectors_map[self.assignedProtectorName].missions_went += 1


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
            self.class_name = class_name # dexterity / strength / magic
            self.base_damage = base_damage # damage
            self.rarity = rarity

    class Equipment:
        _id_counter = 0
        def __init__(self, name, description, equipment_type, class_name, prio1, prio2, rarity):
            self.equipment_id = Equipment._id_counter
            Equipment._id_counter += 1
            self.name = name # name of the equipment
            self.description = description # a small description for the equipment, it also can have a story of the equipment
            self.type = equipment_type # the type (helmet, pants, boots, body)
            self.class_name = class_name # Dexterity / Strength / Magic / Tank / Shield / Evasion / Critical
            self.prio1 = prio1 # prio1 improvement (str, dex, con, int, wis, cha, luc)
            self.prio2 = prio2 # prio1 improvement (str, dex, con, int, wis, cha, luc)
            self.rarity = rarity