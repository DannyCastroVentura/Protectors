init python:
    def initializing_things():
        global protectors_base_information
        global allMissionTemplates
        global allMissions
        global bossMissions
        global weapons
        global initial_weapons_choice
        global equipments
        global myEquipments


        # creating protectors    
        protectors_base_information["ninja"] = BaseProtectorData(10, 17, 12, 14, 13, 8, 11, 0.15, 0.5, 0.2, 0.34, 0.25, 0.125, 0.16)
        # it gains:
        # 1 dex per 2 levels
        # 1 intelligence wisdom per 3 levels
        # 1 wisdom per 4 levels
        # 1 constitution per 5 levels
        # 1 luck per 6 levels
        # 1 strenght per 7 levels
        # 1 charisma per 8 levels

        protectors_base_information["recruit"] = BaseProtectorData(14, 13, 15, 10, 9, 13, 11, 0.5, 0.15, 0.34, 0.25, 0.2, 0.16, 0.2)
        # it gains:
        # 1 strength per 2 levels
        # 1 constitution per 3 levels
        # 1 int per 4 levels
        # 1 wisdom per 5 levels
        # 1 charisma per 6 levels
        # 1 dexterity per 7 levels
        # 1 luck per 8 levels

        protectors_base_information["robot"] = BaseProtectorData(16, 14, 18, 16, 10, 6, 5, 0.25, 0.34, 0.2, 0.5, 0.16, 0.125, 0.1)
        # it gains:
        # 1 intelligence per 2 levels
        # 1 dexterity per 3 levels
        # 1 strenght per 4 levels
        # 1 constitution per 5 levels
        # 1 wisdom per 6 levels
        # 1 charisma per 8 levels
        # 1 luck per 10 levels

        protectors_base_information["samurai"] = BaseProtectorData(14, 13, 13, 12, 14, 10, 9, 0.5, 0.5, 0.25, 0.2, 0.34, 0.16, 0.125)
        # it gains:
        # 1 strenght per 2 levels
        # 1 dexterity per 2 levels
        # 1 wisdom per 3 levels
        # 1 constitution per 4 levels
        # 1 inteligence per 5 levels
        # 1 charisma per 6 levels
        # 1 luck per 8 levels

        protectors_base_information["skeleton"] = BaseProtectorData(17, 18, 10, 6, 8, 6, 20, 0.34, 0.5, 0.25, 0.2, 0.125, 0, 0)
        # it gains:
        # 1 dexterity per 2 levels
        # 1 strenght per 3 levels
        # 1 constitution per 4 levels
        # 1 intelligence per 5 levels
        # 1 wisdom per 6 levels
        
        protectors_base_information["templar"] = BaseProtectorData(15, 10, 14, 11, 15, 12, 8, 0.5, 0.16, 0.5, 0.2, 0.34, 0.2, 0.125)
        # it gains:
        # 1 strenght per 2 levels
        # 1 constitution per 2 levels
        # 1 wisdom per 3 levels
        # 1 charisma per 4 levels
        # 1 intelligence per 5 levels
        # 1 dexterity per 6 levels
        # 1 luck per 8 levels

        # Recreate Possible Missions # Tittle / description
        # 🔥 23
        allMissionTemplates.append(MissionTemplate("Fortress Under Siege", "Enemy forces are surrounding our stronghold. Hold the line and repel the assault.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Ambush the Ambushers", "A convoy was attacked on the trade route. Hunt down the attackers and secure the area.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Eliminate the Threat", "A dangerous warlord has been terrorizing nearby villages. Track him down and end his reign.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Border Skirmish", "Enemies are testing our defenses near the border. Push them back and show no weakness.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Outpost Reclaim", "One of our forward outposts has fallen. Lead a strike team to retake it.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Sabotage the Siege", "Enemy engineers are preparing siege weapons. Destroy them before they are complete.", "Combat"))
        allMissionTemplates.append(MissionTemplate("No Man's Pass", "Hold a mountain pass against overwhelming odds until reinforcements arrive.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Strike from the Shadows", "Lead a surprise night raid on a key enemy encampment.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Broken Line", "Our front line has collapsed. Fall back, regroup, and prevent a total rout.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Minefield Sweep", "Clear a path through a newly discovered minefield under enemy fire.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Airstrike Coordination", "Tag key targets in enemy territory to guide incoming bombardments.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Evacuate Under Fire", "Civilians are trapped in a combat zone. Cover their retreat while under attack.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Hold the Watchtower", "You're the last line of defense. Hold the tower until backup arrives.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Storm the Trenches", "Enemy trenches are heavily fortified. Lead the charge to break through.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Nightfall Offensive", "Launch a surprise attack at dusk to overwhelm the enemy before they regroup.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Flank and Collapse", "Find a weak point in the enemy formation and collapse their rear guard.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Burn the Bridge", "An enemy supply bridge must be destroyed before reinforcements arrive.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Crush the Rebellion", "An armed uprising has begun in the capital. Lead elite forces to suppress it.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Hold the Ridge", "You're the last line of defense on the high ground. Defend it at all costs.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Intercept the Raiders", "Raiders are headed toward a trade route. Intercept and neutralize them.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Tunnel Assault", "Enemies are using underground tunnels. Clear them out room by room.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Frozen Front", "A winter storm is closing in—fight off enemy forces before you're snowed in.", "Combat"))
        allMissionTemplates.append(MissionTemplate("Retaliation Strike", "A nearby outpost was attacked. Launch a swift retaliatory strike to send a message.", "Combat"))


        # 🛡️ 23
        allMissionTemplates.append(MissionTemplate("Saving Hostages", "Bandits have taken hostages in this area. We must act quickly to rescue them before it's too late.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Escort the Caravan", "A merchant caravan needs safe passage through dangerous territory. Ensure their arrival without harm.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Protect the Witness", "A key witness is being targeted. Guard them until they can safely testify.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Save the Lost Scouts", "A scouting party is overdue and feared captured. Find them and bring them back.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Break the Siege", "A town is besieged and running low on supplies. Fight your way in and break the enemy hold.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Hostage Exchange", "Negotiate and protect a delicate exchange—any misstep could turn deadly.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Rescue the Healer", "A renowned healer is being held by raiders. Liberate them before their skills are lost.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Fleeing Refugees", "A column of refugees is fleeing conflict. Escort them to safe territory.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Secure the Convoy", "A high-value cargo convoy must reach its destination unharmed.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Assassins in the Shadows", "The city’s ruler is under threat. Uncover and eliminate the assassins.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Protect the Relic", "A sacred artifact is being transported. Guard it against thieves and zealots alike.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Retrieve the Captive Knight", "One of our champions is being held by the enemy. Storm the prison and free them.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Secure the Safehouse", "A safehouse is compromised. Protect the informants until extraction.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Collapse in the Mine", "A mine has collapsed, trapping workers underground. Organize a swift rescue.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Fishermen Adrift", "A storm has stranded fishermen at sea. Rescue them before their boat sinks.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Save the Pilgrims", "A group of pilgrims is being attacked on a sacred trail. Get them to safety.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Beneath the Rubble", "An explosion has leveled part of a village. Dig out survivors before time runs out.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Ghost Town Retrieval", "A ghost town has become haunted and dangerous. Retrieve a stranded family.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Poisoned Prisoners", "A prison has been sabotaged with poison gas. Rescue the inmates before it’s fatal.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Siege Evacuation", "Civilians are still trapped inside a city under siege. Smuggle them out silently.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Runaway Royalty", "A young noble has fled into enemy territory. Retrieve them before enemies do.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Collapsed Caravan", "A merchant caravan overturned in dangerous terrain. Rescue and protect the survivors.", "Rescue"))
        allMissionTemplates.append(MissionTemplate("Lighthouse in Peril", "A lighthouse keeper hasn't responded in days. Investigate and rescue if needed.", "Rescue"))


        # 🕵️ 23
        allMissionTemplates.append(MissionTemplate("Mystery at Dawnfall", "Strange disappearances are happening in the town of Dawnfall. Investigate and uncover the truth.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Enemy Intel", "We've located a hidden enemy outpost. Infiltrate it and retrieve any valuable information.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Tracking the Shadows", "A spy has slipped past our borders. Follow their trail and report back.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Ciphers in the Dark", "A codebreaker believes an intercepted message holds secrets. Protect them while they work.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Ruins Recon", "Explore ancient ruins rumored to hide enemy scouts or forbidden tech.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Missing Patrol", "A regular patrol failed to report back. Investigate their last known location.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Eyes on the Enemy", "Shadow a convoy suspected of transporting illegal weapons—observe but do not engage.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Infiltrate the Council", "Attend a secret gathering disguised as a delegate and gather intelligence.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Interrogation Duty", "A captured spy refuses to talk. Guard them while the truth is extracted.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Echoes in the Fog", "Locals report strange sightings at night. Uncover the truth behind the rumors.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Dead Drop Retrieval", "A covert informant left intel in a public area. Retrieve it before it's compromised.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Decrypt the Past", "A recovered journal may reveal enemy plans. Help piece it together safely.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Footprints in the Snow", "Follow faint tracks through hostile terrain to uncover a hidden enemy camp.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Hollow Echoes", "Strange sounds come from a remote canyon. Investigate and report your findings.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Undercover Festival", "A known assassin will strike during a local festival. Blend in and find them first.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Smuggler’s Trail", "Follow the trail of a smuggler ring operating across borders.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Lantern Signal", "A coded light signal was seen in the hills. Investigate its source.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Vigil in the Fog", "Scouts claim something hunts in the mist. Stay hidden and learn what it is.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Whispers in the Court", "Court gossip hints at treason. Discreetly find out who's behind it.", "Recon"))
        allMissionTemplates.append(MissionTemplate("The Hidden Cache", "A map points to a hidden supply cache. Find it before others do.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Shifting Tracks", "Enemy patrol routes are changing daily. Record and map their new strategy.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Lurking Below", "Creatures have been seen in sewer tunnels. Investigate and confirm the threat.", "Recon"))
        allMissionTemplates.append(MissionTemplate("Fog of War", "A thick fog conceals enemy movements. Scout and relay their position.", "Recon"))


        # 🌿 23
        allMissionTemplates.append(MissionTemplate("Food for the Famine", "A village is starving after a drought. Deliver supplies and ensure no one interferes.", "Moral"))
        allMissionTemplates.append(MissionTemplate("Justice or Mercy?", "A criminal has surrendered—but the locals want blood. Decide their fate and keep the peace.", "Moral"))
        allMissionTemplates.append(MissionTemplate("Healing the Wounded", "A field hospital is overrun. Defend the medics and help evacuate the wounded.", "Moral"))
        allMissionTemplates.append(MissionTemplate("A Town in Flames", "An accidental fire has devastated a village. Help organize rescue and relief.", "Moral"))
        allMissionTemplates.append(MissionTemplate("Peace Talks", "Two factions are on the verge of war. Broker peace—without drawing your sword.", "Moral"))
        allMissionTemplates.append(MissionTemplate("Defend the Innocent", "Vigilantes seek to punish suspected traitors. Intervene and ensure due process.", "Moral"))
        allMissionTemplates.append(MissionTemplate("Medicine Run", "A deadly illness spreads fast. Deliver antidotes to the afflicted before it's too late.", "Moral"))
        allMissionTemplates.append(MissionTemplate("Prison Riot", "Inmates have taken over a prison. Stop the violence without unnecessary bloodshed.", "Moral"))
        allMissionTemplates.append(MissionTemplate("The Orphan’s Plea", "A child begs you to save their kidnapped parent. Will you answer the call?", "Moral"))
        allMissionTemplates.append(MissionTemplate("Clean Water Crisis", "A poisoned river threatens an entire region. Investigate and resolve the source.", "Moral"))
        allMissionTemplates.append(MissionTemplate("The Unjust Law", "An edict puts innocents in danger. Uphold justice—even if it means defying orders.", "Moral"))
        allMissionTemplates.append(MissionTemplate("Shelter from the Storm", "A deadly storm is coming. Guide survivors to shelter in time.", "Moral"))
        allMissionTemplates.append(MissionTemplate("A Burdened Conscience", "A soldier regrets their actions in battle. Help them find redemption—or justice.", "Moral"))
        allMissionTemplates.append(MissionTemplate("The Execution Order", "You're ordered to execute prisoners you believe are innocent. Decide what to do.", "Moral"))
        allMissionTemplates.append(MissionTemplate("Child Soldiers", "Enemy forces include conscripted children. Find a way to stop the conflict peacefully.", "Moral"))
        allMissionTemplates.append(MissionTemplate("Buried in Shame", "A past atrocity by your side has come to light. How will you respond?", "Moral"))
        allMissionTemplates.append(MissionTemplate("Outcast’s Return", "A wrongly exiled villager seeks protection. Decide whether to risk taking them in.", "Moral"))
        allMissionTemplates.append(MissionTemplate("The Slaver’s Coin", "A wealthy slaver offers gold to look the other way. Will you accept?", "Moral"))
        allMissionTemplates.append(MissionTemplate("Dying Wish", "A wounded enemy begs you to deliver a letter to their family. Will you honor it?", "Moral"))
        allMissionTemplates.append(MissionTemplate("The Silent Ones", "A mute community is being exploited. Help them find justice without violence.", "Moral"))
        allMissionTemplates.append(MissionTemplate("Echoes of Guilt", "An ally admits to a war crime. Do you turn them in or protect them?", "Moral"))
        allMissionTemplates.append(MissionTemplate("False Prophet", "A preacher is stirring hate under the guise of peace. Confront or ignore?", "Moral"))
        allMissionTemplates.append(MissionTemplate("The Beggar Prince", "A beggar claims to be a lost prince. Do you investigate or dismiss the claim?", "Moral"))


        # 🏛️ 23
        allMissionTemplates.append(MissionTemplate("Guard the Summit", "Leaders from across the land are meeting. Ensure their safety and prevent sabotage.", "Political"))
        allMissionTemplates.append(MissionTemplate("Negotiator's Escort", "A diplomat needs protection in hostile lands. Stay vigilant and avoid bloodshed.", "Political"))
        allMissionTemplates.append(MissionTemplate("Suppress the Coup", "A power struggle threatens to erupt into civil war. Step in and restore order before it's too late.", "Political"))
        allMissionTemplates.append(MissionTemplate("Guard the Treaty", "A peace treaty is about to be signed. Protect the venue from saboteurs.", "Political"))
        allMissionTemplates.append(MissionTemplate("Interrogate the Envoy", "A foreign diplomat may be a double agent. Handle the questioning with care.", "Political"))
        allMissionTemplates.append(MissionTemplate("Prevent the Vote", "A corrupt law is about to pass. Delay the council meeting by any (non-lethal) means.", "Political"))
        allMissionTemplates.append(MissionTemplate("Expose the Traitor", "Someone within the court is leaking secrets. Identify and confront them discreetly.", "Political"))
        allMissionTemplates.append(MissionTemplate("Public Trial", "A controversial trial draws angry mobs. Maintain peace during the proceedings.", "Political"))
        allMissionTemplates.append(MissionTemplate("Hidden Alliance", "Uncover a secret alliance that threatens to tip the balance of power.", "Political"))
        allMissionTemplates.append(MissionTemplate("Royal Escort", "The heir to the throne must travel through enemy-controlled territory. Protect them at all costs.", "Political"))
        allMissionTemplates.append(MissionTemplate("Noble Dispute", "A feud between two powerful houses threatens civil war. Mediate before it's too late.", "Political"))
        allMissionTemplates.append(MissionTemplate("Divided City", "A city is torn between factions. Support peaceful reunification through diplomacy and action.", "Political"))
        allMissionTemplates.append(MissionTemplate("Secure the Vote", "Corruption threatens the outcome of an election. Protect the polling process from interference.", "Political"))
        allMissionTemplates.append(MissionTemplate("Backroom Bargain", "A powerful lord is making secret deals. Discover what they're hiding.", "Political"))
        allMissionTemplates.append(MissionTemplate("Crowned in Secret", "A coronation was held in secret. Determine if the claim to power is legitimate.", "Political"))
        allMissionTemplates.append(MissionTemplate("Shield the Reformer", "A reformer wants to change the system. Protect them from assassination attempts.", "Political"))
        allMissionTemplates.append(MissionTemplate("Court of Lies", "Attend a royal court and uncover the falsehoods spreading among nobles.", "Political"))
        allMissionTemplates.append(MissionTemplate("Spoils of Peace", "Peace talks may lead to unjust land grabs. Expose the corruption.", "Political"))
        allMissionTemplates.append(MissionTemplate("Festival of Unity", "Keep tensions low between feuding factions during a national celebration.", "Political"))
        allMissionTemplates.append(MissionTemplate("Uneasy Alliance", "Two former enemies now share power. Keep the alliance from unraveling.", "Political"))
        allMissionTemplates.append(MissionTemplate("The Puppet Master", "A figure behind the throne pulls all the strings. Discover their influence.", "Political"))
        allMissionTemplates.append(MissionTemplate("Scroll of Secrets", "A stolen diplomatic scroll contains dangerous secrets. Retrieve it discreetly.", "Political"))
        allMissionTemplates.append(MissionTemplate("Kingmaker’s Gamble", "A noble is building power to influence the next ruler. Decide whether to support or stop them.", "Political"))


        # Recreate missions
        allMissions.append(Mission("Training", "Send a protector to train in your facilities.", 0, 1, 1, "Training", "not assigned", 9000, 0))

        creating_new_missions()

        bossMissions.append(BossMission(1, "The Mireborn Tyrant", "Deep within a poisonous swamp, a mutated beast commands venomous creatures and twisted flora. It oozes acid and rage — only its death can cleanse the land.", 20))
        bossMissions.append(BossMission(2, "The Pale King", "A ruler who transcended death now commands legions of the undead. His soul is bound to a cursed throne. Break his chains and survive the wrath of his fallen empire.", 25))
        bossMissions.append(BossMission(3, "The Hollow Sentinel", "A forgotten guardian awakens in the ruins of an ancient temple. Armed with rusted steel and remnants of lost magic, it strikes with surprising precision. Defeat it to gain access to the inner sanctum.", 30))
        bossMissions.append(BossMission(4, "The Drowned Prophet", "Sunken beneath a once-great city lies a priest possessed by ancient sea gods. His chants summon tidal waves and spectral leviathans. Silence him before the flood rises.", 35))
        bossMissions.append(BossMission(5, "The Iron Colossus", "A living war machine, awakened from the forgotten age, marches toward civilization. Scale its limbs, sabotage its systems, and battle it atop its metal heart.", 40))
        bossMissions.append(BossMission(6, "The Clockwork Butcher", "In the quiet town of Elderglen, people vanish at night. A deranged clockmaker turned mechanical horror stalks the foggy streets. Enter his twisted workshop and end the nightmare before the town is silenced forever.", 45))
        bossMissions.append(BossMission(7, "The Infernal Architect", "A demon that builds war machines in a fortress of fire and gears. Deactivate his defenses and destroy his creations before confronting him in a hellish showdown.", 50))
        bossMissions.append(BossMission(8, "The Eclipse Warden", "At the edge of the world, a being of shadow and solar flame guards the passage to the void. Fight through alternating light and dark phases in a battle of cosmic rhythm.", 60))
        bossMissions.append(BossMission(9, "The Shattered Queen", "In a realm of mirrors and illusions, an exiled queen of a fallen kingdom bends reality to her will. Break her illusions to reveal her true form — and end her madness.", 70))
        bossMissions.append(BossMission(10, "The Void-Touched Seraph", "Once a divine guardian, now corrupted by the void. This winged horror fights in aerial stages, using celestial and abyssal magic. Only a grounded will can reach the skies.", 90))
        
        
        # Normal weapons (~30 damage)
        weapons.append(Weapon("Thieves knife", 
            "A sleek normal dagger normally used by thieves.", 
            "knife", 
            "Dexterity weapon",
            30))

        weapons.append(Weapon("Ironclad Mace",
            "A sturdy mace used by city guards.",
            "mace",
            "Strength weapon",
            32))
        
        weapons.append(Weapon("Elderwood Staff",
            "A staff carved from ancient trees, buzzing with latent magic.",
            "staff",
            "Magic weapon",
            25))

        weapons.append(Weapon("Whisperwind", 
            "A light lance favored by the swift riders of the northern plains.", 
            "lance", 
            "Dexterity weapon",
            28))

        weapons.append(Weapon("Silent Thorn", 
            "A small but deadly knife used by assassins to strike silently.", 
            "knife", 
            "Dexterity weapon",
            25))

        weapons.append(Weapon("Gale Lance", 
            "A slender lance that strikes as swiftly as the wind.", 
            "lance", 
            "Dexterity weapon",
            30))

        weapons.append(Weapon("Shadow Lance", 
            "A lance forged from shadows, almost invisible to the naked eye.", 
            "lance", 
            "Dexterity weapon",
            33))


        # Better weapons (~100-300 damage)
        weapons.append(Weapon("Dragon's Breath", 
            "A massive flaming sword said to be imbued with the power of an ancient dragon.", 
            "sword", 
            "Strength weapon",
            150))

        weapons.append(Weapon("Earthshaker", 
            "A heavy axe that can split mountains with a single swing.", 
            "axe", 
            "Strength weapon",
            180))

        weapons.append(Weapon("Arcane Edge", 
            "A magical sword glowing with blue runes, capable of slicing through spells.", 
            "sword", 
            "Magic weapon",
            120))

        weapons.append(Weapon("Frostbite", 
            "An icy axe that chills the air with each hit.", 
            "axe", 
            "Strength weapon",
            130))

        weapons.append(Weapon("Stormpiercer", 
            "A lance crackling with electricity, used by the storm riders.", 
            "lance", 
            "Magic weapon",
            110))

        weapons.append(Weapon("Venomfang", 
            "A dagger coated with a potent poison that slowly saps life.", 
            "knife", 
            "Dexterity weapon",
            115))

        weapons.append(Weapon("Titan’s Wrath", 
            "A colossal hammer that channels the fury of giants.", 
            "hammer", 
            "Strength weapon",
            300))

        weapons.append(Weapon("Celestial Staff", 
            "A staff pulsing with divine magic, guiding the wielder’s power.", 
            "staff", 
            "Magic weapon",
            140))

        weapons.append(Weapon("Bloodfang", 
            "A serrated sword that grows sharper with every drop of blood spilled.", 
            "sword", 
            "Strength weapon",
            160))

        weapons.append(Weapon("Emberclaw", 
            "An axe glowing with smoldering embers, burning enemies on contact.", 
            "axe", 
            "Strength weapon",
            170))

        weapons.append(Weapon("Mystic Dagger", 
            "A dagger that can pierce the veil between worlds.", 
            "knife", 
            "Magic weapon",
            125))

        weapons.append(Weapon("Silverlight", 
            "A sword made from enchanted silver, effective against dark creatures.", 
            "sword", 
            "Magic weapon",
            135))

        weapons.append(Weapon("Warbreaker", 
            "A massive axe that can shatter shields with ease.", 
            "axe", 
            "Strength weapon",
            220))

        weapons.append(Weapon("Soulpiercer", 
            "A dagger that drains the soul of its victims, feeding the wielder.", 
            "knife", 
            "Magic weapon",
            130))

        weapons.append(Weapon("Dragonclaw", 
            "A curved sword designed to mimic the claw of a dragon, swift and deadly.", 
            "sword", 
            "Dexterity weapon",
            140))


        # Best weapons (500+ damage)
        weapons.append(Weapon("Oblivion", 
            "A legendary sword said to consume the souls of entire armies.", 
            "sword", 
            "Magic weapon",
            520))

        weapons.append(Weapon("Colossus Crusher", 
            "A gargantuan hammer capable of leveling entire fortresses.", 
            "hammer", 
            "Strength weapon",
            580))

        weapons.append(Weapon("Dragonlord's Fury", 
            "A lance wielded by the ancient dragon kings, burning with eternal flame.", 
            "lance",
            "Strength weapon",
            540))

        weapons.append(Weapon("Nightmare Edge", 
            "A cursed blade that deals unimaginable pain to its victims.", 
            "sword",
            "Magic weapon",
            510))
        
        
        # Normal tier (20-40 damage)
        weapons.append(Weapon("Swiftfang",
            "A quick dagger favored by thieves, light and deadly.",
            "knife",
            "Dexterity weapon",
            35))

        weapons.append(Weapon("Moonlit Spear",
            "A spear that gleams under the moonlight, perfect for precise strikes.",
            "spear",
            "Dexterity weapon",
            30))

        weapons.append(Weapon("Crimson Axe",
            "An axe stained red from countless battles.",
            "axe",
            "Strength weapon",
            38))

        # Mid tier (100-300 damage)
        weapons.append(Weapon("Fang of the Wolf",
            "A curved sword that bites as fiercely as a wolf.",
            "sword",
            "Dexterity weapon",
            140))

        weapons.append(Weapon("Blazefury",
            "A flaming greatsword that ignites enemies on contact.",
            "sword",
            "Strength weapon",
            220))

        weapons.append(Weapon("Thunderstrike Lance",
            "A lance crackling with lightning, it paralyzes foes.",
            "lance",
            "Magic weapon",
            180))

        weapons.append(Weapon("Venomous Claw",
            "A claw-shaped dagger coated with deadly poison.",
            "knife",
            "Dexterity weapon",
            130))

        weapons.append(Weapon("Stonebreaker",
            "A hammer capable of smashing stone walls.",
            "hammer",
            "Strength weapon",
            210))

        # High tier (500-900 damage)
        weapons.append(Weapon("Obsidian Edge",
            "A sword made from volcanic glass, razor sharp and dark.",
            "sword",
            "Strength weapon",
            580))

        weapons.append(Weapon("Celestial Wrath",
            "A staff channeling the fury of the stars.",
            "staff",
            "Magic weapon",
            650))

        weapons.append(Weapon("Silent Gale",
            "A swift lance that can pierce through the thickest armor.",
            "lance",
            "Dexterity weapon",
            510))

        weapons.append(Weapon("Titan's Grasp",
            "A massive axe wielded only by the strongest warriors.",
            "axe",
            "Strength weapon",
            890))

        weapons.append(Weapon("Shadowfang Reaper",
            "An assassin's dagger with a deadly bite and unmatched speed.",
            "knife",
            "Dexterity weapon",
            540))

        # Ultra-powerful tier (1000+ damage)
        weapons.append(Weapon("Dragonfire Greatsword",
            "A legendary sword engulfed in eternal flames of a dragon.",
            "sword",
            "Strength weapon",
            1250))

        weapons.append(Weapon("Ethereal Lance",
            "A lance that phases through solid matter, striking the spirit.",
            "lance",
            "Magic weapon",
            1100))

        weapons.append(Weapon("Soulrend Dagger",
            "A dagger that tears the soul apart, feared by all.",
            "knife",
            "Dexterity weapon",
            1020))

        weapons.append(Weapon("Worldbreaker Hammer",
            "A hammer said to have shattered mountains with a single blow.",
            "hammer",
            "Strength weapon",
            1400))

        weapons.append(Weapon("Archmage's Staff",
            "A staff imbued with unimaginable arcane power.",
            "staff",
            "Magic weapon",
            1350))

            # New weapons in 700-900 damage range
        weapons.append(Weapon("Stormbreaker Axe",
            "An axe that calls down thunder with every swing.",
            "axe",
            "Strength weapon",
            720))

        weapons.append(Weapon("Arcane Tempest Staff",
            "A staff swirling with violent magical storms.",
            "staff",
            "Magic weapon",
            810))

        weapons.append(Weapon("Phantom Lance",
            "A lance that strikes from the shadows with unrelenting force.",
            "lance",
            "Dexterity weapon",
            900))

        # Dexterity weapon with 1400+ damage
        weapons.append(Weapon("Venomstrike Razor",
            "A legendary dagger so fast and deadly it’s said to pierce the fabric of reality.",
            "knife",
            "Dexterity weapon",
            1425))

        weapon = next(w for w in weapons if w.name == "Thieves knife")
        initial_weapons_choice.append(weapon.weapon_id)

        weapon = next(w for w in weapons if w.name == "Ironclad Mace")
        initial_weapons_choice.append(weapon.weapon_id)
        
        weapon = next(w for w in weapons if w.name == "Elderwood Staff")
        initial_weapons_choice.append(weapon.weapon_id)

        # equipment
        equipments.append(Equipment(
            "Reinforced Iron Helmet",
            "A sturdy helmet made of reinforced iron. Offers excellent protection.",
            "helmet",
            "Tank",
            2,
            1.5
        ))

        equipments.append(Equipment(
            "Windrunner Pants",                       # Name
            "Pants designed for swift movement, they boost speed and critical hit chance.",  # Description
            "pants",                                  # Type
            "Critical",                               # Class name
            2.5,                                      # prio1: Scales Dexterity by 2.5x
            1.8                                       # prio2: Scales Critical Hit Chance by 1.8x
        ))

        equipments.append(Equipment(
            "Iron Chestplate",                       # Name
            "A strong iron chestplate offering high defense.",  # Description
            "body armor",                            # Type
            "Tank",                                  # Class name
            2.5,                                     # prio1: Scales Constitution by 2.5x
            1.8                                      # prio2: Scales Strength by 1.8x
        ))

        equipments.append(Equipment(
            "Boots of the Swift",                    # Name
            "Boots that increase your movement speed and dexterity.",  # Description
            "boots",                                 # Type
            "Evasion",                               # Class name
            1.5,                                     # prio1: Scales Dexterity by 1.5x
            1.8                                      # prio2: Scales Evasion by 1.8x
        ))
        
        equipments.append(Equipment(
            "Light Leather Hood",                    # Name
            "A lightweight hood for agility and quick movements.",  # Description
            "helmet",                                # Type
            "Evasion",                               # Class name
            1,                                       # prio1: Scales Dexterity by 1x
            1.2                                      # prio2: Scales Evasion by 1.2x
        ))

        equipments.append(Equipment(
            "Mystic Wizard's Hat",                   # Name
            "A wizard’s hat, enhancing magical powers and intellect.",  # Description
            "helmet",                                # Type
            "Magic",                                 # Class name
            1.8,                                     # prio1: Scales Intelligence by 1.8x
            1.3                                      # prio2: Scales Mana by 1.3x
        ))

        equipments.append(Equipment(
            "Mystic Robe",                           # Name
            "A robe that grants extra magical resistance and boosts mana regeneration.",  # Description
            "body armor",                            # Type
            "Magic",                                 # Class name
            1.2,                                     # prio1: Scales Intelligence by 1.2x
            1.6                                      # prio2: Scales Mana by 1.6x
        ))

        equipments.append(Equipment(
            "Golden Plate Mail",                     # Name
            "A glorious plate mail forged from gold, offers supreme defense.",  # Description
            "body armor",                            # Type
            "Tank",                                  # Class name
            3,                                       # prio1: Scales Constitution by 3x
            1.2                                      # prio2: Scales Strength by 1.2x
        ))

        equipments.append(Equipment(
            "Feathered Boots",                       # Name
            "Light as a feather, offering extreme agility and evasion.",  # Description
            "boots",                                 # Type
            "Evasion",                               # Class name
            2,                                       # prio1: Scales Dexterity by 2x
            2                                       # prio2: Scales Evasion by 2x
        ))

        equipments.append(Equipment(
            "Wraith Cloak",                          # Name
            "A cloak made from the essence of wraiths, enhancing evasion and stealth.",  # Description
            "body armor",                            # Type
            "Evasion",                               # Class name
            2.5,                                     # prio1: Scales Evasion by 2.5x
            1.8                                      # prio2: Scales Stealth by 1.8x
        ))

        equipments.append(Equipment(
            "Elven Cloak",                           # Name
            "A cloak that boosts agility and offers increased critical hit chance.",  # Description
            "body armor",                            # Type
            "Critical",                              # Class name
            2,                                       # prio1: Scales Dexterity by 2x
            2.5                                      # prio2: Scales Critical Chance by 2.5x
        ))

        equipments.append(Equipment(
            "Crown of the Ancients",                 # Name
            "A crown that increases wisdom and enhances magical abilities.",  # Description
            "helmet",                                # Type
            "Magic",                                 # Class name
            2.2,                                     # prio1: Scales Intelligence by 2.2x
            1.6                                      # prio2: Scales Mana Regeneration by 1.6x
        ))

        # equipment
        equipments.append(Equipment(
            "Silver Circlet",                         # Name
            "A delicate circlet that enhances magical defense and intelligence.",  # Description
            "helmet",                                 # Type
            "Magic",                                  # Class name
            1.5,                                      # prio1: Scales Intelligence by 1.5x
            1.8                                       # prio2: Scales Magical Defense by 1.8x
        ))

        equipments.append(Equipment(
            "Titanium Chestplate",                    # Name
            "A high-tech chestplate offering immense defense against all attacks.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            3.2,                                      # prio1: Scales Constitution by 3.2x
            1.4                                       # prio2: Scales Physical Defense by 1.4x
        ))

        equipments.append(Equipment(
            "Boots of the Abyss",                    # Name
            "Boots that grant the wearer enhanced movement speed and dark resistance.",  # Description
            "boots",                                  # Type
            "Evasion",                                # Class name
            2.2,                                      # prio1: Scales Dexterity by 2.2x
            1.5                                       # prio2: Scales Dark Resistance by 1.5x
        ))

        equipments.append(Equipment(
            "Celestial Boots",                        # Name
            "Boots blessed by the stars, increasing speed and mana regeneration.",  # Description
            "boots",                                  # Type
            "Magic",                                  # Class name
            1.7,                                      # prio1: Scales Dexterity by 1.7x
            1.8                                       # prio2: Scales Mana Regeneration by 1.8x
        ))

        equipments.append(Equipment(
            "Shadow Cloak",                           # Name
            "A cloak that grants the wearer invisibility for short periods and boosts stealth.",  # Description
            "body armor",                             # Type
            "Evasion",                                # Class name
            3.0,                                      # prio1: Scales Evasion by 3x
            2.0                                       # prio2: Scales Stealth by 2x
        ))

        equipments.append(Equipment(
            "Vampire's Mantle",                       # Name
            "A dark mantle that increases strength and grants life steal on attacks.",  # Description
            "body armor",                             # Type
            "Strength",                               # Class name
            2.5,                                      # prio1: Scales Strength by 2.5x
            1.4                                       # prio2: Scales Life Steal by 1.4x
        ))

        equipments.append(Equipment(
            "Titan's Helm",                           # Name
            "A massive helmet that grants immense protection and boosts strength.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            3.2,                                      # prio1: Scales Strength by 3.2x
            2.0                                       # prio2: Scales Constitution by 2x
        ))

        equipments.append(Equipment(
            "Assassin's Cowl",                        # Name
            "A cowl that boosts stealth, evasion, and critical hit chance.",  # Description
            "helmet",                                 # Type
            "Critical",                               # Class name
            2.5,                                      # prio1: Scales Evasion by 2.5x
            2.8                                       # prio2: Scales Critical Hit Chance by 2.8x
        ))

        equipments.append(Equipment(
            "Phoenix Wings",                          # Name
            "Wings of a fallen phoenix, offering extreme fire resistance and a chance to rise from the ashes.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            4.5,                                      # prio1: Scales Constitution by 4.5x
            2.0                                       # prio2: Scales Fire Resistance by 2.0x
        ))

        
        equipments.append(Equipment(
            "Crown of the Immortal King",             # Name
            "A crown that gives the wearer the power to revive once upon death and boosts all stats.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            6.0,                                      # prio1: Scales Strength by 6x
            4.0                                       # prio2: Scales Constitution by 4x
        ))

        equipments.append(Equipment(
            "Wings of the Seraphim",                  # Name
            "Wings that bestow divine power, granting increased movement and evasion.",  # Description
            "boots",                                  # Type
            "Evasion",                                # Class name
            3.5,                                      # prio1: Scales Dexterity by 3.5x
            4.0                                       # prio2: Scales Evasion by 4x
        ))

            
        equipments.append(Equipment(
            "Elderwood Armor",                        # Name
            "Armor crafted from the ancient trees of the elderwood. Increases defense and regeneration.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            4.0,                                      # prio1: Scales Constitution by 4x
            2.5                                       # prio2: Scales Health Regeneration by 2.5x
        ))

        equipments.append(Equipment(
            "Cloak of the Revenant",                  # Name
            "A cloak made from the shadows of the dead. It grants invisibility and an aura that weakens enemies.",  # Description
            "body armor",                             # Type
            "Evasion",                                # Class name
            4.0,                                      # prio1: Scales Evasion by 4x
            3.5                                       # prio2: Scales Stealth by 3.5x
        ))

        equipments.append(Equipment(
            "Cloak of the Phoenix",                   # Name
            "A cloak that grants regeneration and the ability to rise from death once, like a phoenix.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            6.0,                                      # prio1: Scales Constitution by 6x
            2.8                                       # prio2: Scales Health Regeneration by 2.8x
        ))

        equipments.append(Equipment(
            "Crown of the Celestial Emperor",         # Name
            "A crown that gives the wearer divine strength and resilience, making them nearly immortal.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            7.0,                                      # prio1: Scales Constitution by 7x
            3.0                                       # prio2: Scales Immortality Chance by 3x
        ))

        # equipment
        equipments.append(Equipment(
            "Titanium Helm",                          # Name
            "A sturdy titanium helmet that grants extra defense and resistance.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            2.5,                                      # prio1: Scales Constitution by 2.5x
            1.8                                       # prio2: Scales Physical Resistance by 1.8x
        ))

        equipments.append(Equipment(
            "Dragonscale Body Armor",                 # Name
            "Armor crafted from dragon scales. Offers great defense and fire resistance.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            3.2,                                      # prio1: Scales Constitution by 3.2x
            2.0                                       # prio2: Scales Fire Resistance by 2x
        ))

        equipments.append(Equipment(
            "Shadowstrike Boots",                     # Name
            "Boots made for stealth and speed. They increase dexterity and evasion.",  # Description
            "boots",                                  # Type
            "Evasion",                                # Class name
            2.5,                                      # prio1: Scales Dexterity by 2.5x
            2.0                                       # prio2: Scales Evasion by 2x
        ))

        equipments.append(Equipment(
            "Elven Armor",                            # Name
            "Lightweight body armor favored by elves, increases dexterity and evasion.",  # Description
            "body armor",                             # Type
            "Evasion",                                # Class name
            2.0,                                      # prio1: Scales Dexterity by 2x
            1.7                                       # prio2: Scales Evasion by 1.7x
        ))

        equipments.append(Equipment(
            "Ironclad Helmet",                        # Name
            "A helmet forged from iron, offers high physical defense and durability.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            3.0,                                      # prio1: Scales Constitution by 3x
            1.5                                       # prio2: Scales Physical Defense by 1.5x
        ))

        equipments.append(Equipment(
            "Mystic Boots",                           # Name
            "Boots imbued with magic, increasing movement speed and resistance to magic attacks.",  # Description
            "boots",                                  # Type
            "Magic",                                  # Class name
            2.0,                                      # prio1: Scales Dexterity by 2x
            2.5                                       # prio2: Scales Magical Resistance by 2.5x
        ))

        equipments.append(Equipment(
            "Darksteel Body Armor",                   # Name
            "A body armor made from darksteel, offering immense protection but reducing speed.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            3.8,                                      # prio1: Scales Constitution by 3.8x
            1.4                                       # prio2: Scales Physical Resistance by 1.4x
        ))

        equipments.append(Equipment(
            "Flameguard Helm",                        # Name
            "A helmet that provides increased fire resistance and boosts physical defense.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            2.5,                                      # prio1: Scales Constitution by 2.5x
            2.0                                       # prio2: Scales Fire Resistance by 2x
        ))

        equipments.append(Equipment(
            "Knight's Armor",                         # Name
            "Heavy armor worn by knights, offering high defense and stability.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            3.0,                                      # prio1: Scales Constitution by 3x
            1.7                                       # prio2: Scales Stability by 1.7x
        ))

        equipments.append(Equipment(
            "Spectral Boots",                         # Name
            "Boots crafted from the essence of shadows. They grant enhanced evasion and a bonus to stealth.",  # Description
            "boots",                                  # Type
            "Evasion",                                # Class name
            2.3,                                      # prio1: Scales Dexterity by 2.3x
            2.3                                       # prio2: Scales Stealth by 2.3x
        ))

        equipments.append(Equipment(
            "Steelfoot Pants",                        # Name
            "Heavy pants made from steel that increase physical defense and movement speed.",  # Description
            "pants",                                  # Type
            "Tank",                                   # Class name
            2.0,                                      # prio1: Scales Constitution by 2x
            1.6                                       # prio2: Scales Movement Speed by 1.6x
        ))

        equipments.append(Equipment(
            "Windward Body Armor",                    # Name
            "A body armor that boosts evasion and agility, perfect for swift fighters.",  # Description
            "body armor",                             # Type
            "Evasion",                                # Class name
            2.8,                                      # prio1: Scales Dexterity by 2.8x
            1.5                                       # prio2: Scales Evasion by 1.5x
        ))

        equipments.append(Equipment(
            "Giant's Helmet",                         # Name
            "A massive helmet that greatly increases strength and durability.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            3.5,                                      # prio1: Scales Strength by 3.5x
            1.8                                       # prio2: Scales Constitution by 1.8x
        ))

        equipments.append(Equipment(
            "Mercenary Pants",                        # Name
            "Pants made for mercenaries, boosting strength and providing extra durability.",  # Description
            "pants",                                  # Type
            "Strength",                               # Class name
            2.5,                                      # prio1: Scales Strength by 2.5x
            1.5                                       # prio2: Scales Constitution by 1.5x
        ))

        equipments.append(Equipment(
            "Ironboots",                              # Name
            "Boots made from iron, providing solid defense and increased resistance to damage.",  # Description
            "boots",                                  # Type
            "Tank",                                   # Class name
            2.8,                                      # prio1: Scales Constitution by 2.8x
            1.6                                       # prio2: Scales Physical Resistance by 1.6x
        ))

        equipments.append(Equipment(
            "Hardened Leather Body Armor",            # Name
            "Light armor made from hardened leather, boosting evasion and critical hit chance.",  # Description
            "body armor",                             # Type
            "Evasion",                                # Class name
            2.3,                                      # prio1: Scales Dexterity by 2.3x
            2.0                                       # prio2: Scales Critical Hit Chance by 2.0x
        ))

        equipments.append(Equipment(
            "Elderhelm",                              # Name
            "An ancient helmet that grants wisdom and protects against magical attacks.",  # Description
            "helmet",                                 # Type
            "Magic",                                  # Class name
            2.0,                                      # prio1: Scales Intelligence by 2x
            1.8                                       # prio2: Scales Magical Defense by 1.8x
        ))

        equipments.append(Equipment(
            "Vanguard Pants",                         # Name
            "Pants worn by the vanguard, enhancing defense and fortitude.",  # Description
            "pants",                                  # Type
            "Tank",                                   # Class name
            2.0,                                      # prio1: Scales Constitution by 2x
            1.5                                       # prio2: Scales Defense by 1.5x
        ))

        equipments.append(Equipment(
            "Swiftstride Boots",                      # Name
            "Boots that increase movement speed and evasion, perfect for agile warriors.",  # Description
            "boots",                                  # Type
            "Evasion",                                # Class name
            2.2,                                      # prio1: Scales Dexterity by 2.2x
            1.9                                       # prio2: Scales Evasion by 1.9x
        ))
        # equipment
        equipments.append(Equipment(
            "Helm of the Fallen King",                # Name
            "A regal helmet that enhances strength and grants resistance to critical hits.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            4.5,                                      # prio1: Scales Strength by 4.5x
            2.5                                       # prio2: Scales Critical Hit Resistance by 2.5x
        ))

        equipments.append(Equipment(
            "Dragonbone Armor",                       # Name
            "A body armor crafted from the bones of ancient dragons, offering massive defense and fire resistance.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            5.0,                                      # prio1: Scales Constitution by 5x
            3.0                                       # prio2: Scales Fire Resistance by 3x
        ))

        equipments.append(Equipment(
            "Demonhunter Boots",                      # Name
            "Boots designed for elite demon hunters, offering speed, evasion, and increased critical damage.",  # Description
            "boots",                                  # Type
            "Critical",                               # Class name
            3.5,                                      # prio1: Scales Dexterity by 3.5x
            3.0                                       # prio2: Scales Critical Damage by 3x
        ))

        equipments.append(Equipment(
            "Celestial Chestplate",                   # Name
            "A chestplate blessed by the gods, offering extraordinary defense and holy resistance.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            5.2,                                      # prio1: Scales Constitution by 5.2x
            2.5                                       # prio2: Scales Holy Resistance by 2.5x
        ))

        equipments.append(Equipment(
            "Windrider Helm",                         # Name
            "A helmet that grants enhanced agility and grants a chance to dodge attacks.",  # Description
            "helmet",                                 # Type
            "Evasion",                                # Class name
            4.0,                                      # prio1: Scales Dexterity by 4x
            2.5                                       # prio2: Scales Dodge Chance by 2.5x
        ))

        equipments.append(Equipment(
            "Armageddon Boots",                       # Name
            "Boots that imbue the wearer with fiery speed, boosting movement speed and fire resistance.",  # Description
            "boots",                                  # Type
            "Tank",                                   # Class name
            3.2,                                      # prio1: Scales Constitution by 3.2x
            2.5                                       # prio2: Scales Fire Resistance by 2.5x
        ))

        equipments.append(Equipment(
            "Phantom Lurker Pants",                   # Name
            "Pants woven from the fabric of shadows, increasing evasion and granting stealth.",  # Description
            "pants",                                  # Type
            "Evasion",                                # Class name
            4.0,                                      # prio1: Scales Dexterity by 4x
            2.8                                       # prio2: Scales Stealth by 2.8x
        ))

        equipments.append(Equipment(
            "Berserker Plate",                        # Name
            "A heavy armor that increases strength and grants a temporary rage buff after being hit.",  # Description
            "body armor",                             # Type
            "Strength",                               # Class name
            4.8,                                      # prio1: Scales Strength by 4.8x
            2.5                                       # prio2: Scales Rage Damage by 2.5x
        ))

        equipments.append(Equipment(
            "Revenant Helm",                          # Name
            "A helm forged from the remains of a powerful revenant. It increases health and provides a shield upon death.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            4.0,                                      # prio1: Scales Constitution by 4x
            3.0                                       # prio2: Scales Death Shield by 3x
        ))

        equipments.append(Equipment(
            "Frostguard Armor",                       # Name
            "An icy armor that greatly boosts defense against frost and grants immunity to freezing effects.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            5.5,                                      # prio1: Scales Constitution by 5.5x
            3.5                                       # prio2: Scales Frost Resistance by 3.5x
        ))

        equipments.append(Equipment(
            "Gladiator's Boots",                      # Name
            "Boots that provide incredible movement speed and stamina, perfect for relentless combat.",  # Description
            "boots",                                  # Type
            "Tank",                                   # Class name
            3.8,                                      # prio1: Scales Dexterity by 3.8x
            2.0                                       # prio2: Scales Stamina by 2x
        ))

        equipments.append(Equipment(
            "Shroud of the Wraith",                   # Name
            "A body armor that enhances evasion and allows the wearer to move through walls for short periods.",  # Description
            "body armor",                             # Type
            "Evasion",                                # Class name
            4.5,                                      # prio1: Scales Dexterity by 4.5x
            3.0                                       # prio2: Scales Stealth by 3x
        ))

        equipments.append(Equipment(
            "Astral Helm",                            # Name
            "A magical helm that boosts intelligence and grants resistance to all types of magical damage.",  # Description
            "helmet",                                 # Type
            "Magic",                                  # Class name
            4.5,                                      # prio1: Scales Intelligence by 4.5x
            2.8                                       # prio2: Scales Magic Resistance by 2.8x
        ))

        equipments.append(Equipment(
            "Valkyrie Armor",                         # Name
            "Armor made from the feathers of Valkyries, offering extreme agility and evasion.",  # Description
            "body armor",                             # Type
            "Evasion",                                # Class name
            4.2,                                      # prio1: Scales Dexterity by 4.2x
            3.2                                       # prio2: Scales Evasion by 3.2x
        ))

        equipments.append(Equipment(
            "Astral Pants",                           # Name
            "Pants imbued with cosmic energy, boosting critical hit chance and damage.",  # Description
            "pants",                                  # Type
            "Critical",                               # Class name
            3.5,                                      # prio1: Scales Dexterity by 3.5x
            3.0                                       # prio2: Scales Critical Hit Chance by 3x
        ))

        equipments.append(Equipment(
            "Emberstorm Boots",                       # Name
            "Boots made from the essence of a volcanic eruption, increasing fire resistance and speed.",  # Description
            "boots",                                  # Type
            "Tank",                                   # Class name
            3.2,                                      # prio1: Scales Constitution by 3.2x
            2.5                                       # prio2: Scales Fire Resistance by 2.5x
        ))

        equipments.append(Equipment(
            "Hellfire Plate",                         # Name
            "A chestplate crafted from molten lava, offering high defense and fire damage reflection.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            5.2,                                      # prio1: Scales Constitution by 5.2x
            3.0                                       # prio2: Scales Fire Damage Reflection by 3x
        ))

        equipments.append(Equipment(
            "Wraith's Garb",                          # Name
            "A body armor made of spectral material, boosting evasion and reducing incoming damage.",  # Description
            "body armor",                             # Type
            "Evasion",                                # Class name
            4.5,                                      # prio1: Scales Dexterity by 4.5x
            2.8                                       # prio2: Scales Damage Reduction by 2.8x
        ))

        equipments.append(Equipment(
            "Guardian's Helmet",                      # Name
            "A helmet worn by ancient guardians, boosting vitality and providing a shield that absorbs damage.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            4.0,                                      # prio1: Scales Constitution by 4x
            3.2                                       # prio2: Scales Shield Absorption by 3.2x
        ))

        # equipment
        equipments.append(Equipment(
            "Crown of the Eternal Emperor",           # Name
            "A crown forged from the celestial essence of an eternal emperor, boosting strength, defense, and resilience.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            6.0,                                      # prio1: Scales Strength by 6x
            4.5                                       # prio2: Scales Constitution by 4.5x
        ))

        equipments.append(Equipment(
            "Abyssal Plate of Immortality",           # Name
            "An ancient plate armor imbued with the power of the Abyss, granting unparalleled defense and regeneration.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            7.0,                                      # prio1: Scales Constitution by 7x
            3.8                                       # prio2: Scales Regeneration by 3.8x
        ))

        equipments.append(Equipment(
            "Hellstorm Boots",                        # Name
            "Boots made from the essence of the underworld, providing immense movement speed and immunity to fire damage.",  # Description
            "boots",                                  # Type
            "Tank",                                   # Class name
            4.8,                                      # prio1: Scales Dexterity by 4.8x
            5.0                                       # prio2: Scales Fire Immunity by 5x
        ))

        equipments.append(Equipment(
            "Warden's Shieldplate",                   # Name
            "A body armor worn by the legendary wardens, providing nearly invincible defense and resistance to all elemental effects.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            6.5,                                      # prio1: Scales Constitution by 6.5x
            4.0                                       # prio2: Scales Elemental Resistance by 4x
        ))

        equipments.append(Equipment(
            "Celestial Crown",                        # Name
            "A crown crafted by the gods, enhancing intelligence and providing divine protection against all types of damage.",  # Description
            "helmet",                                 # Type
            "Magic",                                  # Class name
            5.5,                                      # prio1: Scales Intelligence by 5.5x
            4.5                                       # prio2: Scales All Damage Resistance by 4.5x
        ))

        equipments.append(Equipment(
            "Titanic Stompers",                       # Name
            "Boots forged from the heart of a mountain, granting extraordinary strength and resistance to stun effects.",  # Description
            "boots",                                  # Type
            "Tank",                                   # Class name
            5.0,                                      # prio1: Scales Strength by 5x
            3.5                                       # prio2: Scales Stun Resistance by 3.5x
        ))

        equipments.append(Equipment(
            "Veil of Shadows",                        # Name
            "A cloak imbued with the powers of shadows, increasing stealth, evasion, and damage output in the dark.",  # Description
            "body armor",                             # Type
            "Evasion",                                # Class name
            5.5,                                      # prio1: Scales Dexterity by 5.5x
            4.5                                       # prio2: Scales Stealth Damage by 4.5x
        ))

        equipments.append(Equipment(
            "Phoenix Helm of Rebirth",                # Name
            "A helmet crafted from the ashes of a phoenix, granting rebirth upon death and regeneration over time.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            5.0,                                      # prio1: Scales Constitution by 5x
            4.0                                       # prio2: Scales Rebirth Effect by 4x
        ))

        equipments.append(Equipment(
            "Volcanic Vestments",                     # Name
            "An armor that channels volcanic power, providing immense fire damage immunity and a lava burst counterattack.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            7.5,                                      # prio1: Scales Constitution by 7.5x
            5.0                                       # prio2: Scales Fire Damage Reflection by 5x
        ))

        equipments.append(Equipment(
            "Viperstrike Boots",                      # Name
            "Boots that enhance poison resistance and grant an increased chance to poison enemies on hit.",  # Description
            "boots",                                  # Type
            "Critical",                               # Class name
            5.0,                                      # prio1: Scales Dexterity by 5x
            4.5                                       # prio2: Scales Poison Chance by 4.5x
        ))

        equipments.append(Equipment(
            "Raven's Wings Armor",                    # Name
            "An armor that enhances speed and evasion, allowing the wearer to glide short distances and take no fall damage.",  # Description
            "body armor",                             # Type
            "Evasion",                                # Class name
            6.0,                                      # prio1: Scales Dexterity by 6x
            3.8                                       # prio2: Scales Evasion by 3.8x
        ))

        equipments.append(Equipment(
            "Cloak of the Abyss",                     # Name
            "A dark cloak that greatly increases magical resistance and increases critical hit damage.",  # Description
            "body armor",                             # Type
            "Magic",                                  # Class name
            5.5,                                      # prio1: Scales Intelligence by 5.5x
            4.0                                       # prio2: Scales Critical Hit Damage by 4x
        ))

        equipments.append(Equipment(
            "Unyielding Titan Plate",                 # Name
            "A legendary plate armor worn by the gods of war, providing unparalleled physical defense and immunity to knockback.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            7.0,                                      # prio1: Scales Constitution by 7x
            4.5                                       # prio2: Scales Knockback Resistance by 4.5x
        ))

        equipments.append(Equipment(
            "King's Aegis Helmet",                    # Name
            "A divine helmet that increases the wearer's health and grants a shield that absorbs damage each time they are hit.",  # Description
            "helmet",                                 # Type
            "Tank",                                   # Class name
            6.2,                                      # prio1: Scales Constitution by 6.2x
            4.5                                       # prio2: Scales Shield Absorption by 4.5x
        ))

        equipments.append(Equipment(
            "Shadowborn Leggings",                    # Name
            "Leggings imbued with the essence of darkness, enhancing movement speed and evasion.",  # Description
            "pants",                                  # Type
            "Evasion",                                # Class name
            6.0,                                      # prio1: Scales Dexterity by 6x
            4.0                                       # prio2: Scales Movement Speed by 4x
        ))

        equipments.append(Equipment(
            "Wings of the Seraphim",                  # Name
            "Boots with angelic wings, enabling flight for short distances and boosting evasion.",  # Description
            "boots",                                  # Type
            "Evasion",                                # Class name
            5.5,                                      # prio1: Scales Dexterity by 5.5x
            3.0                                       # prio2: Scales Evasion by 3x
        ))

        equipments.append(Equipment(
            "Heart of the Storm",                     # Name
            "A chestplate that channels the fury of a storm, granting lightning immunity and enhancing agility.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            6.8,                                      # prio1: Scales Constitution by 6.8x
            4.0                                       # prio2: Scales Agility by 4x
        ))

        equipments.append(Equipment(
            "Soulfire Boots",                         # Name
            "Boots that ignite the ground beneath you with each step, dealing fire damage to nearby enemies.",  # Description
            "boots",                                  # Type
            "Tank",                                   # Class name
            5.2,                                      # prio1: Scales Strength by 5.2x
            3.5                                       # prio2: Scales Fire Damage Output by 3.5x
        ))

        equipments.append(Equipment(
            "Divine Embrace Plate",                   # Name
            "A chestplate imbued with divine energy, granting immunity to negative effects and increasing vitality.",  # Description
            "body armor",                             # Type
            "Tank",                                   # Class name
            7.2,                                      # prio1: Scales Constitution by 7.2
            5.2
        ))

        
        myEquipments.append(next(e for e in equipments if e.equipment_id == 0))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 1))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 2))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 3))

        for equipment in myEquipments:
            renpy.say(mc, str(equipment.equipment_id))
            renpy.say(mc, equipment.name)
            renpy.say(mc, equipment.type)

        return 