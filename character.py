import json

class Character:
    def __init__(self, load_path: str) -> None:
        with open(load_path, 'r') as f:
            self.char_dict = json.load(f)