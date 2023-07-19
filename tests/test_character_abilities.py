from pathlib import Path
import sys

# Add top-level directory to path for imports.
sys.path.append(str(Path(__file__).parent.parent))

from character import Abilities


def test_abilities_get_ability_names():
    abilities_dict = {
        "athletics": 4,
        "awareness": 4,
        "bureaucracy": 0,
        "charisma": 0,
        "close_combat": 5,
        "craft": 0,
        "hacking": 7,
        "investigation": 0,
        "larceny": 4,
        "lore": 0,
        "medicine": 0,
        "occult": 0,
        "ranged_combat": 4,
        "socialize": 0,
        "stamina": 2,
        "stealth": 6,
        "strength": 2,
        "survival": 0,
        "travel": 0,
        "war": 0,
        "willpower": 5,
    }
    abilities = Abilities(abilities_dict)
    ability_name_list = abilities.get_ability_names()
    assert isinstance(ability_name_list, list)
    assert ability_name_list[0] == "athletics"


def test_abilities_get_ability_score():
    abilities_dict = {
        "athletics": 4,
        "awareness": 4,
        "bureaucracy": 0,
        "charisma": 0,
        "close_combat": 5,
        "craft": 0,
        "hacking": 7,
        "investigation": 0,
        "larceny": 4,
        "lore": 0,
        "medicine": 0,
        "occult": 0,
        "ranged_combat": 4,
        "socialize": 0,
        "stamina": 2,
        "stealth": 6,
        "strength": 2,
        "survival": 0,
        "travel": 0,
        "war": 0,
        "willpower": 5,
    }
    abilities = Abilities(abilities_dict)
    ability_score = abilities.get_ability_score("athletics")
    assert isinstance(ability_score, int)
    assert ability_score == 4


def test_abilities_set_ability_score():
    abilities_dict = {
        "athletics": 4,
        "awareness": 4,
        "bureaucracy": 0,
        "charisma": 0,
        "close_combat": 5,
        "craft": 0,
        "hacking": 7,
        "investigation": 0,
        "larceny": 4,
        "lore": 0,
        "medicine": 0,
        "occult": 0,
        "ranged_combat": 4,
        "socialize": 0,
        "stamina": 2,
        "stealth": 6,
        "strength": 2,
        "survival": 0,
        "travel": 0,
        "war": 0,
        "willpower": 5,
    }
    abilities = Abilities(abilities_dict)
    abilities.set_ability_score("athletics", 5)
    ability_score = abilities.get_ability_score("athletics")
    assert ability_score == 5


def test_abilities_calc_xp_ability_single():
    abilities_dict = {
        "athletics": 4,
        "awareness": 4,
        "bureaucracy": 0,
        "charisma": 0,
        "close_combat": 5,
        "craft": 0,
        "hacking": 7,
        "investigation": 0,
        "larceny": 4,
        "lore": 0,
        "medicine": 0,
        "occult": 0,
        "ranged_combat": 4,
        "socialize": 0,
        "stamina": 2,
        "stealth": 6,
        "strength": 2,
        "survival": 0,
        "travel": 0,
        "war": 0,
        "willpower": 5,
    }
    abilities = Abilities(abilities_dict)
    xp = abilities.calc_xp_ability_single("athletics")
    assert xp == 10


def test_abilities_calc_xp_abilities_all():
    abilities_dict = {
        "athletics": 4,
        "awareness": 4,
        "bureaucracy": 0,
        "charisma": 0,
        "close_combat": 5,
        "craft": 0,
        "hacking": 7,
        "investigation": 0,
        "larceny": 4,
        "lore": 0,
        "medicine": 0,
        "occult": 0,
        "ranged_combat": 4,
        "socialize": 0,
        "stamina": 2,
        "stealth": 6,
        "strength": 2,
        "survival": 0,
        "travel": 0,
        "war": 0,
        "willpower": 5,
    }
    abilities = Abilities(abilities_dict)
    xp = abilities.calc_xp_abilities_all()
    assert xp == 125
