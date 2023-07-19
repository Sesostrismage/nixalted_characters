from pathlib import Path
import pytest
import sys

import utilities as u

# Add top-level directory to path for imports.
sys.path.append(str(Path(__file__).parent.parent))

from character import Name


def test_get_name():
    name_dict = {
        "name": "The Hacker",
        "defining_aspect": "Hacking",
        "aspects": ["Sense", "Infiltration", "Close Combat"],
    }
    name = Name(name_dict)
    assert name.get_name() == "The Hacker"


def test_set_name():
    name_dict = {
        "name": "The Hacker",
        "defining_aspect": "Hacking",
        "aspects": ["Sense", "Infiltration", "Close Combat"],
    }
    name = Name(name_dict)
    name.set_name("The Soldier")
    assert name.get_name() == "The Soldier"


def test_get_defining_aspect():
    name_dict = {
        "name": "The Hacker",
        "defining_aspect": "Hacking",
        "aspects": ["Sense", "Infiltration", "Close Combat"],
    }
    name = Name(name_dict)
    assert name.get_defining_aspect() == "Hacking"


def test_set_defining_aspect():
    name_dict = {
        "name": "The Hacker",
        "defining_aspect": "Hacking",
        "aspects": ["Sense", "Infiltration", "Close Combat"],
    }
    name = Name(name_dict)
    name.set_defining_aspect("Running")
    assert name.get_defining_aspect() == "Running"


def test_set_defining_aspect_already_aspect():
    name_dict = {
        "name": "The Hacker",
        "defining_aspect": "Hacking",
        "aspects": ["Sense", "Infiltration", "Close Combat"],
    }
    name = Name(name_dict)
    name.set_defining_aspect("Sense")
    assert name.get_defining_aspect() == "Sense"
    assert "Sense" not in name.get_aspects()


def test_add_aspect():
    name_dict = {
        "name": "The Hacker",
        "defining_aspect": "Hacking",
        "aspects": ["Sense", "Infiltration", "Close Combat"],
    }
    name = Name(name_dict)
    name.add_aspect("Running")
    assert "Running" in name.get_aspects()


def test_add_aspect_already_aspect():
    name_dict = {
        "name": "The Hacker",
        "defining_aspect": "Hacking",
        "aspects": ["Sense", "Infiltration", "Close Combat"],
    }
    name = Name(name_dict)
    with pytest.raises(KeyError):
        name.add_aspect("Sense")


def test_add_aspect_already_defining_aspect():
    name_dict = {
        "name": "The Hacker",
        "defining_aspect": "Hacking",
        "aspects": ["Sense", "Infiltration", "Close Combat"],
    }
    name = Name(name_dict)
    with pytest.raises(KeyError):
        name.add_aspect("Hacking")


def test_remove_aspect():
    name_dict = {
        "name": "The Hacker",
        "defining_aspect": "Hacking",
        "aspects": ["Sense", "Infiltration", "Close Combat"],
    }
    name = Name(name_dict)
    name.remove_aspect("Sense")
    assert "Sense" not in name.get_aspects()
