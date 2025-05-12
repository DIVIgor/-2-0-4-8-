from copy import deepcopy

from mechanics import Grid, History


def main():
    # perhaps players should choose grid size: 4x4, 5x5, or 6x6
    # for now it'll stay 4x4
    # Set size and build a grid
    grid_size: int = 4
    grid: Grid = Grid(grid_size)
    prev_moves: History = History()

    while True:
        # print the current grid state to CLI
        print(grid, "="*20, sep="\n")
        # movement controls for CLI
        action = input("Your move: ")
        if action in "wasd":
            prev_moves.save_move(Grid(grid_size, deepcopy(grid.current)))
            match action:
                case "a":
                    grid.move_left()
                case "d":
                    grid.move_right()
                case "s":
                    grid.move_down()
                case "w":
                    grid.move_up()
                case _:
                    break
            if not prev_moves.compare(grid):
                grid.spawn_random_el()
        elif action == "u":
            if prev_moves.length > 0:
                    grid = prev_moves.undo_move()
        else:
            break


if __name__ == "__main__":
    main()