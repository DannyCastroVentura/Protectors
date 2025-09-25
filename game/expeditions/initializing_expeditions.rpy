init python:
    def initializing_expedition_enemies():
        global expeditions_enemies_base_data
        global allExpeditionTemplates
        global allExpeditions

        

        # creating enemies
        # COMBAT (hp + damage)
        expeditions_enemies_base_data["Combat"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
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
            ["Greatsword"], None, None,
            "Melee", None, None,
            "Regular", "Regular", "Regular",
            "Rusty Greatsword"
        )
        
        # RESCUE con, dex, luc, spe
        expeditions_enemies_base_data["Rescue"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "constitution", "dexterity", "luck", "speed", "speed"
                ], 
                "evolution1": [
                    "constitution", "dexterity", "luck", "speed", "speed"
                ], 
                "evolution2": [
                    "constitution", "dexterity", "luck", "speed", "speed"
                ]
            }, 
            "CON_DEX", "CON_DEX", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Greatsword"], None, None,
            "Melee", None, None,
            "Regular", "Regular", "Regular",
            "Rusty Greatsword"
        )
        
        # RECON dex, spe, luc
        expeditions_enemies_base_data["Recon"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 15,
                "constitution": 15,
                "intelligence": 15,
                "wisdom": 15,
                "speed": 15,
                "luck": 15,
                "attack_speed": 1
            },
            {
                "basic": [
                    "dexterity", "speed", "luck", "speed"
                ], 
                "evolution1": [
                    "dexterity", "speed", "luck", "speed"
                ], 
                "evolution2": [
                    "dexterity", "speed", "luck", "speed"
                ]
            }, 
            "EVA", "EVA", 
            "Name 1", 
            "Description 1",
            "Name 2", 
            "Description 2",
            ["Greatsword"], None, None,
            "Melee", None, None,
            "Regular", "Regular", "Regular",
            "Rusty Greatsword"
        )
        

        
        # Recreate Possible Expeditions # Tittle / description
        # 🔥 23 - Combat - damage * atack speed + health
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


        # Recreate expeditions
        allExpeditions.append(Expedition("Training", "Send a protector to train in your facilities.", 0, 1, 1, "Training", "not assigned", 99000, 0))

        creating_new_expeditions()
