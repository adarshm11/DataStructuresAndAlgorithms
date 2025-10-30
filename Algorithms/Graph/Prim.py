"""
Prim's Minimum Spanning Tree Algorithm

Finds a minimum spanning tree by growing the tree from a starting vertex.
Time Complexity: O((V + E) log V) with binary heap
Space Complexity: O(V)
"""

import heapq
from collections import defaultdict


def prim(graph, start=None):
    """
    Find minimum spanning tree using Prim's algorithm.

    Args:
        graph: Adjacency list {vertex: [(neighbor, weight), ...]}
        start: Starting vertex (optional, uses first vertex if not provided)

    Returns:
        tuple: (mst_edges, total_weight)
    """
    if not graph:
        return [], 0

    if start is None:
        start = next(iter(graph))

    visited = {start}
    mst = []
    total_weight = 0

    # Priority queue: (weight, vertex1, vertex2)
    edges = [(weight, start, neighbor) for neighbor, weight in graph.get(start, [])]
    heapq.heapify(edges)

    while edges and len(visited) < len(graph):
        weight, vertex1, vertex2 = heapq.heappop(edges)

        # Skip if both vertices already in MST
        if vertex2 in visited:
            continue

        # Add edge to MST
        visited.add(vertex2)
        mst.append((vertex1, vertex2, weight))
        total_weight += weight

        # Add new edges from the newly added vertex
        for neighbor, edge_weight in graph.get(vertex2, []):
            if neighbor not in visited:
                heapq.heappush(edges, (edge_weight, vertex2, neighbor))

    return mst, total_weight


def prim_with_details(graph, start=None):
    """
    Prim's algorithm with detailed step information.

    Args:
        graph: Adjacency list
        start: Starting vertex

    Returns:
        dict: Contains MST, total weight, and step details
    """
    if not graph:
        return {
            'mst': [],
            'total_weight': 0,
            'steps': [],
            'num_edges': 0,
            'is_complete': False
        }

    if start is None:
        start = next(iter(graph))

    visited = {start}
    mst = []
    total_weight = 0
    steps = []

    edges = [(weight, start, neighbor) for neighbor, weight in graph.get(start, [])]
    heapq.heapify(edges)

    steps.append({
        'step': 0,
        'action': 'initialize',
        'vertex': start,
        'message': f'Starting from vertex {start}'
    })

    step_num = 1
    while edges and len(visited) < len(graph):
        weight, vertex1, vertex2 = heapq.heappop(edges)

        if vertex2 in visited:
            steps.append({
                'step': step_num,
                'action': 'skip',
                'edge': (vertex1, vertex2, weight),
                'message': f'Skip edge {vertex1}-{vertex2} (weight {weight}): {vertex2} already in MST'
            })
            step_num += 1
            continue

        visited.add(vertex2)
        mst.append((vertex1, vertex2, weight))
        total_weight += weight

        steps.append({
            'step': step_num,
            'action': 'add',
            'edge': (vertex1, vertex2, weight),
            'message': f'Add edge {vertex1}-{vertex2} (weight {weight}) to MST'
        })

        # Add new edges
        new_edges = []
        for neighbor, edge_weight in graph.get(vertex2, []):
            if neighbor not in visited:
                heapq.heappush(edges, (edge_weight, vertex2, neighbor))
                new_edges.append((vertex2, neighbor, edge_weight))

        if new_edges:
            steps[-1]['new_edges'] = new_edges

        step_num += 1

    return {
        'mst': mst,
        'total_weight': total_weight,
        'steps': steps,
        'num_edges': len(mst),
        'is_complete': len(mst) == len(graph) - 1,
        'visited': visited
    }


def prim_matrix(adjacency_matrix, num_vertices):
    """
    Prim's algorithm for adjacency matrix representation.

    Args:
        adjacency_matrix: 2D list representing weighted edges (0 or inf for no edge)
        num_vertices: Number of vertices

    Returns:
        tuple: (mst_edges, total_weight)
    """
    INF = float('inf')
    visited = [False] * num_vertices
    min_edge = [INF] * num_vertices
    parent = [-1] * num_vertices

    # Start from vertex 0
    min_edge[0] = 0
    mst = []
    total_weight = 0

    for _ in range(num_vertices):
        # Find minimum edge
        min_weight = INF
        min_vertex = -1

        for v in range(num_vertices):
            if not visited[v] and min_edge[v] < min_weight:
                min_weight = min_edge[v]
                min_vertex = v

        if min_vertex == -1:
            break

        visited[min_vertex] = True

        # Add edge to MST (except for first vertex)
        if parent[min_vertex] != -1:
            mst.append((parent[min_vertex], min_vertex, min_weight))
            total_weight += min_weight

        # Update min_edge values
        for v in range(num_vertices):
            if (not visited[v] and
                adjacency_matrix[min_vertex][v] != INF and
                adjacency_matrix[min_vertex][v] < min_edge[v]):
                min_edge[v] = adjacency_matrix[min_vertex][v]
                parent[v] = min_vertex

    return mst, total_weight


class PrimMST:
    """
    Object-oriented implementation of Prim's algorithm.
    """

    def __init__(self, graph):
        """
        Initialize with graph.

        Args:
            graph: Adjacency list representation
        """
        self.graph = graph
        self.mst = []
        self.total_weight = 0
        self.visited = set()

    def find_mst(self, start=None):
        """
        Find the minimum spanning tree.

        Args:
            start: Starting vertex (optional)
        """
        if not self.graph:
            return

        if start is None:
            start = next(iter(self.graph))

        self.visited = {start}
        self.mst = []
        self.total_weight = 0

        edges = [(weight, start, neighbor)
                 for neighbor, weight in self.graph.get(start, [])]
        heapq.heapify(edges)

        while edges and len(self.visited) < len(self.graph):
            weight, vertex1, vertex2 = heapq.heappop(edges)

            if vertex2 in self.visited:
                continue

            self.visited.add(vertex2)
            self.mst.append((vertex1, vertex2, weight))
            self.total_weight += weight

            for neighbor, edge_weight in self.graph.get(vertex2, []):
                if neighbor not in self.visited:
                    heapq.heappush(edges, (edge_weight, vertex2, neighbor))

    def get_mst(self):
        """Get MST edges."""
        return self.mst

    def get_total_weight(self):
        """Get total MST weight."""
        return self.total_weight

    def is_valid_mst(self):
        """Check if MST is complete."""
        return len(self.mst) == len(self.graph) - 1

    def get_mst_graph(self):
        """
        Get MST as adjacency list.

        Returns:
            dict: MST in adjacency list format
        """
        mst_graph = defaultdict(list)
        for vertex1, vertex2, weight in self.mst:
            mst_graph[vertex1].append((vertex2, weight))
            mst_graph[vertex2].append((vertex1, weight))
        return dict(mst_graph)


# Example usage
if __name__ == "__main__":
    # Example graph
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
        'E': [('C', 10), ('D', 2), ('F', 3)],
        'F': [('D', 6), ('E', 3)]
    }

    print("Graph:")
    for vertex, edges in sorted(graph.items()):
        print(f"  {vertex}: {edges}")

    # Test basic Prim
    print("\nPrim's MST (starting from 'A'):")
    mst, total_weight = prim(graph, 'A')
    for edge in mst:
        print(f"  {edge[0]}-{edge[1]}: {edge[2]}")
    print(f"Total Weight: {total_weight}")

    # Test with different starting vertex
    print("\nPrim's MST (starting from 'D'):")
    mst2, total_weight2 = prim(graph, 'D')
    for edge in mst2:
        print(f"  {edge[0]}-{edge[1]}: {edge[2]}")
    print(f"Total Weight: {total_weight2}")

    # Test with details
    print("\nDetailed Steps (starting from 'A'):")
    result = prim_with_details(graph, 'A')
    for step in result['steps']:
        if step['action'] == 'initialize':
            print(f"  {step['message']}")
        elif step['action'] == 'add':
            edge = step['edge']
            print(f"  Step {step['step']}: {step['message']}")
            if 'new_edges' in step:
                print(f"    New candidate edges: {step['new_edges']}")
        elif step['action'] == 'skip':
            print(f"  Step {step['step']}: {step['message']}")

    print(f"\nMST Complete: {result['is_complete']}")
    print(f"Total Weight: {result['total_weight']}")

    # Test matrix representation
    print("\nUsing adjacency matrix:")
    INF = float('inf')
    matrix = [
        [0, 4, 2, INF, INF, INF],  # A
        [4, 0, 1, 5, INF, INF],    # B
        [2, 1, 0, 8, 10, INF],     # C
        [INF, 5, 8, 0, 2, 6],      # D
        [INF, INF, 10, 2, 0, 3],   # E
        [INF, INF, INF, 6, 3, 0]   # F
    ]
    mst_matrix, weight_matrix = prim_matrix(matrix, 6)
    print(f"MST edges: {mst_matrix}")
    print(f"Total weight: {weight_matrix}")

    # Test OOP implementation
    print("\nUsing OOP implementation:")
    prim_algo = PrimMST(graph)
    prim_algo.find_mst('A')
    print(f"MST edges: {len(prim_algo.get_mst())}")
    print(f"Total weight: {prim_algo.get_total_weight()}")
    print(f"Valid MST: {prim_algo.is_valid_mst()}")
