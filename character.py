import copy
import json


class Character:
    def __init__(self, load_path: str = None) -> None:
        if load_path is None:
            char_dict = copy.deepcopy(new_char_dict)

        else:
            with open(load_path, "r") as f:
                char_dict = json.load(f)

        self.basic_info = BasicInfo(char_dict["basic_info"])
        self.name = Name(char_dict["name_info"])
        self._xp_earned = char_dict["xp_earned"]
        self.intimacies = Intimacies(char_dict["intimacies"])
        self.backgrounds = Backgrounds(char_dict["backgrounds"])
        self.abilities = Abilities(char_dict["abilities"])
        self.powers = Powers(char_dict["powers"])

    def get_xp_earned(self):
        return copy.deepcopy(self._xp_earned)

    def set_xp_earned(self, xp: int):
        self._xp_earned = xp

    def get_legend_level(self):
        xp_earned = self.get_xp_earned()
        legend_level = 0

        for level in sorted(legend_levels.keys()):
            if xp_earned >= legend_levels[level]:
                legend_level = level
            else:
                break

        return legend_level


class BasicInfo:
    def __init__(self, basic_info_dict: dict) -> None:
        self._basic_info_dict = basic_info_dict

    def get_basic_info(self):
        return copy.deepcopy(self._basic_info_dict)

    def set_character_name(self, char_name):
        self._basic_info_dict["character_name"] = char_name

    def set_player_name(self, char_name):
        self._basic_info_dict["player_name"] = char_name


class Name:
    def __init__(self, name_dict: dict) -> None:
        self._name_dict = name_dict

    def get_name_info(self):
        return copy.deepcopy(self._name_dict)

    def set_name(self, name: str):
        self._name_dict["name"] = name

    def set_defining_aspect(self, aspect):
        if aspect in self._name_dict["aspects"]:
            self.remove_aspect(aspect)

        self._name_dict["defining_aspect"] = aspect

    def add_aspect(self, aspect):
        if self._name_dict["defining_aspect"] == aspect:
            raise KeyError(
                f"{aspect} is already a defining aspect. Set another defining aspect first."
            )

        self._name_dict["aspects"] += aspect

    def remove_aspect(self, aspect):
        self._name_dict["aspects"].pop(aspect)

    def get_xp_earned(self) -> int:
        return copy.deepcopy(self._name_dict["xp_earned"])

    def set_xp_earned(self, xp: int):
        self._name_dict["xp_earned"] = xp

    def calc_legend(self) -> int:
        for legend_level in sorted(legend_levels.keys()):
            if self.get_xp_earned() < legend_levels[legend_level]:
                break

        return legend_level - 1


class Intimacies:
    def __init__(self, intimacy_list: list) -> None:
        self._intimacy_list = intimacy_list

    def get_intimacies(self):
        return copy.deepcopy(self._intimacy_list)

    def add_intimacy(self, description: str, strength: str):
        strength_list = ["minor", "major", "defining"]

        if strength not in strength_list:
            raise KeyError(f"Strenght must be one of {strength_list}, got {strength}.")

        self._intimacy_list += {"strength": strength, "description": description}

    def edit_intimacy(self, idx: int, description: str, strength: str):
        strength_list = ["minor", "major", "defining"]

        if strength not in strength_list:
            raise KeyError(f"Strenght must be one of {strength_list}, got {strength}.")

        self._intimacy_list[idx] = {"strength": strength, "description": description}

    def remove_intimacy(self, idx):
        self._intimacy_list.pop(idx)


class Abilities:
    def __init__(self, abilities_dict: dict) -> None:
        self._abilities_dict = abilities_dict

    def get_ability_names(self) -> list:
        return sorted(list(self._abilities_dict.keys()))

    def get_ability_score(self, ability_name) -> int:
        return self._abilities_dict[ability_name]

    def set_ability_score(self, ability_name, score):
        check_ability_name(ability_name)
        self._abilities_dict[ability_name] = score

    def calc_xp_ability_single(self, ability_name: str):
        check_ability_name(ability_name)
        score = self.get_ability_score(ability_name)
        xp = int(score * (score + 1) / 2)
        return xp

    def calc_xp_abilities_all(self):
        xp = 0

        for ability_name in self.get_ability_names():
            xp += self.calc_xp_ability_single(ability_name)

        return xp


class Backgrounds:
    def __init__(self, backgrounds_list: list) -> None:
        self._backgrounds_list = backgrounds_list

    def get_backgrounds(self):
        return copy.deepcopy(self._backgrounds_list)

    def add_background(self, background_type: str, rank: int, details: str):
        self._backgrounds_list += {
            "background_type": background_type,
            "rank": rank,
            "details": details,
        }

    def edit_background(self, idx: int, background_type: str, rank: int, details: str):
        self._backgrounds_list[idx] = {
            "background_type": background_type,
            "rank": rank,
            "details": details,
        }

    def remove_background(self, idx):
        self._backgrounds_list.pop(idx)


class Powers:
    def __init__(self, powers_dict: dict) -> None:
        self._powers_dict = powers_dict

    def add_power(
        self,
        ability_name: str,
        aspect: str,
        name: str,
        base_power: str,
        level: int,
        drawback: str = None,
        amount: int = 0,
        volume: int = 0,
        range: int = 0,
        duration: int = 0,
        time: int = 0,
        mana_discount: int = 0,
    ):
        check_ability_name(ability_name)


def check_ability_name(ability_name: str):
    if ability_name not in new_char_dict["abilities"].keys():
        raise KeyError(f"{ability_name} is not a valid Ability name.")


legend_levels = {1: 100, 2: 150, 3: 250, 4: 500, 5: 1000}

new_char_dict = {
    "basic_info": {"character_name": "", "player_name": ""},
    "name_info": {
        "name": "",
        "defining_aspect": "",
        "aspects": [],
        "xp_earned": 150,
    },
    "intimacies": [],
    "abilities": {
        "athletics": 0,
        "awareness": 0,
        "bureaucracy": 0,
        "charisma": 0,
        "close_combat": 0,
        "craft": 0,
        "hacking": 0,
        "investigation": 0,
        "larceny": 0,
        "lore": 0,
        "medicine": 0,
        "occult": 0,
        "ranged_combat": 0,
        "socialize": 0,
        "stamina": 0,
        "stealth": 0,
        "strength": 0,
        "survival": 0,
        "travel": 0,
        "war": 0,
        "willpower": 0,
    },
    "attacks": [],
    "backgrounds": [],
    "powers": {},
}
