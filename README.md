# 8-Puzzle-by-A-Star-Search
This python file solves 8 Puzzle using A* Search.<br>
<br><b>Current Status:</b> Currently, the solver prints all the possible steps it has explored leading to the answer. I am currently looking for a way to print only those steps that are relevant to the answer. Let me know if you have anything in mind.

## Execution Instructions
To run, use the following notation in command prompt:<br>
```
python Puzzle8Solver.py <heuristicChoice> <1 to 8 in any order with a _ in middle>
```
Example: <br>
```
python Puzzle8Solver.py 1 1 4 2 6 3 5 _ 7 8
```

## Heuristic [[Source](https://www.andrew.cmu.edu/course/15-121/labs/HW-7%20Slide%20Puzzle/lab.html)]
The code currently uses Manhattan Distance as the heuristic function.
The Manhattan distance heuristic is used for its simplicity and also because it is actually a pretty good underestimate (aka a lower bound) on the number of moves required to bring a given board to the solution board. We simply compute the sum of the distances of each tile from where it belongs, completely ignoring all the other tiles. For example, the Manhattan distance between the current state and goal state is 7:

<table>
<tr><th>Current State </th><th>Goal State</th></tr>
<tr><td>
  <table>
    <tr><td>2</td><td>1</td><td>3</td></tr>
    <tr><td>5</td><td>4</td><td>0</td></tr>
    <tr><td>6</td><td>7</td><td>8</td></tr>
  </table>
</td><td>
  <table>
    <tr><td>0</td><td>1</td><td>2</td></tr>
    <tr><td>3</td><td>4</td><td>5</td></tr>
    <tr><td>6</td><td>7</td><td>8</td></tr>
  </table>
</td></tr> </table>

Distance:
|1|2|3|4|5|6|7|8|
|-|-|-|-|-|-|-|-|
|0|2|3|0|2|0|0|0|

0+2+3+0+2+0+0+0 = 7

This is so, because the tile "1" is 0 move away, the tile "2" is 2 moves away, the tile "3" is 3 moves away, the tile "4" is 0 move away, the tile "5" is 2 moves away, the "6" tile is 0 move away, the "7" is 0 move away, and the "8" is 0 move away.

## References
- https://www.andrew.cmu.edu/course/15-121/labs/HW-7%20Slide%20Puzzle/lab.html
- https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288
