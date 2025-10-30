class Graph:
    """
    Graph data structure implementation using adjacency list.
    Supports both directed and undirected graphs.
    """

    def __init__(self, directed=False):
        """
        Initialize an empty graph.

        Args:
            directed (bool): If True, creates a directed graph. Default is False (undirected).
        """
        self.adjacency_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.

        Args:
            vertex: The vertex to add
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=1):
        """
        Add an edge between two vertices.

        Args:
            vertex1: First vertex
            vertex2: Second vertex
            weight: Edge weight (default is 1)
        """
        # Add vertices if they don't exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Add edge
        self.adjacency_list[vertex1].append((vertex2, weight))

        # If undirected, add reverse edge
        if not self.directed:
            self.adjacency_list[vertex2].append((vertex1, weight))

    def remove_edge(self, vertex1, vertex2):
        """
        Remove an edge between two vertices.

        Args:
            vertex1: First vertex
            vertex2: Second vertex
        """
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1] = [(v, w) for v, w in self.adjacency_list[vertex1] if v != vertex2]

        if not self.directed and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex2] = [(v, w) for v, w in self.adjacency_list[vertex2] if v != vertex1]

    def remove_vertex(self, vertex):
        """
        Remove a vertex and all its edges from the graph.

        Args:
            vertex: The vertex to remove
        """
        if vertex in self.adjacency_list:
            # Remove all edges to this vertex
            for v in self.adjacency_list:
                self.adjacency_list[v] = [(neighbor, weight) for neighbor, weight in self.adjacency_list[v]
                                         if neighbor != vertex]

            # Remove the vertex itself
            del self.adjacency_list[vertex]

    def get_neighbors(self, vertex):
        """
        Get all neighbors of a vertex.

        Args:
            vertex: The vertex to get neighbors for

        Returns:
            list: List of tuples (neighbor, weight)
        """
        return self.adjacency_list.get(vertex, [])

    def has_edge(self, vertex1, vertex2):
        """
        Check if an edge exists between two vertices.

        Args:
            vertex1: First vertex
            vertex2: Second vertex

        Returns:
            bool: True if edge exists, False otherwise
        """
        if vertex1 in self.adjacency_list:
            return any(v == vertex2 for v, _ in self.adjacency_list[vertex1])
        return False

    def get_vertices(self):
        """
        Get all vertices in the graph.

        Returns:
            list: List of all vertices
        """
        return list(self.adjacency_list.keys())

    def bfs(self, start_vertex):
        """
        Perform breadth-first search starting from a vertex.

        Args:
            start_vertex: The starting vertex

        Returns:
            list: List of vertices in BFS order
        """
        if start_vertex not in self.adjacency_list:
            return []

        visited = set()
        queue = [start_vertex]
        result = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                for neighbor, _ in self.adjacency_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

    def dfs(self, start_vertex):
        """
        Perform depth-first search starting from a vertex.

        Args:
            start_vertex: The starting vertex

        Returns:
            list: List of vertices in DFS order
        """
        if start_vertex not in self.adjacency_list:
            return []

        visited = set()
        result = []

        def dfs_helper(vertex):
            visited.add(vertex)
            result.append(vertex)

            for neighbor, _ in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start_vertex)
        return result

    def __str__(self):
        """String representation of the graph."""
        result = []
        for vertex in self.adjacency_list:
            edges = ", ".join([f"{v}(w={w})" for v, w in self.adjacency_list[vertex]])
            result.append(f"{vertex} -> [{edges}]")
        return "\n".join(result)
