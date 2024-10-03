This project implements a maze solving algorithm using Breadth First Search (BFS).
It allows users to define a maze using a 2D matrix representation, 
where 0 represents a walkable path and 1 represents a wall. 
the used Algorithms converts the maze into a graph and computes the shortest path
from a Star_node to an End_node using BFS.

*********************************************************************************
The algorithmic Steps:

1.Convert a maze represented as a matrix into a graph.
2.Find the shortest path in the maze using BFS.
*********************************************************************************
how to use it?

1.Create a 2D list representing the maze 
 where 0 is a path and 1 is a wall.
         
 For example:
  maze_matrix= [
  [0, 0, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [1, 1, 1, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 1, 1, 0, 0]
]

2.Define the coordinates of the starting and ending nodes in the maze
  For example: start_node=(0,0) and end_node=(4,4)

3.run solve_maze.py to find the shortest path

4.The output will be the shortest path from the start_node to the end_node 
  as a list of tuppels(the tuppels represent the coordinations), 
  or None if no path exists.
  For example (from 1. the output Will be ) :
      Shortest path in the maze: 
  [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4)]
