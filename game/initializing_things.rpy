init python:
    def initializing_things():
        global protectors_base_information
        global allExpeditionTemplates
        global allExpeditions
        global bossExpeditions
        global weapons
        global initial_weapons_choice
        global equipments
        global myEquipments

        Equipment._id_counter = 0   # Reset the counter
        Weapon._id_counter = 0   # Reset the counter
        Mission._id_counter = 0   # Reset the counter

        # creating protectors    
        protectors_base_information["Ninja"] = BaseProtectorData(
            {
                "strength": 10,
                "dexterity": 17,
                "constitution": 12,
                "intelligence": 14,
                "wisdom": 13,
                "charisma": 8,
                "speed": 15,
                "luck": 11,
                "attack_speed": 1.3
            },
            [
                "dexterity", "luck", "constitution", "dexterity", "speed",
                "constitution", "dexterity", "strength", "dexterity", "charisma", 
                "dexterity", "intelligence", "strength", "constitution", "wisdom", 
                "dexterity", "luck", "dexterity", "strength", "dexterity", 
                "wisdom", "constitution", "dexterity", "speed", "dexterity"
            ], 
            "EVA", "DEX_TAN", 
            "Ash Ninja", 
            "While exploring a forgotten cave, he touched a cursed relic that bound dark magic to his body. From that moment, he gained the power to transform into ash, disappearing into smoke to strike unseen.",
            "Tech Ninja", 
            "Recruited by the army, he wields weapons infused with cutting-edge technology and wears armor that adapts to any threat. Every strike is precise, every movement optimized, making him a deadly force on the battlefield.",
            ["Knife", "Sword", "Katana"], None, None,
            "Melee",
            "Regular",
            "Thieves knife"
        )
        
        protectors_base_information["Templar"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 10,
                "constitution": 18,
                "intelligence": 11,
                "wisdom": 16,
                "charisma": 15,
                "speed": 7,
                "luck": 8,
                "attack_speed": 0.7
            }, 
            [
                "strength", "wisdom", "constitution", "strength", "charisma", 
                "strength", "wisdom", "constitution", "strength", "intelligence", 
                "strength", "wisdom", "strength", "charisma", "constitution", 
                "strength", "wisdom", "strength", "luck", "strength", "speed"
            ], 
            "MIR_TAN", "MIR_STR_STR",
            "Saint Templar",
            "A devoted templar, he was granted a sacred blessing to wield the power of the saints. and every strike carries divine judgment. Guided by unbreakable devotion, he stands as a living vessel of sanctity on the battlefield.",
            "Demonic Templar",
            "Once a templar of faith, he forsook the light and accepted a blasphemous blessing from demons. His blade burns with unholy fire, his armor twists with infernal power, and every strike spreads corruption.",
            ["Sword", "Spear", "Greatsword"], None, None,
            "Melee",
            "Divine",
            "Templar Greatsword"
        )


        protectors_base_information["Wizard"] = BaseProtectorData(
            {
                "strength": 7,
                "dexterity": 12,
                "constitution": 11,
                "intelligence": 21,
                "wisdom": 18,
                "charisma": 9,
                "speed": 10,
                "luck": 12,
                "attack_speed": 0.9
            }, 
            [
                "intelligence", "wisdom", "constitution", "intelligence", "dexterity", 
                "wisdom", "intelligence", "constitution", "wisdom", "dexterity", 
                "intelligence", "wisdom", "constitution", "luck", "intelligence", 
                "wisdom", "charisma", "intelligence", "wisdom", "constitution", "speed"
            ], 
            "MIR_CON", "INT",
            "Thunder Wizard",
            "Through years of study in forgotten libraries, he unlocked the secrets of the arcane. Spells of thunder and lightning bend to his will, making him a master of battlefield control.",
            "Nature Wizard",
            "Clad in enchanted robes, he uses his nature spells to wields traps and kill enemies from the ground using his deadly vines. Using precision and strategy he shows as a dangerous threat for anyone who faces him.",
            ["Wand", "Staff"], None, None,
            "Ranged",
            "Magic",
            "Principiant Wand"
        )

        protectors_base_information["Ace"] = BaseProtectorData(
            {
                "strength": 8,
                "dexterity": 15,
                "constitution": 10,
                "intelligence": 15,
                "wisdom": 15,
                "charisma": 9,
                "speed": 12,
                "luck": 16,
                "attack_speed": 1.2
            }, 
            [
                "dexterity", "wisdom", "luck", "dexterity", "wisdom", 
                "constitution", "dexterity", "wisdom", "speed", "luck", 
                "dexterity", "wisdom", "luck", "luck", "dexterity", 
                "wisdom", "luck", "dexterity", "wisdom", "constitution",
                "constitution", "luck", "wisdom", "dexterity", "constitution"
            ], 
            "MIR_MIR_DEX", "CRI",
            "Demonic Dealer",
            "In a forgotten arcane library, he found a deck of dark enchanted cards, each holding demonic essence. Now, whispers from the cards slowly turn him into a demon with every throw.",
            "Ace of Fates",
            "A master of strategy and dexterity, he wields his deck like a razor-sharp blade. Every card is a weapon, every draw a calculated gamble, turning him into a lethal force from afar.",
            ["Cards"], None, None,
            "Melee",
            "Regular",
            "Deadman Cards"
        )

        protectors_base_information["Samurai"] = BaseProtectorData(
            {
                "strength": 16,
                "dexterity": 14,
                "constitution": 15,
                "intelligence": 12,
                "wisdom": 14,
                "charisma": 10,
                "speed": 10,
                "luck": 9,
                "attack_speed": 1.2
            },
            [
                "strength", "dexterity", "strength", "constitution", "speed", 
                "wisdom", "dexterity", "speed", "constitution", "strength", 
                "dexterity", "wisdom", "strength", "dexterity", "strength", 
                "intelligence", "strength", "dexterity", "constitution", "charisma"
            ], 
            "TAN", "DAM_SPE",
            "Tech Samurai",
            "Once bound by tradition, he forged a secret pact with visionary craftsmen. His blade, born of ancient mastery and hidden technology, strikes with unmatched precision; his armor adapts to any threat.",
            "Wolf Samurai",
            "Once a disciplined samurai, he was transformed into a fearsome wolf. Now faster, and driven by primal instinct, his strikes land with devastating force. He is an unstoppable predator on the battlefield.",
            ["Katana"], ["Katana"], ["Katana", "Sword", "Knife"],
            "Melee",
            "Regular",
            "Samurai Rusty Katana"
        )

        protectors_base_information["Recruit"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 17,
                "intelligence": 10,
                "wisdom": 9,
                "charisma": 13,
                "speed": 9,
                "luck": 11,
                "attack_speed": 1
            },
            [
                "dexterity", "strength", "dexterity", "constitution", "dexterity", 
                "strength", "dexterity", "constitution", "dexterity", "strength", 
                "dexterity", "constitution", "dexterity", "strength", "charisma", 
                "strength", "luck", "strength", "constitution", "charisma", "speed"
            ], 
            "EVA", "STR_STR_STR_CON_SPE",
            "Special Forces Agent",
            "Determined to become one of the best, he enlisted in the Special Forces intense training. After proving his skill, he earned his place and now strikes with unmatched precision, agility, and tactical mastery on every mission.",
            "Berserker",
            "Trapped in fear during a mission, the recruit’s mind finally snapped, and that terror erupted into uncontrollable, burning rage. Now he fights with pure instinct as he charges into battle with relentless ferocity.",
            ["Knife", "Gun", "Machine gun", "Sniper"], ["Knife", "Gun", "Machine gun", "Sniper"], ["Knife", "Sword", "Greatsword", "Greataxe", "Spear", "Axe", "Hammer", "Great Hammer", "Mace"],
            "Melee",
            "Regular",
            "Combat Pistol"
        )

        # protectors_base_information["Robot"] = BaseProtectorData(16, 14, 18, 16, 10, 6, 5, 0.25, 0.34, 0.2, 0.5, 0.16, 0.125, 0.1, 
        #     "HP", "INT_TAN",
        #     "Name 1",
        #     "Description 1",
        #     "Name 2",
        #     "Description 2",
        #     "",
        #     "Ranged"
        # )
        # # it gains:
        # # 1 intelligence per 2 levels
        # # 1 dexterity per 3 levels
        # # 1 strenght per 4 levels
        # # 1 constitution per 5 levels
        # # 1 wisdom per 6 levels
        # # 1 charisma per 8 levels
        # # 1 luck per 10 levels

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

        # Recreate Possible Missions # Tittle / description
        # 🔥 23 - Combat - damage?
        allExpeditionTemplates.append(ExpeditionTemplate("Fortress Under Siege", "Enemy forces are surrounding our stronghold. Hold the line and repel the assault.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Ambush the Ambushers", "A convoy was attacked on the trade route. Hunt down the attackers and secure the area.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Eliminate the Threat", "A dangerous warlord has been terrorizing nearby villages. Track him down and end his reign.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Border Skirmish", "Enemies are testing our defenses near the border. Push them back and show no weakness.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Outpost Reclaim", "One of our forward outposts has fallen. Lead a strike team to retake it.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Sabotage the Siege", "Enemy engineers are preparing siege weapons. Destroy them before they are complete.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("No Man's Pass", "Hold a mountain pass against overwhelming odds until reinforcements arrive.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Strike from the Shadows", "Lead a surprise night raid on a key enemy encampment.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Broken Line", "Our front line has collapsed. Fall back, regroup, and prevent a total rout.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Minefield Sweep", "Clear a path through a newly discovered minefield under enemy fire.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Airstrike Coordination", "Tag key targets in enemy territory to guide incoming bombardments.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Evacuate Under Fire", "Civilians are trapped in a combat zone. Cover their retreat while under attack.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Hold the Watchtower", "You're the last line of defense. Hold the tower until backup arrives.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Storm the Trenches", "Enemy trenches are heavily fortified. Lead the charge to break through.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Nightfall Offensive", "Launch a surprise attack at dusk to overwhelm the enemy before they regroup.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Flank and Collapse", "Find a weak point in the enemy formation and collapse their rear guard.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Burn the Bridge", "An enemy supply bridge must be destroyed before reinforcements arrive.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Crush the Rebellion", "An armed uprising has begun in the capital. Lead elite forces to suppress it.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Hold the Ridge", "You're the last line of defense on the high ground. Defend it at all costs.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Intercept the Raiders", "Raiders are headed toward a trade route. Intercept and neutralize them.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Tunnel Assault", "Enemies are using underground tunnels. Clear them out room by room.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Frozen Front", "A winter storm is closing in—fight off enemy forces before you're snowed in.", "Combat"))
        allExpeditionTemplates.append(ExpeditionTemplate("Retaliation Strike", "A nearby outpost was attacked. Launch a swift retaliatory strike to send a message.", "Combat"))


        # 🛡️ 23 - Rescue - defense
        allExpeditionTemplates.append(ExpeditionTemplate("Saving Hostages", "Bandits have taken hostages in this area. We must act quickly to rescue them before it's too late.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Escort the Caravan", "A merchant caravan needs safe passage through dangerous territory. Ensure their arrival without harm.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Protect the Witness", "A key witness is being targeted. Guard them until they can safely testify.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Save the Lost Scouts", "A scouting party is overdue and feared captured. Find them and bring them back.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Break the Siege", "A town is besieged and running low on supplies. Fight your way in and break the enemy hold.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Hostage Exchange", "Negotiate and protect a delicate exchange—any misstep could turn deadly.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Rescue the Healer", "A renowned healer is being held by raiders. Liberate them before their skills are lost.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Fleeing Refugees", "A column of refugees is fleeing conflict. Escort them to safe territory.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Secure the Convoy", "A high-value cargo convoy must reach its destination unharmed.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Assassins in the Shadows", "The city’s ruler is under threat. Uncover and eliminate the assassins.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Protect the Relic", "A sacred artifact is being transported. Guard it against thieves and zealots alike.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Retrieve the Captive Knight", "One of our champions is being held by the enemy. Storm the prison and free them.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Secure the Safehouse", "A safehouse is compromised. Protect the informants until extraction.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Collapse in the Mine", "A mine has collapsed, trapping workers underground. Organize a swift rescue.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Fishermen Adrift", "A storm has stranded fishermen at sea. Rescue them before their boat sinks.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Save the Pilgrims", "A group of pilgrims is being attacked on a sacred trail. Get them to safety.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Beneath the Rubble", "An explosion has leveled part of a village. Dig out survivors before time runs out.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Ghost Town Retrieval", "A ghost town has become haunted and dangerous. Retrieve a stranded family.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Poisoned Prisoners", "A prison has been sabotaged with poison gas. Rescue the inmates before it’s fatal.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Siege Evacuation", "Civilians are still trapped inside a city under siege. Smuggle them out silently.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Runaway Royalty", "A young noble has fled into enemy territory. Retrieve them before enemies do.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Collapsed Caravan", "A merchant caravan overturned in dangerous terrain. Rescue and protect the survivors.", "Rescue"))
        allExpeditionTemplates.append(ExpeditionTemplate("Lighthouse in Peril", "A lighthouse keeper hasn't responded in days. Investigate and rescue if needed.", "Rescue"))


        # 🕵️ 23 - Recon - evasion
        allExpeditionTemplates.append(ExpeditionTemplate("Mystery at Dawnfall", "Strange disappearances are happening in the town of Dawnfall. Investigate and uncover the truth.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Enemy Intel", "We've located a hidden enemy outpost. Infiltrate it and retrieve any valuable information.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Tracking the Shadows", "A spy has slipped past our borders. Follow their trail and report back.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Ciphers in the Dark", "A codebreaker believes an intercepted message holds secrets. Protect them while they work.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Ruins Recon", "Explore ancient ruins rumored to hide enemy scouts or forbidden tech.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Missing Patrol", "A regular patrol failed to report back. Investigate their last known location.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Eyes on the Enemy", "Shadow a convoy suspected of transporting illegal weapons—observe but do not engage.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Infiltrate the Council", "Attend a secret gathering disguised as a delegate and gather intelligence.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Interrogation Duty", "A captured spy refuses to talk. Guard them while the truth is extracted.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Echoes in the Fog", "Locals report strange sightings at night. Uncover the truth behind the rumors.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Dead Drop Retrieval", "A covert informant left intel in a public area. Retrieve it before it's compromised.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Decrypt the Past", "A recovered journal may reveal enemy plans. Help piece it together safely.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Footprints in the Snow", "Follow faint tracks through hostile terrain to uncover a hidden enemy camp.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Hollow Echoes", "Strange sounds come from a remote canyon. Investigate and report your findings.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Undercover Festival", "A known assassin will strike during a local festival. Blend in and find them first.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Smuggler’s Trail", "Follow the trail of a smuggler ring operating across borders.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Lantern Signal", "A coded light signal was seen in the hills. Investigate its source.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Vigil in the Fog", "Scouts claim something hunts in the mist. Stay hidden and learn what it is.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Whispers in the Court", "Court gossip hints at treason. Discreetly find out who's behind it.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("The Hidden Cache", "A map points to a hidden supply cache. Find it before others do.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Shifting Tracks", "Enemy patrol routes are changing daily. Record and map their new strategy.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Lurking Below", "Creatures have been seen in sewer tunnels. Investigate and confirm the threat.", "Recon"))
        allExpeditionTemplates.append(ExpeditionTemplate("Fog of War", "A thick fog conceals enemy movements. Scout and relay their position.", "Recon"))


        # 🌿 23 - Moral - Intelligence + wisdom?
        allExpeditionTemplates.append(ExpeditionTemplate("Food for the Famine", "A village is starving after a drought. Deliver supplies and ensure no one interferes.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Justice or Mercy?", "A criminal has surrendered—but the locals want blood. Decide their fate and keep the peace.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Healing the Wounded", "A field hospital is overrun. Defend the medics and help evacuate the wounded.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("A Town in Flames", "An accidental fire has devastated a village. Help organize rescue and relief.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Peace Talks", "Two factions are on the verge of war. Broker peace—without drawing your sword.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Defend the Innocent", "Vigilantes seek to punish suspected traitors. Intervene and ensure due process.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Medicine Run", "A deadly illness spreads fast. Deliver antidotes to the afflicted before it's too late.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Prison Riot", "Inmates have taken over a prison. Stop the violence without unnecessary bloodshed.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("The Orphan’s Plea", "A child begs you to save their kidnapped parent. Will you answer the call?", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Clean Water Crisis", "A poisoned river threatens an entire region. Investigate and resolve the source.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("The Unjust Law", "An edict puts innocents in danger. Uphold justice—even if it means defying orders.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Shelter from the Storm", "A deadly storm is coming. Guide survivors to shelter in time.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("A Burdened Conscience", "A soldier regrets their actions in battle. Help them find redemption—or justice.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("The Execution Order", "You're ordered to execute prisoners you believe are innocent. Decide what to do.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Child Soldiers", "Enemy forces include conscripted children. Find a way to stop the conflict peacefully.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Buried in Shame", "A past atrocity by your side has come to light. How will you respond?", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Outcast’s Return", "A wrongly exiled villager seeks protection. Decide whether to risk taking them in.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("The Slaver’s Coin", "A wealthy slaver offers gold to look the other way. Will you accept?", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Dying Wish", "A wounded enemy begs you to deliver a letter to their family. Will you honor it?", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("The Silent Ones", "A mute community is being exploited. Help them find justice without violence.", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("Echoes of Guilt", "An ally admits to a war crime. Do you turn them in or protect them?", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("False Prophet", "A preacher is stirring hate under the guise of peace. Confront or ignore?", "Moral"))
        allExpeditionTemplates.append(ExpeditionTemplate("The Beggar Prince", "A beggar claims to be a lost prince. Do you investigate or dismiss the claim?", "Moral"))


        # 🏛️ 23 - Political - Charisma
        allExpeditionTemplates.append(ExpeditionTemplate("Guard the Summit", "Leaders from across the land are meeting. Ensure their safety and prevent sabotage.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Negotiator's Escort", "A diplomat needs protection in hostile lands. Stay vigilant and avoid bloodshed.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Suppress the Coup", "A power struggle threatens to erupt into civil war. Step in and restore order before it's too late.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Guard the Treaty", "A peace treaty is about to be signed. Protect the venue from saboteurs.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Interrogate the Envoy", "A foreign diplomat may be a double agent. Handle the questioning with care.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Prevent the Vote", "A corrupt law is about to pass. Delay the council meeting by any (non-lethal) means.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Expose the Traitor", "Someone within the court is leaking secrets. Identify and confront them discreetly.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Public Trial", "A controversial trial draws angry mobs. Maintain peace during the proceedings.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Hidden Alliance", "Uncover a secret alliance that threatens to tip the balance of power.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Royal Escort", "The heir to the throne must travel through enemy-controlled territory. Protect them at all costs.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Noble Dispute", "A feud between two powerful houses threatens civil war. Mediate before it's too late.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Divided City", "A city is torn between factions. Support peaceful reunification through diplomacy and action.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Secure the Vote", "Corruption threatens the outcome of an election. Protect the polling process from interference.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Backroom Bargain", "A powerful lord is making secret deals. Discover what they're hiding.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Crowned in Secret", "A coronation was held in secret. Determine if the claim to power is legitimate.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Shield the Reformer", "A reformer wants to change the system. Protect them from assassination attempts.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Court of Lies", "Attend a royal court and uncover the falsehoods spreading among nobles.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Spoils of Peace", "Peace talks may lead to unjust land grabs. Expose the corruption.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Festival of Unity", "Keep tensions low between feuding factions during a national celebration.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Uneasy Alliance", "Two former enemies now share power. Keep the alliance from unraveling.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("The Puppet Master", "A figure behind the throne pulls all the strings. Discover their influence.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Scroll of Secrets", "A stolen diplomatic scroll contains dangerous secrets. Retrieve it discreetly.", "Political"))
        allExpeditionTemplates.append(ExpeditionTemplate("Kingmaker’s Gamble", "A noble is building power to influence the next ruler. Decide whether to support or stop them.", "Political"))


        # Recreate missions
        allExpeditions.append(Mission("Training", "Send a protector to train in your facilities.", 0, 1, 1, "Training", "not assigned", 99000, 0))

        creating_new_missions()

        bossExpeditions.append(BossExpedition(1, "The Mireborn Tyrant", "Deep within a poisonous swamp, a mutated beast commands venomous creatures and twisted flora. It oozes acid and rage — only its death can cleanse the land.", 20))
        bossExpeditions.append(BossExpedition(2, "The Pale King", "A ruler who transcended death now commands legions of the undead. His soul is bound to a cursed throne. Break his chains and survive the wrath of his fallen empire.", 25))
        bossExpeditions.append(BossExpedition(3, "The Hollow Sentinel", "A forgotten guardian awakens in the ruins of an ancient temple. Armed with rusted steel and remnants of lost magic, it strikes with surprising precision. Defeat it to gain access to the inner sanctum.", 30))
        bossExpeditions.append(BossExpedition(4, "The Drowned Prophet", "Sunken beneath a once-great city lies a priest possessed by ancient sea gods. His chants summon tidal waves and spectral leviathans. Silence him before the flood rises.", 35))
        bossExpeditions.append(BossExpedition(5, "The Iron Colossus", "A living war machine, awakened from the forgotten age, marches toward civilization. Scale its limbs, sabotage its systems, and battle it atop its metal heart.", 40))
        bossExpeditions.append(BossExpedition(6, "The Clockwork Butcher", "In the quiet town of Elderglen, people vanish at night. A deranged clockmaker turned mechanical horror stalks the foggy streets. Enter his twisted workshop and end the nightmare before the town is silenced forever.", 45))
        bossExpeditions.append(BossExpedition(7, "The Infernal Architect", "A demon that builds war machines in a fortress of fire and gears. Deactivate his defenses and destroy his creations before confronting him in a hellish showdown.", 50))
        bossExpeditions.append(BossExpedition(8, "The Eclipse Warden", "At the edge of the world, a being of shadow and solar flame guards the passage to the void. Fight through alternating light and dark phases in a battle of cosmic rhythm.", 60))
        bossExpeditions.append(BossExpedition(9, "The Shattered Queen", "In a realm of mirrors and illusions, an exiled queen of a fallen kingdom bends reality to her will. Break her illusions to reveal her true form — and end her madness.", 70))
        bossExpeditions.append(BossExpedition(10, "The Void-Touched Seraph", "Once a divine guardian, now corrupted by the void. This winged horror fights in aerial stages, using celestial and abyssal magic. Only a grounded will can reach the skies.", 90))
        
        # WEAPONS
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        
        # Axe
        weapons.append(Weapon("Rusty Hand Axe", 
            "An old, worn axe with chips along the blade. It can still cut, but barely.", 
            "Axe", 
            "Strength",
            "Melee",
            'E'))

        weapons.append(Weapon("Iron Viking Axe", 
            "A simple iron axe, sturdy enough for combat but still fairly common.", 
            "Axe", 
            "Strength",
            "Melee",
            'D'))

        weapons.append(Weapon("Warrior’s Axe", 
            "A sharpened axe favored by experienced raiders, able to split shields cleanly.", 
            "Axe", 
            "Strength",
            "Melee",
            'C'))

        weapons.append(Weapon("Berserker’s Axe", 
            "A brutal heavy axe designed for ferocious warriors, striking fear into foes.", 
            "Axe", 
            "Strength",
            "Melee",
            'B'))

        weapons.append(Weapon("Jarl’s Axe", 
            "An ornate, perfectly balanced weapon wielded by Viking leaders in battle.", 
            "Axe", 
            "Strength",
            "Melee",
            'A'))

        weapons.append(Weapon("Axe of Valhalla", 
            "A legendary axe said to be blessed by the gods themselves, glowing with power.", 
            "Axe", 
            "Strength",
            "Melee",
            'S'))

        weapons.append(Weapon("Worn Hatchet", 
            "A small, light hatchet. Easy to swing, but weak in power.", 
            "Axe", 
            "Dexterity",
            "Melee",
            'E'))

        weapons.append(Weapon("Raider’s Hatchet", 
            "A balanced axe carried by quick raiders, sharp enough for swift strikes.", 
            "Axe", 
            "Dexterity",
            "Melee",
            'D'))

        weapons.append(Weapon("Scout’s Axe", 
            "Lightweight and razor-edged, designed for hit-and-run tactics.", 
            "Axe", 
            "Dexterity",
            "Melee",
            'C'))

        weapons.append(Weapon("Hunter’s Axe", 
            "An axe honed for precision, favored by hunters who strike with deadly accuracy.", 
            "Axe", 
            "Dexterity",
            "Melee",
            'B'))

        weapons.append(Weapon("Raven’s Talon", 
            "A finely crafted axe with a curved blade, striking swiftly like a raven’s claw.", 
            "Axe", 
            "Dexterity",
            "Melee",
            'A'))

        weapons.append(Weapon("Shadowfang Axe", 
            "A mythical axe said to move faster than the eye can follow, leaving only a blur.", 
            "Axe", 
            "Dexterity",
            "Melee",
            'S'))

        weapons.append(Weapon("Cracked Rune Axe", 
            "An old axe with faint rune carvings. It hums softly with unstable magic.", 
            "Axe", 
            "Magic",
            "Melee",
            'E'))

        weapons.append(Weapon("Runed Hatchet", 
            "A small axe inscribed with basic runes, allowing it to cut with magical sharpness.", 
            "Axe", 
            "Magic",
            "Melee",
            'D'))

        weapons.append(Weapon("Shaman’s Axe", 
            "An axe used by mystics, glowing faintly as it channels elemental energy.", 
            "Axe", 
            "Magic",
            "Melee",
            'C'))

        weapons.append(Weapon("Stormcaller Axe", 
            "Crackling with lightning runes, this axe strikes with thunderous magical power.", 
            "Axe", 
            "Magic",
            "Melee",
            'B'))

        weapons.append(Weapon("Soulreaver Axe", 
            "An enchanted weapon that draws strength from its victim’s soul with every strike.", 
            "Axe", 
            "Magic",
            "Melee",
            'A'))

        weapons.append(Weapon("Axe of the Allfather", 
            "A divine weapon said to be blessed by Odin himself, radiating overwhelming magical might.", 
            "Axe", 
            "Magic",
            "Melee",
            'S'))

        weapons.append(Weapon("Blessed Hatchet", 
            "A simple hatchet engraved with holy symbols. It glimmers faintly with divine light.", 
            "Axe", 
            "Divine",
            "Melee",
            'E'))

        weapons.append(Weapon("Cleric’s Axe", 
            "An axe wielded by warrior-priests, consecrated to smite the unholy.", 
            "Axe", 
            "Divine",
            "Melee",
            'D'))

        weapons.append(Weapon("Sanctified Axe", 
            "Radiating a soft glow, this axe is blessed to pierce through darkness and corruption.", 
            "Axe", 
            "Divine",
            "Melee",
            'C'))

        weapons.append(Weapon("Crusader’s Axe", 
            "A mighty weapon carried by holy warriors, blazing with righteous fury.", 
            "Axe", 
            "Divine",
            "Melee",
            'B'))

        weapons.append(Weapon("Axe of Purity", 
            "Immaculately forged and bathed in sacred light, it cleanses evil with every strike.", 
            "Axe", 
            "Divine",
            "Melee",
            'A'))

        weapons.append(Weapon("Axe of the Valkyrie", 
            "A legendary axe said to be wielded by Odin’s chosen, carrying the judgment of the heavens.", 
            "Axe", 
            "Divine",
            "Melee",
            'S'))

        # BOOK
        weapons.append(Weapon("Tattered Spellbook", 
            "An old, fragile book with faded ink. Its magic is weak, but still functional.", 
            "Book", 
            "Magic",
            "Ranged",
            'E'))

        weapons.append(Weapon("Apprentice’s Grimoire", 
            "A basic spellbook used by novice mages, containing simple incantations.", 
            "Book", 
            "Magic",
            "Ranged",
            'D'))

        weapons.append(Weapon("Runebound Tome", 
            "A book inscribed with glowing runes that strengthen its magical power.", 
            "Book", 
            "Magic",
            "Ranged",
            'C'))

        weapons.append(Weapon("Sorcerer’s Codex", 
            "A powerful grimoire filled with dangerous spells, pulsating with arcane energy.", 
            "Book", 
            "Magic",
            "Ranged",
            'B'))

        weapons.append(Weapon("Archmage’s Grimoire", 
            "A tome of immense magical knowledge, its pages almost too heavy with power to turn.", 
            "Book", 
            "Magic",
            "Ranged",
            'A'))

        weapons.append(Weapon("Book of Eternity", 
            "A legendary spellbook said to contain the secrets of creation itself.", 
            "Book", 
            "Magic",
            "Ranged",
            'S'))

        weapons.append(Weapon("Worn Prayer Book", 
            "A small book of prayers carried by wandering priests. Its divine power is faint.", 
            "Book", 
            "Divine",
            "Ranged",
            'E'))

        weapons.append(Weapon("Cleric’s Scripture", 
            "A holy text used by clerics to channel the light of the divine.", 
            "Book", 
            "Divine",
            "Ranged",
            'D'))

        weapons.append(Weapon("Blessed Hymnal", 
            "A book of sacred hymns that radiates warmth and drives away shadows.", 
            "Book", 
            "Divine",
            "Ranged",
            'C'))

        weapons.append(Weapon("Saint’s Testament", 
            "A revered scripture that carries the blessing of saints, glowing with holy light.", 
            "Book", 
            "Divine",
            "Ranged",
            'B'))

        weapons.append(Weapon("Codex of Radiance", 
            "An ornate tome inscribed in golden ink, radiating divine judgment upon the wicked.", 
            "Book", 
            "Divine",
            "Ranged",
            'A'))

        weapons.append(Weapon("Tome of the Seraphim", 
            "A legendary book said to be written by angels themselves, brimming with heavenly power.", 
            "Book", 
            "Divine",
            "Ranged",
            'S'))

        # Cards
        weapons.append(Weapon("Wooden Playing Cards", 
            "Crude cards carved from wood. Heavier than paper, they still sting when thrown.", 
            "Cards", 
            "Strength",
            "Ranged",
            'E'))

        weapons.append(Weapon("Iron Throwing Cards", 
            "Metal cards forged from iron. Solid and capable of piercing light armor.", 
            "Cards", 
            "Strength",
            "Ranged",
            'D'))

        weapons.append(Weapon("Steel Gambler’s Deck", 
            "A deck of sharpened steel cards, deadly when thrown with brute force.", 
            "Cards", 
            "Strength",
            "Ranged",
            'C'))

        weapons.append(Weapon("Battle Deck", 
            "Thick, reinforced cards forged for war. Each card hits like a thrown axe head.", 
            "Cards", 
            "Strength",
            "Ranged",
            'B'))

        weapons.append(Weapon("Colossus Cards", 
            "Massive metal slabs shaped like cards, thrown with crushing strength to shatter shields.", 
            "Cards", 
            "Strength",
            "Ranged",
            'A'))

        weapons.append(Weapon("Titan’s Deck", 
            "A legendary deck of indestructible cards forged by giants, each strike carrying the force of a boulder.", 
            "Cards", 
            "Strength",
            "Ranged",
            'S'))

        weapons.append(Weapon("Paper Throwing Cards", 
            "Lightweight cards reinforced with thin edges. Weak, but quick to throw.", 
            "Cards", 
            "Dexterity",
            "Ranged",
            'E'))

        weapons.append(Weapon("Weighted Cards", 
            "Specially balanced cards that fly straighter and strike harder than normal ones.", 
            "Cards", 
            "Dexterity",
            "Ranged",
            'D'))

        weapons.append(Weapon("Razor Deck", 
            "A set of razor-edged cards designed for deadly precision throws.", 
            "Cards", 
            "Dexterity",
            "Ranged",
            'C'))

        weapons.append(Weapon("Assassin’s Deck", 
            "A silent killer’s weapon — cards so sharp and fast they can cut a throat before a sound is made.", 
            "Cards", 
            "Dexterity",
            "Ranged",
            'B'))

        weapons.append(Weapon("Phantom Deck", 
            "A masterwork deck of enchanted cards that vanish and reappear mid-flight, striking from unexpected angles.", 
            "Cards", 
            "Dexterity",
            "Ranged",
            'A'))

        weapons.append(Weapon("Deck of the Trickster", 
            "A legendary set of cards wielded by the fastest rogues, said to never miss their mark.", 
            "Cards", 
            "Dexterity",
            "Ranged",
            'S'))


        weapons.append(Weapon("Torn Playing Cards", 
            "A set of worn-out cards with faint magical residue. Weak, but unpredictable.", 
            "Cards", 
            "Magic",
            "Ranged",
            'E'))

        weapons.append(Weapon("Enchanted Deck", 
            "A deck infused with basic enchantments, allowing the user to throw cards like blades.", 
            "Cards", 
            "Magic",
            "Ranged",
            'D'))

        weapons.append(Weapon("Runic Tarot", 
            "A mystical tarot deck inscribed with runes, each card releasing a spark of arcane power.", 
            "Cards", 
            "Magic",
            "Ranged",
            'C'))

        weapons.append(Weapon("Fatebinder’s Deck", 
            "A deck wielded by seers, its cards bend probability and strike with magical precision.", 
            "Cards", 
            "Magic",
            "Ranged",
            'B'))

        weapons.append(Weapon("Deck of the Arcana", 
            "A masterwork deck representing the great arcana, each card unleashing potent spells.", 
            "Cards", 
            "Magic",
            "Ranged",
            'A'))

        weapons.append(Weapon("Deck of Infinity", 
            "A legendary deck said to contain every possible fate, its cards never run out and strike with godlike power.", 
            "Cards", 
            "Magic",
            "Ranged",
            'S'))
        
        weapons.append(Weapon("Blessed Playing Cards", 
            "A simple deck of cards inscribed with holy symbols, faintly glowing with divine light.", 
            "Cards", 
            "Divine",
            "Ranged",
            'E'))

        weapons.append(Weapon("Cleric’s Deck", 
            "A deck used by priest-warriors, each card carrying a minor blessing to smite foes.", 
            "Cards", 
            "Divine",
            "Ranged",
            'D'))

        weapons.append(Weapon("Hallowed Deck", 
            "A deck imbued with sacred energy, shining with a soft, purifying light when thrown.", 
            "Cards", 
            "Divine",
            "Ranged",
            'C'))

        weapons.append(Weapon("Saint’s Deck", 
            "A deck of holy cards that strike with precision, purging darkness and corruption.", 
            "Cards", 
            "Divine",
            "Ranged",
            'B'))

        weapons.append(Weapon("Deck of Radiance", 
            "An ornate set of cards that glows with heavenly energy, burning evil wherever they land.", 
            "Cards", 
            "Divine",
            "Ranged",
            'A'))

        weapons.append(Weapon("Deck of the Archangel", 
            "A legendary deck blessed by the heavens themselves, its cards strike with divine wrath.", 
            "Cards", 
            "Divine",
            "Ranged",
            'S'))

        # Great Hammer
        weapons.append(Weapon("Worn Warhammer", 
            "A simple, battered hammer. Heavy but effective against weak foes.", 
            "Great Hammer", 
            "Strength",
            "Melee",
            'E'))

        weapons.append(Weapon("Iron Great Hammer", 
            "A solid iron hammer, capable of crushing armor and breaking bones.", 
            "Great Hammer", 
            "Strength",
            "Melee",
            'D'))

        weapons.append(Weapon("Battle Great Hammer", 
            "A well-balanced hammer forged for warriors, delivering devastating blows.", 
            "Great Hammer", 
            "Strength",
            "Melee",
            'C'))

        weapons.append(Weapon("Mighty Warhammer", 
            "A massive hammer designed to crush shields and scatter enemies with each swing.", 
            "Great Hammer", 
            "Strength",
            "Melee",
            'B'))

        weapons.append(Weapon("Titan’s Hammer", 
            "A colossal weapon imbued with immense force, wielded only by the strongest warriors.", 
            "Great Hammer", 
            "Strength",
            "Melee",
            'A'))

        weapons.append(Weapon("Hammer of the Earthshaker", 
            "A legendary great hammer said to shake the very ground with every strike.", 
            "Great Hammer", 
            "Strength",
            "Melee",
            'S'))

        weapons.append(Weapon("Cracked Rune Hammer", 
            "A simple hammer etched with faint runes. Its magical power is unstable and weak.", 
            "Great Hammer", 
            "Magic",
            "Melee",
            'E'))

        weapons.append(Weapon("Runed Iron Hammer", 
            "A sturdy hammer inscribed with glowing runes, allowing it to release small bursts of magic.", 
            "Great Hammer", 
            "Magic",
            "Melee",
            'D'))

        weapons.append(Weapon("Elemental Hammer", 
            "A magical hammer that channels elemental energy, striking with fire, ice, or lightning.", 
            "Great Hammer", 
            "Magic",
            "Melee",
            'C'))

        weapons.append(Weapon("Sorcerer’s Warhammer", 
            "A finely crafted hammer that amplifies the wielder’s magical power with every swing.", 
            "Great Hammer", 
            "Magic",
            "Melee",
            'B'))

        weapons.append(Weapon("Arcane Colossus", 
            "A masterwork hammer pulsating with arcane energy, capable of unleashing devastating magical strikes.", 
            "Great Hammer", 
            "Magic",
            "Melee",
            'A'))

        weapons.append(Weapon("Hammer of the Archmage", 
            "A legendary great hammer imbued with ancient magic, said to channel the raw forces of creation.", 
            "Great Hammer", 
            "Magic",
            "Melee",
            'S'))

        weapons.append(Weapon("Blessed Warhammer", 
            "A simple hammer engraved with sacred symbols. It carries a faint divine aura.", 
            "Great Hammer", 
            "Divine",
            "Melee",
            'E'))

        weapons.append(Weapon("Cleric’s Hammer", 
            "A holy hammer used by priests and paladins, capable of smiting minor evil.", 
            "Great Hammer", 
            "Divine",
            "Melee",
            'D'))

        weapons.append(Weapon("Sanctified Great Hammer", 
            "A radiant hammer blessed with divine energy, striking foes with purifying light.", 
            "Great Hammer", 
            "Divine",
            "Melee",
            'C'))

        weapons.append(Weapon("Crusader’s Hammer", 
            "A mighty weapon wielded by holy warriors, each strike burning with righteous fury.", 
            "Great Hammer", 
            "Divine",
            "Melee",
            'B'))

        weapons.append(Weapon("Hammer of Purity", 
            "A masterfully forged hammer glowing with sacred light, cleansing evil wherever it lands.", 
            "Great Hammer", 
            "Divine",
            "Melee",
            'A'))

        weapons.append(Weapon("Hammer of the Seraphim", 
            "A legendary hammer said to be wielded by angels, raining divine judgment on the wicked.", 
            "Great Hammer", 
            "Divine",
            "Melee",
            'S'))

        # Greataxe
        weapons.append(Weapon("Rusty Battleaxe", 
            "A crude axe with a dull edge. Heavy and unwieldy, but it can still hit hard.", 
            "Greataxe", 
            "Strength",
            "Melee",
            'E'))

        weapons.append(Weapon("Iron Greataxe", 
            "A solid iron axe, capable of splitting shields and cleaving foes.", 
            "Greataxe", 
            "Strength",
            "Melee",
            'D'))

        weapons.append(Weapon("Warrior’s Greataxe", 
            "A balanced greataxe forged for battlefield veterans, delivering powerful strikes.", 
            "Greataxe", 
            "Strength",
            "Melee",
            'C'))

        weapons.append(Weapon("Berserker’s Greataxe", 
            "A massive axe designed for brutal combat, striking fear into enemies.", 
            "Greataxe", 
            "Strength",
            "Melee",
            'B'))

        weapons.append(Weapon("Titan Greataxe", 
            "A colossal axe wielded by the strongest warriors, capable of crushing anything in its path.", 
            "Greataxe", 
            "Strength",
            "Melee",
            'A'))

        weapons.append(Weapon("Axe of the Earthshaker", 
            "A legendary greataxe said to split mountains and strike the very earth.", 
            "Greataxe", 
            "Strength",
            "Melee",
            'S'))

        weapons.append(Weapon("Cracked Rune Axe", 
            "A small axe etched with faint runes, barely containing its magical power.", 
            "Greataxe", 
            "Magic",
            "Melee",
            'E'))

        weapons.append(Weapon("Runed Iron Axe", 
            "An iron greataxe inscribed with glowing runes, releasing minor magical bursts.", 
            "Greataxe", 
            "Magic",
            "Melee",
            'D'))

        weapons.append(Weapon("Elemental Greataxe", 
            "A magical axe channeling fire, ice, or lightning with each swing.", 
            "Greataxe", 
            "Magic",
            "Melee",
            'C'))

        weapons.append(Weapon("Sorcerer’s Greataxe", 
            "A finely crafted greataxe amplifying the wielder’s arcane power.", 
            "Greataxe", 
            "Magic",
            "Melee",
            'B'))

        weapons.append(Weapon("Arcane Colossus", 
            "A masterwork greataxe pulsing with arcane energy, capable of devastating magical strikes.", 
            "Greataxe", 
            "Magic",
            "Melee",
            'A'))

        weapons.append(Weapon("Greataxe of the Archmage", 
            "A legendary greataxe imbued with ancient magic, channeling the raw forces of creation.", 
            "Greataxe", 
            "Magic",
            "Melee",
            'S'))

        weapons.append(Weapon("Blessed Greataxe", 
            "A simple axe engraved with holy symbols, faintly glowing with divine energy.", 
            "Greataxe", 
            "Divine",
            "Melee",
            'E'))

        weapons.append(Weapon("Cleric’s Greataxe", 
            "A holy greataxe used by priests and paladins, smiting minor evil.", 
            "Greataxe", 
            "Divine",
            "Melee",
            'D'))

        weapons.append(Weapon("Sanctified Greataxe", 
            "A radiant axe blessed with divine energy, purifying darkness with every strike.", 
            "Greataxe", 
            "Divine",
            "Melee",
            'C'))

        weapons.append(Weapon("Crusader’s Greataxe", 
            "A mighty weapon wielded by holy warriors, burning with righteous fury.", 
            "Greataxe", 
            "Divine",
            "Melee",
            'B'))

        weapons.append(Weapon("Greataxe of Purity", 
            "A masterfully forged greataxe glowing with sacred light, cleansing evil wherever it lands.", 
            "Greataxe", 
            "Divine",
            "Melee",
            'A'))

        weapons.append(Weapon("Greataxe of the Seraphim", 
            "A legendary greataxe said to be wielded by angels, raining divine judgment on the wicked.", 
            "Greataxe", 
            "Divine",
            "Melee",
            'S'))

        # Greatsword
        weapons.append(Weapon("Rusty Greatsword", 
            "A worn, heavy greatsword. Hard to swing, but it can still deliver powerful blows.", 
            "Greatsword", 
            "Strength",
            "Melee",
            'E'))

        weapons.append(Weapon("Iron Greatsword", 
            "A solid iron greatsword, capable of cleaving armor and shields with brute force.", 
            "Greatsword", 
            "Strength",
            "Melee",
            'D'))

        weapons.append(Weapon("Warrior’s Greatsword", 
            "A balanced blade forged for veterans of the battlefield, delivering devastating strikes.", 
            "Greatsword", 
            "Strength",
            "Melee",
            'C'))

        weapons.append(Weapon("Berserker’s Greatsword", 
            "A massive sword designed for brutal combat, capable of smashing through multiple foes.", 
            "Greatsword", 
            "Strength",
            "Melee",
            'B'))

        weapons.append(Weapon("Titan Greatsword", 
            "A colossal blade wielded only by the strongest warriors, capable of splitting anything in its path.", 
            "Greatsword", 
            "Strength",
            "Melee",
            'A'))

        weapons.append(Weapon("Sword of the Earthshaker", 
            "A legendary greatsword said to shatter mountains and leave tremors with every swing.", 
            "Greatsword", 
            "Strength",
            "Melee",
            'S'))

        weapons.append(Weapon("Lightwood Greatsword", 
            "A lightweight sword made from strong but light wood. Easier to swing quickly.", 
            "Greatsword", 
            "Dexterity",
            "Melee",
            'E'))

        weapons.append(Weapon("Balanced Greatsword", 
            "A carefully balanced greatsword allowing faster and more precise swings.", 
            "Greatsword", 
            "Dexterity",
            "Melee",
            'D'))

        weapons.append(Weapon("Swiftstrike Greatsword", 
            "A finely crafted blade that allows rapid and accurate strikes.", 
            "Greatsword", 
            "Dexterity",
            "Melee",
            'C'))

        weapons.append(Weapon("Razor Greatsword", 
            "A nimble sword with sharpened edges, perfect for fast, precise attacks.", 
            "Greatsword", 
            "Dexterity",
            "Melee",
            'B'))

        weapons.append(Weapon("Phantom Greatsword", 
            "A masterwork blade that moves as fast as its wielder, striking like a shadow.", 
            "Greatsword", 
            "Dexterity",
            "Melee",
            'A'))

        weapons.append(Weapon("Greatsword of the Trickster", 
            "A legendary sword said to strike with impossible speed and precision.", 
            "Greatsword", 
            "Dexterity",
            "Melee",
            'S'))

        weapons.append(Weapon("Cracked Rune Greatsword", 
            "A simple greatsword etched with faint runes. Its magical power is weak and unstable.", 
            "Greatsword", 
            "Magic",
            "Melee",
            'E'))

        weapons.append(Weapon("Runed Greatsword", 
            "A sword inscribed with glowing runes, releasing minor magical bursts.", 
            "Greatsword", 
            "Magic",
            "Melee",
            'D'))

        weapons.append(Weapon("Elemental Greatsword", 
            "A magical blade channeling fire, ice, or lightning with each swing.", 
            "Greatsword", 
            "Magic",
            "Melee",
            'C'))

        weapons.append(Weapon("Sorcerer’s Greatsword", 
            "A finely crafted greatsword that amplifies the wielder’s arcane power.", 
            "Greatsword", 
            "Magic",
            "Melee",
            'B'))

        weapons.append(Weapon("Arcane Colossus", 
            "A masterwork blade pulsing with arcane energy, capable of devastating magical strikes.", 
            "Greatsword", 
            "Magic",
            "Melee",
            'A'))

        weapons.append(Weapon("Greatsword of the Archmage", 
            "A legendary greatsword imbued with ancient magic, channeling the raw forces of creation.", 
            "Greatsword", 
            "Magic",
            "Melee",
            'S'))

        weapons.append(Weapon("Blessed Greatsword", 
            "A simple sword engraved with holy symbols, faintly glowing with divine energy.", 
            "Greatsword", 
            "Divine",
            "Melee",
            'E'))

        weapons.append(Weapon("Cleric’s Greatsword", 
            "A holy blade used by priests and paladins, smiting minor evil.", 
            "Greatsword", 
            "Divine",
            "Melee",
            'D'))

        weapons.append(Weapon("Sanctified Greatsword", 
            "A radiant greatsword blessed with divine energy, purifying darkness with every strike.", 
            "Greatsword", 
            "Divine",
            "Melee",
            'C'))

        weapons.append(Weapon("Crusader’s Greatsword", 
            "A mighty weapon wielded by holy warriors, burning with righteous fury.", 
            "Greatsword", 
            "Divine",
            "Melee",
            'B'))

        weapons.append(Weapon("Greatsword of Purity", 
            "A masterfully forged greatsword glowing with sacred light, cleansing evil wherever it lands.", 
            "Greatsword", 
            "Divine",
            "Melee",
            'A'))

        weapons.append(Weapon("Greatsword of the Seraphim", 
            "A legendary greatsword said to be wielded by angels, raining divine judgment on the wicked.", 
            "Greatsword", 
            "Divine",
            "Melee",
            'S'))

        # Gun
        weapons.append(Weapon("Rusty Pistol", 
            "A small, worn pistol. Lightweight and quick, but unreliable.", 
            "Gun", 
            "Dexterity",
            "Ranged",
            'E'))

        weapons.append(Weapon("Balanced Revolver", 
            "A well-crafted revolver, allowing precise shots at medium range.", 
            "Gun", 
            "Dexterity",
            "Ranged",
            'D'))

        weapons.append(Weapon("Sharpshooter’s Pistol", 
            "A finely tuned firearm designed for deadly accuracy and fast reloads.", 
            "Gun", 
            "Dexterity",
            "Ranged",
            'C'))

        weapons.append(Weapon("Twin-Barrel Pistol", 
            "A dual-shot pistol that allows rapid, skillful firing on multiple targets.", 
            "Gun", 
            "Dexterity",
            "Ranged",
            'B'))

        weapons.append(Weapon("Marksman’s Revolver", 
            "A masterwork revolver with unmatched precision, favored by elite sharpshooters.", 
            "Gun", 
            "Dexterity",
            "Ranged",
            'A'))

        weapons.append(Weapon("Phantom Shooter", 
            "A legendary firearm said to never miss its target, moving as fast as the wielder’s hand.", 
            "Gun", 
            "Dexterity",
            "Ranged",
            'S'))

        weapons.append(Weapon("Cracked Rune Pistol", 
            "A basic pistol etched with faint runes. Its magical power is weak and unstable.", 
            "Gun", 
            "Magic",
            "Ranged",
            'E'))

        weapons.append(Weapon("Runed Handgun", 
            "A small firearm inscribed with glowing runes, firing minor magical projectiles.", 
            "Gun", 
            "Magic",
            "Ranged",
            'D'))

        weapons.append(Weapon("Elemental Pistol", 
            "A magical handgun capable of shooting fire, ice, or lightning bullets.", 
            "Gun", 
            "Magic",
            "Ranged",
            'C'))

        weapons.append(Weapon("Sorcerer’s Firearm", 
            "A finely crafted gun that channels the wielder’s arcane energy into powerful shots.", 
            "Gun", 
            "Magic",
            "Ranged",
            'B'))

        weapons.append(Weapon("Arcane Revolver", 
            "A masterwork magical gun, firing devastating projectiles infused with raw magic.", 
            "Gun", 
            "Magic",
            "Ranged",
            'A'))

        weapons.append(Weapon("Gun of the Archmage", 
            "A legendary firearm imbued with ancient magic, said to fire bullets of pure arcane force.", 
            "Gun", 
            "Magic",
            "Ranged",
            'S'))

        weapons.append(Weapon("Blessed Pistol", 
            "A small pistol engraved with holy symbols. Its divine aura is faint but potent.", 
            "Gun", 
            "Divine",
            "Ranged",
            'E'))

        weapons.append(Weapon("Cleric’s Revolver", 
            "A holy firearm used by priest-warriors, smiting minor evil with each shot.", 
            "Gun", 
            "Divine",
            "Ranged",
            'D'))

        weapons.append(Weapon("Sanctified Handgun", 
            "A radiant pistol blessed with divine energy, purging darkness with every bullet.", 
            "Gun", 
            "Divine",
            "Ranged",
            'C'))

        weapons.append(Weapon("Crusader’s Pistol", 
            "A powerful firearm wielded by holy warriors, firing bullets burning with righteous fury.", 
            "Gun", 
            "Divine",
            "Ranged",
            'B'))

        weapons.append(Weapon("Pistol of Purity", 
            "A masterfully forged firearm glowing with sacred light, cleansing evil wherever it lands.", 
            "Gun", 
            "Divine",
            "Ranged",
            'A'))

        weapons.append(Weapon("Gun of the Seraphim", 
            "A legendary divine gun said to be wielded by angels, striking with holy judgment.", 
            "Gun", 
            "Divine",
            "Ranged",
            'S'))

        # Hammer
        weapons.append(Weapon("Worn Warhammer", 
            "A simple, battered hammer. Heavy but effective against weak foes.", 
            "Hammer", 
            "Strength",
            "Melee",
            'E'))

        weapons.append(Weapon("Iron Warhammer", 
            "A solid iron hammer, capable of crushing armor and breaking bones.", 
            "Hammer", 
            "Strength",
            "Melee",
            'D'))

        weapons.append(Weapon("Battle Hammer", 
            "A well-balanced hammer forged for warriors, delivering devastating blows.", 
            "Hammer", 
            "Strength",
            "Melee",
            'C'))

        weapons.append(Weapon("Mighty Warhammer", 
            "A massive hammer designed to crush shields and scatter enemies with each swing.", 
            "Hammer", 
            "Strength",
            "Melee",
            'B'))

        weapons.append(Weapon("Titan’s Hammer", 
            "A colossal weapon imbued with immense force, wielded only by the strongest warriors.", 
            "Hammer", 
            "Strength",
            "Melee",
            'A'))

        weapons.append(Weapon("Hammer of the Earthshaker", 
            "A legendary hammer said to shake the very ground with every strike.", 
            "Hammer", 
            "Strength",
            "Melee",
            'S'))

        weapons.append(Weapon("Cracked Rune Hammer", 
            "A simple hammer etched with faint runes. Its magic is weak and unstable.", 
            "Hammer", 
            "Magic",
            "Melee",
            'E'))

        weapons.append(Weapon("Runed Iron Hammer", 
            "A sturdy hammer inscribed with glowing runes, releasing minor magical bursts.", 
            "Hammer", 
            "Magic",
            "Melee",
            'D'))

        weapons.append(Weapon("Elemental Hammer", 
            "A magical hammer that channels elemental energy, striking with fire, ice, or lightning.", 
            "Hammer", 
            "Magic",
            "Melee",
            'C'))

        weapons.append(Weapon("Sorcerer’s Hammer", 
            "A finely crafted hammer that amplifies the wielder’s magical power with every swing.", 
            "Hammer", 
            "Magic",
            "Melee",
            'B'))

        weapons.append(Weapon("Arcane Colossus", 
            "A masterwork hammer pulsating with arcane energy, capable of unleashing devastating magical strikes.", 
            "Hammer", 
            "Magic",
            "Melee",
            'A'))

        weapons.append(Weapon("Hammer of the Archmage", 
            "A legendary hammer imbued with ancient magic, said to channel the raw forces of creation.", 
            "Hammer", 
            "Magic",
            "Melee",
            'S'))

        weapons.append(Weapon("Blessed Hammer", 
            "A simple hammer engraved with sacred symbols. It carries a faint divine aura.", 
            "Hammer", 
            "Divine",
            "Melee",
            'E'))

        weapons.append(Weapon("Cleric’s Hammer", 
            "A holy hammer used by priests and paladins, capable of smiting minor evil.", 
            "Hammer", 
            "Divine",
            "Melee",
            'D'))

        weapons.append(Weapon("Sanctified Hammer", 
            "A radiant hammer blessed with divine energy, purifying darkness with every strike.", 
            "Hammer", 
            "Divine",
            "Melee",
            'C'))

        weapons.append(Weapon("Crusader’s Hammer", 
            "A mighty weapon wielded by holy warriors, each strike burning with righteous fury.", 
            "Hammer", 
            "Divine",
            "Melee",
            'B'))

        weapons.append(Weapon("Hammer of Purity", 
            "A masterfully forged hammer glowing with sacred light, cleansing evil wherever it lands.", 
            "Hammer", 
            "Divine",
            "Melee",
            'A'))

        weapons.append(Weapon("Hammer of the Seraphim", 
            "A legendary hammer said to be wielded by angels, raining divine judgment on the wicked.", 
            "Hammer", 
            "Divine",
            "Melee",
            'S'))

        # Katana
        weapons.append(Weapon("Rusty Katana", 
            "A worn katana, heavy and unwieldy. Requires brute strength to wield effectively.", 
            "Katana", 
            "Strength",
            "Melee",
            'E'))

        weapons.append(Weapon("Iron Katana", 
            "A solid iron blade, capable of cleaving through armor and shields.", 
            "Katana", 
            "Strength",
            "Melee",
            'D'))

        weapons.append(Weapon("Warrior’s Katana", 
            "A balanced katana forged for battlefield veterans, delivering powerful strikes.", 
            "Katana", 
            "Strength",
            "Melee",
            'C'))

        weapons.append(Weapon("Berserker’s Katana", 
            "A massive katana designed to deal devastating blows to multiple foes.", 
            "Katana", 
            "Strength",
            "Melee",
            'B'))

        weapons.append(Weapon("Titan Katana", 
            "A colossal blade wielded only by the strongest warriors, capable of slicing anything in its path.", 
            "Katana", 
            "Strength",
            "Melee",
            'A'))

        weapons.append(Weapon("Katana of the Earthshaker", 
            "A legendary katana said to split mountains and leave tremors with every strike.", 
            "Katana", 
            "Strength",
            "Melee",
            'S'))

        weapons.append(Weapon("Lightwood Katana", 
            "A lightweight katana, easy to swing quickly but less damaging.", 
            "Katana", 
            "Dexterity",
            "Melee",
            'E'))

        weapons.append(Weapon("Balanced Katana", 
            "A well-balanced blade allowing for precise, swift attacks.", 
            "Katana", 
            "Dexterity",
            "Melee",
            'D'))

        weapons.append(Weapon("Swiftstrike Katana", 
            "A finely crafted katana designed for rapid and accurate strikes.", 
            "Katana", 
            "Dexterity",
            "Melee",
            'C'))

        weapons.append(Weapon("Razor Katana", 
            "A nimble katana with sharpened edges, perfect for cutting with precision.", 
            "Katana", 
            "Dexterity",
            "Melee",
            'B'))

        weapons.append(Weapon("Phantom Katana", 
            "A masterwork blade that moves as fast as its wielder, striking like a shadow.", 
            "Katana", 
            "Dexterity",
            "Melee",
            'A'))

        weapons.append(Weapon("Katana of the Trickster", 
            "A legendary katana said to strike with impossible speed and accuracy.", 
            "Katana", 
            "Dexterity",
            "Melee",
            'S'))

        weapons.append(Weapon("Cracked Rune Katana", 
            "A simple katana etched with faint runes. Its magic is weak and unstable.", 
            "Katana", 
            "Magic",
            "Melee",
            'E'))

        weapons.append(Weapon("Runed Katana", 
            "A blade inscribed with glowing runes, releasing minor magical bursts.", 
            "Katana", 
            "Magic",
            "Melee",
            'D'))

        weapons.append(Weapon("Elemental Katana", 
            "A magical katana channeling fire, ice, or lightning with each swing.", 
            "Katana", 
            "Magic",
            "Melee",
            'C'))

        weapons.append(Weapon("Sorcerer’s Katana", 
            "A finely crafted katana that amplifies the wielder’s arcane power.", 
            "Katana", 
            "Magic",
            "Melee",
            'B'))

        weapons.append(Weapon("Arcane Blade", 
            "A masterwork magical katana capable of unleashing devastating arcane strikes.", 
            "Katana", 
            "Magic",
            "Melee",
            'A'))

        weapons.append(Weapon("Katana of the Archmage", 
            "A legendary katana imbued with ancient magic, channeling the raw forces of creation.", 
            "Katana", 
            "Magic",
            "Melee",
            'S'))

        weapons.append(Weapon("Blessed Katana", 
            "A simple katana engraved with holy symbols, faintly glowing with divine energy.", 
            "Katana", 
            "Divine",
            "Melee",
            'E'))

        weapons.append(Weapon("Cleric’s Katana", 
            "A holy katana used by priests and paladins, smiting minor evil.", 
            "Katana", 
            "Divine",
            "Melee",
            'D'))

        weapons.append(Weapon("Sanctified Katana", 
            "A radiant katana blessed with divine energy, purifying darkness with every strike.", 
            "Katana", 
            "Divine",
            "Melee",
            'C'))

        weapons.append(Weapon("Crusader’s Katana", 
            "A mighty weapon wielded by holy warriors, burning with righteous fury.", 
            "Katana", 
            "Divine",
            "Melee",
            'B'))

        weapons.append(Weapon("Katana of Purity", 
            "A masterfully forged katana glowing with sacred light, cleansing evil wherever it lands.", 
            "Katana", 
            "Divine",
            "Melee",
            'A'))

        weapons.append(Weapon("Katana of the Seraphim", 
            "A legendary katana said to be wielded by angels, raining divine judgment on the wicked.", 
            "Katana", 
            "Divine",
            "Melee",
            'S'))

        # Knife
        weapons.append(Weapon("Rusty Combat Knife", 
            "A simple, worn knife. Heavy and crude, but still capable of cutting through flesh.", 
            "Knife", 
            "Strength",
            "Melee",
            'E'))

        weapons.append(Weapon("Iron Knife", 
            "A solid knife forged from iron, capable of piercing armor with brute force.", 
            "Knife", 
            "Strength",
            "Melee",
            'D'))

        weapons.append(Weapon("Warrior’s Knife", 
            "A balanced blade forged for combat veterans, dealing devastating close-range damage.", 
            "Knife", 
            "Strength",
            "Melee",
            'C'))

        weapons.append(Weapon("Berserker’s Knife", 
            "A large, brutal knife designed for heavy strikes and chopping attacks.", 
            "Knife", 
            "Strength",
            "Melee",
            'B'))

        weapons.append(Weapon("Titan Knife", 
            "A massive knife wielded only by the strongest fighters, capable of cleaving through shields.", 
            "Knife", 
            "Strength",
            "Melee",
            'A'))

        weapons.append(Weapon("Knife of the Earthshaker", 
            "A legendary knife said to split stone and leave shockwaves with every strike.", 
            "Knife", 
            "Strength",
            "Melee",
            'S'))

        weapons.append(Weapon("Rusty Throwing Knife", 
            "A small, worn knife. Lightweight and easy to throw, but weak.", 
            "Knife", 
            "Dexterity",
            "Melee",
            'E'))

        weapons.append(Weapon("Balanced Throwing Knife", 
            "A well-balanced knife for precise throws and quick slashes.", 
            "Knife", 
            "Dexterity",
            "Melee",
            'D'))

        weapons.append(Weapon("Assassin’s Knife", 
            "A sharp, agile blade designed for fast, accurate strikes.", 
            "Knife", 
            "Dexterity",
            "Melee",
            'C'))

        weapons.append(Weapon("Razor Knife", 
            "A finely honed knife capable of slicing cleanly with minimal effort.", 
            "Knife", 
            "Dexterity",
            "Melee",
            'B'))

        weapons.append(Weapon("Phantom Knife", 
            "A masterwork blade that moves as fast as its wielder, hitting before the enemy can react.", 
            "Knife", 
            "Dexterity",
            "Melee",
            'A'))

        weapons.append(Weapon("Knife of the Trickster", 
            "A legendary knife said to strike with impossible speed and precision.", 
            "Knife", 
            "Dexterity",
            "Melee",
            'S'))

        weapons.append(Weapon("Cracked Rune Knife", 
            "A simple knife etched with faint runes. Its magic is weak and unstable.", 
            "Knife", 
            "Magic",
            "Melee",
            'E'))

        weapons.append(Weapon("Runed Knife", 
            "A knife inscribed with glowing runes, capable of releasing minor magical bursts.", 
            "Knife", 
            "Magic",
            "Melee",
            'D'))

        weapons.append(Weapon("Elemental Knife", 
            "A magical knife that channels fire, ice, or lightning with every strike.", 
            "Knife", 
            "Magic",
            "Melee",
            'C'))

        weapons.append(Weapon("Sorcerer’s Knife", 
            "A finely crafted blade that amplifies the wielder’s arcane power.", 
            "Knife", 
            "Magic",
            "Melee",
            'B'))

        weapons.append(Weapon("Arcane Blade", 
            "A masterwork magical knife capable of devastating arcane strikes.", 
            "Knife", 
            "Magic",
            "Melee",
            'A'))

        weapons.append(Weapon("Knife of the Archmage", 
            "A legendary knife imbued with ancient magic, channeling the raw forces of creation.", 
            "Knife", 
            "Magic",
            "Melee",
            'S'))
        
        weapons.append(Weapon("Blessed Knife", 
            "A small knife engraved with holy symbols, faintly glowing with divine energy.", 
            "Knife", 
            "Divine",
            "Melee",
            'E'))

        weapons.append(Weapon("Cleric’s Knife", 
            "A holy knife used by priests and paladins, smiting minor evil.", 
            "Knife", 
            "Divine",
            "Melee",
            'D'))

        weapons.append(Weapon("Sanctified Knife", 
            "A radiant knife blessed with divine energy, purifying darkness with every strike.", 
            "Knife", 
            "Divine",
            "Melee",
            'C'))

        weapons.append(Weapon("Crusader’s Knife", 
            "A powerful weapon wielded by holy warriors, burning with righteous fury.", 
            "Knife", 
            "Divine",
            "Melee",
            'B'))

        weapons.append(Weapon("Knife of Purity", 
            "A masterfully forged knife glowing with sacred light, cleansing evil wherever it lands.", 
            "Knife", 
            "Divine",
            "Melee",
            'A'))

        weapons.append(Weapon("Knife of the Seraphim", 
            "A legendary knife said to be wielded by angels, raining divine judgment on the wicked.", 
            "Knife", 
            "Divine",
            "Melee",
            'S'))

        # Mace
        weapons.append(Weapon("Rusty Mace", 
            "A simple, worn mace. Heavy and crude, but still capable of dealing painful blows.", 
            "Mace", 
            "Strength",
            "Melee",
            'E'))

        weapons.append(Weapon("Iron Mace", 
            "A solid iron mace, capable of smashing shields and breaking bones.", 
            "Mace", 
            "Strength",
            "Melee",
            'D'))

        weapons.append(Weapon("Warrior’s Mace", 
            "A balanced mace forged for experienced fighters, delivering devastating strikes.", 
            "Mace", 
            "Strength",
            "Melee",
            'C'))

        weapons.append(Weapon("Mighty Mace", 
            "A heavy mace designed to crush enemies and scatter opponents.", 
            "Mace", 
            "Strength",
            "Melee",
            'B'))

        weapons.append(Weapon("Titan’s Mace", 
            "A colossal mace wielded only by the strongest warriors, capable of smashing through anything.", 
            "Mace", 
            "Strength",
            "Melee",
            'A'))

        weapons.append(Weapon("Mace of the Earthshaker", 
            "A legendary mace said to shake the ground with every strike, splitting earth and bone alike.", 
            "Mace", 
            "Strength",
            "Melee",
            'S'))

        weapons.append(Weapon("Cracked Rune Mace", 
            "A simple mace etched with faint runes. Its magic is weak and unstable.", 
            "Mace", 
            "Magic",
            "Melee",
            'E'))

        weapons.append(Weapon("Runed Mace", 
            "A sturdy mace inscribed with glowing runes, capable of minor magical strikes.", 
            "Mace", 
            "Magic",
            "Melee",
            'D'))

        weapons.append(Weapon("Elemental Mace", 
            "A magical mace that channels fire, ice, or lightning with each swing.", 
            "Mace", 
            "Magic",
            "Melee",
            'C'))

        weapons.append(Weapon("Sorcerer’s Mace", 
            "A finely crafted mace that amplifies the wielder’s magical power.", 
            "Mace", 
            "Magic",
            "Melee",
            'B'))

        weapons.append(Weapon("Arcane Colossus", 
            "A masterwork magical mace capable of unleashing devastating arcane strikes.", 
            "Mace", 
            "Magic",
            "Melee",
            'A'))

        weapons.append(Weapon("Mace of the Archmage", 
            "A legendary mace imbued with ancient magic, channeling the raw forces of creation.", 
            "Mace", 
            "Magic",
            "Melee",
            'S'))

        weapons.append(Weapon("Blessed Mace", 
            "A simple mace engraved with sacred symbols, faintly glowing with divine energy.", 
            "Mace", 
            "Divine",
            "Melee",
            'E'))

        weapons.append(Weapon("Cleric’s Mace", 
            "A holy mace used by priests and paladins, smiting minor evil.", 
            "Mace", 
            "Divine",
            "Melee",
            'D'))

        weapons.append(Weapon("Sanctified Mace", 
            "A radiant mace blessed with divine energy, purifying darkness with every strike.", 
            "Mace", 
            "Divine",
            "Melee",
            'C'))

        weapons.append(Weapon("Crusader’s Mace", 
            "A mighty weapon wielded by holy warriors, burning with righteous fury.", 
            "Mace", 
            "Divine",
            "Melee",
            'B'))

        weapons.append(Weapon("Mace of Purity", 
            "A masterfully forged mace glowing with sacred light, cleansing evil wherever it lands.", 
            "Mace", 
            "Divine",
            "Melee",
            'A'))

        weapons.append(Weapon("Mace of the Seraphim", 
            "A legendary mace said to be wielded by angels, raining divine judgment on the wicked.", 
            "Mace", 
            "Divine",
            "Melee",
            'S'))

        # Machine Gun
        weapons.append(Weapon("Rusty Submachine Gun", 
            "A worn, lightweight machine gun. Easy to handle but its firepower is weak.", 
            "Machine Gun", 
            "Dexterity",
            "Ranged",
            'E'))

        weapons.append(Weapon("Balanced SMG", 
            "A well-crafted submachine gun that allows rapid, accurate bursts.", 
            "Machine Gun", 
            "Dexterity",
            "Ranged",
            'D'))

        weapons.append(Weapon("Sharpshooter’s SMG", 
            "A finely tuned machine gun for precision fire at high speed.", 
            "Machine Gun", 
            "Dexterity",
            "Ranged",
            'C'))

        weapons.append(Weapon("Twin-Barrel SMG", 
            "A nimble dual-barrel machine gun, firing rapid bursts with expert control.", 
            "Machine Gun", 
            "Dexterity",
            "Ranged",
            'B'))

        weapons.append(Weapon("Marksman’s SMG", 
            "A masterwork firearm capable of delivering deadly precision at high rate of fire.", 
            "Machine Gun", 
            "Dexterity",
            "Ranged",
            'A'))

        weapons.append(Weapon("Phantom SMG", 
            "A legendary machine gun said to fire faster than the eye can track, never missing its target.", 
            "Machine Gun", 
            "Dexterity",
            "Ranged",
            'S'))

        weapons.append(Weapon("Cracked Rune SMG", 
            "A basic machine gun etched with faint runes. Its magic is unstable and weak.", 
            "Machine Gun", 
            "Magic",
            "Ranged",
            'E'))

        weapons.append(Weapon("Runed SMG", 
            "A small machine gun inscribed with glowing runes, firing minor magical projectiles.", 
            "Machine Gun", 
            "Magic",
            "Ranged",
            'D'))

        weapons.append(Weapon("Elemental SMG", 
            "A magical machine gun capable of firing bursts of fire, ice, or lightning.", 
            "Machine Gun", 
            "Magic",
            "Ranged",
            'C'))

        weapons.append(Weapon("Sorcerer’s SMG", 
            "A finely crafted arcane firearm, amplifying the wielder’s magical power.", 
            "Machine Gun", 
            "Magic",
            "Ranged",
            'B'))

        weapons.append(Weapon("Arcane SMG", 
            "A masterwork magical machine gun capable of devastating bursts of raw arcane energy.", 
            "Machine Gun", 
            "Magic",
            "Ranged",
            'A'))

        weapons.append(Weapon("SMG of the Archmage", 
            "A legendary magical machine gun said to fire bullets imbued with pure arcane force.", 
            "Machine Gun", 
            "Magic",
            "Ranged",
            'S'))

        weapons.append(Weapon("Blessed SMG", 
            "A small machine gun engraved with holy symbols, faintly glowing with divine energy.", 
            "Machine Gun", 
            "Divine",
            "Ranged",
            'E'))

        weapons.append(Weapon("Cleric’s SMG", 
            "A holy firearm used by priest-warriors, smiting minor evil with every burst.", 
            "Machine Gun", 
            "Divine",
            "Ranged",
            'D'))

        weapons.append(Weapon("Sanctified SMG", 
            "A radiant machine gun firing bullets blessed to purify darkness.", 
            "Machine Gun", 
            "Divine",
            "Ranged",
            'C'))

        weapons.append(Weapon("Crusader’s SMG", 
            "A powerful divine firearm, raining holy judgment with every rapid burst.", 
            "Machine Gun", 
            "Divine",
            "Ranged",
            'B'))

        weapons.append(Weapon("SMG of Purity", 
            "A masterfully forged firearm glowing with sacred light, cleansing evil wherever it lands.", 
            "Machine Gun", 
            "Divine",
            "Ranged",
            'A'))

        weapons.append(Weapon("SMG of the Seraphim", 
            "A legendary divine machine gun said to be wielded by angels, firing bursts of holy wrath.", 
            "Machine Gun", 
            "Divine",
            "Ranged",
            'S'))

        # Sniper
        weapons.append(Weapon("Rusty Sniper Rifle", 
            "A worn, lightweight sniper rifle. Accurate but has low damage.", 
            "Sniper", 
            "Dexterity",
            "Ranged",
            'E'))

        weapons.append(Weapon("Balanced Sniper", 
            "A well-crafted sniper rifle allowing precise long-range shots.", 
            "Sniper", 
            "Dexterity",
            "Ranged",
            'D'))

        weapons.append(Weapon("Sharpshooter’s Sniper", 
            "A finely tuned sniper rifle designed for deadly accuracy and critical hits.", 
            "Sniper", 
            "Dexterity",
            "Ranged",
            'C'))

        weapons.append(Weapon("Twin-Barrel Sniper", 
            "A dual-shot sniper rifle capable of rapid, precise follow-up shots.", 
            "Sniper", 
            "Dexterity",
            "Ranged",
            'B'))

        weapons.append(Weapon("Marksman’s Sniper", 
            "A masterwork sniper rifle that delivers high-damage, pinpoint shots at extreme range.", 
            "Sniper", 
            "Dexterity",
            "Ranged",
            'A'))

        weapons.append(Weapon("Phantom Sniper", 
            "A legendary sniper rifle said to hit targets instantly, no matter the distance.", 
            "Sniper", 
            "Dexterity",
            "Ranged",
            'S'))

        weapons.append(Weapon("Cracked Rune Sniper", 
            "A basic sniper rifle etched with faint runes. Its magic is weak and unstable.", 
            "Sniper", 
            "Magic",
            "Ranged",
            'E'))

        weapons.append(Weapon("Runed Sniper", 
            "A sniper rifle inscribed with glowing runes, firing minor magical projectiles.", 
            "Sniper", 
            "Magic",
            "Ranged",
            'D'))

        weapons.append(Weapon("Elemental Sniper", 
            "A magical sniper rifle that fires bullets of fire, ice, or lightning.", 
            "Sniper", 
            "Magic",
            "Ranged",
            'C'))

        weapons.append(Weapon("Sorcerer’s Sniper", 
            "A finely crafted arcane sniper, amplifying the wielder’s magical power.", 
            "Sniper", 
            "Magic",
            "Ranged",
            'B'))

        weapons.append(Weapon("Arcane Sniper", 
            "A masterwork magical sniper rifle capable of devastating arcane shots.", 
            "Sniper", 
            "Magic",
            "Ranged",
            'A'))

        weapons.append(Weapon("Sniper of the Archmage", 
            "A legendary magical sniper rifle said to fire bullets imbued with pure arcane energy.", 
            "Sniper", 
            "Magic",
            "Ranged",
            'S'))

        weapons.append(Weapon("Blessed Sniper", 
            "A sniper rifle engraved with holy symbols, faintly glowing with divine energy.", 
            "Sniper", 
            "Divine",
            "Ranged",
            'E'))

        weapons.append(Weapon("Cleric’s Sniper", 
            "A holy sniper rifle used by priest-warriors, smiting minor evil with each shot.", 
            "Sniper", 
            "Divine",
            "Ranged",
            'D'))

        weapons.append(Weapon("Sanctified Sniper", 
            "A radiant sniper rifle firing bullets blessed to purify darkness.", 
            "Sniper", 
            "Divine",
            "Ranged",
            'C'))

        weapons.append(Weapon("Crusader’s Sniper", 
            "A powerful divine firearm, delivering holy judgment with every precise shot.", 
            "Sniper", 
            "Divine",
            "Ranged",
            'B'))

        weapons.append(Weapon("Sniper of Purity", 
            "A masterfully forged sniper rifle glowing with sacred light, cleansing evil wherever it lands.", 
            "Sniper", 
            "Divine",
            "Ranged",
            'A'))

        weapons.append(Weapon("Sniper of the Seraphim", 
            "A legendary divine sniper rifle said to be wielded by angels, striking with holy wrath.", 
            "Sniper", 
            "Divine",
            "Ranged",
            'S'))

        # Spear
        weapons.append(Weapon("Rusty Spear", 
            "A worn, heavy spear. Difficult to wield but can pierce through foes.", 
            "Spear", 
            "Strength",
            "Melee",
            'E'))

        weapons.append(Weapon("Iron Spear", 
            "A solid iron spear, capable of puncturing armor and shields.", 
            "Spear", 
            "Strength",
            "Melee",
            'D'))

        weapons.append(Weapon("Warrior’s Spear", 
            "A balanced spear forged for combat veterans, delivering strong thrusts.", 
            "Spear", 
            "Strength",
            "Melee",
            'C'))

        weapons.append(Weapon("Berserker’s Spear", 
            "A massive spear designed to pierce multiple enemies in a single strike.", 
            "Spear", 
            "Strength",
            "Melee",
            'B'))

        weapons.append(Weapon("Titan Spear", 
            "A colossal spear wielded by the strongest warriors, capable of cleaving anything in its path.", 
            "Spear", 
            "Strength",
            "Melee",
            'A'))

        weapons.append(Weapon("Spear of the Earthshaker", 
            "A legendary spear said to split the ground and crush enemies with every thrust.", 
            "Spear", 
            "Strength",
            "Melee",
            'S'))

        weapons.append(Weapon("Lightwood Spear", 
            "A lightweight spear, easy to handle quickly but less damaging.", 
            "Spear", 
            "Dexterity",
            "Melee",
            'E'))

        weapons.append(Weapon("Balanced Spear", 
            "A well-balanced spear allowing for precise and rapid thrusts.", 
            "Spear", 
            "Dexterity",
            "Melee",
            'D'))

        weapons.append(Weapon("Swiftstrike Spear", 
            "A finely crafted spear designed for fast, accurate attacks.", 
            "Spear", 
            "Dexterity",
            "Melee",
            'C'))

        weapons.append(Weapon("Razor Spear", 
            "A nimble spear with sharpened edges, perfect for slicing and piercing quickly.", 
            "Spear", 
            "Dexterity",
            "Melee",
            'B'))

        weapons.append(Weapon("Phantom Spear", 
            "A masterwork spear that moves as fast as its wielder, striking before enemies can react.", 
            "Spear", 
            "Dexterity",
            "Melee",
            'A'))

        weapons.append(Weapon("Spear of the Trickster", 
            "A legendary spear said to strike with impossible speed and precision.", 
            "Spear", 
            "Dexterity",
            "Melee",
            'S'))

        weapons.append(Weapon("Cracked Rune Spear", 
            "A simple spear etched with faint runes. Its magic is weak and unstable.", 
            "Spear", 
            "Magic",
            "Melee",
            'E'))

        weapons.append(Weapon("Runed Spear", 
            "A spear inscribed with glowing runes, releasing minor magical bursts.", 
            "Spear", 
            "Magic",
            "Melee",
            'D'))

        weapons.append(Weapon("Elemental Spear", 
            "A magical spear channeling fire, ice, or lightning with every thrust.", 
            "Spear", 
            "Magic",
            "Melee",
            'C'))

        weapons.append(Weapon("Sorcerer’s Spear", 
            "A finely crafted spear that amplifies the wielder’s arcane power.", 
            "Spear", 
            "Magic",
            "Melee",
            'B'))

        weapons.append(Weapon("Arcane Spear", 
            "A masterwork magical spear capable of devastating elemental strikes.", 
            "Spear", 
            "Magic",
            "Melee",
            'A'))

        weapons.append(Weapon("Spear of the Archmage", 
            "A legendary spear imbued with ancient magic, channeling the raw forces of creation.", 
            "Spear", 
            "Magic",
            "Melee",
            'S'))

        weapons.append(Weapon("Blessed Spear", 
            "A simple spear engraved with holy symbols, faintly glowing with divine energy.", 
            "Spear", 
            "Divine",
            "Melee",
            'E'))

        weapons.append(Weapon("Cleric’s Spear", 
            "A holy spear used by priests and paladins, smiting minor evil.", 
            "Spear", 
            "Divine",
            "Melee",
            'D'))

        weapons.append(Weapon("Sanctified Spear", 
            "A radiant spear blessed with divine energy, purifying darkness with every strike.", 
            "Spear", 
            "Divine",
            "Melee",
            'C'))

        weapons.append(Weapon("Crusader’s Spear", 
            "A mighty weapon wielded by holy warriors, burning with righteous fury.", 
            "Spear", 
            "Divine",
            "Melee",
            'B'))

        weapons.append(Weapon("Spear of Purity", 
            "A masterfully forged spear glowing with sacred light, cleansing evil wherever it lands.", 
            "Spear", 
            "Divine",
            "Melee",
            'A'))

        weapons.append(Weapon("Spear of the Seraphim", 
            "A legendary spear said to be wielded by angels, raining divine judgment on the wicked.", 
            "Spear", 
            "Divine",
            "Melee",
            'S'))

        # Staff
        weapons.append(Weapon("Cracked Wooden Staff", 
            "A simple wooden staff etched with faint runes. Its magic is weak and unstable.", 
            "Staff", 
            "Magic",
            "Ranged",
            'E'))

        weapons.append(Weapon("Runed Staff", 
            "A sturdy staff inscribed with glowing runes, releasing minor magical bursts.", 
            "Staff", 
            "Magic",
            "Ranged",
            'D'))

        weapons.append(Weapon("Elemental Staff", 
            "A magical staff that channels fire, ice, or lightning with every swing.", 
            "Staff", 
            "Magic",
            "Ranged",
            'C'))

        weapons.append(Weapon("Sorcerer’s Staff", 
            "A finely crafted staff that amplifies the wielder’s arcane power.", 
            "Staff", 
            "Magic",
            "Ranged",
            'B'))

        weapons.append(Weapon("Arcane Staff", 
            "A masterwork magical staff capable of devastating elemental strikes.", 
            "Staff", 
            "Magic",
            "Ranged",
            'A'))

        weapons.append(Weapon("Staff of the Archmage", 
            "A legendary staff imbued with ancient magic, channeling the raw forces of creation.", 
            "Staff", 
            "Magic",
            "Ranged",
            'S'))

        weapons.append(Weapon("Blessed Staff", 
            "A simple staff engraved with holy symbols, faintly glowing with divine energy.", 
            "Staff", 
            "Divine",
            "Ranged",
            'E'))

        weapons.append(Weapon("Cleric’s Staff", 
            "A holy staff used by priests and paladins, smiting minor evil.", 
            "Staff", 
            "Divine",
            "Ranged",
            'D'))

        weapons.append(Weapon("Sanctified Staff", 
            "A radiant staff blessed with divine energy, purifying darkness with every strike.", 
            "Staff", 
            "Divine",
            "Ranged",
            'C'))

        weapons.append(Weapon("Crusader’s Staff", 
            "A mighty weapon wielded by holy warriors, burning with righteous fury.", 
            "Staff", 
            "Divine",
            "Ranged",
            'B'))

        weapons.append(Weapon("Staff of Purity", 
            "A masterfully forged staff glowing with sacred light, cleansing evil wherever it lands.", 
            "Staff", 
            "Divine",
            "Ranged",
            'A'))

        weapons.append(Weapon("Staff of the Seraphim", 
            "A legendary staff said to be wielded by angels, raining divine judgment on the wicked.", 
            "Staff", 
            "Divine",
            "Ranged",
            'S'))

        # Sword
        weapons.append(Weapon("Rusty Sword", 
            "A worn, heavy sword. Difficult to swing, but can deliver powerful blows.", 
            "Sword", 
            "Strength",
            "Melee",
            'E'))

        weapons.append(Weapon("Iron Sword", 
            "A solid iron sword, capable of cleaving armor and shields.", 
            "Sword", 
            "Strength",
            "Melee",
            'D'))

        weapons.append(Weapon("Warrior’s Sword", 
            "A balanced sword forged for battlefield veterans, delivering strong strikes.", 
            "Sword", 
            "Strength",
            "Melee",
            'C'))

        weapons.append(Weapon("Berserker’s Sword", 
            "A massive sword designed to crush multiple foes with brute force.", 
            "Sword", 
            "Strength",
            "Melee",
            'B'))

        weapons.append(Weapon("Titan Sword", 
            "A colossal blade wielded only by the strongest warriors, capable of cleaving anything in its path.", 
            "Sword", 
            "Strength",
            "Melee",
            'A'))

        weapons.append(Weapon("Sword of the Earthshaker", 
            "A legendary sword said to split mountains and leave tremors with every strike.", 
            "Sword", 
            "Strength",
            "Melee",
            'S'))

        weapons.append(Weapon("Lightwood Sword", 
            "A lightweight sword, easy to swing quickly but less damaging.", 
            "Sword", 
            "Dexterity",
            "Melee",
            'E'))

        weapons.append(Weapon("Balanced Sword", 
            "A well-balanced sword allowing for precise, rapid strikes.", 
            "Sword", 
            "Dexterity",
            "Melee",
            'D'))

        weapons.append(Weapon("Swiftstrike Sword", 
            "A finely crafted sword designed for fast and accurate attacks.", 
            "Sword", 
            "Dexterity",
            "Melee",
            'C'))

        weapons.append(Weapon("Razor Sword", 
            "A nimble sword with sharpened edges, perfect for slicing with precision.", 
            "Sword", 
            "Dexterity",
            "Melee",
            'B'))

        weapons.append(Weapon("Phantom Sword", 
            "A masterwork blade that moves as fast as its wielder, striking before enemies can react.", 
            "Sword", 
            "Dexterity",
            "Melee",
            'A'))

        weapons.append(Weapon("Sword of the Trickster", 
            "A legendary sword said to strike with impossible speed and accuracy.", 
            "Sword", 
            "Dexterity",
            "Melee",
            'S'))

        weapons.append(Weapon("Cracked Rune Sword", 
            "A simple sword etched with faint runes. Its magic is weak and unstable.", 
            "Sword", 
            "Magic",
            "Melee",
            'E'))

        weapons.append(Weapon("Runed Sword", 
            "A sword inscribed with glowing runes, releasing minor magical bursts.", 
            "Sword", 
            "Magic",
            "Melee",
            'D'))

        weapons.append(Weapon("Elemental Sword", 
            "A magical sword channeling fire, ice, or lightning with every swing.", 
            "Sword", 
            "Magic",
            "Melee",
            'C'))

        weapons.append(Weapon("Sorcerer’s Sword", 
            "A finely crafted sword that amplifies the wielder’s arcane power.", 
            "Sword", 
            "Magic",
            "Melee",
            'B'))

        weapons.append(Weapon("Arcane Blade", 
            "A masterwork magical sword capable of devastating elemental strikes.", 
            "Sword", 
            "Magic",
            "Melee",
            'A'))

        weapons.append(Weapon("Sword of the Archmage", 
            "A legendary sword imbued with ancient magic, channeling the raw forces of creation.", 
            "Sword", 
            "Magic",
            "Melee",
            'S'))

        weapons.append(Weapon("Blessed Sword", 
            "A simple sword engraved with holy symbols, faintly glowing with divine energy.", 
            "Sword", 
            "Divine",
            "Melee",
            'E'))

        weapons.append(Weapon("Cleric’s Sword", 
            "A holy sword used by priests and paladins, smiting minor evil.", 
            "Sword", 
            "Divine",
            "Melee",
            'D'))

        weapons.append(Weapon("Sanctified Sword", 
            "A radiant sword blessed with divine energy, purifying darkness with every strike.", 
            "Sword", 
            "Divine",
            "Melee",
            'C'))

        weapons.append(Weapon("Crusader’s Sword", 
            "A mighty weapon wielded by holy warriors, burning with righteous fury.", 
            "Sword", 
            "Divine",
            "Melee",
            'B'))

        weapons.append(Weapon("Sword of Purity", 
            "A masterfully forged sword glowing with sacred light, cleansing evil wherever it lands.", 
            "Sword", 
            "Divine",
            "Melee",
            'A'))

        weapons.append(Weapon("Sword of the Seraphim", 
            "A legendary sword said to be wielded by angels, raining divine judgment on the wicked.", 
            "Sword", 
            "Divine",
            "Melee",
            'S'))

        # Wand
        weapons.append(Weapon("Cracked Wooden Wand", 
            "A simple wooden wand etched with faint runes. Its magic is weak and unstable.", 
            "Wand", 
            "Magic",
            "Ranged",
            'E'))

        weapons.append(Weapon("Runed Wand", 
            "A sturdy wand inscribed with glowing runes, releasing minor magical projectiles.", 
            "Wand", 
            "Magic",
            "Ranged",
            'D'))

        weapons.append(Weapon("Elemental Wand", 
            "A magical wand that fires bursts of fire, ice, or lightning.", 
            "Wand", 
            "Magic",
            "Ranged",
            'C'))

        weapons.append(Weapon("Sorcerer’s Wand", 
            "A finely crafted wand that amplifies the wielder’s arcane power.", 
            "Wand", 
            "Magic",
            "Ranged",
            'B'))

        weapons.append(Weapon("Arcane Wand", 
            "A masterwork magical wand capable of devastating elemental attacks.", 
            "Wand", 
            "Magic",
            "Ranged",
            'A'))

        weapons.append(Weapon("Wand of the Archmage", 
            "A legendary wand imbued with ancient magic, channeling the raw forces of creation.", 
            "Wand", 
            "Magic",
            "Ranged",
            'S'))

        weapons.append(Weapon("Blessed Wand", 
            "A wand engraved with holy symbols, faintly glowing with divine energy.", 
            "Wand", 
            "Divine",
            "Ranged",
            'E'))

        weapons.append(Weapon("Cleric’s Wand", 
            "A holy wand used by priests and paladins, firing minor divine energy.", 
            "Wand", 
            "Divine",
            "Ranged",
            'D'))

        weapons.append(Weapon("Sanctified Wand", 
            "A radiant wand blessed with divine power, purifying darkness with every shot.", 
            "Wand", 
            "Divine",
            "Ranged",
            'C'))

        weapons.append(Weapon("Crusader’s Wand", 
            "A powerful divine wand, shooting holy energy to smite evil.", 
            "Wand", 
            "Divine",
            "Ranged",
            'B'))

        weapons.append(Weapon("Wand of Purity", 
            "A masterfully forged wand glowing with sacred light, cleansing evil wherever its shots land.", 
            "Wand", 
            "Divine",
            "Ranged",
            'A'))

        weapons.append(Weapon("Wand of the Seraphim", 
            "A legendary divine wand said to be wielded by angels, firing beams of holy wrath.", 
            "Wand", 
            "Divine",
            "Ranged",
            'S'))




        weapon = next(w for w in weapons if w.name == "Thieves knife")
        initial_weapons_choice.append(weapon.weapon_id)

        weapon = next(w for w in weapons if w.name == "Ironclad Mace")
        initial_weapons_choice.append(weapon.weapon_id)
        
        weapon = next(w for w in weapons if w.name == "Elderwood Staff")
        initial_weapons_choice.append(weapon.weapon_id)

        
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
        
        myWeapons.append(next(w for w in weapons if w.weapon_id == 15))
        myWeapons.append(adding_weapon)
        myEquipments.append(next(e for e in equipments if e.equipment_id == 0))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 1))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 2))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 3))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 4))
        return 