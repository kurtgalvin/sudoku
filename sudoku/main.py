


class Board(object):
    def __init__(self, *rows):
        assert len(rows) == 9, f"got {len(rows)} rows, must be 9"
        for n, row in enumerate(rows):
            assert isinstance(row, list), f"row must be {type([])}, got type {type(row)}"
            assert len(row) == 9, f"row {n} has {len(row)} columns, must be 9"

    @classmethod
    def create(self):
        # TODO
        pass