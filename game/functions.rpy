default my_protectors_map = {}
default protectors_base_information = {}
default allMissions = []
define config.console = True
default allMissionTemplates = []

init python:
    import os
    import json


    if 'my_protectors_map' not in globals():
        my_protectors_map = {}

    if 'protectors_base_information' not in globals():
        protectors_base_information = {}
    
    if 'allMissions' not in globals():
        allMissions = []

    if 'allMissionTemplates' not in globals():
        allMissionTemplates = []
    
    dynamic_backgrounds = {}

    missionsListSize = 51
    maxDifficulty = 200
    maxNeededDaysToFinish = 5
    maxDisapearingInThisDays = 10

    background_folder = "images/bg"
    valid_extensions = [".png", ".jpg", ".jpeg", ".webp"]

    # creating basic multipliers for stat
    health_size = 30
    damage_size = 3
    atack_speed_size = 1
    xp_starter_size = 10
    xp_size = 20

    # multiplier per level
    level_factor_health = 0.05
    level_factor_damage = 0.05
    increasing_per_level_multiplier_xp = 0.5

    # multiplier per stage
    stage_factor_health = 1.5
    stage_factor_damage = 1.5
    increasing_per_stage_multiplier_xp = 10
    
    # showing disabled options
    config.menu_include_disabled = False

    folder_path = "game\images\protectors"
    full_path = os.path.join(config.basedir, folder_path)
    folder_map = {}

    # Scan and define backgrounds
    for f in renpy.list_files():
        if f.startswith(background_folder + "/") and any(f.endswith(ext) for ext in valid_extensions):
            name = f[len(background_folder) + 1:].rsplit(".", 1)[0]  # Extract filename without folder or extension
            tag_name = "bg " + name  # Prefix the image name with "bg"
            dynamic_backgrounds[name] = tag_name
            renpy.image(tag_name, f)  # Define as a Ren'Py image

    if os.path.isdir(full_path):
        for name in os.listdir(full_path):
            subfolder_path = os.path.join(full_path, name)
            if os.path.isdir(subfolder_path):
                relative_path = os.path.join(folder_path, name).replace("\\", "/")
                folder_map[name] = "/".join(relative_path.split("/")[1:])

    def getImage(path):
        for ext in valid_extensions:
            if renpy.loadable(path + ext):
                return path + ext
        return None

    def set_background(name):
        if name in dynamic_backgrounds:
            tag = dynamic_backgrounds[name]
            
            # Show the background and apply the matrix transformation for night mode
            renpy.scene()
            renpy.show(tag, at_list=[stretch_fullscreen])
        
        else:
            renpy.say("System", f"Background '{name}' not found.")

    def get_folder_from_map(key):
        global folder_map
        """
        Retrieves the path associated with a folder name (key) from the map.
        """
        return folder_map.get(key, None)

    def add_new_protector(protector_name, stage = 1, level = 1):
        global my_protectors_map
        my_protectors_map[protector_name] = Protector(protector_name, capitalize_first_letter(protector_name), stage, level, "Available")
        return

    def get_count_of_my_protectors():
        global my_protectors_map
        # Parse JSON to Python dictionary
        return len(my_protectors_map)

    def capitalize_first_letter(s):
        if not s:
            return s  # return empty string as is
        return s[0].upper() + s[1:]

    def update_menu_disable_options(value):
        config.menu_include_disabled = value

    def updating_wallet(incoming_money):
        global money
        money = money + incoming_money
        return

    def initializing_things():
        # creating protectors    
        protectors_base_information["ninja"] = BaseProtectorData(0.7, 1, 1.3)
        protectors_base_information["recruit"] = BaseProtectorData(1.1, 0.8, 1.1)
        protectors_base_information["robot"] = BaseProtectorData(1.5, 0.75, 0.75)
        protectors_base_information["samurai"] = BaseProtectorData(1.25, 1.25, 0.5)
        protectors_base_information["skeleton"] = BaseProtectorData(0.5, 1.5, 1)
        protectors_base_information["templar"] = BaseProtectorData(1.5, 1.2, 0.3)

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
        allMissions.append(Mission("Training", "Send a protector to train in your facilities.", 0, 1, 1, "Training", "not assigned", 1900, 0))

        for missionNumber in range(len(allMissions), missionsListSize, 1):
            randomNumber = renpy.random.randint(1, maxDifficulty)
            neededDaysToFinish = renpy.random.randint(1, maxNeededDaysToFinish)
            disapearingInThisDays = renpy.random.randint(1, maxDisapearingInThisDays)
            randomMission = renpy.random.randint(1, len(allMissionTemplates) - 1)
            mission = allMissionTemplates[randomMission]
            allMissions.append(
                Mission(
                    mission.title,
                    mission.description,
                    randomNumber,
                    neededDaysToFinish,
                    disapearingInThisDays,
                    mission.mission_type
                )
            )
        return 

    def testing_things():
        # global allMissions
        # for mission in allMissions:
        #     renpy.say(None, str(mission.title))
        return