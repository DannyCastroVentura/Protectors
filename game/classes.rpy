init python:
    import random
    import copy
    
    levelAttributeIncrements = 1
    bossLevelPerStage = 25
    melee_starting_period = 10
    ranged_starting_period = 50
    start_fight_timer_period = 100
    fight_you_attacked_message = "You attacked the enemy.."
    fight_you_are_defending_message = "You are now defending.."
    fight_enemy_attacked_message = "Enemy attacked you.."
    fight_enemy_is_defending_message = "Enemy is now defending.."
    fight_victory_message = "You won!"
    fight_defeat_message = "You lost!"
    fight_your_turn_message = "It's your turn"
    fight_enemy_turn_message = "It's the enemy turn"

    bossExpeditionVictoryResult = "Victory!"
    bossExpeditionDefeatResult = "Defeat..."
    bossExpeditionFledResult = "You fled the battle."
            
    # define the base multiplier per rank
    rank_multipliers = {
        "E": 0,  # exponent 0 → base_damage * (ratio^0) = base_damage
        "D": 1,
        "C": 2,
        "B": 3,
        "A": 4,
        "S": 5
    }

    # CLASSES
    class BaseProtectorData:
        def __init__(self, stats, increasing_list, evolution_1, 
            evolution_2, evolution_name_1, evolution_description_1,
            evolution_name_2, evolution_description_2, usable_weapon_types, 
            usable_weapon_types_evolution_1, usable_weapon_types_evolution_2,
            unarmed_range, basic_unarmed_damage_type, evo1_unarmed_damage_type, 
            evo2_unarmed_damage_type, default_weapon):
            self.strength = stats["strength"]
            self.dexterity = stats["dexterity"]
            self.constitution = stats["constitution"]
            self.intelligence = stats["intelligence"]
            self.wisdom = stats["wisdom"]
            self.charisma = stats["charisma"]
            self.speed = stats["speed"]
            self.luck = stats["luck"]
            self.attack_speed = stats["attack_speed"]
            self.increasing_list = increasing_list
            self.evolution_1 = evolution_1
            self.evolution_2 = evolution_2
            self.evolution_name_1 = evolution_name_1
            self.evolution_description_1 = evolution_description_1
            self.evolution_name_2 = evolution_name_2
            self.evolution_description_2 = evolution_description_2
            self.usable_weapon_types = usable_weapon_types
            if usable_weapon_types_evolution_1 == None:
                self.usable_weapon_types_evolution_1 = self.usable_weapon_types
            else:
                self.usable_weapon_types_evolution_1 = usable_weapon_types_evolution_1
            if usable_weapon_types_evolution_2 == None:
                self.usable_weapon_types_evolution_2 = self.usable_weapon_types
            else:
                self.usable_weapon_types_evolution_2 = usable_weapon_types_evolution_2
            self.unarmed_range = unarmed_range
            self.basic_unarmed_damage_type = basic_unarmed_damage_type
            self.evo1_unarmed_damage_type = evo1_unarmed_damage_type
            self.evo2_unarmed_damage_type = evo2_unarmed_damage_type
            self.can_it_use_weapons = True
            if usable_weapon_types == "":
                self.can_it_use_weapons = False
            self.default_weapon = default_weapon
            return

        def get_base_information(self):
            return {
                "strength": self.strength,
                "dexterity": self.dexterity,
                "constitution": self.constitution,
                "intelligence": self.intelligence,
                "wisdom": self.wisdom,
                "charisma": self.charisma,
                "speed": self.speed,
                "luck": self.luck
            }
        
        def increase_attribute(self, att, value = 1):
            setattr(self, att, getattr(self, att) + value)
            return

    class Protector:
        def __init__(self, name, stage, level, status, protector_enemies_map, chosen_evolution_value = None):
            self.name = name
            self.stage = stage
            self.level = level
            self.status = status
            self.xp = 0
            self.not_available_counter = 0
            self.readyForPromotion = False
            self.equipedWeapon = None
            self.equipedHelmet = None
            self.equipedBodyArmor = None
            self.equipedPants = None
            self.equipedBoots = None
            self.basePoints = copy.deepcopy(protector_enemies_map[name])
            self.expeditions_succeeded = 0
            self.expeditions_failed = 0
            self.expeditions_went = 0
            self.boss_expeditions_succeeded = 0
            self.boss_expeditions_failed = 0
            self.boss_expeditions_went = 0
            self.chosen_evolution = 0
            if chosen_evolution_value != None:
                self.chosen_evolution = chosen_evolution_value
            if self.level > 1:
                aux = 1
                while aux <= self.level:
                    self.leveling_up()
                    aux += 1
            self.refresh_stats()

        def refresh_stats(self):
            self.hp = self.get_health_points()
            return

        def adding_not_available_counter(self):
            self.not_available_counter += 1
            if self.not_available_counter >= 10:
                self.status = "Available"
                self.not_available_counter = 0
                renpy.notify(f"Something unexpected occured, but {self.name} is back!")
            return

        def reset_not_available_counter(self):
            self.not_available_counter = 0
            return

        def leveling_up(self):
            attribute_train = self.basePoints.increasing_list['basic']
            if self.chosen_evolution != None:
                if self.chosen_evolution == 1:
                    attribute_train = self.basePoints.increasing_list['evolution1']
                elif self.chosen_evolution == 2:
                    attribute_train = self.basePoints.increasing_list['evolution2']
            # Add the needed attributes to the base stats variable accordingly
            for i in range(levelAttributeIncrements):
                attribute = attribute_train.pop(0)
                self.basePoints.increase_attribute(attribute)
                attribute_train.append(attribute)
            self.refresh_stats()

        def re_evaluate_level_points(self):
            global protectors_base_information
            self.basePoints = copy.deepcopy(protectors_base_information[self.name])
            xp_needed = self.get_total_xp_needed_for_level(self.level)
            self.level = 0
            self.increasing_xp(xp_needed)
            return
        
        def increasing_xp(self, incoming_xp):
            if self.level / 20 > (self.stage):
                if self.stage != 10:
                    self.readyForPromotion = True

            self.xp += incoming_xp

            while True:
                xp_needed = self.get_amount_of_xp_needed_for_leveling_up()
                if self.xp >= xp_needed:
                    # Then we are going to level up!
                    self.xp -= xp_needed
                    self.level += 1

                    self.leveling_up()

                    # check if level is ready for promotion
                    if self.level / 20 >= (self.stage):
                        # we need to increase the stage
                        # check if stage is already at 10
                        if self.stage != 10:
                            self.readyForPromotion = True
                else:
                    break
            return
        
        def set_status(self, status_message):
            self.status = status_message
            return

        def set_weapon(self, weapon):
            self.equipedWeapon = weapon
            return

        def set_helmet(self, helmet):
            self.equipedHelmet = helmet
            return

        def set_body(self, body):
            self.equipedBodyArmor = body
            return

        def set_pants(self, pants):
            self.equipedPants = pants
            return

        def set_boots(self, boots):
            self.equipedBoots = boots
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

        def get_amount_of_xp_needed_for_leveling_up(self, lvl = None):
            if lvl == None:
                lvl = self.level
            return ( 
                round(( xp_starter_size + 
                    (xp_size * increasing_per_level_multiplier_xp * (lvl - 1))
                ), 2)
            )

        def get_total_xp_needed_for_level(self, target_level: int) -> float:
            """
            Calculate the total amount of XP required to reach a given level from level 1.
            
            :param target_level: The level you want to reach.
            :return: The total XP required.
            """
            total_xp = 0.0
            for lvl in range(1, target_level):
                total_xp += self.get_amount_of_xp_needed_for_leveling_up(lvl)
            return round(total_xp, 2)

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
            return int(self.basePoints.strength * used_stage * self.get_increments("Strength") * self.get_evolution_increments("Strength", fake_evolution))
        
        def get_dexterity(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int(self.basePoints.dexterity * used_stage * self.get_increments("Dexterity") * self.get_evolution_increments("Dexterity", fake_evolution))
        
        def get_constitution(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int(self.basePoints.constitution * used_stage * self.get_increments("Constitution") * self.get_evolution_increments("Constitution", fake_evolution))
        
        def get_intelligence(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int(self.basePoints.intelligence * used_stage * self.get_increments("Intelligence") * self.get_evolution_increments("Intelligence", fake_evolution))
        
        def get_wisdom(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int(self.basePoints.wisdom * used_stage * self.get_increments("Wisdom") * self.get_evolution_increments("Wisdom", fake_evolution))
        
        # TODO: add things to increment charisma attribute
        def get_charisma(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int(self.basePoints.charisma * used_stage * self.get_increments("Charisma") * self.get_evolution_increments("Charisma", fake_evolution))

        def get_speed(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int(self.basePoints.speed * used_stage * self.get_increments("Speed") * self.get_evolution_increments("Speed", fake_evolution))
        
        def get_luck(self, fake_stage = None, fake_evolution = None):
            used_stage = self.stage
            if fake_stage != None:
                used_stage = fake_stage
            return int(self.basePoints.luck * used_stage * self.get_increments("Luck") * self.get_evolution_increments("Luck", fake_evolution))
        
        def get_health_points(self):
            return int(50 + self.get_constitution() * 10 + self.get_strength() * 2)

        def get_mana_points(self):
            return int(20 + self.get_intelligence() * 5 + self.get_wisdom() * 3)

        def get_damage_points(self):
            value = 0
            type_damage = 0.5

            if self.basePoints.can_it_use_weapons == False:
                type_damage = 1.2

            using_unarmed_damage_type = self.basePoints.basic_unarmed_damage_type
            if self.chosen_evolution != None:
                if self.chosen_evolution == 1:
                    using_unarmed_damage_type = self.basePoints.evo1_unarmed_damage_type
                elif self.chosen_evolution == 2:
                    using_unarmed_damage_type = self.basePoints.evo2_unarmed_damage_type

            weapon_base_damage = 3
            if self.equipedWeapon == None:
                if using_unarmed_damage_type == "Regular":
                    value = (self.get_strength() * 2 + self.get_dexterity() + self.get_luck()) * type_damage
                elif using_unarmed_damage_type == "Magic":
                    value = (self.get_intelligence() * 2 + self.get_wisdom() + self.get_luck()) * type_damage
                elif using_unarmed_damage_type == "Divine":
                    value = (self.get_wisdom() * 3 + self.get_luck()) * type_damage
            else:
                if self.equipedWeapon.class_name == "Strength":
                    value = (self.get_strength() * 2 + self.get_dexterity() + self.get_luck())
                elif self.equipedWeapon.class_name == "Dexterity":
                    value = (self.get_dexterity() * 2 + self.get_strength() + self.get_luck())
                elif self.equipedWeapon.class_name == "Magic":
                    value = (self.get_intelligence() * 2 + self.get_wisdom() + self.get_luck())
                elif self.equipedWeapon.class_name == "Divine":
                    value = (self.get_wisdom() * 3 + self.get_luck())

                # # commenting this out because I don't want the damage output to be depending on the type of the weapon
                # # it seemed a good idea, but thinking about it, I'm not sure if I like that idea anymore
                # class_damage = 0.5
                # if self.equipedWeapon.type == "Axe" or self.equipedWeapon.type == "Hammer" or self.equipedWeapon.type == "Mace":
                #     value += (self.get_strength() * 2 + self.get_dexterity() + self.get_luck()) * class_damage
                # elif self.equipedWeapon.type == "Cards" or self.equipedWeapon.type == "Gun" or self.equipedWeapon.type == "Machine gun" or self.equipedWeapon.type == "Sniper":
                #     value += (self.get_dexterity() * 3 + self.get_luck()) * class_damage
                # elif self.equipedWeapon.type == "Great Hammer" or self.equipedWeapon.type == "Greataxe" or self.equipedWeapon.type == "Greatsword":
                #     value += (self.get_strength() * 2.7 + self.get_dexterity() * 0.3 + self.get_luck()) * class_damage
                # elif self.equipedWeapon.type == "Katana" or self.equipedWeapon.type == "Spear" or self.equipedWeapon.type == "Sword":
                #     value += (self.get_strength() * 1.5 + self.get_dexterity() * 1.5 + self.get_luck()) * class_damage
                # elif self.equipedWeapon.type == "Knife":
                #     value += (self.get_dexterity() * 2 + self.get_strength() * 1 + self.get_luck()) * class_damage
                # elif self.equipedWeapon.type == "Staff" or self.equipedWeapon.type == "Wand":
                #     value += (self.get_intelligence() * 2 + self.get_wisdom() * 1 + self.get_luck()) * class_damage
                # elif self.equipedWeapon.type == "Book":
                #     value += (self.get_wisdom() * 3 + self.get_luck()) * class_damage
                
                weapon_base_damage = self.equipedWeapon.base_damage
                if self.equipedWeapon.type == "Staff" or self.equipedWeapon.type == "Wand":
                    weapon_base_damage += (self.get_intelligence() * (1/3) + self.get_wisdom() * (1/6)) * (rank_multipliers.get(self.equipedWeapon.rarity, 0) + 1)
                elif self.equipedWeapon.type == "Book":
                    weapon_base_damage += (self.get_wisdom()) * (1/2) * (rank_multipliers.get(self.equipedWeapon.rarity, 0) + 1)
            return int(value + weapon_base_damage)

        def get_critical_chance(self):
            critical_chance = round(0.05 + self.get_luck() * 0.001 + self.get_dexterity() * 0.0005, 4)
            if critical_chance > 1:
                critical_chance = 1
            return critical_chance
        
        def get_critical_damage(self):
            critical_damage = round(1.5 + self.get_dexterity() * 0.001 + self.get_luck() * 0.0005 + self.get_strength() * 0.0005, 2)

            # Get the critical boost from the weapon
            if self.equipedWeapon != None:
                critical_damage *= self.equipedWeapon.crit_damage

            return critical_damage

        def get_evasion(self):
            return round(self.get_dexterity() * 0.03 + self.get_luck() * 0.003, 2)

        def get_recon_points(self):
            return round(self.get_dexterity() * 0.5 + self.get_speed() * 0.5 + self.get_evasion() * 10, 2)

        def get_rescue_points(self):
            return round(self.get_defense() * 0.2 + self.get_recon_points() * 0.8, 2)
        
        def get_defense(self):
            return round(self.get_defense_from_equipment() + int(self.get_constitution() * 0.5 + self.get_evasion() * 0.5), 2)
        
        def get_morality(self, fake_stage = None, fake_evolution = None):
            return round(self.get_charisma(fake_stage, fake_evolution) * 0.6 + self.get_wisdom(fake_stage, fake_evolution) * 0.4, 2)

        def get_cooldown_reduction(self):
            return round(self.get_wisdom() * 0.05, 2)

        def get_attack_speed(self):
            atack_speed = round(self.basePoints.attack_speed + self.get_dexterity() * 0.001 + self.get_speed() * 0.0005, 2)
            
            # Get the attack speed boost from the weapon
            if self.equipedWeapon != None:
                atack_speed *= self.equipedWeapon.attack_speed_boost
            return atack_speed

        def get_current_stats(self, fake_stage = None, fake_evolution = None):
            return {
                "strength": self.get_strength(fake_stage, fake_evolution),
                "dexterity": self.get_dexterity(fake_stage, fake_evolution),
                "constitution": self.get_constitution(fake_stage, fake_evolution),
                "intelligence": self.get_intelligence(fake_stage, fake_evolution),
                "wisdom": self.get_wisdom(fake_stage, fake_evolution),
                "charisma": self.get_charisma(fake_stage, fake_evolution),
                "speed": self.get_speed(fake_stage, fake_evolution),
                "luck": self.get_luck(fake_stage, fake_evolution),                
                "attack_speed": self.get_attack_speed(),
                "defense": self.get_defense(),
                "evasion": self.get_evasion(),
                "morality": self.get_morality(),
                "cooldown_reduction": self.get_cooldown_reduction(),
                "critical_chance": self.get_critical_chance(),
                "critical_damage": self.get_critical_damage()
            }

        def get_defense_from_equipment(self):
            total_defense = 0
            if self.equipedHelmet != None:
                total_defense = total_defense + self.equipedHelmet.base_defense
            if self.equipedBodyArmor != None:
                total_defense = total_defense + self.equipedBodyArmor.base_defense
            if self.equipedPants != None:
                total_defense = total_defense + self.equipedPants.base_defense
            if self.equipedBoots != None:
                total_defense = total_defense + self.equipedBoots.base_defense
            return total_defense
        
        def get_increments(self, searchingClassName):
            totalIncrement = 1
            for className, prios in stats_increment_map.items():
                # helmet
                if self.equipedHelmet is not None:
                    if self.equipedHelmet.class_name == className:
                        if prios["prio1"] == searchingClassName:
                            totalIncrement += (self.equipedHelmet.prio1 / 100)
                        if prios["prio2"] == searchingClassName:
                            totalIncrement += (self.equipedHelmet.prio2 / 100)
                # body
                if self.equipedBodyArmor is not None:
                    if self.equipedBodyArmor.class_name == className:
                        if prios["prio1"] == searchingClassName:
                            totalIncrement += (self.equipedBodyArmor.prio1 / 100)
                        if prios["prio2"] == searchingClassName:
                            totalIncrement += (self.equipedBodyArmor.prio2 / 100)
                # pants
                if self.equipedPants is not None:
                    if self.equipedPants.class_name == className:
                        if prios["prio1"] == searchingClassName:
                            totalIncrement += (self.equipedPants.prio1 / 100)
                        if prios["prio2"] == searchingClassName:
                            totalIncrement += (self.equipedPants.prio2 / 100)
                # boots
                if self.equipedBoots is not None:
                    if self.equipedBoots.class_name == className:
                        if prios["prio1"] == searchingClassName:
                            totalIncrement += (self.equipedBoots.prio1 / 100)
                        if prios["prio2"] == searchingClassName:
                            totalIncrement += (self.equipedBoots.prio2 / 100)
            return totalIncrement

        def get_evolution_increments(self, searchingAttributeName, fake_evolution = None):
            used_chosen_evolution = self.chosen_evolution
            if fake_evolution != None:
                used_chosen_evolution = fake_evolution
            totalIncrement = 1

            # get what incrementation are we going to add
            if used_chosen_evolution != 0:
                choosed_evolution = self.basePoints.evolution_1
                if used_chosen_evolution == 2:
                    choosed_evolution = self.basePoints.evolution_2

                # check if this attribute is one of the attributes which will get that incrementation
                increment_array = evolution_increment_map[choosed_evolution]["increase"]
                if searchingAttributeName in increment_array:
                    count_times_there = increment_array.count(searchingAttributeName)
                    # check how much increment are we going to add to this attribute
                    totalIncrement += percentage_for_increasing_on_evolutions / len(increment_array) * count_times_there
                    
                # check if this attribute is one of the attributes which will get that decrementation
                decrement_array = evolution_increment_map[choosed_evolution]["decrease"]
                if searchingAttributeName in decrement_array:
                    count_times_there = decrement_array.count(searchingAttributeName)
                    # check how much increment are we going to add to this attribute
                    totalIncrement -= percentage_for_decreasing_on_evolutions / len(decrement_array) * count_times_there
            return totalIncrement
    
        def promote(self):
            self.stage += 1
            self.readyForPromotion = False
            self.increasing_xp(0)
            return

        def choose_evolution(self, evolution):
            self.chosen_evolution = evolution
            self.basePoints.usable_weapon_types = self.basePoints.usable_weapon_types_evolution_1
            if evolution == 2:
                self.basePoints.usable_weapon_types = self.basePoints.usable_weapon_types_evolution_2
            if self.equipedWeapon != None:
                if self.equipedWeapon.type not in self.basePoints.usable_weapon_types:
                    self.unequip_weapon()

            self.re_evaluate_level_points()
            return

    class Expedition:
        _id_counter = 0
        def __init__(self, title, description, difficulty, neededDaysToFinish, disapearingInThisDays, expedition_type, status = "not assigned", xp_received = None, gold_received = None):
            self.expedition_id = Expedition._id_counter
            Expedition._id_counter += 1
            self.title = title + " - N" + str(self.expedition_id)
            self.description = description
            self.difficulty = difficulty
            self.neededDaysToFinish = neededDaysToFinish 
            self.disapearingInThisDays = disapearingInThisDays # this will going to be updated every time a day passes and this mission is assigned #if this reaches 0 and mission title is not "training", then the mission is deleted
            self.expedition_type = expedition_type
            self.success_rate = None # This will have a value once the mission starts
            self.daysPassed = 0 # days passed since the mission started, this will be updated every day passed while the mission is running -> we should multiple the xp received per day worked.
            self.status = status # possible values: not assigned / assigned / started # if the mission title is not training, once this is concluded, this mission needs to be deleted, if not, this needs to be reseted
            self.assignedProtectorName = None # on assigning the protector to a specific mission, this variable is going to be updated accordingly # this needs to be reseted once this mission is finished
            if xp_received == None or gold_received == None:
                self.gold_received = difficulty * 10
                self.xp_received = self.gold_received * 2
            else:
                self.xp_received = xp_received
                self.gold_received = gold_received

            
            enemy = None
            enemy_target_value = None
            chosen_evolution_value = 0
            enemy_stage = None
            rarity_number = None
            rank_multipliers_array = None
            weapon = None
            target_class_name = None
            helmet = None
            body = None
            pants = None
            boots = None

            if expedition_type != "Training":
                
                if difficulty >= 100:
                    chosen_evolution_value = 1
                    
                enemy_stage = int((difficulty - 1) / 20)
                
                enemy = Protector(expedition_type, enemy_stage + 1, difficulty, "Available", expeditions_enemies_base_data, chosen_evolution_value)
                
                # calculating rarity of weapon
                rarity_number = int(enemy.level * len(rank_multipliers) / maxDifficulty)

                enemy_equip_weapon(enemy, rarity_number)

                # if combat:
                target_class_name = "Tank"
                if self.expedition_type == "Moral":
                    target_class_name = "Political"
                elif self.expedition_type == "Political":
                    target_class_name = "Political"
                elif self.expedition_type == "Recon":
                    target_class_name = "Speed"
                elif self.expedition_type == "Rescue":
                    target_class_name = "Shield"

                enemy = enemy_equip_equipments(enemy, rarity_number, target_class_name)

                # Assign the target value of the needed thing for this expedition_type
                if self.expedition_type == "Combat":
                    enemy_target_value = enemy.get_damage_points() * enemy.get_attack_speed() + enemy.get_health_points()
                elif self.expedition_type == "Moral":
                    enemy_target_value = enemy.get_morality()
                elif self.expedition_type == "Political":
                    enemy_target_value = enemy.get_charisma()
                elif self.expedition_type == "Recon":
                    enemy_target_value = enemy.get_recon_points()
                elif self.expedition_type == "Rescue":
                    enemy_target_value = enemy.get_rescue_points()

                self.target_value = enemy_target_value
            return
        
        def startExpedition(self, success_rate = 100):
            protectorName = self.assignedProtectorName
            self.status = "started"
            self.success_rate = success_rate
            my_protector = get_my_protector(protectorName)
            my_protector.set_status("In a mission")
            resetAssignmentsForThisProtectorName(protectorName)
            return

        def assignProtector(self, protectorName):
            self.assignedProtectorName = protectorName
            self.status = "assigned"
            return

        def unassignProtector(self):
            self.assignedProtectorName = None
            self.status = "not assigned"
            return

        def updateDaysPassed(self):
            # if started, we don't make it disapear
            if self.status == "started":
                self.neededDaysToFinish -= 1
                self.daysPassed += 1
                if self.neededDaysToFinish <= 0:
                    self.finishExpedition()
            # we want to update every expedition, except for 0 as 0 is the training
            elif self.expedition_id != 0:
                self.disapearingInThisDays -= 1
                if self.disapearingInThisDays <= 0:
                    marking_expeditions_to_be_deleted(self.expedition_id)
            return
        
        def get_success_rate(self, protector):
            expedition_type = self.expedition_type
            protector_stat = 0
            if expedition_type == "Rescue":
                protector_stat = protector.get_rescue_points()
            if expedition_type == "Recon":
                protector_stat = protector.get_recon_points()
            if expedition_type == "Political":
                protector_stat = protector.get_charisma()
            if expedition_type == "Moral":
                protector_stat = protector.get_morality()
            if expedition_type == "Combat":
                protector_stat = protector.get_damage_points() * protector.get_attack_speed() + protector.get_health_points()
            difficulty = self.difficulty

            return int((protector_stat * 100 / self.target_value) + protector.get_luck() * 0.15)

        def finishExpedition(self):
            global my_protectors_map
            global bossExpeditions

            # Evaluate if the mission was a success
            success_rate = self.success_rate  # already in percentage (0–100)

            roll = int(random.uniform(0, 100))  # get a random float between 0 and 100

            if success_rate >= roll:
                mission_success = True

                # updating xp
                my_protectors_map[self.assignedProtectorName].increasing_xp(self.xp_received * self.daysPassed)

                # updating the expeditions succeeded on this protector
                my_protectors_map[self.assignedProtectorName].expeditions_succeeded += 1

                # Updating wallet
                updating_wallet(self.gold_received)
                
                # updating the boss mission for this stage
                mission_stage = min(((self.difficulty - 1) // 20) + 1, 10)

                # if not training, update the bossExpedition
                if self.expedition_id != 0:
                    bossExpedition = next((m for m in bossExpeditions if m.regionNumber == mission_stage), None)
                    bossExpedition.successfulMinorExpeditions += 1

                if my_protectors_map[self.assignedProtectorName].readyForPromotion == True:
                    # TODO: make this show a report instead of poping up this notification
                    # notifying that the mission was a success!
                    messages = [
                        f"Expedition success (rolled {roll:.2f} vs rate {success_rate}%)",
                        f"{self.assignedProtectorName} is ready for promotion!"
                    ]
                    renpy.notify(messages)
                    
                else:
                    # TODO: make this show a report instead of poping up this notification
                    # notifying that the mission was a success!
                    renpy.notify(f"Expedition success ✅ (rolled {roll:.2f} vs rate {success_rate}%)")
            else:
                mission_success = False
                # TODO: make this show a report instead of poping up this notification
                renpy.notify(f"Expedition failed ❌ (rolled {roll:.2f} vs rate {success_rate}%)")
                
                # updating the expeditions failed on this protector
                my_protectors_map[self.assignedProtectorName].expeditions_failed += 1

            
            # updating the protector status and xp
            my_protectors_map[self.assignedProtectorName].status = "Available"

            # Reset counter
            my_protectors_map[self.assignedProtectorName].reset_not_available_counter()
            
            # updating the expeditions went on this protector
            my_protectors_map[self.assignedProtectorName].expeditions_went += 1


            # deleting the mission if not training
            if self.expedition_id != 0:
                delete_expedition(self.expedition_id)

            # if training            
            self.neededDaysToFinish = 1
            self.status = "not assigned"
            self.assignedProtectorName = None
            return
    
    class ExpeditionTemplate:
        def __init__(self, title, description, expedition_type):
            self.title = title
            self.description = description
            self.expedition_type = expedition_type
            return

    class BossExpedition:
        def __init__(self, regionNumber, title, description, successfulMinorExpeditionsRequired):
            self.regionNumber = regionNumber
            self.title = title
            self.description = description
            self.successfulMinorExpeditionsRequired = successfulMinorExpeditionsRequired
            self.successfulMinorExpeditions = 0
            self.assignedProtectorName = None
            self.status = "not assigned"
            self.gold_received = regionNumber * 300
            self.xp_received = self.gold_received * 2

        def assignProtector(self, protectorName):
            self.assignedProtectorName = protectorName
            self.status = "assigned"
            return

        def unassignProtector(self):
            self.assignedProtectorName = None
            self.status = "not assigned"
            return

        def startBossExpedition(self):
            my_protector = get_my_protector(self.assignedProtectorName)
            chosen_evolution_value = 0
            if self.regionNumber * bossLevelPerStage >= 100:
                chosen_evolution_value = 1
            enemy = Protector(self.title, self.regionNumber, self.regionNumber * bossLevelPerStage, "expedition_boss_status", expeditions_bosses_base_data, chosen_evolution_value)
            
            maxDifficulty = bossLevelPerStage * 10

            # calculating rarity of weapon
            rarity_number = int(enemy.level * len(rank_multipliers) / maxDifficulty)

            enemy = enemy_equip_weapon(enemy, rarity_number)
            
            # Getting equipments
            if rarity_number >= 0:
                if self.title == "The Mireborn Tyrant":
                    target_class_name = "Tank"
                if self.title == "The Pale King":
                    target_class_name = "Miracle"

                enemy = enemy_equip_equipments(enemy, rarity_number, target_class_name)

            enemy.refresh_stats()
            fight = Fight(my_protector, enemy, self)
            renpy.hide_screen("expedition_screen")
            renpy.show_screen("boss_expedition", self, fight)
            return

        def finishBossExpedition(self, result):
            if result == bossExpeditionVictoryResult:
                # updating xp
                my_protectors_map[self.assignedProtectorName].increasing_xp(self.xp_received)

                # updating the expeditions succeeded on this protector
                my_protectors_map[self.assignedProtectorName].boss_expeditions_succeeded += 1

                # Updating wallet
                updating_wallet(self.gold_received)

                # unlock the next region
                if self.regionNumber != 10:
                    unlockingExpeditionStage(self.regionNumber)
                
                # check if the protector is now ready for promotion
                if my_protectors_map[self.assignedProtectorName].readyForPromotion == True:
                    # TODO: make this show a report instead of poping up this notification
                    renpy.notify(f"{self.assignedProtectorName} is ready for promotion!")
                    
            elif result == bossExpeditionDefeatResult or result == bossExpeditionVictoryResult:                
                # updating the expeditions failed on this protector
                my_protectors_map[self.assignedProtectorName].boss_expeditions_failed += 1

            # updating the expeditions went on this protector
            my_protectors_map[self.assignedProtectorName].boss_expeditions_went += 1

            # reseting the BossExpedition
            self.successfulMinorExpeditions = 0
            self.assignedProtectorName = None
            self.status = "not assigned"
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
        _names_list = []
        def __init__(self, name, description, weapon_type, class_name, _range, rarity):
            self.weapon_id = Weapon._id_counter
            Weapon._id_counter += 1
            if name in Weapon._names_list:
                raise ExceptionType("Error message")
            else:
                Weapon._names_list.append(name)
            self.name = name # name of the weapon
            self.description = description # a small description for the weapon, it also can have a story of the weapon
            self.type = weapon_type # the type (knife, sword, axe, lance, etc..)
            self.class_name = class_name # Dexterity / Strength / Magic / Divine
            self.range = _range
            self.rarity = rarity
            self.crit_damage = 1
            self.attack_speed_boost = 1

            if self.type == "Wand" or self.type == "Book":
                # defining base damage
                base_damage = 5
                
            elif self.type == "Staff":
                # defining base damage
                base_damage = 10

            else:
                # defining base damage
                base_damage = 30

                # update the damage type if its a great (big and heavy) weapon, or a knife
                if self.type == "Great Hammer" or self.type == "Greataxe" or self.type == "Greatsword":
                    base_damage *=  2
                    self.attack_speed_boost = 0.67
                elif self.type == "Katana" or self.type == "Spear":
                    base_damage *=  1.2
                    self.attack_speed_boost = 0.83
                elif self.type == "Knife":
                    base_damage *= 0.67
                    self.crit_damage = 1.5                    
                    self.attack_speed_boost = 1.1
                if self.range == "Ranged":
                    base_damage *= 0.8

                # ratio between ranks (from previous calculation)
                ratio = 2.512  # each rank multiplies damage by ~2.5

                # compute final damage
                exponent = rank_multipliers.get(self.rarity, 0)  # default 0 if unknown
                base_damage = base_damage * (ratio ** exponent)
            
            self.base_damage = base_damage


    class Equipment:
        _id_counter = 0
        def __init__(self, name, description, equipment_type, class_name, rarity):
            self.equipment_id = Equipment._id_counter
            Equipment._id_counter += 1
            self.name = name # name of the equipment
            self.description = description # a small description for the equipment, it also can have a story of the equipment
            self.type = equipment_type # the type (helmet, pants, boots, body)
            self.class_name = class_name # Dexterity / Strength / Magic / Tank / Shield / Evasion / Critical
            self.rarity = rarity
            
            base_defense = 0
            prio1 = 1
            prio2 = 1

            # get the defense depending on the type
            if self.type == "helmet":
                base_defense = 8
            elif self.type == "body":
                base_defense = 25
            elif self.type == "pants":
                base_defense = 17
            elif self.type == "boots":
                base_defense = 12
                
            # get the defense depending on the rarity
            if self.rarity == "E":
                base_defense = base_defense * 1
                prio1 = 5
                prio2 = 5
            elif self.rarity == "D":
                base_defense = base_defense * 2
                prio1 = 10
                prio2 = 5
            elif self.rarity == "C":
                base_defense = base_defense * 4
                prio1 = 15
                prio2 = 10
            elif self.rarity == "B":
                base_defense = base_defense * 7
                prio1 = 25
                prio2 = 15
            elif self.rarity == "A":
                base_defense = base_defense * 11
                prio1 = 35
                prio2 = 25
            elif self.rarity == "S":
                base_defense = base_defense * 16
                prio1 = 50
                prio2 = 35

            # Update the base defense and priorities depending on the class            
            if self.class_name == "Dexterity" or self.class_name == "Strength":
                base_defense = base_defense * 0.8
                prio1 = prio1 * 1.2
                prio2 = prio2 * 1.2
            elif self.class_name == "Magic" or self.class_name == "Evasion" or self.class_name == "Critical":
                base_defense = base_defense * 0.5
                prio1 = prio1 * 1.5
                prio2 = prio2 * 1.5
            elif self.class_name == "Tank":
                base_defense = base_defense * 1.3
                prio1 = prio1 * 0.7
                prio2 = prio2 * 0.7
            elif self.class_name == "Shield":
                base_defense = base_defense * 1.5
                prio1 = prio1 * 0.5
                prio2 = prio2 * 0.5
            elif self.class_name == "Speed":
                base_defense = base_defense * 1
                prio1 = prio1 * 1
                prio2 = prio2 * 1
            elif self.class_name == "Political" or self.class_name == "Miracle":
                base_defense = base_defense * 0.2
                prio1 = prio1 * 1.8
                prio2 = prio2 * 1.8

            self.base_defense = int(base_defense)
            self.prio1 = prio1
            self.prio2 = prio2
            
    class OnlineShop:
        def __init__(self):
            global equipments
            global weapons
            self.selling_equipments_list = self.get_items_for_sale(equipments)
            self.selling_weapons_list = self.get_items_for_sale(weapons)
            self.selling_protectors_list = self.get_protectors_for_sale()

        def get_items_for_sale(self, items):
            results = {}
            
            rarities = [ "E", "D", "C", "B", "A", "S" ]
            prices = [ 250, 600, 1500, 5000, 12000, 50000 ]
            aux = 0
            for rar in rarities:
                
                # filter items of this rarity
                filtered = [i for i in items if i.rarity == rar]
                
                random.shuffle(filtered)

                chosen = []
                seen_types = set()

                for e in filtered:
                    if e.type not in seen_types:
                        e.price = prices[aux]
                        e.stillAvailable = True
                        chosen.append(e)
                        seen_types.add(e.type)
                    if len(chosen) == 2:
                        break

                results[rar] = chosen
                aux += 1
            return results
        
        def get_protectors_for_sale(self):
            global protectors_base_information
            global my_protectors_map
            global weapons
            protectors_base_information_name_array = protectors_base_information.keys()
            my_protectors_array = my_protectors_map.keys()
            # filter items of this rarity
            filtered = [p_name for p_name in protectors_base_information_name_array if p_name not in my_protectors_array]
            
            random.shuffle(filtered)

            chosen = []

            for p_name in filtered:
                protector_to_sell = Protector(p_name, 1, 1, "To sell", protectors_base_information)
                protector_to_sell.price = 10000
                protector_to_sell.stillAvailable = True
                default_weapon = get_weapon_by_name(protector_to_sell.basePoints.default_weapon)
                protector_to_sell.set_weapon(default_weapon)
                chosen.append(protector_to_sell)
                if len(chosen) == 2:
                    break

            return chosen

        def update_store(self):
            global equipments
            global weapons
            global online_shop_new_protectors
            global online_shop_new_weapons
            global online_shop_new_equipments
            self.selling_equipments_list = self.get_items_for_sale(equipments)
            self.selling_weapons_list = self.get_items_for_sale(weapons)
            self.selling_protectors_list = self.get_protectors_for_sale()
            online_shop_new_protectors = True
            online_shop_new_weapons = True
            online_shop_new_equipments = True

        def checkIfProtectorStillAvailable(self):
            global my_protectors_map
            my_protectors_array = my_protectors_map.keys()
            for protector in self.selling_protectors_list:
                if protector.name in my_protectors_array:
                    protector.stillAvailable = False
            return
        

    class Fight:
        def __init__(self, protector, enemy, boss_expedition):
            self.protector = copy.deepcopy(protector)
            self.enemy = copy.deepcopy(enemy)
            self.boss_expedition = boss_expedition
            self.protector_defend = False
            self.enemy_defend = False
            self.battle_message = "The battle is about to beggin!"
            self.protector_time_until_atack = None
            self.enemy_time_until_atack = None
            self.message_turn = True
            self.your_turn = False

        def protector_attack_enemy(self):
            damage = self.protector.get_damage_points()
            if self.enemy_defend == True:
                damage = int(damage / 2)
                self.enemy_defend = False
            self.enemy.hp -= damage * ( 100 / (100 + self.enemy.get_defense()))
            self.enemy_time_until_atack -= self.protector_time_until_atack
            self.protector_time_until_atack = 1 / self.protector.get_attack_speed()
            self.battle_message = fight_you_attacked_message
            self.your_turn = False
            
            # checking if protector killed enemy
            if int(self.enemy.hp) <= 0:
                self.battle_message = fight_victory_message
            return

        def protector_defend_enemy(self):
            self.protector_defend = True
            self.enemy_time_until_atack -= self.protector_time_until_atack
            self.protector_time_until_atack = 1 / self.protector.get_attack_speed()
            self.battle_message = fight_you_are_defending_message
            self.your_turn = False
            return

        def enemy_attack_protector(self):
            damage = self.enemy.get_damage_points()
            if self.protector_defend == True:
                damage = int(damage / 2)
                self.protector_defend = False
            self.protector.hp -= damage * ( 100 / (100 + self.protector.get_defense()))
            self.protector_time_until_atack -= self.enemy_time_until_atack
            self.enemy_time_until_atack = 1 / self.enemy.get_attack_speed()
            self.battle_message = fight_enemy_attacked_message

            # checking if enemy killed protector            
            if int(self.protector.hp) <= 0:
                self.battle_message = fight_defeat_message
            return

        def enemy_defend_protector(self):
            self.enemy_defend = True
            self.protector_time_until_atack -= self.enemy_time_until_atack
            self.enemy_time_until_atack = 1 / self.enemy.get_attack_speed()
            self.battle_message = fight_enemy_is_defending_message
            return

        def continue_fight(self):
            if self.battle_message == "The battle is about to beggin!":
                # lets calculate who should be the first to attack!
                protector_timer = 0
                enemy_timer = 0
                # get the protector range type
                protector_range_type = self.protector.basePoints.unarmed_range
                if self.protector.equipedWeapon != None:
                    protector_range_type = self.protector.equipedWeapon.range

                if protector_range_type == "Melee":
                    protector_timer += melee_starting_period
                elif protector_range_type == "Ranged":
                    protector_timer += ranged_starting_period
                
                # get the enemy range type
                enemy_range_type = self.enemy.basePoints.unarmed_range
                if self.protector.equipedWeapon != None:
                    enemy_range_type = self.enemy.equipedWeapon.range

                if enemy_range_type == "Melee":
                    enemy_timer += melee_starting_period
                elif enemy_range_type == "Ranged":
                    enemy_timer += ranged_starting_period
                
                # get the time remaining for the protector
                protector_remaining_time = start_fight_timer_period - protector_timer

                # get the time until atack
                self.protector_time_until_atack = protector_remaining_time / self.protector.get_speed()
                
                # get the time remaining for the enemy
                enemy_remaining_time = start_fight_timer_period - enemy_timer

                # get the time until atack
                self.enemy_time_until_atack = enemy_remaining_time / self.enemy.get_speed()

                if self.protector_time_until_atack <= self.enemy_time_until_atack:
                    self.battle_message = fight_your_turn_message
                    self.your_turn = True
                else: 
                    self.battle_message = fight_enemy_turn_message
                    self.your_turn = False
                
            elif self.battle_message == fight_enemy_turn_message:
                self.your_turn = False

                roll = int(random.uniform(0, 100))  # get a random float between 0 and 100

                if 0 <= roll and roll < 30 :
                    self.enemy_defend_protector()
                if 30 <= roll:
                    self.enemy_attack_protector()
                
            elif self.battle_message == fight_you_attacked_message or \
                self.battle_message == fight_you_are_defending_message or \
                self.battle_message == fight_enemy_attacked_message or \
                self.battle_message == fight_enemy_is_defending_message:
                if self.protector_time_until_atack <= self.enemy_time_until_atack:
                    self.battle_message = fight_your_turn_message
                    self.your_turn = True
                else: 
                    self.battle_message = fight_enemy_turn_message
                    self.your_turn = False
            return
            