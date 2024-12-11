class Character:
    def __init__(self, name: str, race: str, params: dict):
        self.name = name
        self.race = race
        self.params = params
        self.location = "Port Prospect"
        self.inventory = {
            "left_hand": "",
            "right_hand": "",
            "torso": "",
            "waist": "",
            "legs": ""
            
        }