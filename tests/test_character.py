import os

from character import Character

base_dir = os.path.dirname(__file__)
char_dir = os.path.join(base_dir, "char_examples")


def test_character_init():
    load_path = os.path.join(char_dir, "test_char_1.json")
    _ = Character(load_path)


def test_abilities_get_ability_names():
    load_path = os.path.join(char_dir, "test_char_1.json")
    char = Character(load_path)
    ability_name_list = char.abilities.get_ability_names()
    assert isinstance(ability_name_list, list)
    assert ability_name_list[0] == "athletics"


def test_abilities_get_ability_score():
    load_path = os.path.join(char_dir, "test_char_1.json")
    char = Character(load_path)
    ability_score = char.abilities.get_ability_score("athletics")
    assert isinstance(ability_score, int)
    assert ability_score == 4


def test_abilities_set_ability_score():
    load_path = os.path.join(char_dir, "test_char_1.json")
    char = Character(load_path)
    char.abilities.set_ability_score("athletics", 5)
    ability_score = char.abilities.get_ability_score("athletics")
    assert ability_score == 5


def test_abilities_calc_xp_ability_single():
    load_path = os.path.join(char_dir, "test_char_1.json")
    char = Character(load_path)
    xp = char.abilities.calc_xp_ability_single("athletics")
    assert xp == 10


def test_abilities_calc_xp_abilities_all():
    load_path = os.path.join(char_dir, "test_char_1.json")
    char = Character(load_path)
    xp = char.abilities.calc_xp_abilities_all()
    assert xp == 125
