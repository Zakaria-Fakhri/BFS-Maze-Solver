def maze_to_graph(maze_matrix):
    """
    Converts a maze represented as a matrix into a graph.
    
    In this representation:
    - Each 0 in the maze matrix represents a vertex in the graph.
    - An edge exists between two vertices if they are neighboring cells in the maze.
    
    Parameters:
    maze_matrix  A 2D list representing the maze, where 0 indicates a path and 1 indicates a wall.

    Returns:
    dict: A dictionary representing the graph, where keys are coordinates (tuples) of vertices,
          and values are lists of neighboring vertices (tuples) connected by edges.
    """
    
    # Initialize an empty dictionary to store the graph representation of the maze
    maze_paths_graph = {}
    
    # Get the number of rows and columns in the maze
    rows = len(maze_matrix)
    cols = len(maze_matrix[0])
    
    # Define possible movements in the maze: right, down, left, up
    Map = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Iterate through each cell in the maze matrix
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is a path (0)
            if maze_matrix[i][j] == 0:  # Node
                # Initialize an entry in the graph for the current position with an empty list
                maze_paths_graph[(i, j)] = []
                
                # Explore all possible directions from the current cell
                for dx in Map:
                    di = i + dx[0]  # Calculate the new row index
                    dj = j + dx[1]  # Calculate the new column index
                    
                    # Check if the new position is within bounds and is a path (0)
                    if 0 <= di < rows and 0 <= dj < cols and maze_matrix[di][dj] == 0:
                        # Add the neighboring position as an edge in the graph
                        maze_paths_graph[(i, j)].append((di, dj))

    return maze_paths_graph
