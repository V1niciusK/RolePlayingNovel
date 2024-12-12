class CharParams:
    """ ## Parameters as a whole
    There are six parameters (stats): str, dex, agi, vit, int, luk
### Strength
        *More meat!*
 - Sheer brute force
 - Required for contact attacks (blunt or cutting weapons, fistfighting)
 - Increases inventory capacity
 - Increases damage delt by contact attacks
 - Increases archer range

### Dexterity
        *Hit me with your best shot*
 - Ability to hit the target
 - Required for ranged attacks (archers, clerics and mages)
 - Reduces misses in contact attacks (swordsman)
 - Increases damage dealt to a certain point to all attacks
 - Increases inventory capacity to a certain point

### Agility
        *Gotta go fast*
 - Useful in general for all types of attacks (increases attack rate)
 - Reduce stamina consumed by contact attacks
 - Increases chances of evading an attack

### Vitality
        *So heal me up when its all over*
 - Increases the amount of damage a character can take before fainting (10% health) or dying (0% health)
 - Increases inventory capacity to a lesser extent than str, but higher than dex and int
 - Increases effectiveness of food, potions and healing

### Intelligence
        *Required to eat without stabbing your eye with a fork*
 - Required for mages (increases their damage dealt)
 - Required for clerics (increases their healing amount)
 - Increases storage capacity to a lesser extent
 - Will help with story

### Luck
        *Winner winner chicken dinner*
 - Useful in general for all attacks (increases the chance of critical)
 - Increases attack rate to a lesser extent
 - Increses evade rate
 - Reduces chances of missing
    """
    def __init__(self, strength=0, dexterity=0, agility=0, vitality=0, intelligence=0, luck=0):
        self.strength = strength
        self.dexterity = dexterity
        self.agility = agility
        self.vitality = vitality
        self.intelligence = intelligence
        self.luck = luck
    
    def lvlstr(xp: int):
        lvlstr += xp
    
    def lvldex(xp: int):
        lvldex += xp
    
    def lvlagi(xp: int):
        lvlagi += xp
    
    def lvlvit(xp: int):
        lvlvit += xp
    
    def lvlint(xp: int):
        lvlint += xp
    
    def lvlluk(xp: int):
        lvlluk += xp


class Character:
    def __init__(self, name: str, job: str, params: CharParams):
        self.name = name
        self.job = job
        self.params = params
        self.level = 1
        self.location = "Port Prospect"
        self.body = {
            "head": "",
            "left_hand": "",
            "right_hand": "",
            "torso": "",
            "waist": "",
            "legs": ""            
        }
    def getCharStats(self) -> None:
        print(f'''
┌─────────────── ...
│
│  {self.name.upper()} (lvl {self.level})
│  ――――――――――
│  Job: {self.job}
│
└───────────────...
              ''')

class Player(Character):
    def __init__(self, name, job, params):
        super().__init__(name, job, params)
        pass