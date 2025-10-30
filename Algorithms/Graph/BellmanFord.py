"""
Bellman-Ford Shortest Path Algorithm

Finds shortest paths from a source vertex to all other vertices.
Works with negative edge weights and can detect negative cycles.

Time Complexity: O(V * E)
Space Complexity: O(V)
"""


def bellman_ford(vertices, edges, start):
    """
    Find shortest paths from start using Bellman-Ford algorithm.

    Args:
        vertices: List of vertices
        edges: List of edges as tuples (source, destination, weight)
        start: Starting vertex

    Returns:
        tuple: (distances dict, parent dict) or None if negative cycle exists
    """
    # Initialize distances
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    parent = {v: None for v in vertices}

    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        updated = False
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                parent[v] = u
                updated = True

        # Early termination if no updates
        if not updated:
            break

    # Check for negative cycles
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None  # Negative cycle detected

    return distances, parent


def bellman_ford_with_path(vertices, edges, start, end):
    """
    Find shortest path between two vertices using Bellman-Ford.

    Args:
        vertices: List of vertices
        edges: List of edges
        start: Starting vertex
        end: Target vertex

    Returns:
        tuple: (distance, path) or (None, None) if negative cycle or no path
    """
    result = bellman_ford(vertices, edges, start)

    if result is None:
        return None, None  # Negative cycle

    distances, parent = result

    if distances[end] == float('inf'):
        return float('inf'), []  # No path

    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return distances[end], path


def bellman_ford_detect_negative_cycle(vertices, edges):
    """
    Detect if graph has a negative cycle.

    Args:
        vertices: List of vertices
        edges: List of edges

    Returns:
        tuple: (has_cycle, cycle_vertices)
    """
    # Run from arbitrary start
    if not vertices:
        return False, []

    start = vertices[0]
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    parent = {v: None for v in vertices}

    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                parent[v] = u

    # Check for negative cycle and find a vertex in it
    cycle_vertex = None
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            cycle_vertex = v
            parent[v] = u
            break

    if cycle_vertex is None:
        return False, []

    # Trace back to find cycle
    visited = set()
    current = cycle_vertex

    # Move back V steps to ensure we're in the cycle
    for _ in range(len(vertices)):
        current = parent[current]

    # Now extract the cycle
    cycle = []
    start_of_cycle = current
    while True:
        cycle.append(current)
        current = parent[current]
        if current == start_of_cycle:
            cycle.append(current)
            break

    cycle.reverse()
    return True, cycle


def bellman_ford_all_paths(vertices, edges, start):
    """
    Bellman-Ford with detailed information including all relaxations.

    Args:
        vertices: List of vertices
        edges: List of edges
        start: Starting vertex

    Returns:
        dict: Contains distances, paths, and iteration details
    """
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    parent = {v: None for v in vertices}
    iterations = []

    # Relax edges V-1 times
    for iteration in range(len(vertices) - 1):
        updated = False
        relaxations = []

        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                old_distance = distances[v]
                distances[v] = distances[u] + weight
                parent[v] = u
                updated = True

                relaxations.append({
                    'edge': (u, v, weight),
                    'old_distance': old_distance,
                    'new_distance': distances[v]
                })

        iterations.append({
            'iteration': iteration + 1,
            'updated': updated,
            'relaxations': relaxations,
            'distances': distances.copy()
        })

        if not updated:
            break

    # Check for negative cycle
    negative_cycle = False
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            negative_cycle = True
            break

    # Build paths
    paths = {}
    for vertex in vertices:
        if distances[vertex] != float('inf'):
            path = []
            current = vertex
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            paths[vertex] = path

    return {
        'distances': distances,
        'paths': paths,
        'parent': parent,
        'iterations': iterations,
        'negative_cycle': negative_cycle
    }


class BellmanFordAlgorithm:
    """
    Object-oriented implementation of Bellman-Ford algorithm.
    """

    def __init__(self, vertices, edges):
        """
        Initialize with graph.

        Args:
            vertices: List of vertices
            edges: List of edges as tuples (u, v, weight)
        """
        self.vertices = vertices
        self.edges = edges
        self.distances = {}
        self.parent = {}
        self.has_negative_cycle = False

    def find_shortest_paths(self, start):
        """
        Find shortest paths from start vertex.

        Args:
            start: Starting vertex

        Returns:
            bool: True if successful, False if negative cycle exists
        """
        self.distances = {v: float('inf') for v in self.vertices}
        self.distances[start] = 0
        self.parent = {v: None for v in self.vertices}

        # Relax edges V-1 times
        for _ in range(len(self.vertices) - 1):
            for u, v, weight in self.edges:
                if (self.distances[u] != float('inf') and
                    self.distances[u] + weight < self.distances[v]):
                    self.distances[v] = self.distances[u] + weight
                    self.parent[v] = u

        # Check for negative cycles
        for u, v, weight in self.edges:
            if (self.distances[u] != float('inf') and
                self.distances[u] + weight < self.distances[v]):
                self.has_negative_cycle = True
                return False

        return True

    def get_distance(self, vertex):
        """Get distance to vertex."""
        return self.distances.get(vertex, float('inf'))

    def get_path(self, vertex):
        """Get path to vertex."""
        if self.distances.get(vertex, float('inf')) == float('inf'):
            return []

        path = []
        current = vertex
        while current is not None:
            path.append(current)
            current = self.parent[current]

        path.reverse()
        return path


# Example usage
if __name__ == "__main__":
    # Example graph
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 3),
        ('B', 'D', 2),
        ('B', 'E', 3),
        ('C', 'B', 1),
        ('C', 'D', 4),
        ('C', 'E', 5),
        ('E', 'D', -5)
    ]

    print("Graph Edges (with negative weight):")
    for edge in edges:
        print(f"  {edge[0]} -> {edge[1]}: {edge[2]}")

    # Test basic Bellman-Ford
    print("\nBellman-Ford from 'A':")
    result = bellman_ford(vertices, edges, 'A')
    if result:
        distances, parent = result
        for vertex in sorted(vertices):
            print(f"  {vertex}: distance={distances[vertex]}, parent={parent[vertex]}")
    else:
        print("  Negative cycle detected!")

    # Test path finding
    print("\nShortest path from 'A' to 'D':")
    distance, path = bellman_ford_with_path(vertices, edges, 'A', 'D')
    if distance is not None:
        print(f"  Distance: {distance}")
        print(f"  Path: {' -> '.join(path)}")
    else:
        print("  Negative cycle detected!")

    # Test negative cycle detection
    print("\nChecking for negative cycles:")
    has_cycle, cycle = bellman_ford_detect_negative_cycle(vertices, edges)
    print(f"  Has negative cycle: {has_cycle}")
    if has_cycle:
        print(f"  Cycle: {' -> '.join(cycle)}")

    # Test with negative cycle
    print("\n--- Graph with negative cycle ---")
    edges_with_cycle = edges + [('D', 'C', -10)]
    print("Added edge: D -> C: -10")

    result = bellman_ford(vertices, edges_with_cycle, 'A')
    if result is None:
        print("Negative cycle detected!")

    has_cycle, cycle = bellman_ford_detect_negative_cycle(vertices, edges_with_cycle)
    print(f"Negative cycle: {' -> '.join(cycle)}")

    # Test detailed version
    print("\n--- Detailed Bellman-Ford ---")
    detailed = bellman_ford_all_paths(vertices, edges, 'A')
    print(f"Number of iterations: {len(detailed['iterations'])}")
    print(f"Negative cycle: {detailed['negative_cycle']}")
    print("\nFinal distances:")
    for vertex in sorted(vertices):
        distance = detailed['distances'][vertex]
        path = detailed['paths'].get(vertex, [])
        print(f"  {vertex}: distance={distance}, path={' -> '.join(path)}")

    # Test OOP implementation
    print("\nUsing OOP implementation:")
    bf = BellmanFordAlgorithm(vertices, edges)
    success = bf.find_shortest_paths('A')
    if success:
        print(f"  Distance to D: {bf.get_distance('D')}")
        print(f"  Path to D: {' -> '.join(bf.get_path('D'))}")
    else:
        print("  Negative cycle detected!")
