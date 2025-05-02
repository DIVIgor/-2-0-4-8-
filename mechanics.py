from random import choice, choices


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
    row_id_to_spawn_into = choice(rows_with_free_slots)
    empty_spaces = [
        idx for idx, el in enumerate(grid[row_id_to_spawn_into]) if el == 0
    ]
    chosen_place_id = choice(empty_spaces)
    grid[row_id_to_spawn_into][chosen_place_id] = choices((2, 4), (90, 10))[0]


def move_left(grid: list[list[int]]):
    """Move elements to their respective most left empty slots."""
    for row in grid:
        last_not_empty_idx = -1
        for idx, el in enumerate(row):
            if el != 0:
                if idx - last_not_empty_idx > 1:
                    row[last_not_empty_idx+1] = el
                    row[idx] = 0
                last_not_empty_idx = idx


def move_up(grid: list[list[int]]):
    """Move elements to their respective most top empty slots."""
    # skip the first row since it shouldn't move
    for row_idx, row in enumerate(grid[1:], 1):
        for el_idx, el in enumerate(row):
            if el != 0:
                # find the highest one row that has empty slots for this idx
                # probably with while loop for row indexes > 0
                temp_row_idx = row_idx - 1
                highest_empty_idx = None
                while temp_row_idx >= 0:
                    if grid[temp_row_idx][el_idx] == 0:
                        highest_empty_idx = temp_row_idx
                    temp_row_idx -= 1

                # move element to an empty slot if any
                if highest_empty_idx is not None:
                    grid[highest_empty_idx][el_idx] = el
                    row[el_idx] = 0
