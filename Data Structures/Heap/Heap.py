class MinHeap:
    """
    Min Heap implementation where the smallest element is at the root.
    """

    def __init__(self):
        """Initialize an empty min heap."""
        self.heap = []

    def parent(self, index):
        """Get the parent index of a node."""
        return (index - 1) // 2

    def left_child(self, index):
        """Get the left child index of a node."""
        return 2 * index + 1

    def right_child(self, index):
        """Get the right child index of a node."""
        return 2 * index + 2

    def swap(self, i, j):
        """Swap two elements in the heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        """
        Insert a value into the heap.

        Args:
            value: The value to insert
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """
        Move an element up the heap to maintain heap property.

        Args:
            index: The index to start heapifying from
        """
        parent_idx = self.parent(index)

        if index > 0 and self.heap[index] < self.heap[parent_idx]:
            self.swap(index, parent_idx)
            self._heapify_up(parent_idx)

    def extract_min(self):
        """
        Remove and return the minimum element (root).

        Returns:
            The minimum element

        Raises:
            IndexError: If heap is empty
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return min_value

    def _heapify_down(self, index):
        """
        Move an element down the heap to maintain heap property.

        Args:
            index: The index to start heapifying from
        """
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self._heapify_down(smallest)

    def peek(self):
        """
        Return the minimum element without removing it.

        Returns:
            The minimum element

        Raises:
            IndexError: If heap is empty
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self):
        """Return the number of elements in the heap."""
        return len(self.heap)

    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.heap) == 0

    def __str__(self):
        """String representation of the heap."""
        return str(self.heap)


class MaxHeap:
    """
    Max Heap implementation where the largest element is at the root.
    """

    def __init__(self):
        """Initialize an empty max heap."""
        self.heap = []

    def parent(self, index):
        """Get the parent index of a node."""
        return (index - 1) // 2

    def left_child(self, index):
        """Get the left child index of a node."""
        return 2 * index + 1

    def right_child(self, index):
        """Get the right child index of a node."""
        return 2 * index + 2

    def swap(self, i, j):
        """Swap two elements in the heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        """
        Insert a value into the heap.

        Args:
            value: The value to insert
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """
        Move an element up the heap to maintain heap property.

        Args:
            index: The index to start heapifying from
        """
        parent_idx = self.parent(index)

        if index > 0 and self.heap[index] > self.heap[parent_idx]:
            self.swap(index, parent_idx)
            self._heapify_up(parent_idx)

    def extract_max(self):
        """
        Remove and return the maximum element (root).

        Returns:
            The maximum element

        Raises:
            IndexError: If heap is empty
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return max_value

    def _heapify_down(self, index):
        """
        Move an element down the heap to maintain heap property.

        Args:
            index: The index to start heapifying from
        """
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.swap(index, largest)
            self._heapify_down(largest)

    def peek(self):
        """
        Return the maximum element without removing it.

        Returns:
            The maximum element

        Raises:
            IndexError: If heap is empty
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self):
        """Return the number of elements in the heap."""
        return len(self.heap)

    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.heap) == 0

    def __str__(self):
        """String representation of the heap."""
        return str(self.heap)
