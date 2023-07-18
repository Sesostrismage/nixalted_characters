from pathlib import Path
import sys

from utilities import get_test_char_path

# Add top-level directory to path for imports.
sys.path.append(str(Path(__file__).parent.parent))

from character import Character


def test_character_init():
    _ = Character(get_test_char_path(1))


def test_abilities_get_ability_names():
    char = Character(get_test_char_path(1))
    ability_name_list = char.abilities.get_ability_names()
    assert isinstance(ability_name_list, list)
    assert ability_name_list[0] == "athletics"


def test_abilities_get_ability_score():
    char = Character(get_test_char_path(1))
    ability_score = char.abilities.get_ability_score("athletics")
    assert isinstance(ability_score, int)
    assert ability_score == 4


def test_abilities_set_ability_score():
    char = Character(get_test_char_path(1))
    char.abilities.set_ability_score("athletics", 5)
    ability_score = char.abilities.get_ability_score("athletics")
    assert ability_score == 5


def test_abilities_calc_xp_ability_single():
    char = Character(get_test_char_path(1))
    xp = char.abilities.calc_xp_ability_single("athletics")
    assert xp == 10


def test_abilities_calc_xp_abilities_all():
    char = Character(get_test_char_path(1))
    xp = char.abilities.calc_xp_abilities_all()
    assert xp == 125
