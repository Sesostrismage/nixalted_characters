import os

from character import Character

test_dir = os.path.dirname(__file__)


def test_init():
    load_path = os.path.join(test_dir, "test_char_1.json")
    _ = Character(load_path)


def test_get_ability_names():
    load_path = os.path.join(test_dir, "test_char_1.json")
    char = Character(load_path)
    ability_name_list = char.get_ability_names()
    assert isinstance(ability_name_list, list)
    assert ability_name_list[0] == "athletics"


def test_get_ability_score():
    load_path = os.path.join(test_dir, "test_char_1.json")
    char = Character(load_path)
    ability_score = char.get_ability_score("athletics")
    assert isinstance(ability_score, int)
    assert ability_score == 4


def test_set_ability_score():
    load_path = os.path.join(test_dir, "test_char_1.json")
    char = Character(load_path)
    char.set_ability_score("athletics", 5)
    ability_score = char.get_ability_score("athletics")
    assert ability_score == 5


def test_calc_xp_ability_single():
    load_path = os.path.join(test_dir, "test_char_1.json")
    char = Character(load_path)
    xp = char.calc_xp_ability_single("athletics")
    assert xp == 10


def test_calc_xp_abilities_all():
    load_path = os.path.join(test_dir, "test_char_1.json")
    char = Character(load_path)
    xp = char.calc_xp_abilities_all()
    assert xp == 125
