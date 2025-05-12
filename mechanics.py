from random import choice, choices
    

class Slot:
    """Representation of a grid cell.
    
    Could contain only `None` and integers that are divisible by 2.
    `None` means an empty slot.
    """
    def __init__(self):
        self._value: int|None = None
    
    def __str__(self) -> str:
        return f"{self.value}"
    
    def __repr__(self) -> str:
        """Helps with easier grid printing to CLI."""
        return self.__str__()

    @property
    def value(self) -> int|None:
        return self._value

    @value.setter
    def value(self, new_value: int):
        self._value = new_value

    def clean(self):
        """Set value of the slot to `None`."""
        self.value = None
    
    def spawn(self):
        """Spawn `2` or `4` with 90% and 10% chance respectively."""
        if self.value is None:
            self.value = choices((2, 4), (90, 10))[0]

    def move(self, el: "Slot"):
        """Compare two elements and stack them only if the current one is
        not empty and provided element is empty (0) has the same value.

        Stacking means that the provided element will change its value and
        the current one will be cleared if conditions are met.
        """
        if self.value is not None:
            if el.value is None:
                el.value = self.value
                self.clean()

    def stack(self, el: "Slot"):
        """Compare two elements and stack them only if the current one is
        not empty and provided element is empty (0) has the same value.

        Stacking means that the provided element will change its value and
        the current one will be cleared if conditions are met.
        """
        if self.value is not None:
            if self.value == el.value:
                el.value *= 2
                self.clean()
            else:
                self.move(el)


class Grid:
    """A playing deck representation. Consists of equal slots number
    horizontally and vertically.

    Supported operations:

    • get size of the grid;

    • get current grid;

    • spawn random element (2 or 4);

    • move to left/right/down/up
    """
    def __init__(self, size: int, previous: list[list[Slot]]|None = None):
        self._size: int = size
        if previous is None:
            self._grid: list[list[Slot]] = self.__build_grid()
            # New grid requires to spawn 2 elements
            self.spawn_random_el()
            self.spawn_random_el()
        else:
            self._grid: list[list[Slot]] = previous

    def __str__(self) -> str:
        """A string representation of the grid that is useful for CLI mode.
        """
        return f"\n{"-" * (self.size*2)}\n".join(
            "|".join(str(row).strip("[]").replace("None", ' ').split(", "))
            for row in self.current
    )


    def __build_grid(self) -> list[list[Slot]]:
        """Build and return a grid (matrix) filled with `0`."""
        grid: list[list[Slot]] = []
        for _ in range(self.size):
            grid.append([Slot() for _ in range(self.size)])

        return grid


    @property
    def size(self) -> int:
        """Return a size of the grid."""
        return self._size


    @property
    def current(self) -> list[list[Slot]]:
        """Return the current grid."""
        return self._grid


    def spawn_random_el(self):
        """Choose a random row from ones with empty spaces and
        spawn there `2` with 90% chance or `4` with 10% chance
        """
        rows_with_free_slots: list[int] = [
            idx for idx, row in enumerate(self.current)
            if any(el.value is None for el in row)
        ]
        row_id_to_spawn_into: int = choice(rows_with_free_slots)
        empty_spaces: list[int] = [
            idx for idx, el in enumerate(self.current[row_id_to_spawn_into]) if el.value is None
        ]
        chosen_place_id: int = choice(empty_spaces)
        self.current[row_id_to_spawn_into][chosen_place_id].spawn()  # change the value of the slot


    def move_left(self):
        """Move elements to their respective most left empty slots
        and stack with their respective left neighbors if they are equal.
        """
        for row in self.current:
            # move elements
            farthest_empty: int|None = None
            for idx in range(len(row)):
                if not row[idx].value:
                    if farthest_empty is None:
                        farthest_empty = idx
                else:
                    if farthest_empty is not None:
                        row[idx].move(row[farthest_empty])
                        farthest_empty = farthest_empty + 1
            # stack elements
            for idx in range(len(row)):
                if row[idx].value is not None:
                    if idx - 1 >= 0:
                        row[idx].stack(row[idx-1])

    def move_right(self):
        """Move elements to their respective most right empty slots
        and stack with their respective right neighbors if they are equal.
        """
        for row in self.current:
            # move elements
            farthest_empty: int|None = None
            for idx in range(len(row)-1, -1, -1):
                if not row[idx].value:
                    if farthest_empty is None:
                        farthest_empty = idx
                else:
                    if farthest_empty is not None:
                        row[idx].move(row[farthest_empty])
                        farthest_empty = farthest_empty - 1
            # stack elements
            for idx in range(len(row)-1, -1, -1):
                if row[idx].value is not None:
                    if idx + 1 < len(row):
                        row[idx].stack(row[idx+1])

    def move_down(self):
        """Move elements to their respective most bottom empty slots
        and stack with their respective bottom neighbors if they are equal.
        """
        for slot_id in range(len(self.current)):
            # move elements
            farthest_empty: int|None = None
            for row_id in range(len(self.current)-1,-1,-1):
                if not self.current[row_id][slot_id].value:
                    if farthest_empty is None:
                        farthest_empty = row_id
                else:
                    if farthest_empty is not None:
                        self.current[row_id][slot_id].move(self.current[farthest_empty][slot_id])
                        farthest_empty = farthest_empty - 1
            # stack elements
            for row_id in range(len(self.current)-1,-1,-1):
                if self.current[row_id][slot_id].value is not None:
                    if row_id + 1 < len(self.current[row_id]):
                        self.current[row_id][slot_id].stack(
                            self.current[row_id+1][slot_id]
                        )

    def move_up(self):
        """Move elements to their respective most top empty slots
        and stack with their respective top neighbors if they are equal.
        """
        for slot_id in range(len(self.current)):
            # move elements
            farthest_empty: int|None = None
            for row_id in range(len(self.current)):
                if not self.current[row_id][slot_id].value:
                    if farthest_empty is None:
                        farthest_empty = row_id
                else:
                    if farthest_empty is not None:
                        self.current[row_id][slot_id].move(self.current[farthest_empty][slot_id])
                        farthest_empty = farthest_empty + 1
            # stack elements
            for row_id in range(len(self.current)):
                if self.current[row_id][slot_id].value is not None:
                    if row_id - 1 >= 0:
                        self.current[row_id][slot_id].stack(
                            self.current[row_id-1][slot_id]
                        )


class History:
    """A list of the player's last 3 moves (grids).

    Available actions:

    • get a number of saved moves,

    • clean too old moves (when there are more than 3 saved ones),

    • save the current move (and automatically delete too old one),

    • undo the latest move
    """
    def __init__(self):
        self.__previous_3_moves: list[Grid] = []
    
    def __clean_too_old(self):
        """Delete the oldest saved move if the length of saved moves
        is greater than 3.
        """
        if self.length > 3:
            del self.__previous_3_moves[0]


    @property
    def length(self) -> int:
        """Return the number of saved moves."""
        return len(self.__previous_3_moves)
    
    def save_move(self, grid: Grid):
        """Save the last move and remove the oldest one from the history
        if there are more than 3 saved moves (including the current one).
        """
        self.__previous_3_moves.append(grid)
        self.__clean_too_old()

    def undo_move(self) -> Grid:
        """Delete the latest move and return the previous one."""
        return self.__previous_3_moves.pop()

    def get_latest(self) -> Grid:
        """Return the previous move."""
        if self.length > 0:
            return self.__previous_3_moves[-1]

    def compare(self, grid: Grid) -> bool:
        """Compare string representations of the current and previous grids.
        It's useful to prevent spawns if all the elements are near the edge
        and yet still is recorded movement towards that edge.
        """
        if self.length > 0:
            return str(self.get_latest().current) == str(grid.current)

        return False