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
        protectors_base_information["Ninja"] = BaseProtectorData(
            {
                "strength": 10,
                "dexterity": 17,
                "constitution": 12,
                "intelligence": 14,
                "wisdom": 13,
                "charisma": 8,
                "luck": 11
            }, 
            [
                "dexterity", "luck", "constitution", "dexterity", "intelligence", 
                "constitution", "dexterity", "strength", "dexterity", "charisma", 
                "dexterity", "intelligence", "strength", "constitution", "wisdom", 
                "dexterity", "luck", "dexterity", "strength", "dexterity", 
                "wisdom", "constitution", "dexterity", "luck", "dexterity"
            ], 
            "EVA", "DEX_TAN", 
            "Ash Ninja", 
            "While exploring a forgotten cave, he touched a cursed relic that bound dark magic to his body. From that moment, he gained the power to transform into ash, disappearing into smoke to strike unseen.",
            "Tech Ninja", 
            "Recruited by the army, he wields weapons infused with cutting-edge technology and wears armor that adapts to any threat. Every strike is precise, every movement optimized, making him a deadly force on the battlefield.",
            ["Knife", "Sword", "Hands"], None, None,
            "Melee",
            "Regular",
            "Thieves knife"
        )
        
        protectors_base_information["Templar"] = BaseProtectorData(
            {
                "strength": 15,
                "dexterity": 10,
                "constitution": 14,
                "intelligence": 11,
                "wisdom": 15,
                "charisma": 12,
                "luck": 8
            }, 
            [
                "strength", "wisdom", "constitution", "strength", "charisma", 
                "strength", "wisdom", "constitution", "strength", "intelligence", 
                "strength", "wisdom", "strength", "charisma", "constitution", 
                "strength", "wisdom", "strength", "luck", "strength"
            ], 
            "MIR_TAN", "MIR_STR_STR",
            "Saint Templar",
            "A devoted templar, he was granted a sacred blessing to wield the power of the saints. and every strike carries divine judgment. Guided by unbreakable devotion, he stands as a living vessel of sanctity on the battlefield.",
            "Demonic Templar",
            "Once a templar of faith, he forsook the light and accepted a blasphemous blessing from demons. His blade burns with unholy fire, his armor twists with infernal power, and every strike spreads corruption.",
            ["Sword", "Spear", "Greatsword", "Hands"], None, None,
            "Melee",
            "Divine",
            "Templar Greatsword"
        )

        protectors_base_information["Wizard"] = BaseProtectorData(
            {
                "strength": 7,
                "dexterity": 10,
                "constitution": 11,
                "intelligence": 18,
                "wisdom": 18,
                "charisma": 9,
                "luck": 12
            }, 
            [
                "intelligence", "wisdom", "constitution", "intelligence", "intelligence", 
                "wisdom", "intelligence", "constitution", "wisdom", "dexterity", 
                "intelligence", "wisdom", "constitution", "luck", "intelligence", 
                "wisdom", "charisma", "intelligence", "wisdom", "constitution"
            ], 
            "MIR_CON", "INT",
            "Thunder Wizard",
            "Through years of study in forgotten libraries, he unlocked the secrets of the arcane. Spells of thunder and lightning bend to his will, making him a master of battlefield control.",
            "Nature Wizard",
            "Clad in enchanted robes, he uses his nature spells to wields traps and kill enemies from the ground using his deadly vines. Using precision and strategy he shows as a dangerous threat for anyone who faces him.",
            ["Wand", "Staff", "Hands"], None, None,
            "Ranged",
            "Magic",
            "Principiant Wand"
        )

        protectors_base_information["Joker"] = BaseProtectorData(
            {
                "strength": 8,
                "dexterity": 14,
                "constitution": 10,
                "intelligence": 14,
                "wisdom": 14,
                "charisma": 9,
                "luck": 16
            }, 
            [
                "dexterity", "wisdom", "luck", "dexterity", "wisdom", 
                "constitution", "dexterity", "wisdom", "luck", "luck", 
                "dexterity", "wisdom", "luck", "luck", "dexterity", 
                "wisdom", "luck", "dexterity", "wisdom", "constitution",
                "constitution", "luck", "wisdom", "dexterity", "constitution"
            ], 
            "MIR_MIR_DEX", "CRI",
            "Demonic Joker",
            "In a forgotten arcane library, he found a deck of dark enchanted cards, each holding demonic essence. Now, whispers from the cards slowly turn him into a demon with every throw.",
            "Sharpen Joker",
            "A master of strategy and dexterity, he wields his deck like a razor-sharp blade. Every card is a weapon, every draw a calculated gamble, turning him into a lethal force from afar.",
            ["Cards", "Hands"], None, None,
            "Melee",
            "Regular",
            "Deadman Cards"
        )

        protectors_base_information["Samurai"] = BaseProtectorData(
            {
                "strength": 14,
                "dexterity": 13,
                "constitution": 13,
                "intelligence": 12,
                "wisdom": 14,
                "charisma": 10,
                "luck": 9
            },
            [
                "strength", "dexterity", "strength", "constitution", "strength", 
                "wisdom", "dexterity", "dexterity", "constitution", "strength", 
                "dexterity", "wisdom", "strength", "dexterity", "strength", 
                "intelligence", "strength", "dexterity", "constitution", "charisma"
            ], 
            "TAN", "DAM",
            "Tech Samurai",
            "Once bound by tradition, he forged a secret pact with visionary craftsmen. His blade, born of ancient mastery and hidden technology, strikes with unmatched precision; his armor adapts to any threat.",
            "Wolf Samurai",
            "Once a disciplined samurai, he was transformed into a fearsome wolf. Now faster, and driven by primal instinct, his strikes land with devastating force. He is an unstoppable predator on the battlefield.",
            ["Hands", "Katana"], None, None,
            "Melee",
            "Regular",
            "Samurai Rusty Katana"
        )

        protectors_base_information["Recruit"] = BaseProtectorData(
            {
                "strength": 14,
                "dexterity": 13,
                "constitution": 15,
                "intelligence": 10,
                "wisdom": 9,
                "charisma": 12,
                "luck": 11
            },
            [
                "dexterity", "strength", "dexterity", "constitution", "dexterity", 
                "strength", "dexterity", "constitution", "dexterity", "strength", 
                "dexterity", "constitution", "dexterity", "strength", "charisma", 
                "strength", "luck", "strength", "constitution", "charisma"
            ], 
            "EVA", "STR_STR_STR_CON",
            "Special Forces Agent",
            "Determined to become one of the best, he enlisted in the Special Forces intense training. After proving his skill, he earned his place and now strikes with unmatched precision, agility, and tactical mastery on every mission.",
            "Berserker",
            "Trapped in fear during a mission, the recruit’s mind finally snapped, and that terror erupted into uncontrollable, burning rage. Now he fights with pure instinct as he charges into battle with relentless ferocity.",
            ["Knife", "Gun", "Hands", "Machine gun", "Sniper"], ["Knife", "Gun", "Machine gun", "Sniper", "Hands"], ["Hands", "Knife", "Sword", "Greatsword", "Greataxe", "Spear", "Axe", "Hammer", "Great Hammer", "Mace"],
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


        # 🛡️ 23 - Rescue - defense
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


        # 🕵️ 23 - Recon - evasion
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


        # 🌿 23 - Moral - Intelligence + wisdom?
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


        # 🏛️ 23 - Political - Charisma
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
        allMissions.append(Mission("Training", "Send a protector to train in your facilities.", 0, 1, 1, "Training", "not assigned", 99000, 0))

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
        
        # WEAPONS
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # E CLASS
        weapons.append(Weapon("Thieves knife", 
            "A sleek normal dagger normally used by thieves.", 
            "Knife", 
            "Dexterity",
            30,
            'E'))
        
        weapons.append(Weapon("Templar Greatsword", 
            "A rusty giant sword used in the crusades.", 
            "Greatsword", 
            "Strength",
            35,
            'E'))
        weapons.append(Weapon("Principiant Wand",
            "A wand used by the iniciants on magic training.",
            "Wand",
            "Magic",
            25,
            'E'))
        
        weapons.append(Weapon("Gambling Cards",
            "Normal cards, used for gamling.",
            "Cards",
            "Dexterity",
            27,
            'E'))
        
        weapons.append(Weapon("Deadman Cards",
            "Pack of cards gotten from a dead man.",
            "Cards",
            "Divine",
            27,
            'E'))
        
        weapons.append(Weapon("Samurai Rusty Katana", 
            "A rusty katana used by Samurais for training.", 
            "Katana", 
            "Strength",
            28,
            'E'))
        
        weapons.append(Weapon("Combat knife", 
            "A rusty knife used by the army.",
            "Knife", 
            "Strength",
            26,
            'E'))
        
        weapons.append(Weapon("Combat Pistol", 
            "A rusty pistol used by the army on its intensive training.",
            "Gun", 
            "Dexterity",
            26,
            'E'))

        weapons.append(Weapon("Ironclad Mace",
            "A sturdy mace used by city guards.",
            "Mace",
            "Strength",
            32,
            'E'))
        
        weapons.append(Weapon("Elderwood Staff",
            "A staff carved from ancient trees, buzzing with latent magic.",
            "Staff",
            "Magic",
            25,
            'E'))

        weapons.append(Weapon("Whisperwind", 
            "A light lance favored by the swift riders of the northern plains.", 
            "Spear", 
            "Dexterity",
            28,
            'E'))

        weapons.append(Weapon("Small Vikings Axe", 
            "A small but deadly axe used by vikings to kill their enemies.", 
            "Axe", 
            "Strength",
            25,
            'E'))

        weapons.append(Weapon("Gale Hammer", 
            "A slender hammer that strikes as hard as a rock.", 
            "Hammer", 
            "Strength",
            30,
            'E'))

        weapons.append(Weapon("Iron Sword", 
            "A sword forged with iron stone.", 
            "Sword", 
            "Strength",
            33,
            'E'))

        weapons.append(Weapon("Shadow Sword", 
            "A sword forged from shadows, almost invisible to the naked eye.", 
            "Sword", 
            "Dexterity",
            29,
            'E'))
            
        weapons.append(Weapon("Swiftfang",
            "A quick dagger favored by thieves, light and deadly.",
            "Knife",
            "Dexterity",
            35,
            'E'))

        weapons.append(Weapon("Moonlit Spear",
            "A spear that gleams under the moonlight, perfect for precise strikes.",
            "Spear",
            "Magic",
            30,
            'E'))

        weapons.append(Weapon("Crimson Axe",
            "An axe stained red from countless battles.",
            "Axe",
            "Strength",
            38,
            'E'))
        
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # D CLASS
        weapons.append(Weapon("Nightfang Dagger", 
            "A wicked, curved blade rumored to drink the strength of its victims.", 
            "Knife", 
            "Dexterity",
            72,
            'D'))

        weapons.append(Weapon("Sentinel’s War Mace",
            "A heavy iron mace favored by royal guards to shatter armor and bone alike.",
            "Mace",
            "Strength",
            85,
            'D'))

        weapons.append(Weapon("Runebark Staff",
            "A mystical staff etched with ancient runes, channeling deep forest magic.",
            "Staff",
            "Magic",
            78,
            'D'))

        weapons.append(Weapon("Stormpiercer Lance", 
            "A long, gleaming lance said to cut through wind and flesh with equal ease.", 
            "Spear", 
            "Dexterity",
            80,
            'D'))

        weapons.append(Weapon("Mage Lance", 
            "A magic infused lance - which gives magic blows to the enemy.", 
            "Spear", 
            "Magic",
            88,
            'D'))

        weapons.append(Weapon("Raven’s Bite Axe", 
            "A brutal, blackened axe once wielded by northern raiders in the dead of winter.", 
            "Axe", 
            "Strength",
            88,
            'D'))

        weapons.append(Weapon("Thunderstrike Hammer", 
            "A massive hammer that crackles faintly with the sound of distant storms.", 
            "Hammer", 
            "Strength",
            90,
            'D'))

        weapons.append(Weapon("Bloodforged Blade", 
            "A broad sword quenched in the blood of its enemies, said to thirst for more.", 
            "Sword", 
            "Strength",
            79,
            'D'))

        weapons.append(Weapon("Moonveil Saber", 
            "A thin, silvery sword that glimmers faintly even in complete darkness.", 
            "Sword", 
            "Dexterity",
            84,
            'D'))
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # C CLASS
        weapons.append(Weapon("Dragon's Breath", 
            "A massive flaming sword said to be imbued with the power of an ancient dragon.", 
            "Sword", 
            "Strength",
            150,
            "C"))

        weapons.append(Weapon("Earthshaker", 
            "A heavy axe that can split mountains with a single swing.", 
            "Axe", 
            "Strength",
            180,
            "C"))

        weapons.append(Weapon("Arcane Edge", 
            "A magical sword glowing with blue runes, capable of slicing through spells.", 
            "Sword", 
            "Magic",
            120,
            "C"))

        weapons.append(Weapon("Frostbite", 
            "An icy axe that chills the air with each hit.", 
            "Axe", 
            "Strength",
            130,
            "C"))

        weapons.append(Weapon("Stormpiercer", 
            "A lance crackling with electricity, used by the storm riders.", 
            "Spear", 
            "Magic",
            110,
            "C"))

        weapons.append(Weapon("Venomfang", 
            "A dagger coated with a potent poison that slowly saps life.", 
            "Knife", 
            "Dexterity",
            115,
            "C"))

        weapons.append(Weapon("Celestial Staff", 
            "A staff pulsing with divine magic, guiding the wielder’s power.", 
            "Staff", 
            "Magic",
            140,
            "C"))

        weapons.append(Weapon("Bloodfang", 
            "A serrated sword that grows sharper with every drop of blood spilled.", 
            "Sword", 
            "Strength",
            160,
            "C"))

        weapons.append(Weapon("Emberclaw", 
            "An axe glowing with smoldering embers, burning enemies on contact.", 
            "Axe", 
            "Strength",
            170,
            "C"))

        weapons.append(Weapon("Mystic Dagger", 
            "A dagger that can pierce the veil between worlds.", 
            "Knife", 
            "Magic",
            125,
            "C"))

        weapons.append(Weapon("Silverlight", 
            "A sword made from enchanted silver, effective against dark creatures.", 
            "Sword", 
            "Magic",
            135,
            "C"))

        weapons.append(Weapon("Warbreaker", 
            "A massive axe that can shatter shields with ease.", 
            "Axe", 
            "Strength",
            220,
            "C"))

        weapons.append(Weapon("Soulpiercer", 
            "A dagger that drains the soul of its victims, feeding the wielder.", 
            "Knife", 
            "Magic",
            130,
            "C"))

        weapons.append(Weapon("Dragonclaw", 
            "A curved sword designed to mimic the claw of a dragon, swift and deadly.", 
            "Sword", 
            "Dexterity",
            140,
            "C"))


        weapons.append(Weapon("Titan’s Wrath", 
            "A colossal hammer that channels the fury of giants.", 
            "Hammer", 
            "Strength",
            300,
            "C"))
            
        weapons.append(Weapon("Fang of the Wolf",
            "A curved sword that bites as fiercely as a wolf.",
            "Sword",
            "Dexterity",
            140,
            "C"))

        weapons.append(Weapon("Blazefury",
            "A flaming greatsword that ignites enemies on contact.",
            "Sword",
            "Strength",
            220,
            "C"))

        weapons.append(Weapon("Thunderstrike Lance",
            "A lance crackling with lightning, it paralyzes foes.",
            "Spear",
            "Magic",
            180,
            "C"))

        weapons.append(Weapon("Venomous Claw",
            "A claw-shaped dagger coated with deadly poison.",
            "Knife",
            "Dexterity",
            130,
            "C"))

        weapons.append(Weapon("Stonebreaker",
            "A hammer capable of smashing stone walls.",
            "Hammer",
            "Strength",
            210,
            "C"))

        
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # B CLASS
        weapons.append(Weapon("Oblivion", 
            "A legendary sword said to consume the souls of entire armies.", 
            "Sword", 
            "Magic",
            520,
            "B"))

        weapons.append(Weapon("Colossus Crusher", 
            "A gargantuan hammer capable of leveling entire fortresses.", 
            "Hammer", 
            "Strength",
            580,
            "B"))

        weapons.append(Weapon("Dragonlord's Fury", 
            "A lance wielded by the ancient dragon kings, burning with eternal flame.", 
            "Spear",
            "Strength",
            540,
            "B"))

        weapons.append(Weapon("Nightmare Edge", 
            "A cursed blade that deals unimaginable pain to its victims.", 
            "Sword",
            "Magic",
            510,
            "B"))
            
        weapons.append(Weapon("Obsidian Edge",
            "A sword made from volcanic glass, razor sharp and dark.",
            "Sword",
            "Strength",
            580,
            "B"))

        weapons.append(Weapon("Celestial Wrath",
            "A staff channeling the fury of the stars.",
            "Staff",
            "Magic",
            650,
            "B"))

        weapons.append(Weapon("Silent Gale",
            "A swift lance that can pierce through the thickest armor.",
            "Spear",
            "Dexterity",
            510,
            "B"))

        weapons.append(Weapon("Shadowfang Reaper",
            "An assassin's dagger with a deadly bite and unmatched speed.",
            "Knife",
            "Dexterity",
            540,
            "B"))

            
        weapons.append(Weapon("Stormbreaker Axe",
            "An axe that calls down thunder with every swing.",
            "Axe",
            "Strength",
            720,
            "B"))

        
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #  
        # A CLASS
        
        weapons.append(Weapon("Arcane Tempest Staff",
            "A staff swirling with violent magical storms.",
            "Staff",
            "Magic",
            810,
            "A"))

        weapons.append(Weapon("Phantom Lance",
            "A lance that strikes from the shadows with unrelenting force.",
            "Spear",
            "Dexterity",
            900,
            "A"))

        weapons.append(Weapon("Titan's Grasp",
            "A massive axe wielded only by the strongest warriors.",
            "Axe",
            "Strength",
            890,
            "A"))

        weapons.append(Weapon("Ethereal Lance",
            "A lance that phases through solid matter, striking the spirit.",
            "Spear",
            "Magic",
            1100,
            "A"))

        weapons.append(Weapon("Soulrend Dagger",
            "A dagger that tears the soul apart, feared by all.",
            "Knife",
            "Dexterity",
            1020,
            "A"))

        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #  
        # S CLASS
        weapons.append(Weapon("Dragonfire Greatsword",
            "A legendary sword engulfed in eternal flames of a dragon.",
            "Sword",
            "Strength",
            1250,
            "S"))

        weapons.append(Weapon("Worldbreaker Hammer",
            "A hammer said to have shattered mountains with a single blow.",
            "Hammer",
            "Strength",
            1400,
            "S"))

        weapons.append(Weapon("Archmage's Staff",
            "A staff imbued with unimaginable arcane power.",
            "Staff",
            "Magic",
            1350,
            "S"))

        weapons.append(Weapon("Venomstrike Razor",
            "A legendary dagger so fast and deadly it’s said to pierce the fabric of reality.",
            "Knife",
            "Dexterity",
            1425,
            "S"))

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
            0.3,
            0.3,
            "E"
        ))

        equipments.append(Equipment(
            "Phoenix Wings",
            "Wings of a fallen phoenix, offering extreme fire resistance and a chance to rise from the ashes.",
            "body",
            "Tank",
            0.85,
            0.5,
            "D"
        ))

        equipments.append(Equipment(
            "Vanguard Pants",
            "Pants worn by the vanguard, enhancing defense and fortitude.",
            "pants",
            "Tank",
            1.5,
            0.9,
            "C"
        ))

        equipments.append(Equipment(
            "Gladiator's Boots",
            "Boots that provide incredible movement speed and stamina, perfect for relentless combat.",
            "boots",
            "Tank",
            2.8,
            1.9,
            "B"
        ))
        
        equipments.append(Equipment(
            "Stormbreak Helm",
            "A helmet that sharpens reflexes and boosts critical hit chance.",
            "helmet",
            "Critical",
            4.8,
            2.7,
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
            0.25,
            0.1,
            "E"
        ))
        
        equipments.append(Equipment(
            "Reinforced Body Armor",
            "A sturdy body armor made of reinforced iron. Offers good protection.",
            "body",
            "Tank",
            0.25,
            0.1,
            "D"
        ))

        equipments.append(Equipment(
            "Reinforced Pants",
            "A sturdy pants made of reinforced iron. Offers good protection.",
            "pants",
            "Tank",
            0.25,
            0.1,
            "C"
        ))

        equipments.append(Equipment(
            "Reinforced Boots",
            "A sturdy boots made of reinforced iron. Offers good protection.",
            "boots",
            "Tank",
            0.25,
            0.1,
            "S"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Windrunner Helmet",
            "Helmet designed for swift movement, they boost speed and critical hit chance.",
            "helmet",
            "Critical",
            0.2,
            0.12,
            "E"
        ))
        
        equipments.append(Equipment(
            "Windrunner Body Armor",
            "Body armor designed for swift movement, they boost speed and critical hit chance.",
            "body",
            "Critical",
            0.2,
            0.12,
            "E"
        ))

        equipments.append(Equipment(
            "Windrunner Pants",
            "Pants designed for swift movement, they boost speed and critical hit chance.",
            "pants",
            "Critical",
            0.2,
            0.12,
            "E"
        ))

        equipments.append(Equipment(
            "Windrunner Boots",
            "Boots designed for swift movement, they boost speed and critical hit chance.",
            "boots",
            "Critical",
            0.2,
            0.12,
            "E"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Iron Helmet",
            "A strong iron helmet offering high defense.",
            "helmet",
            "Shield",
            0.3,
            0.2,
            "E"
        ))

        equipments.append(Equipment(
            "Iron Chestplate",
            "A strong iron chestplate offering high defense.",
            "body",
            "Shield",
            0.3,
            0.2,
            "E"
        ))

        equipments.append(Equipment(
            "Iron Trousers",
            "A strong iron trousers offering high defense.",
            "pants",
            "Shield",
            0.3,
            0.2,
            "E"
        ))

        equipments.append(Equipment(
            "Iron Boots",
            "A strong iron boots offering high defense.",
            "boots",
            "Shield",
            0.3,
            0.2,
            "E"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Helmet of the Swift",
            "Helmet that increase your movement speed and dexterity.",
            "helmet",
            "Evasion",
            0.3,
            0.15,
            "E"
        ))

        equipments.append(Equipment(
            "Upper rags of the Swift",
            "Body armor that increase your movement speed and dexterity.",
            "body",
            "Evasion",
            0.3,
            0.15,
            "E"
        ))

        equipments.append(Equipment(
            "Pants of the Swift",
            "Pants that increase your movement speed and dexterity.",
            "pants",
            "Evasion",
            0.3,
            0.15,
            "E"
        ))

        equipments.append(Equipment(
            "Boots of the Swift",
            "Boots that increase your movement speed and dexterity.",
            "boots",
            "Evasion",
            0.3,
            0.15,
            "E"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Mystic Wizard's Hat",
            "A wizard’s hat, enhancing magical powers and intellect.",
            "helmet",
            "Magic",
            0.4,
            0.05,
            "E"
        ))

        equipments.append(Equipment(
            "Mystic Robe",
            "A robe which grants magical powers and intellect.",
            "body",
            "Magic",
            0.3,
            0.2,
            "E"
        ))

        equipments.append(Equipment(
            "Mystic Pants",
            "A wizard’s pants, enhancing magical powers and intellect.",
            "pants",
            "Magic",
            0.4,
            0.05,
            "E"
        ))

        equipments.append(Equipment(
            "Mystic Boots",
            "Boots which grants magical powers and intellect.",
            "boots",
            "Magic",
            0.3,
            0.2,
            "E"
        ))
        
        ######## OTHER ONES ########
        equipments.append(Equipment(
            "Golden Plate Mail",
            "A glorious plate mail forged from gold, offers supreme defense.",
            "body",
            "Tank",
            0.3,
            0.2,
            "E"
        ))

        equipments.append(Equipment(
            "Feathered Boots",
            "Light as a feather, offering extreme agility and evasion.",
            "boots",
            "Evasion",
            0.35,
            0.25,
            "E"
        ))

        equipments.append(Equipment(
            "Wraith Cloak",
            "A cloak made from the essence of wraiths, enhancing evasion and stealth.",
            "body",
            "Evasion",
            0.3,
            0.3,
            "E"
        ))

        equipments.append(Equipment(
            "Elven Cloak",
            "A cloak that boosts agility and offers increased critical hit chance.",
            "body",
            "Critical",
            0.3,
            0.25,
            "E"
        ))

        equipments.append(Equipment(
            "Crown of the Ancients",
            "A crown that increases wisdom and enhances magical abilities.",
            "helmet",
            "Magic",
            0.4,
            0.3,
            "E"
        ))

        equipments.append(Equipment(
            "Silver Circlet",
            "A delicate circlet that enhances magical defense and intelligence.",
            "helmet",
            "Magic",
            0.45,
            0.1,
            "E"
        ))

        equipments.append(Equipment(
            "Titanium Chestplate",
            "A high-tech chestplate offering immense defense against all attacks.",
            "body",
            "Tank",
            0.3,
            0.3,
            "E"
        ))

        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # D CLASS
        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Helm of the Abyss",
            "A helm that shrouds the wearer’s mind from dark influence while enhancing awareness.",
            "helmet",
            "Evasion",
            0.6,
            0.5,
            "D"
        ))

        equipments.append(Equipment(
            "Chestplate of the Abyss",
            "A chestplate forged in shadowsteel, offering strong protection against darkness.",
            "body",
            "Evasion",
            0.6,
            0.5,
            "D"
        ))

        equipments.append(Equipment(
            "Legguards of the Abyss",
            "Armored pants infused with abyssal magic, granting resilience and agility.",
            "pants",
            "Evasion",
            0.6,
            0.5,
            "D"
        ))

        equipments.append(Equipment(
            "Boots of the Abyss",
            "Boots that grant the wearer enhanced movement speed and dark resistance.",
            "boots",
            "Evasion",
            0.6,
            0.5,
            "D"
        ))
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Celestial Helm",
            "A helm blessed by the stars, sharpening focus and magical control.",
            "helmet",
            "Magic",
            0.9,
            0.3,
            "D"
        ))

        equipments.append(Equipment(
            "Celestial Robe",
            "A flowing robe woven with stardust, enhancing mana flow and spell potency.",
            "body",
            "Magic",
            0.9,
            0.3,
            "D"
        ))

        equipments.append(Equipment(
            "Celestial Legwraps",
            "Light enchanted legwraps that improve mobility and channel magical energy.",
            "pants",
            "Magic",
            0.9,
            0.3,
            "D"
        ))

        equipments.append(Equipment(
            "Celestial Boots",
            "Boots blessed by the stars, increasing speed and mana regeneration.",
            "boots",
            "Magic",
            0.9,
            0.3,
            "D"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Vampire's Visage",
            "A sinister helm that instills fear and strengthens the wearer’s resolve.",
            "helmet",
            "Strength",
            0.7,
            0.4,
            "D"
        ))

        equipments.append(Equipment(
            "Vampire's Mantle",
            "A dark mantle that increases strength and grants life steal on attacks.",
            "body",
            "Strength",
            0.7,
            0.4,
            "D"
        ))

        equipments.append(Equipment(
            "Vampire's Greaves",
            "Heavy pants reinforced with cursed metal, granting power with each strike.",
            "pants",
            "Strength",
            0.7,
            0.4,
            "D"
        ))

        equipments.append(Equipment(
            "Vampire's Treads",
            "Boots infused with vampiric essence, allowing swift movement while draining foes.",
            "boots",
            "Strength",
            0.7,
            0.4,
            "D"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Titan's Helm",
            "A massive helmet that grants immense protection and boosts strength.",
            "helmet",
            "Tank",
            0.7,
            0.7,
            "D"
        ))

        equipments.append(Equipment(
            "Titan's Chestguard",
            "An enormous chestpiece forged for warriors who stand like unyielding mountains.",
            "body",
            "Tank",
            0.7,
            0.7,
            "D"
        ))

        equipments.append(Equipment(
            "Titan's Legplates",
            "Heavy armored greaves that root the wearer firmly in battle.",
            "pants",
            "Tank",
            0.7,
            0.7,
            "D"
        ))

        equipments.append(Equipment(
            "Titan's Boots",
            "Boots as solid as the earth, making each step unshakable.",
            "boots",
            "Tank",
            0.7,
            0.7,
            "D"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Assassin's Cowl",
            "A cowl that boosts stealth, evasion, and critical hit chance.",
            "helmet",
            "Critical",
            0.7,
            0.5,
            "D"
        ))

        equipments.append(Equipment(
            "Assassin's Vest",
            "A lightweight, reinforced vest designed for swift and lethal strikes.",
            "body",
            "Critical",
            0.7,
            0.5,
            "D"
        ))

        equipments.append(Equipment(
            "Assassin's Leggings",
            "Flexible leggings that allow silent movement and deadly agility.",
            "pants",
            "Critical",
            0.7,
            0.5,
            "D"
        ))

        equipments.append(Equipment(
            "Assassin's Boots",
            "Boots crafted for speed and silence, perfect for striking from the shadows.",
            "boots",
            "Critical",
            0.7,
            0.5,
            "D"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Crown of the Immortal King",
            "A crown that gives the wearer the power to revive once upon death and boosts all stats.",
            "helmet",
            "Shield",
            0.75,
            0.65,
            "D"
        ))

        equipments.append(Equipment(
            "Armor of the Immortal King",
            "A regal chestplate that radiates divine protection, shielding its wearer from fatal blows.",
            "body",
            "Shield",
            0.75,
            0.65,
            "D"
        ))

        equipments.append(Equipment(
            "Greaves of the Immortal King",
            "Sturdy leg armor that empowers each stride with the might of an eternal ruler.",
            "pants",
            "Shield",
            0.75,
            0.65,
            "D"
        ))

        equipments.append(Equipment(
            "Sabatons of the Immortal King",
            "Boots that carry the weight of countless victories and unmatched resilience.",
            "boots",
            "Shield",
            0.75,
            0.65,
            "D"
        ))

        
        ######## OTHER ONES ########
        equipments.append(Equipment(
            "Shadow Cloak",
            "A cloak that grants the wearer invisibility for short periods and boosts stealth.",
            "body",
            "Evasion",
            0.7,
            0.6,
            "D"
        ))

        equipments.append(Equipment(
            "Wings of the Seraphim",
            "Wings that bestow divine power, granting increased movement and evasion.",
            "boots",
            "Evasion",
            0.8,
            0.55,
            "D"
        ))

            
        equipments.append(Equipment(
            "Elderwood Armor",
            "Armor crafted from the ancient trees of the elderwood. Increases defense and regeneration.",
            "body",
            "Tank",
            0.7,
            0.7,
            "D"
        ))

        equipments.append(Equipment(
            "Cloak of the Revenant",
            "A cloak made from the shadows of the dead. It grants invisibility and an aura that weakens enemies.",
            "body",
            "Evasion",
            0.8,
            0.75,
            "D"
        ))

        equipments.append(Equipment(
            "Cloak of the Phoenix",
            "A cloak that grants regeneration and the ability to rise from death once, like a phoenix.",
            "body",
            "Tank",
            0.95,
            0.3,
            "D"
        ))

        equipments.append(Equipment(
            "Crown of the Celestial Emperor",
            "A crown that gives the wearer divine strength and resilience, making them nearly immortal.",
            "helmet",
            "Tank",
            1,
            0.05,
            "D"
        ))
        
        equipments.append(Equipment(
            "Titanium Helm",
            "A sturdy titanium helmet that grants extra defense and resistance.",
            "helmet",
            "Tank",
            0.8,
            0.5,
            "D"
        ))

        equipments.append(Equipment(
            "Dragonscale Body Armor",
            "Armor crafted from dragon scales. Offers great defense and fire resistance.",
            "body",
            "Tank",
            0.7,
            0.6,
            "D"
        ))

        equipments.append(Equipment(
            "Shadow Boots",
            "Boots made for stealth and speed. They increase dexterity and evasion.",
            "boots",
            "Evasion",
            0.8,
            0.8,
            "D"
        ))

        ######## 
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # C CLASS
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Elven Hood",
            "A finely crafted hood that sharpens the senses and aids in swift movements.",
            "helmet",
            "Evasion",
            1.3,
            0.7,
            "C"
        ))

        equipments.append(Equipment(
            "Elven Armor",
            "Lightweight body armor favored by elves, increases dexterity and evasion.",
            "body",
            "Evasion",
            1.3,
            0.7,
            "C"
        ))

        equipments.append(Equipment(
            "Elven Leggings",
            "Slim, flexible leggings that allow for quiet steps and quick maneuvers.",
            "pants",
            "Evasion",
            1.3,
            0.7,
            "C"
        ))

        equipments.append(Equipment(
            "Elven Boots",
            "Boots designed for swiftness, perfect for traversing forests without a sound.",
            "boots",
            "Evasion",
            1.3,
            0.7,
            "C"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Ironclad Helmet",
            "A helmet forged from iron, offers high physical defense and durability.",
            "helmet",
            "Tank",
            1.4,
            0.6,
            "C"
        ))

        equipments.append(Equipment(
            "Ironclad Chestplate",
            "A solid iron chestplate built to withstand even the heaviest blows.",
            "body",
            "Tank",
            1.4,
            0.6,
            "C"
        ))

        equipments.append(Equipment(
            "Ironclad Legplates",
            "Heavy iron greaves that protect the wearer’s legs while anchoring them in place.",
            "pants",
            "Tank",
            1.4,
            0.6,
            "C"
        ))

        equipments.append(Equipment(
            "Ironclad Boots",
            "Boots of solid iron that make every step feel unshakable.",
            "boots",
            "Tank",
            1.4,
            0.6,
            "C"
        ))
        

        ######## FULL GEAR ########
        
        equipments.append(Equipment(
            "Mercenary Helm",
            "A sturdy helm favored by mercenaries, offering protection and enhancing focus.",
            "helmet",
            "Strength",
            1.5,
            0.5,
            "C"
        ))

        equipments.append(Equipment(
            "Mercenary Chestplate",
            "A tough chestplate designed for battlefield endurance and strength.",
            "body",
            "Strength",
            1.5,
            0.5,
            "C"
        ))

        equipments.append(Equipment(
            "Mercenary Pants",
            "Pants made for mercenaries, boosting strength and providing extra durability.",
            "pants",
            "Strength",
            1.5,
            0.5,
            "C"
        ))

        equipments.append(Equipment(
            "Mercenary Boots",
            "Boots built for long campaigns, improving stamina and power.",
            "boots",
            "Strength",
            1.5,
            0.5,
            "C"
        ))

        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Sorcery Hood",
            "A hood woven with enchanted threads that amplify magical power.",
            "helmet",
            "Magic",
            1.5,
            0.7,
            "C"
        ))

        equipments.append(Equipment(
            "Sorcery Robe",
            "A robe imbued with arcane energies, enhancing spellcasting abilities.",
            "body",
            "Magic",
            1.5,
            0.7,
            "C"
        ))

        equipments.append(Equipment(
            "Sorcery Pants",
            "Pants made for sorcerers, boosting magic.",
            "pants",
            "Magic",
            1.5,
            0.7,
            "C"
        ))

        equipments.append(Equipment(
            "Sorcery Boots",
            "Boots that increase mana flow and magical speed.",
            "boots",
            "Magic",
            1.5,
            0.7,
            "C"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Flameguard Helm",
            "A helmet that provides increased fire resistance and boosts physical defense.",
            "helmet",
            "Shield",
            1.3,
            1,
            "C"
        ))

        equipments.append(Equipment(
            "Flameguard Chestplate",
            "A chestplate forged in dragon fire, enhancing resistance and durability.",
            "body",
            "Shield",
            1.3,
            1,
            "C"
        ))

        equipments.append(Equipment(
            "Flameguard Legplates",
            "Legplates that protect against flames and physical attacks alike.",
            "pants",
            "Shield",
            1.3,
            1,
            "C"
        ))

        equipments.append(Equipment(
            "Flameguard Boots",
            "Boots that help the wearer withstand intense heat and harsh impacts.",
            "boots",
            "Shield",
            1.3,
            1,
            "C"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Demonhunter Hood",
            "A hood that sharpens senses and grants enhanced stealth for hunting fiends.",
            "helmet",
            "Critical",
            1.5,
            1.0,
            "C"
        ))

        equipments.append(Equipment(
            "Demonhunter Vest",
            "Light armor that balances protection and agility for demon slayers.",
            "body",
            "Critical",
            1.5,
            1.0,
            "C"
        ))

        equipments.append(Equipment(
            "Demonhunter Leggings",
            "Flexible leggings that increase evasion and critical strike potential.",
            "pants",
            "Critical",
            1.5,
            1.0,
            "C"
        ))

        equipments.append(Equipment(
            "Demonhunter Boots",
            "Boots designed for elite demon hunters, offering speed, evasion, and increased critical damage.",
            "boots",
            "Critical",
            1.5,
            1.0,
            "C"
        ))
        

        ######## FULL GEAR ########


        equipments.append(Equipment(
            "Berserker Helm",
            "A rugged helm that sharpens reflexes and fuels the wearer’s fury.",
            "helmet",
            "Dexterity",
            1.3,
            1.1,
            "C"
        ))

        equipments.append(Equipment(
            "Berserker Plate",
            "A heavy armor that increases dexterity and grants a temporary rage buff after being hit.",
            "body",
            "Dexterity",
            1.3,
            1.1,
            "C"
        ))

        equipments.append(Equipment(
            "Berserker Greaves",
            "Armored pants that enhance movement speed and provoke berserk fury.",
            "pants",
            "Dexterity",
            1.3,
            1.1,
            "C"
        ))

        equipments.append(Equipment(
            "Berserker Boots",
            "Boots that increase agility and feed the wearer’s rage on impact.",
            "boots",
            "Dexterity",
            1.3,
            1.1,
            "C"
        ))


        ######## Other ########
        

        equipments.append(Equipment(
            "Knight's Armor",
            "Heavy armor worn by knights, offering high defense and stability.",
            "body", 
            "Tank",
            1.5,
            0.7,
            "C"
        ))

        equipments.append(Equipment(
            "Spectral Boots",
            "Boots crafted from the essence of shadows. They grant enhanced evasion and a bonus to stealth.",
            "boots",
            "Evasion",
            1.3,
            1.3,
            "C"
        ))

        equipments.append(Equipment(
            "Steelfoot Pants",
            "Heavy pants made from steel that increase physical defense and movement speed.",
            "pants",
            "Tank",
            3.0,
            0,
            "C"
        ))

        equipments.append(Equipment(
            "Windward Body Armor",
            "A body armor that boosts evasion and agility, perfect for swift fighters.",
            "body",
            "Evasion",
            1.7,
            0.7,
            "C"
        ))

        equipments.append(Equipment(
            "Giant's Helmet",
            "A massive helmet that greatly increases strength and durability.",
            "helmet",
            "Tank",
            1.5,
            0.8,
            "C"
        ))

        
        equipments.append(Equipment(
            "Darksteel Body Armor",
            "A body armor made from darksteel, offering immense protection but reducing speed.",
            "body",
            "Tank",
            1.4,
            1.2,
            "C"
        ))

        equipments.append(Equipment(
            "Ironboots",
            "Boots made from iron, providing solid defense and increased resistance to damage.",
            "boots",
            "Tank",
            2,
            0.8,
            "C"
        ))

        equipments.append(Equipment(
            "Hardened Leather Body Armor",
            "Light armor made from hardened leather, boosting evasion and critical hit chance.",
            "body",
            "Evasion",
            1.4,
            1.3,
            "C"
        ))

        equipments.append(Equipment(
            "Elderhelm",
            "An ancient helmet that grants wisdom and protects against magical attacks.",
            "helmet",
            "Magic",
            1.7,
            0.8,
            "C"
        ))

        ########
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # B CLASS
        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Swiftstride Hood",
            "A lightweight hood that enhances agility and sharpens reflexes.",
            "helmet",
            "Evasion",
            2.5,
            1.5,
            "B"
        ))

        equipments.append(Equipment(
            "Swiftstride Armor",
            "Armor designed for speed, granting increased evasion and movement.",
            "body",
            "Evasion",
            2.5,
            1.5,
            "B"
        ))

        equipments.append(Equipment(
            "Swiftstride Leggings",
            "Flexible leggings that improve quickness and dodge capabilities.",
            "pants",
            "Evasion",
            2.5,
            1.5,
            "B"
        ))

        equipments.append(Equipment(
            "Swiftstride Boots",
            "Boots that increase movement speed and evasion, perfect for agile warriors.",
            "boots",
            "Evasion",
            2.5,
            1.5,
            "B"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Helm of the Fallen King",
            "A regal helmet that enhances strength and grants resistance to critical hits.",
            "helmet",
            "Tank",
            2.7,
            1.4,
            "B"
        ))

        equipments.append(Equipment(
            "Armor of the Fallen King",
            "A chestplate that embodies the resilience and might of a fallen monarch.",
            "body",
            "Tank",
            2.7,
            1.4,
            "B"
        ))

        equipments.append(Equipment(
            "Legplates of the Fallen King",
            "Leg armor that fortifies and empowers the wearer with royal strength.",
            "pants",
            "Tank",
            2.7,
            1.4,
            "B"
        ))

        equipments.append(Equipment(
            "Boots of the Fallen King",
            "Boots that ground the wearer with unmatched stability and endurance.",
            "boots",
            "Tank",
            2.7,
            1.4,
            "B"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Dragonbone Helm",
            "A helm forged from ancient dragon bones, providing exceptional defense and fire resistance.",
            "helmet",
            "Shield",
            4.0,
            0,
            "B"
        ))

        equipments.append(Equipment(
            "Dragonbone Armor",
            "A body armor crafted from the bones of ancient dragons, offering massive defense and fire resistance.",
            "body",
            "Shield",
            4.0,
            0,
            "B"
        ))

        equipments.append(Equipment(
            "Dragonbone Greaves",
            "Leg armor that protects with the strength and heat resistance of dragon bones.",
            "pants",
            "Shield",
            4.0,
            0,
            "B"
        ))

        equipments.append(Equipment(
            "Dragonbone Boots",
            "Boots that shield the wearer from intense heat while providing sturdy footing.",
            "boots",
            "Shield",
            4.0,
            0,
            "B"
        ))


        ######## FULL GEAR ########        
        equipments.append(Equipment(
            "Celestial Crown",
            "An ethereal crown that enhances wisdom and provides protection against elemental magic.",
            "helmet",
            "Magic",
            3,
            1.5,
            "B"
        ))

        equipments.append(Equipment(
            "Celestial Mantle",
            "A radiant mantle woven from stardust, increasing critical damage and mana regeneration.",
            "body",
            "Magic",
            3,
            1.5,
            "B"
        ))

        equipments.append(Equipment(
            "Celestial Leggings",
            "Leggings that shimmer with astral light, boosting critical hit chance and damage.",
            "pants",
            "Magic",
            3,
            1.5,
            "B"
        ))

        equipments.append(Equipment(
            "Celestial Greaves",
            "Greaves that grant swift movement and enhance critical strike efficiency.",
            "boots",
            "Magic",
            3,
            1.5,
            "B"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Valkyrie Helm",
            "A lightweight helm adorned with feathers, boosting agility and reflexes.",
            "helmet",
            "Dexterity",
            2.2,
            2.2,
            "B"
        ))

        equipments.append(Equipment(
            "Valkyrie Armor",
            "Armor made from the feathers of Valkyries, offering extreme agility and dexterity.",
            "body",
            "Dexterity",
            2.2,
            2.2,
            "B"
        ))

        equipments.append(Equipment(
            "Valkyrie Leggings",
            "Flexible leggings that enhance movement speed and nimbleness.",
            "pants",
            "Dexterity",
            2.2,
            2.2,
            "B"
        ))

        equipments.append(Equipment(
            "Valkyrie Boots",
            "Boots designed for swift movement and graceful agility.",
            "boots",
            "Dexterity",
            2.2,
            2.2,
            "B"
        ))

        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Astral Hood",
            "A hood infused with starlight, enhancing critical precision and focus.",
            "helmet",
            "Critical",
            2.5,
            2.0,
            "B"
        ))

        equipments.append(Equipment(
            "Astral Robe",
            "A flowing robe charged with cosmic energy, increasing critical damage.",
            "body",
            "Critical",
            2.5,
            2.0,
            "B"
        ))

        equipments.append(Equipment(
            "Astral Pants",
            "Pants imbued with cosmic energy, boosting critical hit chance and damage.",
            "pants",
            "Critical",
            2.5,
            2.0,
            "B"
        ))

        equipments.append(Equipment(
            "Astral Boots",
            "Boots that enhance movement and critical strike capabilities.",
            "boots",
            "Critical",
            2.5,
            2.0,
            "B"
        ))

        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Viperstrike Helm",
            "A helmet that sharpens the wearer’s strikes and fortifies their resolve.",
            "helmet",
            "Strength",
            2.4,
            2.2,
            "B"
        ))

        equipments.append(Equipment(
            "Viperstrike Chestplate",
            "A chestplate that boosts raw power and deadly precision.",
            "body",
            "Strength",
            2.4,
            2.2,
            "B"
        ))

        equipments.append(Equipment(
            "Viperstrike Legguards",
            "Leg armor that enhances movement strength and lethal force.",
            "pants",
            "Strength",
            2.4,
            2.2,
            "B"
        ))

        equipments.append(Equipment(
            "Viperstrike Boots",
            "Boots that enhance strength and damage.",
            "boots",
            "Strength",
            2.4,
            2.2,
            "B"
        ))


        ######## Other ########

        equipments.append(Equipment(
            "Celestial Chestplate",
            "A chestplate blessed by the gods, offering extraordinary defense and holy resistance.",
            "body",
            "Tank",
            2.7,
            2.5,
            "B"
        ))

        equipments.append(Equipment(
            "Windrider Helm",
            "A helmet that grants enhanced agility and grants a chance to dodge attacks.",
            "helmet",
            "Evasion",
            2.5,
            2.5,
            "B"
        ))

        equipments.append(Equipment(
            "Armageddon Boots",
            "Boots that imbue the wearer with fiery speed, boosting movement speed and fire resistance.",
            "boots",
            "Tank",
            2.8,
            1.9,
            "B"
        ))

        equipments.append(Equipment(
            "Phantom Lurker Pants",
            "Pants woven from the fabric of shadows, increasing evasion and granting stealth.",
            "pants",
            "Evasion",
            2.9,
            1.8,
            "B"
        ))

        equipments.append(Equipment(
            "Revenant Helm",
            "A helm forged from the remains of a powerful revenant. It increases health and provides a shield upon death.",
            "helmet",
            "Tank",
            3.0,
            2.0,
            "B"
        ))

        equipments.append(Equipment(
            "Frostguard Armor",
            "An icy armor that greatly boosts defense against frost and grants immunity to freezing effects.",
            "body",
            "Tank",
            2.8,
            2.3,
            "B"
        ))

        equipments.append(Equipment(
            "Shroud of the Wraith",
            "A body armor that enhances evasion and allows the wearer to move through walls for short periods.",
            "body",
            "Evasion",
            2.7,
            2.0,
            "B"
        ))

        ########

        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # A CLASS

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Emberstorm Helm",
            "A helm forged in volcanic flames, boosting fire resistance and endurance.",
            "helmet",
            "Tank",
            4.2,
            2.2,
            "A"
        ))

        equipments.append(Equipment(
            "Emberstorm Chestplate",
            "Chest armor imbued with molten power, granting supreme fire resistance.",
            "body",
            "Tank",
            4.2,
            2.2,
            "A"
        ))

        equipments.append(Equipment(
            "Emberstorm Legplates",
            "Leg armor that protects against extreme heat and enhances durability.",
            "pants",
            "Tank",
            4.2,
            2.2,
            "A"
        ))

        equipments.append(Equipment(
            "Emberstorm Boots",
            "Boots made from the essence of a volcanic eruption, increasing fire resistance and speed.",
            "boots",
            "Tank",
            4.2,
            2.2,
            "A"
        ))
        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Hellfire Helm",
            "A helm infused with molten lava, providing strong defense and fire damage reflection.",
            "helmet",
            "Shield",
            4.4,
            2.0,
            "A"
        ))

        equipments.append(Equipment(
            "Hellfire Plate",
            "A chestplate crafted from molten lava, offering high defense and fire damage reflection.",
            "body",
            "Shield",
            4.4,
            2.0,
            "A"
        ))

        equipments.append(Equipment(
            "Hellfire Greaves",
            "Leg armor that reflects heat and shields against physical attacks.",
            "pants",
            "Shield",
            4.4,
            2.0,
            "A"
        ))

        equipments.append(Equipment(
            "Hellfire Boots",
            "Boots that provide solid footing and reflect fiery damage back at attackers.",
            "boots",
            "Shield",
            4.4,
            2.0,
            "A"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Wraith's Hood",
            "A hood woven from spectral threads, enhancing evasion and ghostly agility.",
            "helmet",
            "Evasion",
            3.5,
            3.0,
            "A"
        ))

        equipments.append(Equipment(
            "Wraith's Garb",
            "A body armor made of spectral material, boosting evasion and reducing incoming damage.",
            "body",
            "Evasion",
            3.5,
            3.0,
            "A"
        ))

        equipments.append(Equipment(
            "Wraith's Leggings",
            "Leggings that grant swift, ghost-like movements and damage mitigation.",
            "pants",
            "Evasion",
            3.5,
            3.0,
            "A"
        ))

        equipments.append(Equipment(
            "Wraith's Boots",
            "Boots that let the wearer slip through danger with ease and resilience.",
            "boots",
            "Evasion",
            3.5,
            3.0,
            "A"
        ))

        
        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Hood of the Abyss",
            "A dark hood that enhances magical resistance and critical strike potency.",
            "helmet",
            "Magic",
            3.3,
            3.3,
            "A"
        ))

        equipments.append(Equipment(
            "Cloak of the Abyss",
            "A dark cloak that greatly increases magical resistance and increases critical hit damage.",
            "body",
            "Magic",
            3.3,
            3.3,
            "A"
        ))

        equipments.append(Equipment(
            "Leggings of the Abyss",
            "Legwear imbued with abyssal magic, boosting magic defense and critical power.",
            "pants",
            "Magic",
            3.3,
            3.3,
            "A"
        ))

        equipments.append(Equipment(
            "Galoshes of the Abyss",
            "Boots that grant swift movement and enhanced magical resistance.",
            "boots",
            "Magic",
            3.3,
            3.3,
            "A"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Shadowveil Hood",
            "A mysterious hood that channels dark power to boost strength and magical resistance.",
            "helmet",
            "Strength",
            4.5,
            2.8,
            "A"
        ))

        equipments.append(Equipment(
            "Shadowveil Mantle",
            "A mysterious mantle that channels dark power to greatly increase your strength, bolster magical resistance, and amplify critical hit damage.",
            "body",
            "Strength",
            4.5,
            2.8,
            "A"
        ))

        equipments.append(Equipment(
            "Shadowveil Legguards",
            "Legguards that enhance strength and protect against magical attacks.",
            "pants",
            "Strength",
            4.5,
            2.8,
            "A"
        ))

        equipments.append(Equipment(
            "Shadowveil Boots",
            "Boots that empower strength and provide magical resistance.",
            "boots",
            "Strength",
            4.5,
            2.8,
            "A"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Swiftstrike Hood",
            "A dark hood that sharpens agility and precision, boosting dexterity and magical resistance.",
            "helmet",
            "Dexterity",
            3.5,
            3.3,
            "A"
        ))
        
        equipments.append(Equipment(
            "Swiftstrike Raiment",
            "A dark cloak that enhances your agility and precision, greatly increasing dexterity, while also boosting magical resistance and critical hit damage.",
            "body",
            "Dexterity",
            3.5,
            3.3,
            "A"
        ))

        equipments.append(Equipment(
            "Swiftstrike Leggings",
            "Leggings that increase dexterity and protect against magical assaults.",
            "pants",
            "Dexterity",
            3.5,
            3.3,
            "A"
        ))

        equipments.append(Equipment(
            "Swiftstrike Boots",
            "Boots designed for swift movement and enhanced precision.",
            "boots",
            "Dexterity",
            3.5,
            3.3,
            "A"
        ))

        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Razorwind Hood",
            "A dark hood that sharpens instincts and boosts critical strike power with magical resistance.",
            "helmet",
            "Critical",
            4.0,
            3.2,
            "A"
        ))

        equipments.append(Equipment(
            "Razorwind Shroud",
            "A dark cloak that sharpens your instincts and amplifies your critical strike power, greatly increasing critical damage while providing strong magical resistance.",
            "body",
            "Critical",
            4.0,
            3.2,
            "A"
        ))

        equipments.append(Equipment(
            "Razorwind Leggings",
            "Leggings that amplify critical damage and offer magical defense.",
            "pants",
            "Critical",
            4.0,
            3.2,
            "A"
        ))

        equipments.append(Equipment(
            "Razorwind Boots",
            "Boots designed to increase agility and critical strike damage.",
            "boots",
            "Critical",
            4.0,
            3.2,
            "A"
        ))


        ######## Other ########

        equipments.append(Equipment(
            "Shadowstep Pants",
            "Pants that enhance dexterity and improve evasive maneuvers.",
            "pants",
            "Dexterity",
            3.5,
            3.0,
            "A"
        ))

        equipments.append(Equipment(
            "Tornado Runner Boots",
            "Light boots that increase movement speed and dexterity.",
            "boots",
            "Dexterity",
            3.7,
            3.2,
            "A"
        ))

        equipments.append(Equipment(
            "Phantom Cloak",
            "A body armor that increases critical damage and magical resistance.",
            "body",
            "Critical",
            4.2,
            2.3,
            "A"
        ))

        equipments.append(Equipment(
            "Eagle’s Gaze Helm",
            "Helmet that enhances dexterity and precision in battle.",
            "helmet",
            "Dexterity",
            3.6,
            3.1,
            "A"
        ))

        equipments.append(Equipment(
            "Swiftstrike Pants",
            "Pants that boost critical hit chance and speed.",
            "pants",
            "Critical",
            3.9,
            2.8,
            "A"
        ))

        equipments.append(Equipment(
            "Shadowblade Boots",
            "Boots that enhance dexterity and allow for swift, silent movement.",
            "boots",
            "Dexterity",
            3.5,
            3.3,
            "A"
        ))

        equipments.append(Equipment(
            "Nightfall Helm",
            "Helmet that increases critical damage and sharpens focus.",
            "helmet",
            "Critical",
            4.1,
            2.6,
            "A"
        ))

        equipments.append(Equipment(
            "Ghostwalker Body Armor",
            "Body armor that improves dexterity and grants enhanced agility.",
            "body",
            "Dexterity",
            3.7,
            3.4,
            "A"
        ))

        equipments.append(Equipment(
            "Aegis Sentinel Helm",
            "A sturdy helmet that greatly increases defense and magical resistance.",
            "helmet",
            "Tank",
            5.0,
            1.0,
            "A"
        ))

        equipments.append(Equipment(
            "Bulwark Boots",
            "Heavy boots that improve endurance and reduce damage taken.",
            "boots",
            "Tank",
            4.8,
            1.3,
            "A"
        ))

        equipments.append(Equipment(
            "Mystic Wardrobe",
            "Body armor that enhances magical power and boosts mana regeneration.",
            "body",
            "Magic",
            3.5,
            4.0,
            "A"
        ))

        equipments.append(Equipment(
            "Arcane Veil Pants",
            "Pants that increase magic defense and spellcasting speed.",
            "pants",
            "Magic",
            3.2,
            3.8,
            "A"
        ))

        equipments.append(Equipment(
            "Fortress Guard Helm",
            "Helmet that improves physical defense and grants shield bonuses.",
            "helmet",
            "Shield",
            4.5,
            1.5,
            "A"
        ))

        equipments.append(Equipment(
            "Guardian’s Step Boots",
            "Boots that increase resistance to knockback and boost stamina.",
            "boots",
            "Shield",
            4.9,
            1.1,
            "A"
        ))

        equipments.append(Equipment(
            "Enchanter’s Robes",
            "Body armor that greatly enhances spell power and magical resistance.",
            "body",
            "Magic",
            4.0,
            2.0,
            "A"
        ))

        equipments.append(Equipment(
            "Ironclad Pants",
            "Durable pants that boost physical defense and health regeneration.",
            "pants",
            "Tank",
            4.9,
            1.4,
            "A"
        ))

        equipments.append(Equipment(
            "Shieldbearer’s Helm",
            "Helmet that improves shield durability and grants increased block chance.",
            "helmet",
            "Shield",
            4.6,
            1.6,
            "A"
        ))

        equipments.append(Equipment(
            "Spellweaver Boots",
            "Boots that enhance magic speed and increase mana regeneration.",
            "boots",
            "Magic",
            3.3,
            3.1,
            "A"
        ))


        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
        # S CLASS


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Guardian's Helmet",
            "A helmet worn by ancient guardians, boosting vitality and providing a shield that absorbs damage.",
            "helmet",
            "Tank",
            6.5,
            6.2,
            "S"
        ))

        equipments.append(Equipment(
            "Guardian's Armor",
            "Body armor of ancient guardians, offering unmatched protection and vitality.",
            "body",
            "Tank",
            6.5,
            6.2,
            "S"
        ))

        equipments.append(Equipment(
            "Guardian's Greaves",
            "Pants forged for ancient guardians, providing resilience and damage absorption.",
            "pants",
            "Tank",
            6.5,
            6.2,
            "S"
        ))

        equipments.append(Equipment(
            "Guardian's Boots",
            "Boots worn by ancient guardians, offering stability, durability, and defense.",
            "boots",
            "Tank",
            6.5,
            6.2,
            "S"
        ))



        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Crown of the Eternal Emperor",
            "A crown forged from the celestial essence of an eternal emperor, boosting strength, defense, and resilience.",
            "helmet",
            "Shield",
            8.0,
            4.5,
            "S"
        ))

        equipments.append(Equipment(
            "Armor of the Eternal Emperor",
            "Armor blessed by the eternal emperor, offering unparalleled protection and resilience.",
            "body",
            "Shield",
            8.0,
            4.5,
            "S"
        ))

        equipments.append(Equipment(
            "Greaves of the Eternal Emperor",
            "Greaves forged from celestial essence, providing unmatched defense and stamina.",
            "pants",
            "Shield",
            8.0,
            4.5,
            "S"
        ))

        equipments.append(Equipment(
            "Boots of the Eternal Emperor",
            "Boots that grant steadfast strength and resilience, worthy of an eternal ruler.",
            "boots",
            "Shield",
            8.0,
            4.5,
            "S"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Hood of Shadows",
            "A hood imbued with the powers of shadows, enhancing stealth, evasion, and awareness in the dark.",
            "helmet",
            "Evasion",
            7.5,
            5.5,
            "S"
        ))

        equipments.append(Equipment(
            "Veil of Shadows",
            "A cloak imbued with the powers of shadows, increasing stealth, evasion, and damage output in the dark.",
            "body",
            "Evasion",
            7.5,
            5.5,
            "S"
        ))

        equipments.append(Equipment(
            "Leggings of Shadows",
            "Leg armor infused with shadow magic, granting swift movements and evasive maneuvers.",
            "pants",
            "Evasion",
            7.5,
            5.5,
            "S"
        ))

        equipments.append(Equipment(
            "Boots of Shadows",
            "Boots that allow the wearer to move silently and dodge with ease in darkness.",
            "boots",
            "Evasion",
            7.5,
            5.5,
            "S"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Vortex Helm",
            "A legendary helmet that maximizes critical strike damage and sharpens reflexes.",
            "helmet",
            "Critical",
            8.5,
            4.5,
            "S"
        ))

        equipments.append(Equipment(
            "Vortex Armor",
            "Body armor designed for masters of precision, greatly enhancing critical strike damage and speed.",
            "body",
            "Critical",
            8.5,
            4.5,
            "S"
        ))

        equipments.append(Equipment(
            "Vortex Greaves",
            "Pants forged for deadly marksmen, increasing agility, precision, and critical damage.",
            "pants",
            "Critical",
            8.5,
            4.5,
            "S"
        ))

        equipments.append(Equipment(
            "Vortex Boots",
            "Boots that boost movement speed and reflexes, enabling devastating critical strikes.",
            "boots",
            "Critical",
            8.5,
            4.5,
            "S"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Arcane Sovereign Crown",
            "A crown infused with pure arcane power, enhancing magical strength and focus.",
            "helmet",
            "Magic",
            7.8,
            5.8,
            "S"
        ))

        equipments.append(Equipment(
            "Arcane Sovereign Robe",
            "Body armor pulsing with pure magic, vastly increasing spell power and mana regeneration.",
            "body",
            "Magic",
            7.8,
            5.8,
            "S"
        ))

        equipments.append(Equipment(
            "Arcane Sovereign Leggings",
            "Pants woven with threads of raw magic, improving mana flow and magical potency.",
            "pants",
            "Magic",
            7.8,
            5.8,
            "S"
        ))

        equipments.append(Equipment(
            "Arcane Sovereign Boots",
            "Boots that increase movement speed and channel magical energy with each step.",
            "boots",
            "Magic",
            7.8,
            5.8,
            "S"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Titan’s Helm",
            "A massive helm that significantly boosts strength and physical damage output.",
            "helmet",
            "Strength",
            6.5,
            6.5,
            "S"
        ))

        equipments.append(Equipment(
            "Titan’s Plate",
            "Body armor forged for unmatched warriors, greatly boosting strength and physical power.",
            "body",
            "Strength",
            6.5,
            6.5,
            "S"
        ))

        equipments.append(Equipment(
            "Titan’s Greaves",
            "Heavy pants built for unstoppable fighters, increasing strength and endurance.",
            "pants",
            "Strength",
            6.5,
            6.5,
            "S"
        ))

        equipments.append(Equipment(
            "Titan’s Boots",
            "Boots that grant unshakable stability and power, enhancing strength and striking force.",
            "boots",
            "Strength",
            6.5,
            6.5,
            "S"
        ))


        ######## FULL GEAR ########
        equipments.append(Equipment(
            "Shadowstrike Helm",
            "A helm crafted for swift warriors, boosting dexterity, reaction speed, and precision.",
            "helmet",
            "Dexterity",
            7.4,
            5.1,
            "S"
        ))

        equipments.append(Equipment(
            "Shadowstrike Armor",
            "Body armor designed to heighten dexterity and precision, granting swift and deadly attacks.",
            "body",
            "Dexterity",
            7.4,
            5.1,
            "S"
        ))

        equipments.append(Equipment(
            "Shadowstrike Legguards",
            "Lightweight pants enhancing agility, precision, and flawless movement.",
            "pants",
            "Dexterity",
            7.4,
            5.1,
            "S"
        ))

        equipments.append(Equipment(
            "Shadowstrike Boots",
            "Boots built for lightning-fast movement, boosting dexterity and precision with every step.",
            "boots",
            "Dexterity",
            7.4,
            5.1,
            "S"
        ))



        ######## Other ########

        equipments.append(Equipment(
            "Eclipse Boots",
            "Boots imbued with shadow energy that greatly boost critical hit chance and movement speed.",
            "boots",
            "Critical",
            7.2,
            5.3,
            "S"
        ))

        equipments.append(Equipment(
            "Celestial Pants",
            "Pants woven from starlight that enhance magical defense and casting speed.",
            "pants",
            "Magic",
            6.5,
            6.2,
            "S"
        ))

        equipments.append(Equipment(
            "Berserker’s Boots",
            "Boots that grant unmatched power and increase critical hit damage for strength-based warriors.",
            "boots",
            "Strength",
            7.3,
            5.2,
            "S"
        ))

        
        equipments.append(Equipment(
            "Windblade Pants",
            "Light pants that increase dexterity and critical hit chance with unparalleled agility.",
            "pants",
            "Dexterity",
            6.5,
            6.0,
            "S"
        ))

        equipments.append(Equipment(
            "Phantom Helm",
            "A helmet that blends magic and critical precision, amplifying spell crit damage significantly.",
            "helmet",
            "Critical",
            10,
            4.1,
            "S"
        ))

        equipments.append(Equipment(
            "Sorcerer’s Step Boots",
            "Boots that boost magical speed and critical damage, favored by the most skilled mages.",
            "boots",
            "Magic",
            10,
            8,
            "S"
        ))

        myWeapons.append(next(w for w in weapons if w.weapon_id == 15))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 0))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 1))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 2))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 3))
        myEquipments.append(next(e for e in equipments if e.equipment_id == 4))
        return 