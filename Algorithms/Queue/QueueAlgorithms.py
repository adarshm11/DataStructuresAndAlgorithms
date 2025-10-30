"""
Queue-Based Algorithms

Common algorithms that use queue data structure.
"""

from collections import deque


def sliding_window_maximum(nums, k):
    """
    Find maximum in each sliding window of size k.
    Time: O(N), Space: O(k)

    Args:
        nums: Input array
        k: Window size

    Returns:
        Array of maximums for each window

    Uses monotonic decreasing deque.
    """
    if not nums or k == 0:
        return []

    result = []
    dq = deque()  # Stores indices

    for i in range(len(nums)):
        # Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements (they won't be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Add to result if window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


def sliding_window_minimum(nums, k):
    """
    Find minimum in each sliding window of size k.
    Time: O(N), Space: O(k)

    Args:
        nums: Input array
        k: Window size

    Returns:
        Array of minimums for each window
    """
    if not nums or k == 0:
        return []

    result = []
    dq = deque()

    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] > nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


def first_negative_in_window(nums, k):
    """
    Find first negative number in each window of size k.
    Time: O(N), Space: O(k)

    Args:
        nums: Input array
        k: Window size

    Returns:
        Array of first negative in each window (0 if none)
    """
    result = []
    negatives = deque()

    for i in range(len(nums)):
        # Remove elements outside window
        while negatives and negatives[0] < i - k + 1:
            negatives.popleft()

        # Add negative numbers
        if nums[i] < 0:
            negatives.append(i)

        # Add to result if window is complete
        if i >= k - 1:
            if negatives:
                result.append(nums[negatives[0]])
            else:
                result.append(0)

    return result


def generate_binary_numbers(n):
    """
    Generate binary numbers from 1 to n using queue.
    Time: O(N), Space: O(N)

    Args:
        n: Upper limit

    Returns:
        List of binary strings
    """
    result = []
    queue = deque(['1'])

    for _ in range(n):
        binary = queue.popleft()
        result.append(binary)

        # Generate next numbers by appending 0 and 1
        queue.append(binary + '0')
        queue.append(binary + '1')

    return result


def level_order_traversal_nary(root):
    """
    Level order traversal of n-ary tree using queue.
    Time: O(N), Space: O(N)

    Args:
        root: Root of n-ary tree

    Returns:
        List of lists (nodes at each level)
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            # Add all children
            for child in node.children:
                queue.append(child)

        result.append(current_level)

    return result


def circular_queue_tour(petrol, distance):
    """
    Find starting point for circular tour.
    Given petrol and distance arrays, find first index from where
    a truck can complete the circular tour.
    Time: O(N), Space: O(1)

    Args:
        petrol: Array of petrol at each pump
        distance: Array of distance to next pump

    Returns:
        Starting index, or -1 if not possible
    """
    n = len(petrol)
    total_petrol = 0
    current_petrol = 0
    start = 0

    for i in range(n):
        total_petrol += petrol[i] - distance[i]
        current_petrol += petrol[i] - distance[i]

        # If current petrol becomes negative, start from next
        if current_petrol < 0:
            start = i + 1
            current_petrol = 0

    return start if total_petrol >= 0 else -1


def max_of_subarrays_with_size_k(arr, k):
    """
    Find maximum of all subarrays of size k.
    Time: O(N), Space: O(k)

    Args:
        arr: Input array
        k: Subarray size

    Returns:
        List of maximums
    """
    return sliding_window_maximum(arr, k)


def time_to_rot_oranges(grid):
    """
    Find minimum time to rot all oranges.
    0 = empty, 1 = fresh orange, 2 = rotten orange
    Each minute, rotten oranges rot adjacent fresh ones.
    Time: O(M*N), Space: O(M*N)

    Args:
        grid: 2D grid

    Returns:
        Minutes to rot all, or -1 if impossible
    """
    if not grid:
        return -1

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    # Find all rotten oranges and count fresh
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  # (row, col, time)
            elif grid[i][j] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_time = 0

    while queue:
        row, col, time = queue.popleft()
        max_time = max(max_time, time)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < rows and 0 <= new_col < cols and
                grid[new_row][new_col] == 1):
                grid[new_row][new_col] = 2
                fresh_count -= 1
                queue.append((new_row, new_col, time + 1))

    return max_time if fresh_count == 0 else -1


def first_unique_character_stream():
    """
    Find first unique character in a stream.
    Returns a class that can process stream.
    """
    class FirstUniqueChar:
        def __init__(self):
            self.queue = deque()
            self.freq = {}

        def add(self, char):
            """Add character to stream."""
            self.queue.append(char)
            self.freq[char] = self.freq.get(char, 0) + 1

        def get_first_unique(self):
            """Get first unique character."""
            while self.queue:
                char = self.queue[0]
                if self.freq[char] == 1:
                    return char
                self.queue.popleft()
            return None

    return FirstUniqueChar


def reverse_queue(queue):
    """
    Reverse a queue using recursion.
    Time: O(N), Space: O(N) for recursion

    Args:
        queue: Deque object

    Returns:
        Reversed queue
    """
    if not queue:
        return queue

    # Remove front
    front = queue.popleft()

    # Reverse remaining
    reverse_queue(queue)

    # Add front to back
    queue.append(front)

    return queue


def interleave_queue(queue):
    """
    Interleave first and second half of queue.
    Time: O(N), Space: O(N)

    Args:
        queue: Deque object with even length

    Returns:
        Interleaved queue

    Example: [1,2,3,4,5,6] -> [1,4,2,5,3,6]
    """
    n = len(queue)
    if n % 2 != 0:
        return queue

    # Move first half to temp
    temp = deque()
    for _ in range(n // 2):
        temp.append(queue.popleft())

    # Interleave
    result = deque()
    while temp:
        result.append(temp.popleft())
        result.append(queue.popleft())

    return result


def reverse_first_k(queue, k):
    """
    Reverse first k elements of queue.
    Time: O(N), Space: O(k)

    Args:
        queue: Deque object
        k: Number of elements to reverse

    Returns:
        Queue with first k elements reversed
    """
    if not queue or k <= 0 or k > len(queue):
        return queue

    # Remove first k elements to stack
    stack = []
    for _ in range(k):
        stack.append(queue.popleft())

    # Add back in reverse order
    while stack:
        queue.append(stack.pop())

    # Move remaining (n-k) elements to back
    for _ in range(len(queue) - k):
        queue.append(queue.popleft())

    return queue


# Example usage
if __name__ == "__main__":
    print("Queue Algorithms Demo\n")

    # Test sliding window maximum
    print("--- Sliding Window Maximum ---")
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = sliding_window_maximum(nums, k)
    print(f"Array: {nums}")
    print(f"Window size: {k}")
    print(f"Maximums: {result}")

    # Test first negative in window
    print("\n--- First Negative in Window ---")
    nums2 = [12, -1, -7, 8, -15, 30, 16, 28]
    k2 = 3
    result2 = first_negative_in_window(nums2, k2)
    print(f"Array: {nums2}")
    print(f"First negatives: {result2}")

    # Test generate binary numbers
    print("\n--- Generate Binary Numbers ---")
    binary_nums = generate_binary_numbers(10)
    print(f"First 10 binary numbers: {binary_nums}")

    # Test circular tour
    print("\n--- Circular Tour ---")
    petrol = [4, 6, 7, 4]
    distance = [6, 5, 3, 5]
    start = circular_queue_tour(petrol, distance)
    print(f"Petrol: {petrol}")
    print(f"Distance: {distance}")
    print(f"Starting index: {start}")

    # Test rotten oranges
    print("\n--- Rotten Oranges ---")
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    time = time_to_rot_oranges(grid)
    print(f"Time to rot all oranges: {time}")

    # Test first unique character
    print("\n--- First Unique Character Stream ---")
    FirstUniqueChar = first_unique_character_stream()
    stream = FirstUniqueChar()
    chars = ['a', 'a', 'b', 'c']
    for char in chars:
        stream.add(char)
        print(f"After adding '{char}': {stream.get_first_unique()}")

    # Test queue reversal
    print("\n--- Reverse Queue ---")
    q = deque([1, 2, 3, 4, 5])
    print(f"Original: {list(q)}")
    reverse_queue(q)
    print(f"Reversed: {list(q)}")

    # Test interleave
    print("\n--- Interleave Queue ---")
    q2 = deque([1, 2, 3, 4, 5, 6])
    print(f"Original: {list(q2)}")
    q2 = interleave_queue(q2)
    print(f"Interleaved: {list(q2)}")

    # Test reverse first k
    print("\n--- Reverse First K Elements ---")
    q3 = deque([1, 2, 3, 4, 5])
    k3 = 3
    print(f"Original: {list(q3)}")
    q3 = reverse_first_k(q3, k3)
    print(f"After reversing first {k3}: {list(q3)}")
