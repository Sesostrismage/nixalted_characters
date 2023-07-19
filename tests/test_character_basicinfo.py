from pathlib import Path
import sys


# Add top-level directory to path for imports.
sys.path.append(str(Path(__file__).parent.parent))

from character import BasicInfo


def test_get_character_name():
    d = {
        "character_name": "Test Character",
        "player_name": "Test Player",
    }
    basic_info = BasicInfo(d)
    assert basic_info.get_player_name() == "Test Player"


def test_set_character_name():
    d = {
        "character_name": "Test Character",
        "player_name": "Test Player",
    }
    basic_info = BasicInfo(d)
    basic_info.set_character_name("Jane Doe")
    assert basic_info.get_character_name() == "Jane Doe"


def test_get_player_name():
    d = {
        "character_name": "Test Character",
        "player_name": "Test Player",
    }
    basic_info = BasicInfo(d)
    assert basic_info.get_player_name() == "Test Player"


def test_set_player_name():
    d = {
        "character_name": "Test Character",
        "player_name": "Test Player",
    }
    basic_info = BasicInfo(d)
    basic_info.set_player_name("Player 2")
    assert basic_info.get_player_name() == "Player 2"
