from pathlib import Path
import sys

import utilities as u

# Add top-level directory to path for imports.
sys.path.append(str(Path(__file__).parent.parent))

from character import Character


# Tests for the Character class.
def test_character_init():
    _ = Character(u.get_test_char_path(1))
