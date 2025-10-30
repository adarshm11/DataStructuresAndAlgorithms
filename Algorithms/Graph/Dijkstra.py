"""
Dijkstra's Shortest Path Algorithm

Finds the shortest path from a source vertex to all other vertices in a weighted graph.
Works only with non-negative edge weights.

Time Complexity: O((V + E) log V) with binary heap
Space Complexity: O(V)
"""

import heapq
from collections import defaultdict


def dijkstra(graph, start):
    """
    Find shortest paths from start vertex to all other vertices.

    Args:
        graph: Adjacency list with weights {vertex: [(neighbor, weight), ...]}
        start: Starting vertex

    Returns:
        dict: {vertex: (distance, path)}
    """
    # Initialize distances
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Track paths
    paths = {start: [start]}

    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    visited = set()

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Skip if already visited
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        # Check all neighbors
        for neighbor, weight in graph.get(current_vertex, []):
            distance = current_distance + weight

            # If found shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_vertex] + [neighbor]
                heapq.heappush(pq, (distance, neighbor))

    return {vertex: (distances[vertex], paths.get(vertex, []))
            for vertex in graph}


def dijkstra_simple(graph, start, end):
    """
    Find shortest path between two specific vertices.

    Args:
        graph: Adjacency list with weights
        start: Starting vertex
        end: Target vertex

    Returns:
        tuple: (distance, path) or (inf, []) if no path exists
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    paths = {start: [start]}
    pq = [(0, start)]
    visited = set()

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_vertex == end:
            return distances[end], paths[end]

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.get(current_vertex, []):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_vertex] + [neighbor]
                heapq.heappush(pq, (distance, neighbor))

    return float('inf'), []


def dijkstra_with_reconstruction(graph, start):
    """
    Dijkstra's algorithm with path reconstruction using parent pointers.

    Args:
        graph: Adjacency list with weights
        start: Starting vertex

    Returns:
        tuple: (distances dict, parent dict)
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    parent = {start: None}
    pq = [(0, start)]
    visited = set()

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.get(current_vertex, []):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, parent


def reconstruct_path(parent, start, end):
    """
    Reconstruct path from parent pointers.

    Args:
        parent: Parent pointer dictionary
        start: Starting vertex
        end: Target vertex

    Returns:
        list: Path from start to end
    """
    if end not in parent:
        return []

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path if path[0] == start else []


class DijkstraAlgorithm:
    """
    Object-oriented implementation of Dijkstra's algorithm.
    """

    def __init__(self, graph):
        """
        Initialize with a graph.

        Args:
            graph: Adjacency list with weights
        """
        self.graph = graph
        self.distances = {}
        self.paths = {}

    def find_shortest_paths(self, start):
        """
        Find shortest paths from start to all vertices.

        Args:
            start: Starting vertex
        """
        self.distances = {vertex: float('inf') for vertex in self.graph}
        self.distances[start] = 0
        self.paths = {start: [start]}

        pq = [(0, start)]
        visited = set()

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = current_distance + weight

                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    self.paths[neighbor] = self.paths[current_vertex] + [neighbor]
                    heapq.heappush(pq, (distance, neighbor))

    def get_distance(self, vertex):
        """Get distance to a vertex."""
        return self.distances.get(vertex, float('inf'))

    def get_path(self, vertex):
        """Get path to a vertex."""
        return self.paths.get(vertex, [])


# Example usage
if __name__ == "__main__":
    # Example weighted graph
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }

    print("Weighted Graph:")
    for vertex, edges in graph.items():
        print(f"  {vertex}: {edges}")

    # Test basic dijkstra
    print("\nDijkstra from 'A':")
    result = dijkstra(graph, 'A')
    for vertex, (distance, path) in sorted(result.items()):
        print(f"  {vertex}: distance={distance}, path={path}")

    # Test specific path
    print("\nShortest path from 'A' to 'E':")
    distance, path = dijkstra_simple(graph, 'A', 'E')
    print(f"  Distance: {distance}, Path: {path}")

    # Test with reconstruction
    print("\nUsing parent pointer reconstruction:")
    distances, parent = dijkstra_with_reconstruction(graph, 'A')
    path_to_e = reconstruct_path(parent, 'A', 'E')
    print(f"  Path to E: {path_to_e}, Distance: {distances['E']}")

    # Test OOP implementation
    print("\nUsing OOP implementation:")
    dijkstra_algo = DijkstraAlgorithm(graph)
    dijkstra_algo.find_shortest_paths('A')
    print(f"  Distance to E: {dijkstra_algo.get_distance('E')}")
    print(f"  Path to E: {dijkstra_algo.get_path('E')}")
