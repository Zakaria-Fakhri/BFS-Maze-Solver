from BFS_shortest_path import bfs
from maze_into_graph import maze_to_graph

def solve_maze(maze_as_matrix, start_node, end_node):
    """
    This function solves a maze by converting the maze matrix into a graph 
    and then finding the shortest path from the start to the end using BFS.

    Parameters:
    maze_as_matrix (list of lists): A 2D maze matrix where:
                                    - 0 represents a walkable path
                                    - 1 represents a wall
                                    
                                    Example:
                                    [
                                     [0, 0, 1, 1, 1],
                                     [1, 0, 0, 0, 1],
                                     [1, 1, 1, 0, 1],
                                     [1, 0, 0, 0, 1],
                                     [1, 1, 1, 0, 0]
                                    ]

                                    
    start_node: Coordinates of the starting point in the maze, as (row, col).
                   Example: (0, 0) for the top-left corner.
                   
    end_node: Coordinates of the target destination in the maze, as (row, col).
                 Example: (4, 4) for the bottom-right corner.

    Returns:
    list: A list of coordinates representing the shortest path from start to end.
          Example: [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4)]
          
          If no path exists, returns None.
    """
    
    # Ensure the maze matrix exists (is not None or empty)
    if maze_as_matrix:
        # Step 1: Convert the maze matrix into a graph representation
        # Each 0 in the matrix becomes a node in the graph, and edges connect 0 s .
        maze_graph = maze_to_graph(maze_as_matrix)
        
        # Step 2: Use BFS to find the shortest path from the start point to the end point in the graph
        # The BFS algorithm returns the shortest path as a list of coordinates, or None if no path is found.
        shortest_maze_path = bfs(maze_graph, start_node, end_node)
        
        # Step 3: Output the result - either the shortest path or a message indicating no path was found.
        print("Shortest path in the maze:", shortest_maze_path)
        
        # Return the shortest path for potential further processing
        return shortest_maze_path
    else:
        # If the input maze is empty or invalid, print an error message and return None.
        print("Error: The maze is empty or invalid.")
        return None



    
