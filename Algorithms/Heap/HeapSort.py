"""
Heap Sort Algorithm and Heap Operations

Heap Sort uses a binary heap to sort elements.
Time Complexity: O(N log N)
Space Complexity: O(1) for in-place version
"""


def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i.

    Args:
        arr: Array to heapify
        n: Size of heap
        i: Root index of subtree

    Time: O(log N)
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, i=largest)


def build_max_heap(arr):
    """
    Build a max heap from an array.

    Args:
        arr: Array to heapify

    Time: O(N)
    """
    n = len(arr)

    # Start from last non-leaf node and heapify all nodes
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    """
    Sort array using heap sort algorithm.

    Args:
        arr: Array to sort

    Returns:
        list: Sorted array

    Time: O(N log N)
    Space: O(1) in-place
    """
    n = len(arr)

    # Build max heap
    build_max_heap(arr)

    # Extract elements one by one from heap
    for i in range(n - 1, 0, -1):
        # Move current root (largest) to end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify the reduced heap
        heapify(arr, i, 0)

    return arr


def heap_sort_with_steps(arr):
    """
    Heap sort with detailed step information.

    Args:
        arr: Array to sort

    Returns:
        dict: Contains sorted array and step details
    """
    n = len(arr)
    steps = []
    arr_copy = arr.copy()

    # Build max heap
    steps.append({
        'phase': 'build_heap',
        'description': 'Building max heap',
        'array': arr_copy.copy()
    })

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr_copy, n, i)

    steps.append({
        'phase': 'heap_built',
        'description': 'Max heap built',
        'array': arr_copy.copy()
    })

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr_copy[0], arr_copy[i] = arr_copy[i], arr_copy[0]

        steps.append({
            'phase': 'extract',
            'description': f'Extracted {arr_copy[i]}, heap size now {i}',
            'array': arr_copy.copy(),
            'sorted_portion': arr_copy[i:]
        })

        heapify(arr_copy, i, 0)

        steps.append({
            'phase': 'heapify',
            'description': f'Heapified after extraction',
            'array': arr_copy.copy()
        })

    return {
        'sorted': arr_copy,
        'steps': steps
    }


def min_heapify(arr, n, i):
    """
    Heapify for min heap.

    Args:
        arr: Array to heapify
        n: Size of heap
        i: Root index of subtree
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


def build_min_heap(arr):
    """
    Build a min heap from an array.

    Args:
        arr: Array to heapify
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)


def heap_sort_descending(arr):
    """
    Sort array in descending order using min heap.

    Args:
        arr: Array to sort

    Returns:
        list: Array sorted in descending order
    """
    n = len(arr)
    build_min_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heapify(arr, i, 0)

    return arr


def find_kth_largest(arr, k):
    """
    Find kth largest element using heap.

    Args:
        arr: Input array
        k: Position (1-indexed)

    Returns:
        kth largest element

    Time: O(N log N)
    """
    arr_copy = arr.copy()
    heap_sort(arr_copy)
    return arr_copy[-k] if k <= len(arr_copy) else None


def find_kth_smallest(arr, k):
    """
    Find kth smallest element using heap.

    Args:
        arr: Input array
        k: Position (1-indexed)

    Returns:
        kth smallest element
    """
    arr_copy = arr.copy()
    heap_sort(arr_copy)
    return arr_copy[k - 1] if k <= len(arr_copy) else None


class HeapSort:
    """
    Object-oriented implementation of heap sort.
    """

    def __init__(self, arr):
        """
        Initialize with array.

        Args:
            arr: Array to sort
        """
        self.arr = arr.copy()
        self.comparisons = 0
        self.swaps = 0

    def heapify(self, n, i):
        """Heapify with statistics tracking."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.comparisons += 1
            if self.arr[left] > self.arr[largest]:
                largest = left

        if right < n:
            self.comparisons += 1
            if self.arr[right] > self.arr[largest]:
                largest = right

        if largest != i:
            self.swaps += 1
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)

    def sort(self):
        """Sort the array."""
        n = len(self.arr)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        # Extract elements
        for i in range(n - 1, 0, -1):
            self.swaps += 1
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.heapify(i, 0)

        return self.arr

    def get_sorted(self):
        """Get sorted array."""
        return self.arr

    def get_stats(self):
        """Get sorting statistics."""
        return {
            'comparisons': self.comparisons,
            'swaps': self.swaps
        }


# Example usage
if __name__ == "__main__":
    # Test basic heap sort
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)

    sorted_arr = heap_sort(arr.copy())
    print("Sorted array (ascending):", sorted_arr)

    # Test descending sort
    desc_arr = heap_sort_descending(arr.copy())
    print("Sorted array (descending):", desc_arr)

    # Test with steps
    print("\n--- Heap Sort with Steps ---")
    arr2 = [4, 10, 3, 5, 1]
    result = heap_sort_with_steps(arr2)
    print(f"Original: {arr2}")
    for i, step in enumerate(result['steps']):
        print(f"Step {i + 1}: {step['description']}")
        print(f"  Array: {step['array']}")
    print(f"Final sorted: {result['sorted']}")

    # Test kth largest/smallest
    arr3 = [7, 10, 4, 3, 20, 15]
    print(f"\n3rd largest in {arr3}: {find_kth_largest(arr3, 3)}")
    print(f"3rd smallest in {arr3}: {find_kth_smallest(arr3, 3)}")

    # Test OOP implementation
    print("\n--- OOP Heap Sort ---")
    sorter = HeapSort([64, 34, 25, 12, 22, 11, 90])
    sorted_result = sorter.sort()
    print(f"Sorted: {sorted_result}")
    stats = sorter.get_stats()
    print(f"Statistics: {stats}")
