init python:
    def initializing_things():
        global protectors_base_information
        global equipments
        global myEquipments

        Equipment._id_counter = 0   # Reset the counter
        Weapon._id_counter = 0   # Reset the counter
        Weapon._names_list = []   # Reset the counter
        Expedition._id_counter = 0   # Reset the counter

        # creating protectors    
        protectors_base_information["Ninja"] = BaseProtectorData(
            {
                "strength": 10,
                "dexterity": 17,
                "constitution": 12,
                "intelligence": 14,
                "wisdom": 13,
                "speed": 15,
                "luck": 11,
                "attack_speed": 1.3
            },
            {
                "basic": [
                    "dexterity", "luck", "constitution", "dexterity", "speed",
                    "constitution", "dexterity", "strength", "speed", "constitution", 
                    "dexterity", "speed", "strength", "constitution", "luck", 
                    "speed", "luck", "dexterity", "strength", "dexterity", 
                    "dexterity", "constitution", "dexterity", "speed", "dexterity"
                ], 
                "evolution1": [
                    "dexterity", "dexterity", "luck", "speed", "speed", "constitution", "constitution"
                ], 
                "evolution2": [
                    "dexterity", "dexterity", "constitution", "constitution", "constitution", "speed"
                ]
            },
            "EVA", "DEX_TAN", 
            "Ash Ninja", 
            "While exploring a forgotten cave, he touched a cursed relic that bound dark magic to his body. From that moment, he gained the power to transform into ash, disappearing into smoke to strike unseen.",
            "Tech Ninja", 
            "Recruited by the army, he wields weapons infused with cutting-edge technology and wears armor that adapts to any threat. Every strike is precise, every movement optimized, making him a deadly force on the battlefield.",
            ["Knife", "Sword", "Katana"], None, None,
            "Melee", None, None,
            "Regular", "Regular", "Regular",
            "Thief’s Knife"
        )
        
        protectors_base_information["Templar"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 10,
                "constitution": 18,
                "intelligence": 11,
                "wisdom": 16,
                "speed": 7,
                "luck": 8,
                "attack_speed": 0.7
            },
            {
                "basic": [
                    "strength", "wisdom", "constitution", "strength", "constitution", 
                    "strength", "wisdom", "constitution", "strength", "constitution", 
                    "strength", "wisdom", "strength", "constitution", "constitution", 
                    "strength", "wisdom", "strength", "wisdom", "strength", "wisdom"
                ], 
                "evolution1": [
                    "strength", "wisdom", "constitution", "strength", "constitution", 
                    "strength", "wisdom", "constitution", "strength", "constitution", 
                    "strength", "wisdom", "strength", "constitution", "constitution", 
                    "strength", "wisdom", "strength", "wisdom", "strength", "wisdom"
                ], 
                "evolution2": [
                    "strength", "wisdom", "constitution", "strength", "constitution", 
                    "strength", "wisdom", "constitution", "strength", "constitution", 
                    "strength", "wisdom", "strength", "constitution", "constitution", 
                    "strength", "wisdom", "strength", "wisdom", "strength", "wisdom"
                ]
            },
            "MIR_TAN", "MIR_STR_STR",
            "Saint Templar",
            "A devoted templar, he was granted a sacred blessing to wield the power of the saints. and every strike carries divine judgment. Guided by unbreakable devotion, he stands as a living vessel of sanctity on the battlefield.",
            "Demonic Templar",
            "Once a templar of faith, he forsook the light and accepted a blasphemous blessing from demons. His blade burns with unholy fire, his armor twists with infernal power, and every strike spreads corruption.",
            ["Sword", "Spear", "Greatsword", "Great Hammer", "Greataxe"], None, None,
            "Melee", None, None,
            "Regular", "Divine", "Divine",
            "Rusty Greatsword"
        )


        protectors_base_information["Wizard"] = BaseProtectorData(
            {
                "strength": 7,
                "dexterity": 12,
                "constitution": 12,
                "intelligence": 22,
                "wisdom": 18,
                "speed": 8,
                "luck": 12,
                "attack_speed": 0.9
            }, 
            {
                "basic": [
                    "intelligence", "wisdom", "constitution", "intelligence", "dexterity", 
                    "wisdom", "intelligence", "constitution", "wisdom", "dexterity", 
                    "intelligence", "wisdom", "constitution", "luck", "intelligence", 
                    "wisdom", "constitution", "intelligence", "wisdom", "constitution", "speed"
                ], 
                "evolution1": [
                    "wisdom", "wisdom", "constitution", "wisdom", "constitution", 
                    "wisdom", "wisdom", "constitution", "wisdom", "constitution", 
                    "wisdom", "wisdom", "constitution", "constitution", "wisdom", 
                    "wisdom", "constitution", "wisdom", "wisdom", "constitution", "constitution"
                ], 
                "evolution2": [
                    "intelligence", "intelligence", "constitution", "intelligence", "dexterity", 
                    "intelligence", "intelligence", "constitution", "intelligence", "dexterity", 
                    "intelligence", "intelligence", "constitution", "luck", "intelligence", 
                    "intelligence", "constitution", "intelligence", "intelligence", "constitution", "speed"
                ], 
            },
            "MIR_CON", "INT",
            "Thunder Wizard",
            "Through years of study in forgotten libraries, he unlocked the secrets of the arcane. Spells of thunder and lightning bend to his will, making him a master of battlefield control.",
            "Nature Wizard",
            "Clad in enchanted robes, he uses his nature spells to wields traps and kill enemies from the ground using his deadly vines. Using precision and strategy he shows as a dangerous threat for anyone who faces him.",
            ["Wand", "Staff"], ["Wand", "Staff", "Book"], ["Wand", "Staff"],
            "Ranged", None, None,
            "Magic", "Divine", "Magic",
            "Cracked Wooden Wand"
        )

        protectors_base_information["Ace"] = BaseProtectorData(
            {
                "strength": 8,
                "dexterity": 15,
                "constitution": 12,
                "intelligence": 15,
                "wisdom": 15,
                "speed": 10,
                "luck": 16,
                "attack_speed": 1.2
            }, 
            {
                "basic": [
                    "dexterity", "speed", "luck", "dexterity", "constitution", 
                    "constitution", "dexterity", "dexterity", "speed", "luck", 
                    "dexterity", "dexterity", "luck", "luck", "dexterity", 
                    "dexterity", "luck", "luck", "dexterity", "constitution",
                    "speed", "luck", "dexterity", "luck", "constitution"
                ],
                "evolution1": [
                    "wisdom", "wisdom", "constitution", "wisdom", "wisdom", 
                    "constitution", "wisdom", "wisdom", "speed", "constitution", 
                    "wisdom", "wisdom", "constitution", "luck", "wisdom", 
                    "wisdom", "constitution", "wisdom", "wisdom", "constitution",
                    "constitution", "constitution", "wisdom", "wisdom", "constitution"
                ],
                "evolution2": [
                    "dexterity", "speed", "luck", "constitution", "luck", 
                    "luck", "luck", "dexterity", "speed", "luck", 
                    "dexterity", "dexterity", "luck", "constitution", "dexterity", 
                    "dexterity", "luck", "luck", "dexterity", "dexterity",
                    "speed", "luck", "dexterity", "luck", "luck"
                ]
            }, 
            "MIR_CON", "CRI",
            "Demonic Dealer",
            "In a forgotten arcane library, he found a deck of dark enchanted cards, each holding demonic essence. Now, whispers from the cards slowly turn him into a demon with every throw.",
            "Ace of Fates",
            "A master of strategy and dexterity, he wields his deck like a razor-sharp blade. Every card is a weapon, every draw a calculated gamble, turning him into a lethal force from afar.",
            ["Cards"], None, None,
            "Melee", None, None,
            "Regular", "Divine", "Regular",
            "Paper Throwing Cards"
        )

        protectors_base_information["Samurai"] = BaseProtectorData(
            {
                "strength": 16,
                "dexterity": 14,
                "constitution": 15,
                "intelligence": 12,
                "wisdom": 14,
                "speed": 10,
                "luck": 9,
                "attack_speed": 1.2
            },
            {
                "basic": [
                    "strength", "speed", "strength", "constitution", "speed", 
                    "wisdom", "dexterity", "speed", "constitution", "strength", 
                    "dexterity", "wisdom", "strength", "dexterity", "strength", 
                    "intelligence", "strength", "dexterity", "constitution", "constitution"
                ], 
                "evolution1": [
                    "strength", "strength", "strength", "constitution", "constitution", 
                    "strength", "constitution", "speed", "constitution", "strength", 
                    "strength", "constitution", "strength", "strength", "strength", 
                    "constitution", "strength", "constitution", "constitution", "strength"
                ], 
                "evolution2": [
                    "dexterity", "speed", "dexterity", "constitution", "speed", 
                    "constitution", "dexterity", "speed", "constitution", "dexterity", 
                    "dexterity", "speed", "dexterity", "dexterity", "dexterity", 
                    "speed", "dexterity", "dexterity", "constitution", "speed"
                ], 
            },            
            "TAN", "DEX",
            "Tech Samurai",
            "Once bound by tradition, he forged a secret pact with visionary craftsmen. His blade, born of ancient mastery and hidden technology, strikes with unmatched precision; his armor adapts to any threat.",
            "Wolf Samurai",
            "Once a disciplined samurai, he was transformed into a fearsome wolf. Now faster, and driven by primal instinct, his strikes land with devastating force. He is an unstoppable predator on the battlefield.",
            ["Katana"], ["Katana"], ["Katana", "Sword", "Knife"],
            "Melee", None, None,
            "Regular", "Regular", "Regular",
            "Rusty Katana"
        )

        protectors_base_information["Recruit"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 17,
                "intelligence": 10,
                "wisdom": 8,
                "speed": 11,
                "luck": 11,
                "attack_speed": 1
            },
            {
                "basic": [
                    "dexterity", "strength", "speed", "constitution", "dexterity", 
                    "strength", "dexterity", "constitution", "dexterity", "strength", 
                    "dexterity", "constitution", "dexterity", "strength", "constitution", 
                    "strength", "luck", "strength", "constitution", "constitution", "speed"
                ], 
                "evolution1": [
                    "dexterity", "dexterity", "speed", "constitution", "dexterity", 
                    "luck", "dexterity", "constitution", "dexterity", "dexterity", 
                    "dexterity", "constitution", "dexterity", "speed", "dexterity", 
                    "luck", "luck", "dexterity", "constitution", "speed", "speed"
                ], 
                "evolution2": [
                    "strength", "strength", "speed", "constitution", "constitution", 
                    "strength", "strength", "constitution", "speed", "strength", 
                    "strength", "constitution", "strength", "strength", "speed", 
                    "strength", "constitution", "strength", "constitution", "constitution", "speed"
                ], 
            },
            "EVA", "STR_STR_STR_CON_SPE",
            "Special Forces Agent",
            "Determined to become one of the best, he enlisted in the Special Forces intense training. After proving his skill, he earned his place and now strikes with unmatched precision, agility, and tactical mastery on every mission.",
            "Berserker",
            "Trapped in fear during a mission, the recruit’s mind finally snapped, and that terror erupted into uncontrollable, burning rage. Now he fights with pure instinct as he charges into battle with relentless ferocity.",
            ["Knife", "Gun", "Machine gun", "Sniper"], ["Knife", "Gun", "Machine gun", "Sniper"], ["Knife", "Sword", "Greatsword", "Greataxe", "Spear", "Axe", "Hammer", "Great Hammer", "Mace"],
            "Melee", None, None,
            "Regular", "Regular", "Regular",
            "Rusty Combat Knife"
        )

        protectors_base_information["Robot"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 18,
                "constitution": 20,
                "intelligence": 12,
                "wisdom": 8,
                "speed": 8,
                "luck": 9,
                "attack_speed": 1
            },
            {
                "basic": [
                    "dexterity", "constitution", "constitution", "dexterity", "speed", 
                    "constitution", "dexterity", "speed", "constitution", "dexterity", 
                    "dexterity", "constitution", "constitution", "dexterity", "constitution", 
                    "constitution", "dexterity", "constitution", "constitution", "constitution"
                ], 
                "evolution1": [
                    "dexterity", "dexterity", "dexterity", "constitution", "constitution", 
                    "dexterity", "constitution", "speed", "constitution", "dexterity", 
                    "dexterity", "constitution", "dexterity", "dexterity", "dexterity", 
                    "constitution", "dexterity", "constitution", "constitution", "dexterity"
                ], 
                "evolution2": [
                    "constitution", "speed", "constitution", "constitution", "constitution", 
                    "constitution", "strength", "constitution", "constitution", "strength", 
                    "constitution", "constitution", "strength", "constitution", "constitution", 
                    "strength", "constitution", "constitution", "constitution", "speed"
                ], 
            },            
            "CON_DEX", "HP",
            "Bladeform X",
            "The humanoid robot has downloaded advanced Agile combat data, allowing it to redesign its body and incorporate fluid, high-speed sword techniques into its movements.",
            "Titanform Y",
            "The massive tank-like robot has downloaded advanced heavy combat protocols, redesigning its armor and systems to maximize durability, firepower, and battlefield dominance.",
            [""], None, None,
            "Ranged", "Melee", "Melee",
            "Dexterity", "Dexterity", "Regular",
            ""
        )

        # protectors_base_information["Skeleton"] = BaseProtectorData(17, 18, 10, 6, 8, 6, 20, 0.34, 0.5, 0.25, 0.2, 0.125, 0, 0, 
        #     "EVA", "DAM",
        #     "Name 1",
        #     "Description 1",
        #     "Name 2",
        #     "Description 2",
        #     "Knife,Sword,Hands",
        #     "Melee"
        # )
        # # it gains:
        # # 1 dexterity per 2 levels
        # # 1 strenght per 3 levels
        # # 1 constitution per 4 levels
        # # 1 intelligence per 5 levels
        # # 1 wisdom per 6 levels

        # WEAPONS
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        initializing_axes()
        initializing_books()
        initializing_cards()
        initializing_great_hammers()
        initializing_greataxes()
        initializing_greatswords()
        initializing_guns()
        initializing_hammers()
        initializing_katanas()
        initializing_knifes()
        initializing_maces()
        initializing_machine_guns()
        initializing_snipers()
        initializing_spears()
        initializing_staffs()
        initializing_swords()
        initializing_wands()

        
        # EQUIPMENT
        # ADDING TEST EQUIPMENTS

        equipments.append(Equipment(
            "Light Leather Hood",
            "A lightweight hood for agility and quick movements.",
            "helmet",
            "Evasion",
            "E"
        ))

        equipments.append(Equipment(
            "Phoenix Wings",
            "Wings of a fallen phoenix, offering extreme fire resistance and a chance to rise from the ashes.",
            "body",
            "Tank",
            "D"
        ))

        equipments.append(Equipment(
            "Vanguard Pants",
            "Pants worn by the vanguard, enhancing defense and fortitude.",
            "pants",
            "Tank",
            "C"
        ))

        equipments.append(Equipment(
            "Gladiator's Boots",
            "Boots that provide incredible movement speed and stamina, perfect for relentless combat.",
            "boots",
            "Tank",
            "B"
        ))
        
        equipments.append(Equipment(
            "Stormbreak Helm",
            "A helmet that sharpens reflexes and boosts critical hit chance.",
            "helmet",
            "Critical",
            "A"
        ))

        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # E CLASS

        ######## FULL MIRACLE GEAR (Rank E) ########
        equipments.append(Equipment(
            "Simple Veil",
            "A plain veil that carries a faint blessing. Inspires small hope.",
            "helmet",
            "Miracle",
            "E"
        ))

        equipments.append(Equipment(
            "Simple Vestment",
            "A modest garment, worn by those who believe. Grants a touch of serenity.",
            "body",
            "Miracle",
            "E"
        ))

        equipments.append(Equipment(
            "Simple Slacks",
            "Unassuming pants, stitched with care. Brings quiet dignity.",
            "pants",
            "Miracle",
            "E"
        ))

        equipments.append(Equipment(
            "Simple Sandals",
            "Humble sandals, softened by many steps. Symbol of walking the faithful path.",
            "boots",
            "Miracle",
            "E"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Reinforced Helmet",
            "A sturdy helmet made of reinforced iron. Offers good protection.",
            "helmet",
            "Tank",
            "E"
        ))
        
        equipments.append(Equipment(
            "Reinforced Body Armor",
            "A sturdy body armor made of reinforced iron. Offers good protection.",
            "body",
            "Tank",
            "E"
        ))

        equipments.append(Equipment(
            "Reinforced Pants",
            "A sturdy pants made of reinforced iron. Offers good protection.",
            "pants",
            "Tank",
            "E"
        ))

        equipments.append(Equipment(
            "Reinforced Boots",
            "A sturdy boots made of reinforced iron. Offers good protection.",
            "boots",
            "Tank",
            "E"
        ))

        ######## FULL GEAR FOR SPEED: NOVICE VELOCITY SET ########
        equipments.append(Equipment(
            "Novice Speed Helmet",
            "A lightweight helmet that slightly enhances reflexes and reduces wind resistance. Perfect for beginners learning the basics of speed.",
            "helmet",
            "Speed",
            "E"
        ))

        equipments.append(Equipment(
            "Novice Speed Suit",
            "A simple, flexible suit that improves mobility and movement speed slightly. Not very flashy, but practical for training.",
            "body",
            "Speed",
            "E"
        ))

        equipments.append(Equipment(
            "Novice Speed Pants",
            "Basic pants designed for comfort and light acceleration. Gives a small boost to running speed without restricting movement.",
            "pants",
            "Speed",
            "E"
        ))

        equipments.append(Equipment(
            "Novice Speed Boots",
            "Light shoes that slightly improve stride and running efficiency. Good for short sprints and training exercises.",
            "boots",
            "Speed",
            "E"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Windrunner Helmet",
            "Helmet designed for swift movement, they boost speed and critical hit chance.",
            "helmet",
            "Critical",
            "E"
        ))
        
        equipments.append(Equipment(
            "Windrunner Body Armor",
            "Body armor designed for swift movement, they boost speed and critical hit chance.",
            "body",
            "Critical",
            "E"
        ))

        equipments.append(Equipment(
            "Windrunner Pants",
            "Pants designed for swift movement, they boost speed and critical hit chance.",
            "pants",
            "Critical",
            "E"
        ))

        equipments.append(Equipment(
            "Windrunner Boots",
            "Boots designed for swift movement, they boost speed and critical hit chance.",
            "boots",
            "Critical",
            "E"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Iron Helmet",
            "A strong iron helmet offering high defense.",
            "helmet",
            "Shield",
            "E"
        ))

        equipments.append(Equipment(
            "Iron Chestplate",
            "A strong iron chestplate offering high defense.",
            "body",
            "Shield",
            "E"
        ))

        equipments.append(Equipment(
            "Iron Trousers",
            "A strong iron trousers offering high defense.",
            "pants",
            "Shield",
            "E"
        ))

        equipments.append(Equipment(
            "Iron Boots",
            "A strong iron boots offering high defense.",
            "boots",
            "Shield",
            "E"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Helmet of the Swift",
            "Helmet that increase your movement speed and dexterity.",
            "helmet",
            "Evasion",
            "E"
        ))

        equipments.append(Equipment(
            "Upper rags of the Swift",
            "Body armor that increase your movement speed and dexterity.",
            "body",
            "Evasion",
            "E"
        ))

        equipments.append(Equipment(
            "Pants of the Swift",
            "Pants that increase your movement speed and dexterity.",
            "pants",
            "Evasion",
            "E"
        ))

        equipments.append(Equipment(
            "Boots of the Swift",
            "Boots that increase your movement speed and dexterity.",
            "boots",
            "Evasion",
            "E"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Mystic Wizard's Hat",
            "A wizard’s hat, enhancing magical powers and intellect.",
            "helmet",
            "Magic",
            "E"
        ))

        equipments.append(Equipment(
            "Mystic Robe",
            "A robe which grants magical powers and intellect.",
            "body",
            "Magic",
            "E"
        ))

        equipments.append(Equipment(
            "Mystic Pants",
            "A wizard’s pants, enhancing magical powers and intellect.",
            "pants",
            "Magic",
            "E"
        ))

        equipments.append(Equipment(
            "Mystic Boots",
            "Boots which grants magical powers and intellect.",
            "boots",
            "Magic",
            "E"
        ))
        
        ######## OTHER ONES ########
        equipments.append(Equipment(
            "Golden Plate Mail",
            "A glorious plate mail forged from gold, offers supreme defense.",
            "body",
            "Tank",
            "E"
        ))

        equipments.append(Equipment(
            "Feathered Boots",
            "Light as a feather, offering extreme agility and evasion.",
            "boots",
            "Evasion",
            "E"
        ))

        equipments.append(Equipment(
            "Wraith Cloak",
            "A cloak made from the essence of wraiths, enhancing evasion and stealth.",
            "body",
            "Evasion",
            "E"
        ))

        equipments.append(Equipment(
            "Elven Cloak",
            "A cloak that boosts agility and offers increased critical hit chance.",
            "body",
            "Critical",
            "E"
        ))

        equipments.append(Equipment(
            "Crown of the Ancients",
            "A crown that increases wisdom and enhances magical abilities.",
            "helmet",
            "Magic",
            "E"
        ))

        equipments.append(Equipment(
            "Silver Circlet",
            "A delicate circlet that enhances magical defense and intelligence.",
            "helmet",
            "Magic",
            "E"
        ))

        equipments.append(Equipment(
            "Titanium Chestplate",
            "A high-tech chestplate offering immense defense against all attacks.",
            "body",
            "Tank",
            "E"
        ))

        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # D CLASS

        ######## FULL MIRACLE GEAR (Rank D) ########
        equipments.append(Equipment(
            "Blessed Hood",
            "A hood embroidered with small symbols of faith. Offers protection from doubt.",
            "helmet",
            "Miracle",
            "D"
        ))

        equipments.append(Equipment(
            "Blessed Robe",
            "A robe lightly infused with divine essence. Brings comfort to the wearer.",
            "body",
            "Miracle",
            "D"
        ))

        equipments.append(Equipment(
            "Blessed Trousers",
            "Simple yet well-kept trousers, carrying a quiet sacred charm.",
            "pants",
            "Miracle",
            "D"
        ))

        equipments.append(Equipment(
            "Blessed Sandals",
            "Sandals reinforced with care. Each step feels guided by unseen hands.",
            "boots",
            "Miracle",
            "D"
        ))

        ######## FULL GEAR FOR SPEED: WINDRUNNER SET ########
        equipments.append(Equipment(
            "Windrunner Helmet",
            "A streamlined helmet that channels airflow to sharpen reflexes and slightly increase running speed. Ideal for aspiring speedsters.",
            "helmet",
            "Speed",
            "D"
        ))

        equipments.append(Equipment(
            "Windrunner Body Suit",
            "A lightweight, flexible suit that subtly enhances agility and reduces fatigue. Gives a noticeable boost to movement without hindering mobility.",
            "body",
            "Speed",
            "D"
        ))

        equipments.append(Equipment(
            "Windrunner Pants",
            "Comfortable, form-fitting pants designed to improve leg movement and acceleration. Great for short sprints and quick maneuvers.",
            "pants",
            "Speed",
            "D"
        ))

        equipments.append(Equipment(
            "Windrunner Boots",
            "Soft, agile boots that slightly increase stride length and running efficiency. Perfect for novice speed adventurers.",
            "boots",
            "Speed",
            "D"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Helm of the Abyss",
            "A helm that shrouds the wearer’s mind from dark influence while enhancing awareness.",
            "helmet",
            "Evasion",
            "D"
        ))

        equipments.append(Equipment(
            "Chestplate of the Abyss",
            "A chestplate forged in shadowsteel, offering strong protection against darkness.",
            "body",
            "Evasion",
            "D"
        ))

        equipments.append(Equipment(
            "Legguards of the Abyss",
            "Armored pants infused with abyssal magic, granting resilience and agility.",
            "pants",
            "Evasion",
            "D"
        ))

        equipments.append(Equipment(
            "Boots of the Abyss",
            "Boots that grant the wearer enhanced movement speed and dark resistance.",
            "boots",
            "Evasion",
            "D"
        ))
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Celestial Helm",
            "A helm blessed by the stars, sharpening focus and magical control.",
            "helmet",
            "Magic",
            "D"
        ))

        equipments.append(Equipment(
            "Celestial Robe",
            "A flowing robe woven with stardust, enhancing mana flow and spell potency.",
            "body",
            "Magic",
            "D"
        ))

        equipments.append(Equipment(
            "Celestial Legwraps",
            "Light enchanted legwraps that improve mobility and channel magical energy.",
            "pants",
            "Magic",
            "D"
        ))

        equipments.append(Equipment(
            "Celestial Boots",
            "Boots blessed by the stars, increasing speed and mana regeneration.",
            "boots",
            "Magic",
            "D"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Vampire's Visage",
            "A sinister helm that instills fear and strengthens the wearer’s resolve.",
            "helmet",
            "Strength",
            "D"
        ))

        equipments.append(Equipment(
            "Vampire's Mantle",
            "A dark mantle that increases strength and grants life steal on attacks.",
            "body",
            "Strength",
            "D"
        ))

        equipments.append(Equipment(
            "Vampire's Greaves",
            "Heavy pants reinforced with cursed metal, granting power with each strike.",
            "pants",
            "Strength",
            "D"
        ))

        equipments.append(Equipment(
            "Vampire's Treads",
            "Boots infused with vampiric essence, allowing swift movement while draining foes.",
            "boots",
            "Strength",
            "D"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Titan's Helm",
            "A massive helmet that grants immense protection and boosts strength.",
            "helmet",
            "Tank",
            "D"
        ))

        equipments.append(Equipment(
            "Titan's Chestguard",
            "An enormous chestpiece forged for warriors who stand like unyielding mountains.",
            "body",
            "Tank",
            "D"
        ))

        equipments.append(Equipment(
            "Titan's Legplates",
            "Heavy armored greaves that root the wearer firmly in battle.",
            "pants",
            "Tank",
            "D"
        ))

        equipments.append(Equipment(
            "Titan's Boots",
            "Boots as solid as the earth, making each step unshakable.",
            "boots",
            "Tank",
            "D"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Assassin's Cowl",
            "A cowl that boosts stealth, evasion, and critical hit chance.",
            "helmet",
            "Critical",
            "D"
        ))

        equipments.append(Equipment(
            "Assassin's Vest",
            "A lightweight, reinforced vest designed for swift and lethal strikes.",
            "body",
            "Critical",
            "D"
        ))

        equipments.append(Equipment(
            "Assassin's Leggings",
            "Flexible leggings that allow silent movement and deadly agility.",
            "pants",
            "Critical",
            "D"
        ))

        equipments.append(Equipment(
            "Assassin's Boots",
            "Boots crafted for speed and silence, perfect for striking from the shadows.",
            "boots",
            "Critical",
            "D"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Crown of the Immortal King",
            "A crown that gives the wearer the power to revive once upon death and boosts all stats.",
            "helmet",
            "Shield",
            "D"
        ))

        equipments.append(Equipment(
            "Armor of the Immortal King",
            "A regal chestplate that radiates divine protection, shielding its wearer from fatal blows.",
            "body",
            "Shield",
            "D"
        ))

        equipments.append(Equipment(
            "Greaves of the Immortal King",
            "Sturdy leg armor that empowers each stride with the might of an eternal ruler.",
            "pants",
            "Shield",
            "D"
        ))

        equipments.append(Equipment(
            "Sabatons of the Immortal King",
            "Boots that carry the weight of countless victories and unmatched resilience.",
            "boots",
            "Shield",
            "D"
        ))

        
        ######## OTHER ONES ########
        equipments.append(Equipment(
            "Shadow Cloak",
            "A cloak that grants the wearer invisibility for short periods and boosts stealth.",
            "body",
            "Evasion",
            "D"
        ))

        equipments.append(Equipment(
            "Wings of the Seraphim",
            "Wings that bestow divine power, granting increased movement and evasion.",
            "boots",
            "Evasion",
            "D"
        ))

            
        equipments.append(Equipment(
            "Elderwood Armor",
            "Armor crafted from the ancient trees of the elderwood. Increases defense and regeneration.",
            "body",
            "Tank",
            "D"
        ))

        equipments.append(Equipment(
            "Cloak of the Revenant",
            "A cloak made from the shadows of the dead. It grants invisibility and an aura that weakens enemies.",
            "body",
            "Evasion",
            "D"
        ))

        equipments.append(Equipment(
            "Cloak of the Phoenix",
            "A cloak that grants regeneration and the ability to rise from death once, like a phoenix.",
            "body",
            "Tank",
            "D"
        ))

        equipments.append(Equipment(
            "Crown of the Celestial Emperor",
            "A crown that gives the wearer divine strength and resilience, making them nearly immortal.",
            "helmet",
            "Tank",
            "D"
        ))
        
        equipments.append(Equipment(
            "Titanium Helm",
            "A sturdy titanium helmet that grants extra defense and resistance.",
            "helmet",
            "Tank",
            "D"
        ))

        equipments.append(Equipment(
            "Dragonscale Body Armor",
            "Armor crafted from dragon scales. Offers great defense and fire resistance.",
            "body",
            "Tank",
            "D"
        ))

        equipments.append(Equipment(
            "Shadow Boots",
            "Boots made for stealth and speed. They increase dexterity and evasion.",
            "boots",
            "Evasion",
            "D"
        ))

        ######## 
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # C CLASS

        ######## FULL MIRACLE GEAR (Rank C) ########
        equipments.append(Equipment(
            "Holy Hood",
            "A hood that glows faintly in candlelight. Said to ward off despair.",
            "helmet",
            "Miracle",
            "C"
        ))

        equipments.append(Equipment(
            "Holy Robe",
            "A flowing robe adorned with sacred patterns. Strengthens the spirit.",
            "body",
            "Miracle",
            "C"
        ))

        equipments.append(Equipment(
            "Holy Trousers",
            "Finely woven trousers blessed by ritual. Offers dignity and grace.",
            "pants",
            "Miracle",
            "C"
        ))

        equipments.append(Equipment(
            "Holy Sandals",
            "Sandals said to leave footprints of light. Brings steadiness to each step.",
            "boots",
            "Miracle",
            "C"
        ))

        ######## FULL GEAR FOR SPEED: SKYBLADE SET ########
        equipments.append(Equipment(
            "Skyblade Helmet",
            "A reinforced, aerodynamic helmet with faint electric-blue streaks. Enhances reflexes and slightly sharpens perception, perfect for mid-level speedsters.",
            "helmet",
            "Speed",
            "C"
        ))

        equipments.append(Equipment(
            "Skyblade Body Suit",
            "A streamlined suit with flexible panels that boost movement speed and agility. Its subtle energy channels leave faint afterimages when running fast.",
            "body",
            "Speed",
            "C"
        ))

        equipments.append(Equipment(
            "Skyblade Leggings",
            "Durable leggings that improve stride efficiency and leg strength. Quick movements leave faint trails of blue light, signaling growing speed mastery.",
            "pants",
            "Speed",
            "C"
        ))

        equipments.append(Equipment(
            "Skyblade Boots",
            "Aerodynamic boots designed for acceleration and swift turns. Each step leaves a shimmer of speed energy, enhancing overall mobility for mid-level adventurers.",
            "boots",
            "Speed",
            "C"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Elven Hood",
            "A finely crafted hood that sharpens the senses and aids in swift movements.",
            "helmet",
            "Evasion",
            "C"
        ))

        equipments.append(Equipment(
            "Elven Armor",
            "Lightweight body armor favored by elves, increases dexterity and evasion.",
            "body",
            "Evasion",
            "C"
        ))

        equipments.append(Equipment(
            "Elven Leggings",
            "Slim, flexible leggings that allow for quiet steps and quick maneuvers.",
            "pants",
            "Evasion",
            "C"
        ))

        equipments.append(Equipment(
            "Elven Boots",
            "Boots designed for swiftness, perfect for traversing forests without a sound.",
            "boots",
            "Evasion",
            "C"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Ironclad Helmet",
            "A helmet forged from iron, offers high physical defense and durability.",
            "helmet",
            "Tank",
            "C"
        ))

        equipments.append(Equipment(
            "Ironclad Chestplate",
            "A solid iron chestplate built to withstand even the heaviest blows.",
            "body",
            "Tank",
            "C"
        ))

        equipments.append(Equipment(
            "Ironclad Legplates",
            "Heavy iron greaves that protect the wearer’s legs while anchoring them in place.",
            "pants",
            "Tank",
            "C"
        ))

        equipments.append(Equipment(
            "Ironclad Boots",
            "Boots of solid iron that make every step feel unshakable.",
            "boots",
            "Tank",
            "C"
        ))
        

        ######## FULL GEAR ########
        
        equipments.append(Equipment(
            "Mercenary Helm",
            "A sturdy helm favored by mercenaries, offering protection and enhancing focus.",
            "helmet",
            "Strength",
            "C"
        ))

        equipments.append(Equipment(
            "Mercenary Chestplate",
            "A tough chestplate designed for battlefield endurance and strength.",
            "body",
            "Strength",
            "C"
        ))

        equipments.append(Equipment(
            "Mercenary Pants",
            "Pants made for mercenaries, boosting strength and providing extra durability.",
            "pants",
            "Strength",
            "C"
        ))

        equipments.append(Equipment(
            "Mercenary Boots",
            "Boots built for long campaigns, improving stamina and power.",
            "boots",
            "Strength",
            "C"
        ))

        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Sorcery Hood",
            "A hood woven with enchanted threads that amplify magical power.",
            "helmet",
            "Magic",
            "C"
        ))

        equipments.append(Equipment(
            "Sorcery Robe",
            "A robe imbued with arcane energies, enhancing spellcasting abilities.",
            "body",
            "Magic",
            "C"
        ))

        equipments.append(Equipment(
            "Sorcery Pants",
            "Pants made for sorcerers, boosting magic.",
            "pants",
            "Magic",
            "C"
        ))

        equipments.append(Equipment(
            "Sorcery Boots",
            "Boots that increase mana flow and magical speed.",
            "boots",
            "Magic",
            "C"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Flameguard Helm",
            "A helmet that provides increased fire resistance and boosts physical defense.",
            "helmet",
            "Shield",
            "C"
        ))

        equipments.append(Equipment(
            "Flameguard Chestplate",
            "A chestplate forged in dragon fire, enhancing resistance and durability.",
            "body",
            "Shield",
            "C"
        ))

        equipments.append(Equipment(
            "Flameguard Legplates",
            "Legplates that protect against flames and physical attacks alike.",
            "pants",
            "Shield",
            "C"
        ))

        equipments.append(Equipment(
            "Flameguard Boots",
            "Boots that help the wearer withstand intense heat and harsh impacts.",
            "boots",
            "Shield",
            "C"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Demonhunter Hood",
            "A hood that sharpens senses and grants enhanced stealth for hunting fiends.",
            "helmet",
            "Critical",
            "C"
        ))

        equipments.append(Equipment(
            "Demonhunter Vest",
            "Light armor that balances protection and agility for demon slayers.",
            "body",
            "Critical",
            "C"
        ))

        equipments.append(Equipment(
            "Demonhunter Leggings",
            "Flexible leggings that increase evasion and critical strike potential.",
            "pants",
            "Critical",
            "C"
        ))

        equipments.append(Equipment(
            "Demonhunter Boots",
            "Boots designed for elite demon hunters, offering speed, evasion, and increased critical damage.",
            "boots",
            "Critical",
            "C"
        ))
        

        ######## FULL GEAR ########


        equipments.append(Equipment(
            "Berserker Helm",
            "A rugged helm that sharpens reflexes and fuels the wearer’s fury.",
            "helmet",
            "Dexterity",
            "C"
        ))

        equipments.append(Equipment(
            "Berserker Plate",
            "A heavy armor that increases dexterity and grants a temporary rage buff after being hit.",
            "body",
            "Dexterity",
            "C"
        ))

        equipments.append(Equipment(
            "Berserker Greaves",
            "Armored pants that enhance movement speed and provoke berserk fury.",
            "pants",
            "Dexterity",
            "C"
        ))

        equipments.append(Equipment(
            "Berserker Boots",
            "Boots that increase agility and feed the wearer’s rage on impact.",
            "boots",
            "Dexterity",
            "C"
        ))


        ######## Other ########
        

        equipments.append(Equipment(
            "Knight's Armor",
            "Heavy armor worn by knights, offering high defense and stability.",
            "body", 
            "Tank",
            "C"
        ))

        equipments.append(Equipment(
            "Spectral Boots",
            "Boots crafted from the essence of shadows. They grant enhanced evasion and a bonus to stealth.",
            "boots",
            "Evasion",
            "C"
        ))

        equipments.append(Equipment(
            "Steelfoot Pants",
            "Heavy pants made from steel that increase physical defense and movement speed.",
            "pants",
            "Tank",
            "C"
        ))

        equipments.append(Equipment(
            "Windward Body Armor",
            "A body armor that boosts evasion and agility, perfect for swift fighters.",
            "body",
            "Evasion",
            "C"
        ))

        equipments.append(Equipment(
            "Giant's Helmet",
            "A massive helmet that greatly increases strength and durability.",
            "helmet",
            "Tank",
            "C"
        ))

        
        equipments.append(Equipment(
            "Darksteel Body Armor",
            "A body armor made from darksteel, offering immense protection but reducing speed.",
            "body",
            "Tank",
            "C"
        ))

        equipments.append(Equipment(
            "Ironboots",
            "Boots made from iron, providing solid defense and increased resistance to damage.",
            "boots",
            "Tank",
            "C"
        ))

        equipments.append(Equipment(
            "Hardened Leather Body Armor",
            "Light armor made from hardened leather, boosting evasion and critical hit chance.",
            "body",
            "Evasion",
            "C"
        ))

        equipments.append(Equipment(
            "Elderhelm",
            "An ancient helmet that grants wisdom and protects against magical attacks.",
            "helmet",
            "Magic",
            "C"
        ))

        ########
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # B CLASS
        
        ######## FULL MIRACLE GEAR (Rank B) ########
        equipments.append(Equipment(
            "Sacred Hood",
            "A hood woven with golden thread, radiating quiet reverence.",
            "helmet",
            "Miracle",
            "B"
        ))

        equipments.append(Equipment(
            "Sacred Vestments",
            "Elaborate robes carrying the weight of ancient prayers. Inspires awe.",
            "body",
            "Miracle",
            "B"
        ))

        equipments.append(Equipment(
            "Sacred Trousers",
            "Garments imbued with solemn rites. Worn only by the devoted.",
            "pants",
            "Miracle",
            "B"
        ))

        equipments.append(Equipment(
            "Sacred Sandals",
            "Sandals strengthened by blessings. Each step echoes with faith.",
            "boots",
            "Miracle",
            "B"
        ))
        ######## FULL GEAR FOR SPEED ########
        equipments.append(Equipment(
            "Speedster Helmet",
            "A sleek helmet designed for maximum agility. Reduces air resistance and enhances reflexes.",
            "helmet",
            "Speed",
            "B"
        ))

        equipments.append(Equipment(
            "Speedster Body Suit",
            "A tight-fitting suit that increases movement speed and flexibility, perfect for rapid maneuvers.",
            "body",
            "Speed",
            "B"
        ))

        equipments.append(Equipment(
            "Speedster Pants",
            "Lightweight pants designed for quick movement, with energy-enhancing lines that boost speed.",
            "pants",
            "Speed",
            "B"
        ))

        equipments.append(Equipment(
            "Speedster Boots",
            "Streamlined boots that increase running speed and reduce fatigue during long sprints.",
            "boots",
            "Speed",
            "B"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Swiftstride Hood",
            "A lightweight hood that enhances agility and sharpens reflexes.",
            "helmet",
            "Evasion",
            "B"
        ))

        equipments.append(Equipment(
            "Swiftstride Armor",
            "Armor designed for speed, granting increased evasion and movement.",
            "body",
            "Evasion",
            "B"
        ))

        equipments.append(Equipment(
            "Swiftstride Leggings",
            "Flexible leggings that improve quickness and dodge capabilities.",
            "pants",
            "Evasion",
            "B"
        ))

        equipments.append(Equipment(
            "Swiftstride Boots",
            "Boots that increase movement speed and evasion, perfect for agile warriors.",
            "boots",
            "Evasion",
            "B"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Helm of the Fallen King",
            "A regal helmet that enhances strength and grants resistance to critical hits.",
            "helmet",
            "Tank",
            "B"
        ))

        equipments.append(Equipment(
            "Armor of the Fallen King",
            "A chestplate that embodies the resilience and might of a fallen monarch.",
            "body",
            "Tank",
            "B"
        ))

        equipments.append(Equipment(
            "Legplates of the Fallen King",
            "Leg armor that fortifies and empowers the wearer with royal strength.",
            "pants",
            "Tank",
            "B"
        ))

        equipments.append(Equipment(
            "Boots of the Fallen King",
            "Boots that ground the wearer with unmatched stability and endurance.",
            "boots",
            "Tank",
            "B"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Dragonbone Helm",
            "A helm forged from ancient dragon bones, providing exceptional defense and fire resistance.",
            "helmet",
            "Shield",
            "B"
        ))

        equipments.append(Equipment(
            "Dragonbone Armor",
            "A body armor crafted from the bones of ancient dragons, offering massive defense and fire resistance.",
            "body",
            "Shield",
            "B"
        ))

        equipments.append(Equipment(
            "Dragonbone Greaves",
            "Leg armor that protects with the strength and heat resistance of dragon bones.",
            "pants",
            "Shield",
            "B"
        ))

        equipments.append(Equipment(
            "Dragonbone Boots",
            "Boots that shield the wearer from intense heat while providing sturdy footing.",
            "boots",
            "Shield",
            "B"
        ))


        ######## FULL GEAR ########        
        equipments.append(Equipment(
            "Celestial Crown",
            "An ethereal crown that enhances wisdom and provides protection against elemental magic.",
            "helmet",
            "Magic",
            "B"
        ))

        equipments.append(Equipment(
            "Celestial Mantle",
            "A radiant mantle woven from stardust, increasing critical damage and mana regeneration.",
            "body",
            "Magic",
            "B"
        ))

        equipments.append(Equipment(
            "Celestial Leggings",
            "Leggings that shimmer with astral light, boosting critical hit chance and damage.",
            "pants",
            "Magic",
            "B"
        ))

        equipments.append(Equipment(
            "Celestial Greaves",
            "Greaves that grant swift movement and enhance critical strike efficiency.",
            "boots",
            "Magic",
            "B"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Valkyrie Helm",
            "A lightweight helm adorned with feathers, boosting agility and reflexes.",
            "helmet",
            "Dexterity",
            "B"
        ))

        equipments.append(Equipment(
            "Valkyrie Armor",
            "Armor made from the feathers of Valkyries, offering extreme agility and dexterity.",
            "body",
            "Dexterity",
            "B"
        ))

        equipments.append(Equipment(
            "Valkyrie Leggings",
            "Flexible leggings that enhance movement speed and nimbleness.",
            "pants",
            "Dexterity",
            "B"
        ))

        equipments.append(Equipment(
            "Valkyrie Boots",
            "Boots designed for swift movement and graceful agility.",
            "boots",
            "Dexterity",
            "B"
        ))

        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Astral Hood",
            "A hood infused with starlight, enhancing critical precision and focus.",
            "helmet",
            "Critical",
            "B"
        ))

        equipments.append(Equipment(
            "Astral Robe",
            "A flowing robe charged with cosmic energy, increasing critical damage.",
            "body",
            "Critical",
            "B"
        ))

        equipments.append(Equipment(
            "Astral Pants",
            "Pants imbued with cosmic energy, boosting critical hit chance and damage.",
            "pants",
            "Critical",
            "B"
        ))

        equipments.append(Equipment(
            "Astral Boots",
            "Boots that enhance movement and critical strike capabilities.",
            "boots",
            "Critical",
            "B"
        ))

        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Viperstrike Helm",
            "A helmet that sharpens the wearer’s strikes and fortifies their resolve.",
            "helmet",
            "Strength",
            "B"
        ))

        equipments.append(Equipment(
            "Viperstrike Chestplate",
            "A chestplate that boosts raw power and deadly precision.",
            "body",
            "Strength",
            "B"
        ))

        equipments.append(Equipment(
            "Viperstrike Legguards",
            "Leg armor that enhances movement strength and lethal force.",
            "pants",
            "Strength",
            "B"
        ))

        equipments.append(Equipment(
            "Viperstrike Boots",
            "Boots that enhance strength and damage.",
            "boots",
            "Strength",
            "B"
        ))


        ######## Other ########

        equipments.append(Equipment(
            "Celestial Chestplate",
            "A chestplate blessed by the gods, offering extraordinary defense and holy resistance.",
            "body",
            "Tank",
            "B"
        ))

        equipments.append(Equipment(
            "Windrider Helm",
            "A helmet that grants enhanced agility and grants a chance to dodge attacks.",
            "helmet",
            "Evasion",
            "B"
        ))

        equipments.append(Equipment(
            "Armageddon Boots",
            "Boots that imbue the wearer with fiery speed, boosting movement speed and fire resistance.",
            "boots",
            "Tank",
            "B"
        ))

        equipments.append(Equipment(
            "Phantom Lurker Pants",
            "Pants woven from the fabric of shadows, increasing evasion and granting stealth.",
            "pants",
            "Evasion",
            "B"
        ))

        equipments.append(Equipment(
            "Revenant Helm",
            "A helm forged from the remains of a powerful revenant. It increases health and provides a shield upon death.",
            "helmet",
            "Tank",
            "B"
        ))

        equipments.append(Equipment(
            "Frostguard Armor",
            "An icy armor that greatly boosts defense against frost and grants immunity to freezing effects.",
            "body",
            "Tank",
            "B"
        ))

        equipments.append(Equipment(
            "Shroud of the Wraith",
            "A body armor that enhances evasion and allows the wearer to move through walls for short periods.",
            "body",
            "Evasion",
            "B"
        ))

        ########

        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # A CLASS

        ######## FULL MIRACLE GEAR (Rank A) ########
        equipments.append(Equipment(
            "Divine Hood",
            "A hood that shines with otherworldly light. Said to silence all fear.",
            "helmet",
            "Miracle",
            "A"
        ))

        equipments.append(Equipment(
            "Divine Robe",
            "Robes woven with threads of celestial grace. They uplift all who gaze upon them.",
            "body",
            "Miracle",
            "A"
        ))

        equipments.append(Equipment(
            "Divine Trousers",
            "Finely tailored garments, radiant with sanctity. Bestowed upon the chosen.",
            "pants",
            "Miracle",
            "A"
        ))

        equipments.append(Equipment(
            "Divine Sandals",
            "Footwear said to tread upon both earth and heavens. Each step carries divine will.",
            "boots",
            "Miracle",
            "A"
        ))

        ######## FULL GEAR FOR SPEED ########
        equipments.append(Equipment(
            "Azure Velocity Helmet",
            "A sleek, aerodynamic helmet infused with speed energy. Minimizes wind resistance and sharpens reflexes, allowing the wearer to react in the blink of an eye.",
            "helmet",
            "Speed",
            "A"
        ))

        equipments.append(Equipment(
            "Azure Velocity Body Suit",
            "A form-fitting suit designed for ultimate mobility. Its energy-lined fibers enhance stride and agility, leaving faint streaks of blue light with each movement.",
            "body",
            "Speed",
            "A"
        ))

        equipments.append(Equipment(
            "Azure Velocity Pants",
            "Lightweight, flexible pants that boost leg movement and acceleration. Motion trails and subtle energy currents wrap the wearer’s legs, signaling unmatched swiftness.",
            "pants",
            "Speed",
            "A"
        ))

        equipments.append(Equipment(
            "Azure Velocity Boots",
            "Streamlined boots that channel kinetic energy into rapid movement. Every step leaves a shimmer of blue energy, turning sprints into bursts of near-instant travel.",
            "boots",
            "Speed",
            "A"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Emberstorm Helm",
            "A helm forged in volcanic flames, boosting fire resistance and endurance.",
            "helmet",
            "Tank",
            "A"
        ))

        equipments.append(Equipment(
            "Emberstorm Chestplate",
            "Chest armor imbued with molten power, granting supreme fire resistance.",
            "body",
            "Tank",
            "A"
        ))

        equipments.append(Equipment(
            "Emberstorm Legplates",
            "Leg armor that protects against extreme heat and enhances durability.",
            "pants",
            "Tank",
            "A"
        ))

        equipments.append(Equipment(
            "Emberstorm Boots",
            "Boots made from the essence of a volcanic eruption, increasing fire resistance and speed.",
            "boots",
            "Tank",
            "A"
        ))
        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Hellfire Helm",
            "A helm infused with molten lava, providing strong defense and fire damage reflection.",
            "helmet",
            "Shield",
            "A"
        ))

        equipments.append(Equipment(
            "Hellfire Plate",
            "A chestplate crafted from molten lava, offering high defense and fire damage reflection.",
            "body",
            "Shield",
            "A"
        ))

        equipments.append(Equipment(
            "Hellfire Greaves",
            "Leg armor that reflects heat and shields against physical attacks.",
            "pants",
            "Shield",
            "A"
        ))

        equipments.append(Equipment(
            "Hellfire Boots",
            "Boots that provide solid footing and reflect fiery damage back at attackers.",
            "boots",
            "Shield",
            "A"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Wraith's Hood",
            "A hood woven from spectral threads, enhancing evasion and ghostly agility.",
            "helmet",
            "Evasion",
            "A"
        ))

        equipments.append(Equipment(
            "Wraith's Garb",
            "A body armor made of spectral material, boosting evasion and reducing incoming damage.",
            "body",
            "Evasion",
            "A"
        ))

        equipments.append(Equipment(
            "Wraith's Leggings",
            "Leggings that grant swift, ghost-like movements and damage mitigation.",
            "pants",
            "Evasion",
            "A"
        ))

        equipments.append(Equipment(
            "Wraith's Boots",
            "Boots that let the wearer slip through danger with ease and resilience.",
            "boots",
            "Evasion",
            "A"
        ))

        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Hood of the Abyss",
            "A dark hood that enhances magical resistance and critical strike potency.",
            "helmet",
            "Magic",
            "A"
        ))

        equipments.append(Equipment(
            "Cloak of the Abyss",
            "A dark cloak that greatly increases magical resistance and increases critical hit damage.",
            "body",
            "Magic",
            "A"
        ))

        equipments.append(Equipment(
            "Leggings of the Abyss",
            "Legwear imbued with abyssal magic, boosting magic defense and critical power.",
            "pants",
            "Magic",
            "A"
        ))

        equipments.append(Equipment(
            "Galoshes of the Abyss",
            "Boots that grant swift movement and enhanced magical resistance.",
            "boots",
            "Magic",
            "A"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Shadowveil Hood",
            "A mysterious hood that channels dark power to boost strength and magical resistance.",
            "helmet",
            "Strength",
            "A"
        ))

        equipments.append(Equipment(
            "Shadowveil Mantle",
            "A mysterious mantle that channels dark power to greatly increase your strength, bolster magical resistance, and amplify critical hit damage.",
            "body",
            "Strength",
            "A"
        ))

        equipments.append(Equipment(
            "Shadowveil Legguards",
            "Legguards that enhance strength and protect against magical attacks.",
            "pants",
            "Strength",
            "A"
        ))

        equipments.append(Equipment(
            "Shadowveil Boots",
            "Boots that empower strength and provide magical resistance.",
            "boots",
            "Strength",
            "A"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Swiftstrike Hood",
            "A dark hood that sharpens agility and precision, boosting dexterity and magical resistance.",
            "helmet",
            "Dexterity",
            "A"
        ))
        
        equipments.append(Equipment(
            "Swiftstrike Raiment",
            "A dark cloak that enhances your agility and precision, greatly increasing dexterity, while also boosting magical resistance and critical hit damage.",
            "body",
            "Dexterity",
            "A"
        ))

        equipments.append(Equipment(
            "Swiftstrike Leggings",
            "Leggings that increase dexterity and protect against magical assaults.",
            "pants",
            "Dexterity",
            "A"
        ))

        equipments.append(Equipment(
            "Swiftstrike Boots",
            "Boots designed for swift movement and enhanced precision.",
            "boots",
            "Dexterity",
            "A"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Razorwind Hood",
            "A dark hood that sharpens instincts and boosts critical strike power with magical resistance.",
            "helmet",
            "Critical",
            "A"
        ))

        equipments.append(Equipment(
            "Razorwind Shroud",
            "A dark cloak that sharpens your instincts and amplifies your critical strike power, greatly increasing critical damage while providing strong magical resistance.",
            "body",
            "Critical",
            "A"
        ))

        equipments.append(Equipment(
            "Razorwind Leggings",
            "Leggings that amplify critical damage and offer magical defense.",
            "pants",
            "Critical",
            "A"
        ))

        equipments.append(Equipment(
            "Razorwind Boots",
            "Boots designed to increase agility and critical strike damage.",
            "boots",
            "Critical",
            "A"
        ))


        ######## Other ########

        equipments.append(Equipment(
            "Shadowstep Pants",
            "Pants that enhance dexterity and improve evasive maneuvers.",
            "pants",
            "Dexterity",
            "A"
        ))

        equipments.append(Equipment(
            "Tornado Runner Boots",
            "Light boots that increase movement speed and dexterity.",
            "boots",
            "Dexterity",
            "A"
        ))

        equipments.append(Equipment(
            "Phantom Cloak",
            "A body armor that increases critical damage and magical resistance.",
            "body",
            "Critical",
            "A"
        ))

        equipments.append(Equipment(
            "Eagle’s Gaze Helm",
            "Helmet that enhances dexterity and precision in battle.",
            "helmet",
            "Dexterity",
            "A"
        ))

        equipments.append(Equipment(
            "Swiftstrike Pants",
            "Pants that boost critical hit chance and speed.",
            "pants",
            "Critical",
            "A"
        ))

        equipments.append(Equipment(
            "Shadowblade Boots",
            "Boots that enhance dexterity and allow for swift, silent movement.",
            "boots",
            "Dexterity",
            "A"
        ))

        equipments.append(Equipment(
            "Nightfall Helm",
            "Helmet that increases critical damage and sharpens focus.",
            "helmet",
            "Critical",
            "A"
        ))

        equipments.append(Equipment(
            "Ghostwalker Body Armor",
            "Body armor that improves dexterity and grants enhanced agility.",
            "body",
            "Dexterity",
            "A"
        ))

        equipments.append(Equipment(
            "Aegis Sentinel Helm",
            "A sturdy helmet that greatly increases defense and magical resistance.",
            "helmet",
            "Tank",
            "A"
        ))

        equipments.append(Equipment(
            "Bulwark Boots",
            "Heavy boots that improve endurance and reduce damage taken.",
            "boots",
            "Tank",
            "A"
        ))

        equipments.append(Equipment(
            "Mystic Wardrobe",
            "Body armor that enhances magical power and boosts mana regeneration.",
            "body",
            "Magic",
            "A"
        ))

        equipments.append(Equipment(
            "Arcane Veil Pants",
            "Pants that increase magic defense and spellcasting speed.",
            "pants",
            "Magic",
            "A"
        ))

        equipments.append(Equipment(
            "Fortress Guard Helm",
            "Helmet that improves physical defense and grants shield bonuses.",
            "helmet",
            "Shield",
            "A"
        ))

        equipments.append(Equipment(
            "Guardian’s Step Boots",
            "Boots that increase resistance to knockback and boost stamina.",
            "boots",
            "Shield",
            "A"
        ))

        equipments.append(Equipment(
            "Enchanter’s Robes",
            "Body armor that greatly enhances spell power and magical resistance.",
            "body",
            "Magic",
            "A"
        ))

        equipments.append(Equipment(
            "Ironclad Pants",
            "Durable pants that boost physical defense and health regeneration.",
            "pants",
            "Tank",
            "A"
        ))

        equipments.append(Equipment(
            "Shieldbearer’s Helm",
            "Helmet that improves shield durability and grants increased block chance.",
            "helmet",
            "Shield",
            "A"
        ))

        equipments.append(Equipment(
            "Spellweaver Boots",
            "Boots that enhance magic speed and increase mana regeneration.",
            "boots",
            "Magic",
            "A"
        ))


        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # S CLASS

        ######## FULL MIRACLE GEAR (Rank S) ########
        equipments.append(Equipment(
            "Transcendent Crown",
            "A radiant crown of pure light. Said to be gifted only to those chosen by the heavens.",
            "helmet",
            "Miracle",
            "S"
        ))

        equipments.append(Equipment(
            "Transcendent Robe",
            "Robes that shimmer with celestial brilliance, flowing as if alive with divine power.",
            "body",
            "Miracle",
            "S"
        ))

        equipments.append(Equipment(
            "Transcendent Garments",
            "Clothing woven from threads of starlight. A symbol of miracles beyond comprehension.",
            "pants",
            "Miracle",
            "S"
        ))

        equipments.append(Equipment(
            "Transcendent Sandals",
            "Sandals that leave no trace upon the earth. Each step echoes in eternity.",
            "boots",
            "Miracle",
            "S"
        ))


        ######## FULL GEAR FOR SPEED: GODSLAYER SET ########
        equipments.append(Equipment(
            "Celestial Tempest Helmet",
            "A razor-sharp, lightning-infused helmet that bends time around the wearer. Eyes glow with divine energy, granting reflexes faster than the blink of a god.",
            "helmet",
            "Speed",
            "S"
        ))

        equipments.append(Equipment(
            "Celestial Tempest Body Suit",
            "Forged from ethereal fibers and infused with storm energy, this suit lets the wearer move at incomprehensible speeds. Every movement leaves trails of crackling blue lightning, capable of rending divine armor.",
            "body",
            "Speed",
            "S"
        ))

        equipments.append(Equipment(
            "Celestial Tempest Leggings",
            "Lightweight yet indestructible, these pants channel kinetic and divine energies to supercharge running and dodging. With every stride, the ground seems to warp beneath them, leaving afterimages that confuse gods.",
            "pants",
            "Speed",
            "S"
        ))

        equipments.append(Equipment(
            "Celestial Tempest Boots",
            "Boots designed to shatter the sound barrier, striking fear into immortals. They release concentrated bursts of speed, turning sprints into teleportation-like movements, leaving trails of god-scorching energy.",
            "boots",
            "Speed",
            "S"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Guardian's Helmet",
            "A helmet worn by ancient guardians, boosting vitality and providing a shield that absorbs damage.",
            "helmet",
            "Tank",
            "S"
        ))

        equipments.append(Equipment(
            "Guardian's Armor",
            "Body armor of ancient guardians, offering unmatched protection and vitality.",
            "body",
            "Tank",
            "S"
        ))

        equipments.append(Equipment(
            "Guardian's Greaves",
            "Pants forged for ancient guardians, providing resilience and damage absorption.",
            "pants",
            "Tank",
            "S"
        ))

        equipments.append(Equipment(
            "Guardian's Boots",
            "Boots worn by ancient guardians, offering stability, durability, and defense.",
            "boots",
            "Tank",
            "S"
        ))



        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Crown of the Eternal Emperor",
            "A crown forged from the celestial essence of an eternal emperor, boosting strength, defense, and resilience.",
            "helmet",
            "Shield",
            "S"
        ))

        equipments.append(Equipment(
            "Armor of the Eternal Emperor",
            "Armor blessed by the eternal emperor, offering unparalleled protection and resilience.",
            "body",
            "Shield",
            "S"
        ))

        equipments.append(Equipment(
            "Greaves of the Eternal Emperor",
            "Greaves forged from celestial essence, providing unmatched defense and stamina.",
            "pants",
            "Shield",
            "S"
        ))

        equipments.append(Equipment(
            "Boots of the Eternal Emperor",
            "Boots that grant steadfast strength and resilience, worthy of an eternal ruler.",
            "boots",
            "Shield",
            "S"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Hood of Shadows",
            "A hood imbued with the powers of shadows, enhancing stealth, evasion, and awareness in the dark.",
            "helmet",
            "Evasion",
            "S"
        ))

        equipments.append(Equipment(
            "Veil of Shadows",
            "A cloak imbued with the powers of shadows, increasing stealth, evasion, and damage output in the dark.",
            "body",
            "Evasion",
            "S"
        ))

        equipments.append(Equipment(
            "Leggings of Shadows",
            "Leg armor infused with shadow magic, granting swift movements and evasive maneuvers.",
            "pants",
            "Evasion",
            "S"
        ))

        equipments.append(Equipment(
            "Boots of Shadows",
            "Boots that allow the wearer to move silently and dodge with ease in darkness.",
            "boots",
            "Evasion",
            "S"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Vortex Helm",
            "A legendary helmet that maximizes critical strike damage and sharpens reflexes.",
            "helmet",
            "Critical",
            "S"
        ))

        equipments.append(Equipment(
            "Vortex Armor",
            "Body armor designed for masters of precision, greatly enhancing critical strike damage and speed.",
            "body",
            "Critical",
            "S"
        ))

        equipments.append(Equipment(
            "Vortex Greaves",
            "Pants forged for deadly marksmen, increasing agility, precision, and critical damage.",
            "pants",
            "Critical",
            "S"
        ))

        equipments.append(Equipment(
            "Vortex Boots",
            "Boots that boost movement speed and reflexes, enabling devastating critical strikes.",
            "boots",
            "Critical",
            "S"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Arcane Sovereign Crown",
            "A crown infused with pure arcane power, enhancing magical strength and focus.",
            "helmet",
            "Magic",
            "S"
        ))

        equipments.append(Equipment(
            "Arcane Sovereign Robe",
            "Body armor pulsing with pure magic, vastly increasing spell power and mana regeneration.",
            "body",
            "Magic",
            "S"
        ))

        equipments.append(Equipment(
            "Arcane Sovereign Leggings",
            "Pants woven with threads of raw magic, improving mana flow and magical potency.",
            "pants",
            "Magic",
            "S"
        ))

        equipments.append(Equipment(
            "Arcane Sovereign Boots",
            "Boots that increase movement speed and channel magical energy with each step.",
            "boots",
            "Magic",
            "S"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Titan’s Helm",
            "A massive helm that significantly boosts strength and physical damage output.",
            "helmet",
            "Strength",
            "S"
        ))

        equipments.append(Equipment(
            "Titan’s Plate",
            "Body armor forged for unmatched warriors, greatly boosting strength and physical power.",
            "body",
            "Strength",
            "S"
        ))

        equipments.append(Equipment(
            "Titan’s Greaves",
            "Heavy pants built for unstoppable fighters, increasing strength and endurance.",
            "pants",
            "Strength",
            "S"
        ))

        equipments.append(Equipment(
            "Titan’s Boots",
            "Boots that grant unshakable stability and power, enhancing strength and striking force.",
            "boots",
            "Strength",
            "S"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Shadowstrike Helm",
            "A helm crafted for swift warriors, boosting dexterity, reaction speed, and precision.",
            "helmet",
            "Dexterity",
            "S"
        ))

        equipments.append(Equipment(
            "Shadowstrike Armor",
            "Body armor designed to heighten dexterity and precision, granting swift and deadly attacks.",
            "body",
            "Dexterity",
            "S"
        ))

        equipments.append(Equipment(
            "Shadowstrike Legguards",
            "Lightweight pants enhancing agility, precision, and flawless movement.",
            "pants",
            "Dexterity",
            "S"
        ))

        equipments.append(Equipment(
            "Shadowstrike Boots",
            "Boots built for lightning-fast movement, boosting dexterity and precision with every step.",
            "boots",
            "Dexterity",
            "S"
        ))



        ######## Other ########

        equipments.append(Equipment(
            "Eclipse Boots",
            "Boots imbued with shadow energy that greatly boost critical hit chance and movement speed.",
            "boots",
            "Critical",
            "S"
        ))

        equipments.append(Equipment(
            "Celestial Pants",
            "Pants woven from starlight that enhance magical defense and casting speed.",
            "pants",
            "Magic",
            "S"
        ))

        equipments.append(Equipment(
            "Berserker’s Boots",
            "Boots that grant unmatched power and increase critical hit damage for strength-based warriors.",
            "boots",
            "Strength",
            "S"
        ))

        
        equipments.append(Equipment(
            "Windblade Pants",
            "Light pants that increase dexterity and critical hit chance with unparalleled agility.",
            "pants",
            "Dexterity",
            "S"
        ))

        equipments.append(Equipment(
            "Phantom Helm",
            "A helmet that blends magic and critical precision, amplifying spell crit damage significantly.",
            "helmet",
            "Critical",
            "S"
        ))

        equipments.append(Equipment(
            "Sorcerer’s Step Boots",
            "Boots that boost magical speed and critical damage, favored by the most skilled mages.",
            "boots",
            "Magic",
            "S"
        ))
        
        # # Starting weapons and equipments for testing purposes
        # myWeapons.append(next(w for w in weapons if w.weapon_id == 15))
        # myEquipments.append(next(e for e in equipments if e.equipment_id == 0))
        # myEquipments.append(next(e for e in equipments if e.equipment_id == 1))
        # myEquipments.append(next(e for e in equipments if e.equipment_id == 2))
        # myEquipments.append(next(e for e in equipments if e.equipment_id == 3))
        # myEquipments.append(next(e for e in equipments if e.equipment_id == 4))

        # initializing the expedition things
        initializing_expedition_enemies()
        
        # initializing the expedition bosses things
        initializing_expedition_bosses()

        # add equipments for testing purposes
        add_new_equipment_to_our_bag(0)
        add_new_equipment_to_our_bag(1)
        add_new_equipment_to_our_bag(2)
        add_new_equipment_to_our_bag(3)
        add_new_equipment_to_our_bag(4)
        
        add_new_weapon_to_our_bag(0)
        add_new_weapon_to_our_bag(1)
        add_new_weapon_to_our_bag(2)
        add_new_weapon_to_our_bag(3)
        add_new_weapon_to_our_bag(4)



        region_map = {
            "Verdenglade": {"unlocked": True},
            "Cinderforge": {"unlocked": False},
            "Moonhollow": {"unlocked": False},
            "Rainmere": {"unlocked": False},
            "Greyspire": {"unlocked": False},
            "Ironridge": {"unlocked": False},
            "Brightgate": {"unlocked": False},
            "Steamcoil": {"unlocked": False},
            "Chronopolis": {"unlocked": False},
            "Techspire": {"unlocked": False},
            "OnlineStore": {"unlocked": True}
        }
        
        global online_shop_variable
        online_shop_variable = OnlineShop()

        global regions_variable
        regions_variable = Regions(region_map)

        return 