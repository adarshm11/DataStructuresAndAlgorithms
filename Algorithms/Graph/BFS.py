"""
Breadth-First Search (BFS) Algorithm for Graphs

BFS explores a graph level by level, starting from a source vertex.
Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V) for the queue and visited set
"""

from collections import deque


def bfs(graph, start):
    """
    Perform BFS traversal on a graph.

    Args:
        graph: Adjacency list representation {vertex: [neighbors]}
        start: Starting vertex

    Returns:
        list: Vertices in BFS order
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        # Visit all unvisited neighbors
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def bfs_shortest_path(graph, start, end):
    """
    Find shortest path between two vertices using BFS.

    Args:
        graph: Adjacency list representation
        start: Starting vertex
        end: Target vertex

    Returns:
        list: Shortest path from start to end, or None if no path exists
    """
    if start == end:
        return [start]

    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                new_path = path + [neighbor]

                if neighbor == end:
                    return new_path

                visited.add(neighbor)
                queue.append((neighbor, new_path))

    return None


def bfs_distance(graph, start):
    """
    Calculate shortest distance from start vertex to all other vertices.

    Args:
        graph: Adjacency list representation
        start: Starting vertex

    Returns:
        dict: {vertex: distance from start}
    """
    distances = {start: 0}
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        current_distance = distances[vertex]

        for neighbor in graph.get(vertex, []):
            if neighbor not in distances:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)

    return distances


def bfs_level_order(graph, start):
    """
    Perform BFS and return vertices grouped by levels.

    Args:
        graph: Adjacency list representation
        start: Starting vertex

    Returns:
        list: List of levels, each containing vertices at that level
    """
    visited = {start}
    queue = deque([start])
    levels = []

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            vertex = queue.popleft()
            current_level.append(vertex)

            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        levels.append(current_level)

    return levels


# Example usage
if __name__ == "__main__":
    # Example graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Graph:", graph)
    print("\nBFS traversal from 'A':", bfs(graph, 'A'))
    print("\nShortest path from 'A' to 'F':", bfs_shortest_path(graph, 'A', 'F'))
    print("\nDistances from 'A':", bfs_distance(graph, 'A'))
    print("\nLevel order from 'A':", bfs_level_order(graph, 'A'))
