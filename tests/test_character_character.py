from pathlib import Path
import sys

import utilities as u

# Add top-level directory to path for imports.
sys.path.append(str(Path(__file__).parent.parent))

from character import Character


# Tests for the Character class.
def test_character_init():
    _ = Character(u.get_test_char_path(1))


def test_get_xp_earned():
    char = Character(u.get_test_char_path(1))
    assert char.get_xp_earned() == 150


def test_set_xp_earned():
    char = Character(u.get_test_char_path(1))
    char.set_xp_earned(100)
    assert char.get_xp_earned() == 100


def test_get_legend_level():
    char = Character(u.get_test_char_path(1))
    char.set_xp_earned(20)
    assert char.get_legend_level() == 1

    char.set_xp_earned(125)
    assert char.get_legend_level() == 2

    char.set_xp_earned(800)
    assert char.get_legend_level() == 5

    char.set_xp_earned(2000)
    assert char.get_legend_level() == 6
