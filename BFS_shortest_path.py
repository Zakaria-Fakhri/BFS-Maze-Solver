from collections import deque

def bfs(maze_graph, start_v, end_v):
    """
    Performs a breadth-first search (BFS) to find the shortest path in an unweighted graph.
    
    Parameters:
    maze_graph : The graph represented as an adjacency list (dictionary of lists).
    start_v : The starting node for the BFS.
    end_v : The goal or destination node.
    
    Returns:
    list: The shortest path from start_v to end_v as a list of nodes. If no path is found, returns None.
    """
    
    # Queue to store the nodes to be visited, starting with the start node
    queue = deque([start_v])
    
    # Dictionary to track predecessors (i.e., the previous node that leads to each node)
    predecessors_dic = {}
    predecessors_dic[start_v] = None  # Start node has no predecessor
    
    # Process nodes until the queue is empty
    while queue:
        # Select the first element from the queue
        node = queue[0]
        queue.popleft()  # Remove the first element from the queue

        # If the current node is the destination, reconstruct the path
        if node == end_v:
            path = []
            # Trace back from the end node to the start node using predecessors_dic
            while node is not None:
                path.insert(0, node)  # Insert the node at the beginning of the path
                node = predecessors_dic[node]  # Move to the predecessor node
            return path  # Return the complete path from start to goal
        
        # Explore all neighbors of the current node
        for neighbor in maze_graph[node]:
            # If the neighbor hasn't been visited yet (not in predecessors_dic)
            if neighbor not in predecessors_dic:
                # Mark the current node as the predecessor of the neighbor
                predecessors_dic[neighbor] = node
                # Add the neighbor to the queue to be processed next
                queue.append(neighbor)
    
    # If no path is found, return None
    return None
