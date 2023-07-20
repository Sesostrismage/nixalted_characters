import sys
from pathlib import Path
import pytest

# Add top-level directory to path for imports.
sys.path.append(str(Path(__file__).parent.parent))

from character import Intimacies


def test_get_intimacies():
    intimacies = Intimacies(
        [
            {"strength": "minor", "description": "Family"},
            {"strength": "major", "description": "Revenge"},
        ]
    )
    assert intimacies.get_intimacies() == [
        {"strength": "minor", "description": "Family"},
        {"strength": "major", "description": "Revenge"},
    ]


def test_add_intimacy():
    intimacies = Intimacies([{"strength": "minor", "description": "Family"}])
    intimacies.add_intimacy("major", "Honor")
    assert intimacies.get_intimacies() == [
        {"strength": "minor", "description": "Family"},
        {"strength": "major", "description": "Honor"},
    ]


def test_add_intimacy_with_invalid_strength():
    intimacies = Intimacies([{"strength": "minor", "description": "Family"}])
    with pytest.raises(KeyError) as e:
        intimacies.add_intimacy("invalid", "Honor")
        assert (
            str(e)
            == "Intimacy strength must be one of ['minor', 'major', 'defining'], got invalid."
        )


def test_get_intimacy_idx():
    intimacies = Intimacies(
        [
            {"strength": "minor", "description": "Family"},
            {"strength": "major", "description": "Revenge"},
        ]
    )

    idx = intimacies.get_intimacy_idx("major", "Revenge")
    assert idx == 1


def test_get_intimacy_idx_with_invalid_strength():
    intimacies = Intimacies([{"strength": "minor", "description": "Family"}])
    with pytest.raises(KeyError) as e:
        intimacies.get_intimacy_idx("invalid", "Family")
        assert str(e) == (
            "Intimacy strength must be one of ['minor', 'major', 'defining'], got invalid."
        )


def test_get_intimacy_idx_with_invalid_description():
    intimacies = Intimacies([{"strength": "minor", "description": "Family"}])
    with pytest.raises(KeyError) as e:
        intimacies.get_intimacy_idx("major", "Family")
        assert str(e) == "Intimacy (major): 'Family' not found."


def test_edit_intimacy_description_only():
    intimacies = Intimacies(
        [
            {"strength": "minor", "description": "Family"},
            {"strength": "major", "description": "Revenge"},
        ]
    )
    intimacies.edit_intimacy(1, "minor", "Revenge")
    assert intimacies.get_intimacies() == [
        {"strength": "minor", "description": "Family"},
        {"strength": "minor", "description": "Revenge"},
    ]


def test_edit_intimacy_strength_only():
    intimacies = Intimacies(
        [
            {"strength": "minor", "description": "Family"},
            {"strength": "major", "description": "Revenge"},
        ]
    )
    intimacies.edit_intimacy(1, "defining", "Revenge")
    assert intimacies.get_intimacies() == [
        {"strength": "minor", "description": "Family"},
        {"strength": "defining", "description": "Revenge"},
    ]


def test_edit_intimacy_description_and_strength():
    intimacies = Intimacies(
        [
            {"strength": "minor", "description": "Family"},
            {"strength": "major", "description": "Revenge"},
        ]
    )
    intimacies.edit_intimacy(1, "defining", "Justice")
    assert intimacies.get_intimacies() == [
        {"strength": "minor", "description": "Family"},
        {"strength": "defining", "description": "Justice"},
    ]


def test_edit_intimacy_with_invalid_strength():
    intimacies = Intimacies(
        [
            {"strength": "minor", "description": "Family"},
            {"strength": "major", "description": "Revenge"},
        ]
    )
    with pytest.raises(KeyError) as e:
        intimacies.edit_intimacy(1, "invalid", "Justice")
        assert str(e) == (
            "Intimacy strength must be one of ['minor', 'major', 'defining'], "
            "got invalid."
        )


def test_remove_intimacy():
    intimacies = Intimacies(
        [
            {"strength": "minor", "description": "Family"},
            {"strength": "major", "description": "Revenge"},
        ]
    )
    intimacies.remove_intimacy(0)
    assert intimacies.get_intimacies() == [
        {"strength": "major", "description": "Revenge"}
    ]


def test_remove_intimacy_with_invalid_index():
    intimacies = Intimacies(
        [
            {"strength": "minor", "description": "Family"},
            {"strength": "major", "description": "Revenge"},
        ]
    )
    with pytest.raises(IndexError) as e:
        intimacies.remove_intimacy(2)
        assert str(e) == "list index out of range"
