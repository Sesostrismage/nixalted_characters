from pathlib import Path


def get_test_char_path(char_num: int) -> Path:
    base_dir = Path(__file__).parent
    char_dir = base_dir / "char_examples"
    return char_dir / f"test_char_{char_num}.json"
