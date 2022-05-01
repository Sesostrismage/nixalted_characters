import copy
import json


class Character:
    def __init__(self, load_path: str) -> None:
        with open(load_path, "r") as f:
            self.__char_dict = json.load(f)

    def get_basic_info(self):
        return copy.deepcopy(self.__char_dict["basic_info"])

    def set_character_name(self, char_name):
        self.__char_dict["basic_info"]["character_name"] = char_name

    def set_player_name(self, char_name):
        self.__char_dict["basic_info"]["player_name"] = char_name

    def get_name_info(self):
        return copy.deepcopy(self.__char_dict["name_info"])

    def set_role_name(self, role_name):
        self.__char_dict["name_info"]["role_name"] = role_name

    def set_defining_aspect(self, aspect):
        if aspect in self.__char_dict["name_info"]["aspects"]:
            self.remove_aspect(aspect)

        self.__char_dict["name_info"]["defining_aspect"] = aspect

    def add_aspect(self, aspect):
        if self.__char_dict["name_info"]["defining_aspect"] == aspect:
            raise KeyError(
                f"{aspect} is already a defining aspect. Set another defining aspect first"
            )

        self.__char_dict["name_info"]["aspects"] += aspect

    def remove_aspect(self, aspect):
        self.__char_dict["name_info"]["aspects"].pop(aspect)

    def get_xp(self) -> int:
        return copy.deepcopy(self.__char_dict["name_info"]["xp"])

    def set_xp(self, xp: int):
        self.__char_dict["name_info"]["xp"] = xp

    def calc_legend(self) -> int:
        pass

    def get_intimacies(self):
        return copy.deepcopy(self.__char_dict["intimacies"])

    def get_ability_names(self) -> list:
        return sorted(list(self.__char_dict["abilities"].keys()))

    def get_ability_score(self, ability_name) -> int:
        return self.__char_dict["abilities"][ability_name]

    def set_ability_score(self, ability_name, score):
        self.__char_dict["abilities"][ability_name] = score

    def calc_xp_ability_single(self, ability_name: str):
        score = self.get_ability_score(ability_name)
        xp = int(score * (score + 1) / 2)
        return xp

    def calc_xp_abilities_all(self):
        xp = 0

        for ability_name in self.get_ability_names():
            xp += self.calc_xp_ability_single(ability_name)

        return xp


legend_levels = {1: 100, 2: 150, 3: 250, 4: 500, 5: 1000}
