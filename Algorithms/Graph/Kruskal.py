"""
Kruskal's Minimum Spanning Tree Algorithm

Finds a minimum spanning tree using a greedy approach with Union-Find.
Time Complexity: O(E log E) for sorting edges
Space Complexity: O(V) for Union-Find structure
"""


class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure with path compression
    and union by rank optimizations.
    """

    def __init__(self, vertices):
        """
        Initialize Union-Find structure.

        Args:
            vertices: List of vertices
        """
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        """
        Find the root of the set containing vertex (with path compression).

        Args:
            vertex: Vertex to find

        Returns:
            Root of the set
        """
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        """
        Unite the sets containing vertex1 and vertex2 (union by rank).

        Args:
            vertex1: First vertex
            vertex2: Second vertex

        Returns:
            bool: True if union was performed, False if already in same set
        """
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 == root2:
            return False

        # Union by rank
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True


def kruskal(vertices, edges):
    """
    Find minimum spanning tree using Kruskal's algorithm.

    Args:
        vertices: List of vertices
        edges: List of edges as tuples (vertex1, vertex2, weight)

    Returns:
        tuple: (mst_edges, total_weight)
    """
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])

    uf = UnionFind(vertices)
    mst = []
    total_weight = 0

    for vertex1, vertex2, weight in sorted_edges:
        # If vertices are in different sets, add edge to MST
        if uf.union(vertex1, vertex2):
            mst.append((vertex1, vertex2, weight))
            total_weight += weight

            # Stop when we have V-1 edges
            if len(mst) == len(vertices) - 1:
                break

    return mst, total_weight


def kruskal_with_details(vertices, edges):
    """
    Kruskal's algorithm with detailed step-by-step information.

    Args:
        vertices: List of vertices
        edges: List of edges as tuples (vertex1, vertex2, weight)

    Returns:
        dict: Contains MST, total weight, and step details
    """
    sorted_edges = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(vertices)
    mst = []
    total_weight = 0
    steps = []

    for vertex1, vertex2, weight in sorted_edges:
        root1 = uf.find(vertex1)
        root2 = uf.find(vertex2)

        if root1 != root2:
            uf.union(vertex1, vertex2)
            mst.append((vertex1, vertex2, weight))
            total_weight += weight
            steps.append({
                'edge': (vertex1, vertex2, weight),
                'action': 'added',
                'reason': f'Connects different components ({root1} and {root2})'
            })

            if len(mst) == len(vertices) - 1:
                break
        else:
            steps.append({
                'edge': (vertex1, vertex2, weight),
                'action': 'skipped',
                'reason': f'Would create cycle (both in component {root1})'
            })

    return {
        'mst': mst,
        'total_weight': total_weight,
        'steps': steps,
        'num_edges': len(mst),
        'is_complete': len(mst) == len(vertices) - 1
    }


def is_connected_graph(vertices, edges):
    """
    Check if graph is connected (has MST).

    Args:
        vertices: List of vertices
        edges: List of edges

    Returns:
        bool: True if connected
    """
    if not vertices:
        return True

    uf = UnionFind(vertices)

    for vertex1, vertex2, _ in edges:
        uf.union(vertex1, vertex2)

    # All vertices should have same root
    root = uf.find(vertices[0])
    return all(uf.find(v) == root for v in vertices)


def kruskal_adjacency_list(graph):
    """
    Kruskal's algorithm for adjacency list representation.

    Args:
        graph: Adjacency list {vertex: [(neighbor, weight), ...]}

    Returns:
        tuple: (mst_edges, total_weight)
    """
    # Extract vertices and edges
    vertices = list(graph.keys())
    edges = []

    # Convert adjacency list to edge list (avoid duplicates)
    seen = set()
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edge = tuple(sorted([vertex, neighbor]))
            if edge not in seen:
                seen.add(edge)
                edges.append((vertex, neighbor, weight))

    return kruskal(vertices, edges)


class KruskalMST:
    """
    Object-oriented implementation of Kruskal's algorithm.
    """

    def __init__(self, vertices, edges):
        """
        Initialize with graph data.

        Args:
            vertices: List of vertices
            edges: List of edges as tuples (vertex1, vertex2, weight)
        """
        self.vertices = vertices
        self.edges = edges
        self.mst = []
        self.total_weight = 0
        self.uf = None

    def find_mst(self):
        """Find the minimum spanning tree."""
        sorted_edges = sorted(self.edges, key=lambda x: x[2])
        self.uf = UnionFind(self.vertices)
        self.mst = []
        self.total_weight = 0

        for vertex1, vertex2, weight in sorted_edges:
            if self.uf.union(vertex1, vertex2):
                self.mst.append((vertex1, vertex2, weight))
                self.total_weight += weight

                if len(self.mst) == len(self.vertices) - 1:
                    break

    def get_mst(self):
        """Get MST edges."""
        return self.mst

    def get_total_weight(self):
        """Get total MST weight."""
        return self.total_weight

    def is_valid_mst(self):
        """Check if MST is valid and complete."""
        return len(self.mst) == len(self.vertices) - 1


# Example usage
if __name__ == "__main__":
    # Example graph
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3)
    ]

    print("Graph Edges:")
    for edge in sorted(edges, key=lambda x: x[2]):
        print(f"  {edge[0]}-{edge[1]}: {edge[2]}")

    # Test basic Kruskal
    print("\nKruskal's MST:")
    mst, total_weight = kruskal(vertices, edges)
    for edge in mst:
        print(f"  {edge[0]}-{edge[1]}: {edge[2]}")
    print(f"Total Weight: {total_weight}")

    # Test with details
    print("\nDetailed Steps:")
    result = kruskal_with_details(vertices, edges)
    for i, step in enumerate(result['steps'], 1):
        edge = step['edge']
        print(f"  Step {i}: Edge {edge[0]}-{edge[1]} (weight {edge[2]})")
        print(f"    Action: {step['action']}")
        print(f"    Reason: {step['reason']}")

    print(f"\nMST Complete: {result['is_complete']}")
    print(f"Total Weight: {result['total_weight']}")

    # Test connectivity
    print(f"\nGraph is connected: {is_connected_graph(vertices, edges)}")

    # Test OOP implementation
    print("\nUsing OOP implementation:")
    kruskal_algo = KruskalMST(vertices, edges)
    kruskal_algo.find_mst()
    print(f"MST edges: {len(kruskal_algo.get_mst())}")
    print(f"Total weight: {kruskal_algo.get_total_weight()}")
    print(f"Valid MST: {kruskal_algo.is_valid_mst()}")
