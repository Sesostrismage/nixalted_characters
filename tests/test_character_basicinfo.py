from pathlib import Path
import sys

import utilities as u

# Add top-level directory to path for imports.
sys.path.append(str(Path(__file__).parent.parent))

from character import BasicInfo


# Tests for the BasicInfo class.
def test_get_character_name():
    basic_info = BasicInfo(u.get_basic_info_dict())
    assert basic_info.get_player_name() == "Test Player"


def test_set_character_name():
    basic_info = BasicInfo(u.get_basic_info_dict())
    basic_info.set_character_name("Jane Doe")
    assert basic_info.get_character_name() == "Jane Doe"


def test_get_player_name():
    basic_info = BasicInfo(u.get_basic_info_dict())
    assert basic_info.get_player_name() == "Test Player"


def test_set_player_name():
    basic_info = BasicInfo(u.get_basic_info_dict())
    basic_info.set_player_name("Player 2")
    assert basic_info.get_player_name() == "Player 2"
