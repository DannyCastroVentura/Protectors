init python:
    def initializing_expedition_bosses():
        global expeditions_bosses_base_data
        global bossExpeditions

        bossExpeditions.append(BossExpedition(1, "The Mireborn Tyrant", "Deep within a poisonous swamp, a mutated beast commands venomous creatures and twisted flora. It oozes acid and rage — only its death can cleanse the land.", expeditions_needed_for_boss_expedition))
        bossExpeditions.append(BossExpedition(2, "The Hollow Sentinel", "A forgotten guardian awakens in the ruins of an ancient temple. Armed with rusted steel and remnants of lost magic, it strikes with surprising precision. Defeat it to gain access to the inner sanctum.", expeditions_needed_for_boss_expedition))
        bossExpeditions.append(BossExpedition(3, "The Clockwork Butcher", "In the quiet town of Elderglen, people vanish at night. A deranged clockmaker turned mechanical horror stalks the foggy streets. Enter his twisted workshop and end the nightmare before the town is silenced forever.", expeditions_needed_for_boss_expedition))        
        bossExpeditions.append(BossExpedition(4, "The Pale King", "A ruler who transcended death now commands legions of the undead. His soul is bound to a cursed throne. Break his chains and survive the wrath of his fallen empire.", expeditions_needed_for_boss_expedition))
        bossExpeditions.append(BossExpedition(5, "The Drowned Prophet", "Sunken beneath a once-great city lies a priest possessed by ancient sea gods. His chants summon tidal waves and spectral leviathans. Silence him before the flood rises.", expeditions_needed_for_boss_expedition))
        bossExpeditions.append(BossExpedition(6, "The Iron Colossus", "A living war machine, awakened from the forgotten age, marches toward civilization. Scale its limbs, sabotage its systems, and battle it atop its metal heart.", expeditions_needed_for_boss_expedition))
        bossExpeditions.append(BossExpedition(7, "The Infernal Architect", "A demon that builds war machines in a fortress of fire and gears. Deactivate his defenses and destroy his creations before confronting him in a hellish showdown.", expeditions_needed_for_boss_expedition))
        bossExpeditions.append(BossExpedition(8, "The Eclipse Warden", "At the edge of the world, a being of shadow and solar flame guards the passage to the void. Fight through alternating light and dark phases in a battle of cosmic rhythm.", expeditions_needed_for_boss_expedition))
        bossExpeditions.append(BossExpedition(9, "The Shattered Queen", "In a realm of mirrors and illusions, an exiled queen of a fallen kingdom bends reality to her will. Break her illusions to reveal her true form — and end her madness.", expeditions_needed_for_boss_expedition))
        bossExpeditions.append(BossExpedition(10, "The Void-Touched Seraph", "Once a divine guardian, now corrupted by the void. This winged horror fights in aerial stages, using celestial and abyssal magic. Only a grounded will can reach the skies.", expeditions_needed_for_boss_expedition))
        
        # creating enemies
        # The Mireborn Tyrant (hp + damage)
        expeditions_bosses_base_data["The Mireborn Tyrant"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "charisma": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "strength", "constitution", "speed"
                ], 
                "evolution1": [
                    "strength", "constitution", "speed"
                ], 
                "evolution2": [
                    "strength", "constitution", "speed"
                ]
            }, 
            "STR_CON", "STR_CON", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Sword"], None, None,
            "Melee", None, None,
            "Regular", "Regular", "Regular",
            "Rusty Sword"
        )
        
        # The Hollow Sentinel (hp + damage)
        expeditions_bosses_base_data["The Hollow Sentinel"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "charisma": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "strength", "constitution"
                ], 
                "evolution1": [
                    "strength", "constitution"
                ], 
                "evolution2": [
                    "strength", "constitution"
                ]
            }, 
            "STR_CON", "STR_CON", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Sword"], None, None,
            "Ranged", None, None,
            "Regular", "Regular", "Regular",
            "Rusty Sword"
        )
        
        # The Clockwork Butcher (hp + dexterity + speed and luck)
        expeditions_bosses_base_data["The Clockwork Butcher"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "charisma": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "dexterity", "constitution", "speed", "luck", "dexterity", "constitution"
                ], 
                "evolution1": [
                    "dexterity", "constitution", "speed", "luck", "dexterity", "constitution"
                ], 
                "evolution2": [
                    "dexterity", "constitution", "speed", "luck", "dexterity", "constitution"
                ]
            }, 
            "EVA", "EVA", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Knife"], None, None,
            "Melee", None, None,
            "Regular", "Regular", "Regular",
            "Balanced Knife"
        )

        # The Pale King (wisdom + hp)
        expeditions_bosses_base_data["The Pale King"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "charisma": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "wisdom", "constitution"
                ], 
                "evolution1": [
                    "wisdom", "constitution"
                ], 
                "evolution2": [
                    "wisdom", "constitution"
                ]
            }, 
            "MIR_CON", "MIR_CON", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Book"], None, None,
            "Ranged", None, None,
            "Divine", "Divine", "Divine",
            "Cleric’s Scripture"
        )

        # The Drowned Prophet (int + hp)
        expeditions_bosses_base_data["The Drowned Prophet"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "charisma": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "intelligence", "constitution"
                ], 
                "evolution1": [
                    "intelligence", "constitution"
                ], 
                "evolution2": [
                    "intelligence", "constitution"
                ]
            }, 
            "INT_TAN", "INT_TAN", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Staff"], None, None,
            "Ranged", None, None,
            "Magic", "Magic", "Magic",
            "Elemental Staff"
        )

        # The Iron Colossus (hp + strength)
        expeditions_bosses_base_data["The Iron Colossus"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "charisma": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "strength", "constitution"
                ], 
                "evolution1": [
                    "strength", "constitution"
                ], 
                "evolution2": [
                    "strength", "constitution"
                ]
            }, 
            "STR_CON", "STR_CON", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Greatsword"], None, None,
            "Ranged", None, None,
            "Magic", "Magic", "Magic",
            "Warrior’s Greatsword"
        )
        
        # The Infernal Architect (hp + wis)
        expeditions_bosses_base_data["The Infernal Architect"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "charisma": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "wisdom", "constitution"
                ], 
                "evolution1": [
                    "wisdom", "constitution"
                ], 
                "evolution2": [
                    "wisdom", "constitution"
                ]
            }, 
            "MIR_CON", "MIR_CON", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Greatsword"], None, None,
            "Melee", None, None,
            "Divine", "Divine", "Divine",
            "Crusader’s Greatsword"
        )

        # The Eclipse Warden (hp + wis)
        expeditions_bosses_base_data["The Eclipse Warden"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "charisma": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "wisdom", "wisdom", "wisdom", "constitution"
                ], 
                "evolution1": [
                    "wisdom", "wisdom", "wisdom", "constitution"
                ], 
                "evolution2": [
                    "wisdom", "wisdom", "wisdom", "constitution"
                ]
            }, 
            "MIR_CON", "MIR_CON", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Sword"], None, None,
            "Melee", None, None,
            "Divine", "Divine", "Divine",
            "Sword of Purity"
        )

        # The Shattered Queen (hp + int)
        expeditions_bosses_base_data["The Shattered Queen"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "charisma": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "intelligence", "intelligence", "intelligence", "constitution"
                ], 
                "evolution1": [
                    "intelligence", "intelligence", "intelligence", "constitution"
                ], 
                "evolution2": [
                    "intelligence", "intelligence", "intelligence", "constitution"
                ]
            }, 
            "INT_TAN", "INT_TAN", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Staff"], None, None,
            "Melee", None, None,
            "Magic", "Magic", "Magic",
            "Arcane Staff"
        )

        # The Void-Touched Seraph (hp + hp + hp + speed + dex)
        expeditions_bosses_base_data["The Void-Touched Seraph"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "charisma": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "constitution", "constitution", "constitution", "speed", "dexterity", "dexterity"
                ], 
                "evolution1": [
                    "constitution", "constitution", "constitution", "speed", "dexterity", "dexterity"
                ], 
                "evolution2": [
                    "constitution", "constitution", "constitution", "speed", "dexterity", "dexterity"
                ]
            }, 
            "DEX_TAN", "DEX_TAN", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Staff"], None, None,
            "Melee", None, None,
            "Regular", "Regular", "Regular",
            "Knife of the Trickster"
        )

        

        