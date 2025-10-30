class Stack:
    """
    Stack data structure implementation using a list.
    Follows LIFO (Last In First Out) principle.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: The item to add
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The top item

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        """
        Return the top item without removing it.

        Returns:
            The top item

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def clear(self):
        """Remove all items from the stack."""
        self.items = []

    def __str__(self):
        """String representation of the stack."""
        return f"Stack({self.items})"

    def __len__(self):
        """Return the size of the stack."""
        return len(self.items)


class MinStack:
    """
    Stack that supports push, pop, top, and retrieving the minimum element in constant time.
    """

    def __init__(self):
        """Initialize an empty min stack."""
        self.stack = []
        self.min_stack = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: The item to add
        """
        self.stack.append(item)

        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The top item

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")

        item = self.stack.pop()

        if item == self.min_stack[-1]:
            self.min_stack.pop()

        return item

    def peek(self):
        """
        Return the top item without removing it.

        Returns:
            The top item

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def get_min(self):
        """
        Get the minimum element in the stack in O(1) time.

        Returns:
            The minimum element

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.min_stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

    def __str__(self):
        """String representation of the min stack."""
        return f"MinStack({self.stack})"

    def __len__(self):
        """Return the size of the stack."""
        return len(self.stack)


class MaxStack:
    """
    Stack that supports push, pop, top, and retrieving the maximum element in constant time.
    """

    def __init__(self):
        """Initialize an empty max stack."""
        self.stack = []
        self.max_stack = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: The item to add
        """
        self.stack.append(item)

        if not self.max_stack or item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The top item

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")

        item = self.stack.pop()

        if item == self.max_stack[-1]:
            self.max_stack.pop()

        return item

    def peek(self):
        """
        Return the top item without removing it.

        Returns:
            The top item

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def get_max(self):
        """
        Get the maximum element in the stack in O(1) time.

        Returns:
            The maximum element

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.max_stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

    def __str__(self):
        """String representation of the max stack."""
        return f"MaxStack({self.stack})"

    def __len__(self):
        """Return the size of the stack."""
        return len(self.stack)
