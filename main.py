"""Move all archives from a user's "Download/Mods" folder to MO2's download folder for a given instance"""

# Imports
import os # Used to get the names of files in directories (listdir)
import json # I know people don't like json but it does the job and is easy to work with
import shutil # Used for actually moving the files

class Main():
    def __init__(self):
        self.modDirectories = self.check_settings()
        self.check_empty_folder()

        self.game = self.get_game_input()
        self.move_mods()
        input("Press any key to exit")


    def check_settings(self):
        if "auto_move_settings.json" not in os.listdir():
            with open("auto_move_settings.json", "w") as f:
                default_settings = {
                    "downloadFolder": rf"{os.environ['UserProfile']}\Downloads\Mods",
                    "MO2Folder": rf"{os.environ['LocalAppData']}\ModOrganizer"
                }
                json.dump(default_settings, f, indent=2)
            
        print("No settings were detected for auto_move.exe, default settings created and loaded. \nYou can edit your settings in the 'auto_move_settings.json' file.")
        
        with open("auto_move_settings.json", "r") as f:
            return json.load(f)
    

    def get_game_input(self):
        """Query the user for the game the mods are for"""
        game = input("\nEnter the name of game that the mods are for: ").lower()
        game = ' '.join(elem.capitalize() for elem in game.split()) # Capitalize the first letter of each word.

        # Common abbreviations
        # TODO: Compare 'game' to a dictionary of a list of abbreviates as a key, and the game as a value
        # Ex. abbreviations = {["SkyrimSE", "Skryimse", "Skyrim Se"]: "Skyrim Special Edition"}
        if game == "Skryimse" or game == "Skryim Se" or game == "Skyrim SE":
            game = "Skyrim Special Edition"
        elif game == "Falloutnv" or game == "Fallout Nv" or game == "Fallout NV":
            game = "Fallout New Vegas"
        
        if game in os.listdir(self.modDirectories['MO2Folder']):
            return game
        else:
            print(f"It does not appear you have a MO2 instance of a game by the name of '{game}'.")
            self.get_game_input()
    

    def check_empty_folder(self):
        """Checks if the user's mod download folder is empty"""
        if os.listdir(self.modDirectories["downloadFolder"]) == []:
            print(f"\nIt does not appear that there are any files are in {self.modDirectories['downloadFolder']}. Continue [y/n]?")
            cont = input()
            if cont != "y":
                exit()
    

    def move_mods(self):
        EXTENSIONS = [".rar", ".zip", ".7z"]

        for file in os.listdir(self.modDirectories["downloadFolder"]):
            print(f"Currently Moving: {file}")
            for extension in EXTENSIONS:
                if file.endswith(extension):
                    shutil.move(rf"{self.modDirectories['downloadFolder']}\{file}", f"{self.modDirectories['MO2Folder']}\{self.game}\downloads")
        print(">> All archives moved! <<")


Main()