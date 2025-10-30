"""
Depth-First Search (DFS) Algorithm for Graphs

DFS explores a graph by going as deep as possible along each branch.
Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V) for the recursion stack/stack and visited set
"""


def dfs_recursive(graph, start, visited=None):
    """
    Perform DFS traversal recursively.

    Args:
        graph: Adjacency list representation {vertex: [neighbors]}
        start: Starting vertex
        visited: Set of visited vertices

    Returns:
        list: Vertices in DFS order
    """
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


def dfs_iterative(graph, start):
    """
    Perform DFS traversal iteratively using a stack.

    Args:
        graph: Adjacency list representation
        start: Starting vertex

    Returns:
        list: Vertices in DFS order
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            # Add neighbors to stack (in reverse order for consistent ordering)
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


def dfs_path(graph, start, end, visited=None, path=None):
    """
    Find a path between two vertices using DFS.

    Args:
        graph: Adjacency list representation
        start: Starting vertex
        end: Target vertex
        visited: Set of visited vertices
        path: Current path

    Returns:
        list: Path from start to end, or None if no path exists
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == end:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, end, visited, path)
            if new_path:
                return new_path

    return None


def dfs_all_paths(graph, start, end, visited=None, path=None):
    """
    Find all paths between two vertices using DFS.

    Args:
        graph: Adjacency list representation
        start: Starting vertex
        end: Target vertex
        visited: Set of visited vertices
        path: Current path

    Returns:
        list: List of all paths from start to end
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == end:
        return [path]

    paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_paths = dfs_all_paths(graph, neighbor, end, visited.copy(), path)
            paths.extend(new_paths)

    return paths


def detect_cycle_undirected(graph):
    """
    Detect if an undirected graph has a cycle using DFS.

    Args:
        graph: Adjacency list representation

    Returns:
        bool: True if cycle exists, False otherwise
    """
    visited = set()

    def dfs_helper(vertex, parent):
        visited.add(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if dfs_helper(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True

        return False

    # Check all components
    for vertex in graph:
        if vertex not in visited:
            if dfs_helper(vertex, None):
                return True

    return False


def detect_cycle_directed(graph):
    """
    Detect if a directed graph has a cycle using DFS.

    Args:
        graph: Adjacency list representation

    Returns:
        bool: True if cycle exists, False otherwise
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {vertex: WHITE for vertex in graph}

    def dfs_helper(vertex):
        color[vertex] = GRAY

        for neighbor in graph.get(vertex, []):
            if color.get(neighbor, WHITE) == GRAY:
                return True
            if color.get(neighbor, WHITE) == WHITE:
                if dfs_helper(neighbor):
                    return True

        color[vertex] = BLACK
        return False

    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs_helper(vertex):
                return True

    return False


def topological_sort_dfs(graph):
    """
    Perform topological sort on a directed acyclic graph (DAG) using DFS.

    Args:
        graph: Adjacency list representation

    Returns:
        list: Vertices in topological order, or None if cycle exists
    """
    visited = set()
    stack = []

    def dfs_helper(vertex):
        visited.add(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs_helper(neighbor)

        stack.append(vertex)

    # Visit all vertices
    for vertex in graph:
        if vertex not in visited:
            dfs_helper(vertex)

    return stack[::-1]


# Example usage
if __name__ == "__main__":
    # Example graph
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("Graph:", graph)
    print("\nDFS (recursive) from 'A':", dfs_recursive(graph, 'A'))
    print("DFS (iterative) from 'A':", dfs_iterative(graph, 'A'))
    print("\nPath from 'A' to 'F':", dfs_path(graph, 'A', 'F'))
    print("All paths from 'A' to 'F':", dfs_all_paths(graph, 'A', 'F'))

    # Cycle detection
    undirected_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A'],
        'D': ['B']
    }
    print("\nUndirected graph has cycle:", detect_cycle_undirected(undirected_graph))

    # Topological sort
    dag = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    print("\nTopological sort:", topological_sort_dfs(dag))
