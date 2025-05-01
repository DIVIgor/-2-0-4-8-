import random


def build_grid(grid_size: int) -> list[list[int]]:
    """Build and return a grid (matrix) filled with `0`"""
    grid = []
    for _ in range(grid_size):
        grid.append([0 for _ in range(grid_size)])

    return grid


def spawn_random_el(grid: list[list[int]]):
    """Choose a random row from ones with empty spaces and
    spawn there `2` with 90% chance or `4` with 10% chance
    """
    # TO CHECK:
    # perhaps it would be better to change the inputted grid in place
    # instead of returning a new one
    rows_with_free_slots = [idx for idx, row in enumerate(grid) if 0 in row]
    row_id_to_spawn_into = random.choice(rows_with_free_slots)
    empty_spaces = [
        idx for idx, el in enumerate(grid[row_id_to_spawn_into]) if el == 0
    ]
    chosen_place_id = random.choice(empty_spaces)
    grid[row_id_to_spawn_into][chosen_place_id] = random.choices((2, 4), (90, 10))[0]
