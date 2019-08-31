import time
from random import shuffle


class Board(object):
    def __init__(self, rows, full=True):
        self.rows = self._validate(rows, full=full)

    @staticmethod
    def _validate(rows, full=True):
        assert isinstance(rows, list), f"rows must be {type([])}"
        if full:
            assert len(rows) == 9, f"got {len(rows)} rows, must be 9"
        for n, row in enumerate(rows):
            assert isinstance(row, list), f"row must be {type([])}, got type {type(row)}"
            assert len(row) == 9, f"row {n} has {len(row)} columns, must be 9"
        return rows

    @classmethod
    def create(cls, rows=[], verbose=False):
        '''
        step 1: set up row to have no doubles
        Step 2: reject row for a column clash
        step 3: reject row for a 3x3 square clash
        '''
        rows = cls._validate(rows, full=False)
        TT = time.time()
        for _ in range(9-len(rows)):
            T = time.time()
            count = 0
            while True:
                pass_ = True
                count += 1

                # step 1:
                row = [1,2,3,4,5,6,7,8,9]
                shuffle(row)
                if row in rows:
                    continue

                # Step 2:
                for n, cell in enumerate(row):
                    for row_ in rows:
                        if row_[n] == cell:
                            pass_ = False
                            break
                    if not pass_:
                        break
                if not pass_:
                    continue

                # step 3:
                for n, cell in enumerate(row):
                    '''we have not yet appended the row we are 
                        currently assessing. 
                        eg: len(rows) == 2 we are currently assesing row 3
                    '''
                    if len(rows) < 3:
                        for row_ in rows:
                            if n < 3:
                                if cell in row_[:3]:
                                    pass_ = False
                                    break
                            elif n < 6:
                                if cell in row_[3:6]:
                                    pass_ = False
                                    break
                            elif n < 9:
                                if cell in row_[6:9]:
                                    pass_ = False
                                    break

                    elif len(rows) < 6:
                        for row_ in rows[3:]:
                            if n < 3:
                                if cell in row_[:3]:
                                    pass_ = False
                                    break
                            elif n < 6:
                                if cell in row_[3:6]:
                                    pass_ = False
                                    break
                            elif n < 9:
                                if cell in row_[6:9]:
                                    pass_ = False
                                    break

                    elif len(rows) < 9:
                        for row_ in rows[6:]:
                            if n < 3:
                                if cell in row_[:3]:
                                    pass_ = False
                                    break
                            elif n < 6:
                                if cell in row_[3:6]:
                                    pass_ = False
                                    break
                            elif n < 9:
                                if cell in row_[6:9]:
                                    pass_ = False
                                    break
                    if not pass_:
                        break
                
                if pass_:
                    rows.append(row)
                    if verbose:
                        print(f"passed: {row} time: {round(time.time() - T, 2)}s iterations: {count}")
                    break
        if verbose:
            print(f"done! total time: {round(time.time() - TT, 2)}s")
        return cls(rows, full=True)

    def __str__(self):
        return 'Board:' + ''.join([f"\n{i}" for i in self.rows])


if __name__ == '__main__':
    board = Board.create(verbose=True)
    print(board)