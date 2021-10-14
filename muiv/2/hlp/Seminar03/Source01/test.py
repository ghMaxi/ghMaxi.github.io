import pprint

from main import start_new_game, bomb_matrix


def test_start_new_game():
    """Тест начала новой игры"""
    test_cases = (
        (1, 1, 1, None),
        (6, 8, 9, None),
        (6, 8, 49, None))
    for w, h, b, _ in test_cases:
        try:
            start_new_game(w, h, b)
        except ValueError:
            assert(b > w * h)
        pprint.pprint(bomb_matrix)


if __name__ == "__main__":
    test_start_new_game()
