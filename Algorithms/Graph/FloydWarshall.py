"""
Floyd-Warshall All-Pairs Shortest Path Algorithm

Finds shortest paths between all pairs of vertices.
Works with negative edge weights and can detect negative cycles.

Time Complexity: O(V^3)
Space Complexity: O(V^2)
"""


def floyd_warshall(vertices, edges):
    """
    Find shortest paths between all pairs of vertices.

    Args:
        vertices: List of vertices
        edges: List of edges as tuples (u, v, weight)

    Returns:
        tuple: (distance matrix dict, next vertex dict) or None if negative cycle
    """
    # Initialize distance matrix
    dist = {v: {u: float('inf') for u in vertices} for v in vertices}
    next_vertex = {v: {u: None for u in vertices} for v in vertices}

    # Distance from vertex to itself is 0
    for v in vertices:
        dist[v][v] = 0

    # Initialize with direct edges
    for u, v, weight in edges:
        dist[u][v] = weight
        next_vertex[u][v] = v

    # Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    # Check for negative cycles
    for v in vertices:
        if dist[v][v] < 0:
            return None

    return dist, next_vertex


def reconstruct_path(next_vertex, start, end):
    """
    Reconstruct path between two vertices.

    Args:
        next_vertex: Next vertex matrix from Floyd-Warshall
        start: Starting vertex
        end: Target vertex

    Returns:
        list: Path from start to end, or empty list if no path
    """
    if next_vertex[start][end] is None:
        return []

    path = [start]
    current = start

    while current != end:
        current = next_vertex[current][end]
        if current is None:
            return []
        path.append(current)

    return path


def floyd_warshall_with_paths(vertices, edges):
    """
    Floyd-Warshall with all paths reconstructed.

    Args:
        vertices: List of vertices
        edges: List of edges

    Returns:
        dict: Contains distances and paths for all pairs
    """
    result = floyd_warshall(vertices, edges)

    if result is None:
        return None  # Negative cycle

    dist, next_vertex = result
    paths = {}

    for start in vertices:
        paths[start] = {}
        for end in vertices:
            if dist[start][end] != float('inf'):
                paths[start][end] = reconstruct_path(next_vertex, start, end)
            else:
                paths[start][end] = []

    return {
        'distances': dist,
        'paths': paths,
        'next_vertex': next_vertex
    }


def floyd_warshall_matrix(adjacency_matrix):
    """
    Floyd-Warshall for adjacency matrix representation.

    Args:
        adjacency_matrix: 2D list where matrix[i][j] is weight of edge i->j
                         (use float('inf') for no edge)

    Returns:
        tuple: (distance matrix, next vertex matrix)
    """
    n = len(adjacency_matrix)

    # Copy the adjacency matrix
    dist = [row[:] for row in adjacency_matrix]
    next_vertex = [[None] * n for _ in range(n)]

    # Initialize next_vertex for direct edges
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != float('inf'):
                next_vertex[i][j] = j

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    return dist, next_vertex


def detect_negative_cycle_fw(vertices, edges):
    """
    Detect negative cycle using Floyd-Warshall.

    Args:
        vertices: List of vertices
        edges: List of edges

    Returns:
        bool: True if negative cycle exists
    """
    result = floyd_warshall(vertices, edges)
    return result is None


def floyd_warshall_detailed(vertices, edges):
    """
    Floyd-Warshall with detailed iteration information.

    Args:
        vertices: List of vertices
        edges: List of edges

    Returns:
        dict: Contains final result and iteration details
    """
    # Initialize
    dist = {v: {u: float('inf') for u in vertices} for v in vertices}
    next_vertex = {v: {u: None for u in vertices} for v in vertices}

    for v in vertices:
        dist[v][v] = 0

    for u, v, weight in edges:
        dist[u][v] = weight
        next_vertex[u][v] = v

    iterations = []

    # Floyd-Warshall algorithm with tracking
    for k in vertices:
        updates = []

        for i in vertices:
            for j in vertices:
                old_dist = dist[i][j]
                new_dist = dist[i][k] + dist[k][j]

                if new_dist < old_dist:
                    dist[i][j] = new_dist
                    next_vertex[i][j] = next_vertex[i][k]
                    updates.append({
                        'from': i,
                        'to': j,
                        'via': k,
                        'old_distance': old_dist,
                        'new_distance': new_dist
                    })

        iterations.append({
            'intermediate': k,
            'updates': updates,
            'num_updates': len(updates)
        })

    # Check for negative cycle
    has_negative_cycle = any(dist[v][v] < 0 for v in vertices)

    # Build paths
    paths = {}
    for start in vertices:
        paths[start] = {}
        for end in vertices:
            if dist[start][end] != float('inf'):
                paths[start][end] = reconstruct_path(next_vertex, start, end)
            else:
                paths[start][end] = []

    return {
        'distances': dist,
        'paths': paths,
        'iterations': iterations,
        'has_negative_cycle': has_negative_cycle
    }


class FloydWarshallAlgorithm:
    """
    Object-oriented implementation of Floyd-Warshall algorithm.
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
        self.dist = None
        self.next_vertex = None
        self.has_negative_cycle = False

    def compute_shortest_paths(self):
        """
        Compute all-pairs shortest paths.

        Returns:
            bool: True if successful, False if negative cycle exists
        """
        # Initialize
        self.dist = {v: {u: float('inf') for u in self.vertices}
                     for v in self.vertices}
        self.next_vertex = {v: {u: None for u in self.vertices}
                           for v in self.vertices}

        for v in self.vertices:
            self.dist[v][v] = 0

        for u, v, weight in self.edges:
            self.dist[u][v] = weight
            self.next_vertex[u][v] = v

        # Floyd-Warshall
        for k in self.vertices:
            for i in self.vertices:
                for j in self.vertices:
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.next_vertex[i][j] = self.next_vertex[i][k]

        # Check for negative cycle
        for v in self.vertices:
            if self.dist[v][v] < 0:
                self.has_negative_cycle = True
                return False

        return True

    def get_distance(self, start, end):
        """Get distance between two vertices."""
        if self.dist is None:
            return None
        return self.dist.get(start, {}).get(end, float('inf'))

    def get_path(self, start, end):
        """Get path between two vertices."""
        if self.next_vertex is None:
            return []
        return reconstruct_path(self.next_vertex, start, end)

    def get_all_distances(self):
        """Get complete distance matrix."""
        return self.dist

    def print_distance_matrix(self):
        """Print formatted distance matrix."""
        if self.dist is None:
            print("No distances computed yet")
            return

        print("Distance Matrix:")
        print(f"     {' '.join(f'{v:>6}' for v in sorted(self.vertices))}")
        for i in sorted(self.vertices):
            row = [self.dist[i][j] if self.dist[i][j] != float('inf') else '∞'
                   for j in sorted(self.vertices)]
            print(f"{i:>4} {' '.join(f'{str(x):>6}' for x in row)}")


# Example usage
if __name__ == "__main__":
    # Example graph
    vertices = ['A', 'B', 'C', 'D']
    edges = [
        ('A', 'B', 3),
        ('A', 'C', 8),
        ('A', 'D', -4),
        ('B', 'D', 1),
        ('B', 'C', 1),
        ('C', 'A', 2),
        ('D', 'C', 7),
        ('D', 'B', 4)
    ]

    print("Graph Edges:")
    for edge in edges:
        print(f"  {edge[0]} -> {edge[1]}: {edge[2]}")

    # Test basic Floyd-Warshall
    print("\nFloyd-Warshall All-Pairs Shortest Paths:")
    result = floyd_warshall(vertices, edges)
    if result:
        dist, next_vertex = result
        print("\nDistance Matrix:")
        for i in sorted(vertices):
            for j in sorted(vertices):
                d = dist[i][j] if dist[i][j] != float('inf') else '∞'
                print(f"  {i} -> {j}: {d}")
    else:
        print("  Negative cycle detected!")

    # Test path reconstruction
    print("\nPath from A to C:")
    if result:
        path = reconstruct_path(next_vertex, 'A', 'C')
        distance = dist['A']['C']
        print(f"  Path: {' -> '.join(path)}")
        print(f"  Distance: {distance}")

    # Test with all paths
    print("\nAll paths:")
    all_paths_result = floyd_warshall_with_paths(vertices, edges)
    if all_paths_result:
        for start in sorted(vertices):
            for end in sorted(vertices):
                if start != end:
                    path = all_paths_result['paths'][start][end]
                    dist = all_paths_result['distances'][start][end]
                    if path:
                        print(f"  {start} -> {end}: {' -> '.join(path)} (distance: {dist})")

    # Test OOP implementation
    print("\nUsing OOP implementation:")
    fw = FloydWarshallAlgorithm(vertices, edges)
    success = fw.compute_shortest_paths()
    if success:
        print(f"  Distance A -> C: {fw.get_distance('A', 'C')}")
        print(f"  Path A -> C: {' -> '.join(fw.get_path('A', 'C'))}")
        print()
        fw.print_distance_matrix()
    else:
        print("  Negative cycle detected!")
