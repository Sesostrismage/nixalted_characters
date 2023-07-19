from pathlib import Path
import sys

import utilities as u

# Add top-level directory to path for imports.
sys.path.append(str(Path(__file__).parent.parent))

from character import Abilities, load_char_dict


def test_abilities_get_ability_names():
    char_dict = load_char_dict(u.get_test_char_path(1))
    abilities = Abilities(char_dict["abilities"])
    ability_name_list = abilities.get_ability_names()
    assert isinstance(ability_name_list, list)
    assert ability_name_list[0] == "athletics"


def test_abilities_get_ability_score():
    char_dict = load_char_dict(u.get_test_char_path(1))
    abilities = Abilities(char_dict["abilities"])
    ability_score = abilities.get_ability_score("athletics")
    assert isinstance(ability_score, int)
    assert ability_score == 4


def test_abilities_set_ability_score():
    char_dict = load_char_dict(u.get_test_char_path(1))
    abilities = Abilities(char_dict["abilities"])
    abilities.set_ability_score("athletics", 5)
    ability_score = abilities.get_ability_score("athletics")
    assert ability_score == 5


def test_abilities_calc_xp_ability_single():
    char_dict = load_char_dict(u.get_test_char_path(1))
    abilities = Abilities(char_dict["abilities"])
    xp = abilities.calc_xp_ability_single("athletics")
    assert xp == 10


def test_abilities_calc_xp_abilities_all():
    char_dict = load_char_dict(u.get_test_char_path(1))
    abilities = Abilities(char_dict["abilities"])
    xp = abilities.calc_xp_abilities_all()
    assert xp == 125
