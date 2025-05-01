from mechanics import *


def main():
    # perhaps let player choose grid size: 4x4, 5x5, or 6x6
    # for now it'll stay 4x4
    # Set size and build a grid
    grid_size = 4
    grid = build_grid(grid_size)

    # Spawn 2 random elements on the grid
    spawn_random_el(grid)
    spawn_random_el(grid)


    for row in grid:
        print(row)

    


if __name__ == "__main__":
    main()