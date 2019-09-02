# sudoku
Sudoku Board Builder

## How to:
Get a full Sudoku board
```python
board = Board.create(verbose=True)
print(board) 
```
Example result with `verbose=True`:
```python
# passed: [2, 8, 6, 4, 1, 5, 9, 3, 7] time: 0.0s iterations: 1
# passed: [4, 7, 9, 2, 8, 3, 6, 5, 1] time: 0.0s iterations: 35
# passed: [3, 5, 1, 9, 7, 6, 2, 4, 8] time: 0.05s iterations: 2364
# passed: [6, 3, 4, 5, 9, 7, 1, 8, 2] time: 0.0s iterations: 45
# passed: [8, 1, 7, 3, 6, 2, 5, 9, 4] time: 0.0s iterations: 86
# passed: [5, 9, 2, 8, 4, 1, 3, 7, 6] time: 1.44s iterations: 85407
# passed: [7, 4, 3, 6, 2, 9, 8, 1, 5] time: 0.01s iterations: 374
# passed: [9, 2, 8, 1, 5, 4, 7, 6, 3] time: 4.88s iterations: 323673
# passed: [1, 6, 5, 7, 3, 8, 4, 2, 9] time: 1.31s iterations: 89834
# done! total time: 7.7s

# Board:
# [2, 8, 6, 4, 1, 5, 9, 3, 7]
# [4, 7, 9, 2, 8, 3, 6, 5, 1]
# [3, 5, 1, 9, 7, 6, 2, 4, 8]
# [6, 3, 4, 5, 9, 7, 1, 8, 2]
# [8, 1, 7, 3, 6, 2, 5, 9, 4]
# [5, 9, 2, 8, 4, 1, 3, 7, 6]
# [7, 4, 3, 6, 2, 9, 8, 1, 5]
# [9, 2, 8, 1, 5, 4, 7, 6, 3]
# [1, 6, 5, 7, 3, 8, 4, 2, 9]
```
