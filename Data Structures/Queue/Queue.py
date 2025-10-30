class Queue:
    """
    Queue data structure implementation using a list.
    Follows FIFO (First In First Out) principle.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.

        Args:
            item: The item to add
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front item from the queue.

        Returns:
            The front item

        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def front(self):
        """
        Return the front item without removing it.

        Returns:
            The front item

        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def rear(self):
        """
        Return the rear item without removing it.

        Returns:
            The rear item

        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[-1]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def clear(self):
        """Remove all items from the queue."""
        self.items = []

    def __str__(self):
        """String representation of the queue."""
        return f"Queue({self.items})"

    def __len__(self):
        """Return the size of the queue."""
        return len(self.items)


class CircularQueue:
    """
    Circular Queue implementation with fixed capacity.
    More efficient than regular queue for fixed-size buffers.
    """

    def __init__(self, capacity):
        """
        Initialize a circular queue with fixed capacity.

        Args:
            capacity: Maximum number of items the queue can hold
        """
        self.capacity = capacity
        self.items = [None] * capacity
        self.front_idx = 0
        self.rear_idx = -1
        self.current_size = 0

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.

        Args:
            item: The item to add

        Raises:
            OverflowError: If queue is full
        """
        if self.is_full():
            raise OverflowError("Queue is full")

        self.rear_idx = (self.rear_idx + 1) % self.capacity
        self.items[self.rear_idx] = item
        self.current_size += 1

    def dequeue(self):
        """
        Remove and return the front item from the queue.

        Returns:
            The front item

        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.items[self.front_idx]
        self.items[self.front_idx] = None
        self.front_idx = (self.front_idx + 1) % self.capacity
        self.current_size -= 1

        return item

    def front(self):
        """
        Return the front item without removing it.

        Returns:
            The front item

        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[self.front_idx]

    def rear(self):
        """
        Return the rear item without removing it.

        Returns:
            The rear item

        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[self.rear_idx]

    def is_empty(self):
        """Check if the queue is empty."""
        return self.current_size == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.current_size == self.capacity

    def size(self):
        """Return the number of items in the queue."""
        return self.current_size

    def __str__(self):
        """String representation of the circular queue."""
        if self.is_empty():
            return "CircularQueue([])"

        result = []
        idx = self.front_idx
        for _ in range(self.current_size):
            result.append(self.items[idx])
            idx = (idx + 1) % self.capacity

        return f"CircularQueue({result})"

    def __len__(self):
        """Return the size of the queue."""
        return self.current_size


class PriorityQueue:
    """
    Priority Queue implementation where elements with higher priority are dequeued first.
    Lower priority number means higher priority.
    """

    def __init__(self):
        """Initialize an empty priority queue."""
        self.items = []

    def enqueue(self, item, priority=0):
        """
        Add an item with a priority to the queue.

        Args:
            item: The item to add
            priority: Priority value (lower number = higher priority, default is 0)
        """
        self.items.append((priority, item))
        self.items.sort(key=lambda x: x[0])

    def dequeue(self):
        """
        Remove and return the highest priority item.

        Returns:
            The highest priority item

        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)[1]

    def front(self):
        """
        Return the highest priority item without removing it.

        Returns:
            The highest priority item

        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0][1]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def clear(self):
        """Remove all items from the queue."""
        self.items = []

    def __str__(self):
        """String representation of the priority queue."""
        return f"PriorityQueue({[(item, priority) for priority, item in self.items]})"

    def __len__(self):
        """Return the size of the queue."""
        return len(self.items)
