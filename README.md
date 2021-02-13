# MO2_Auto_Move
When manually installing a mod in MO2, the mod is installed and nothing else. However, I prefer to keep a backup of all the mods I install, and to do so, you have to move the mod to the downloads folder of MO2. Due to my laziness as a person, I decided to go ahead and make a simple script to handle it for me.

## How to use
When you first run the script it will create a file called `auto_move_settings.json`. This file contains both the default directiories for MO2 instances and the default downloads folder + a "Mods" subfolder. These directories can be customized to your wishes (must be done externally because I wanted the ability to just run the script, give the game name, and let it handle the rest).

## Updates
I do plan on adding some extra features to this script, the most useful one being the abbreviation check. As of now, I would have to have an if/elif statement for each game. I plan on changing this to looping over a dictionary that has a key of a list of names, and the key being the full name. ex. `{["Skyrimse", "Skyrim Se", "Skyrim SE"]: "Skyrim Special Edition"}`.
