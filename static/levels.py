"""
Job system works like so:
There are four jobs: swordsman, archer, mage, cleric.
There are a fifth job: homeless.
Upon level up each job has its parameters (stats) changed by different amounts
"""
from .classes.character import CharParams, Character

def levelUp(character: Character) -> CharParams:
    char_params = character.params
    evolvl = character.job // 10
    if evolvl >= 100:
        evolvl = 10
    evotable = db_levelup[evolvl]
    char_params.lvlstr(evotable["str"][evolvl])
    char_params.lvldex(evotable["dex"][evolvl])
    char_params.lvlagi(evotable["agi"][evolvl])
    char_params.lvlvit(evotable["vit"][evolvl])
    char_params.lvlint(evotable["int"][evolvl])
    char_params.lvlluk(evotable["luk"][evolvl])
    

db_levelup = {
    """ ## How the levelup database works
Data is stored in a dict. Its structure is: { "class"."param".[evo_list] }
We store not the data related to every level, but the deltas to be gained every 10 levels.
take this param evolution: "str": [1,5,11,14]
Until the character is level 10 (non-inclusive) each level up increses str by 1.
After that, before it is level 20 each level up increses str by 5.
So on, and so forth.
    """
    "swordsman": {
        "str": [ 4, 9,14,19,24,30,36,41,47,55],
        "dex": [ 3, 6, 9,12,16,20,24,28,33,38],
        "agi": [ 1, 2, 3, 5, 8,13,21,34,55,89],
        "vit": [ 5,10,15,20,26,32,38,45,56,90],
        "int": [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10],
        "luk": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        },
    "archer": {
        "str": [ 1, 2, 3, 5, 8,13,21,34,55,89],
        "dex": [ 4, 9,14,19,24,30,36,41,47,55],
        "agi": [ 3, 6, 9,12,16,20,24,28,33,38],
        "vit": [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10],
        "int": [ 5, 4, 6, 5, 7, 6, 8, 7, 9,10],
        "luk": [ 5,10,15,20,26,32,38,45,56,90]
        },
    "mage": {
        "str": [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10],
        "dex": [ 3, 6, 9,12,16,20,24,28,33,38],
        "agi": [ 4, 9,14,19,24,30,36,41,47,55],
        "vit": [ 1, 2, 3, 5, 8,13,21,34,55,89],
        "int": [ 5,10,15,20,26,32,38,45,56,90],
        "luk": [ 5, 4, 6, 5, 7, 6, 8, 7, 9,10]
        },
    "cleric": {
        "str": [ 4, 9,14,19,24,30,36,41,47,55],
        "dex": [ 3, 6, 9,12,16,20,24,28,33,38],
        "agi": [ 5, 4, 6, 5, 7, 6, 8, 7, 9,10],
        "vit": [ 5,10,15,20,26,32,38,45,56,90],
        "int": [ 1, 2, 3, 5, 8,13,21,34,55,89],
        "luk": [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    }
    
}