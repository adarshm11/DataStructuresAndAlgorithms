class Node:
    """Node class for LinkedList."""

    def __init__(self, data):
        """
        Initialize a node with data.

        Args:
            data: The data to store in the node
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Singly Linked List implementation.
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.size = 0

    def append(self, data):
        """
        Add a node at the end of the list.

        Args:
            data: The data to add
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        self.size += 1

    def prepend(self, data):
        """
        Add a node at the beginning of the list.

        Args:
            data: The data to add
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at(self, index, data):
        """
        Insert a node at a specific index.

        Args:
            index: The index to insert at
            data: The data to insert

        Raises:
            IndexError: If index is out of bounds
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def delete_at(self, index):
        """
        Delete a node at a specific index.

        Args:
            index: The index to delete

        Raises:
            IndexError: If index is out of bounds or list is empty
        """
        if self.head is None:
            raise IndexError("List is empty")

        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        current.next = current.next.next
        self.size -= 1

    def delete_value(self, value):
        """
        Delete the first node with the specified value.

        Args:
            value: The value to delete

        Returns:
            bool: True if value was found and deleted, False otherwise
        """
        if self.head is None:
            return False

        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next

        return False

    def find(self, value):
        """
        Find the index of the first occurrence of a value.

        Args:
            value: The value to search for

        Returns:
            int: The index of the value, or -1 if not found
        """
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1

        return -1

    def get(self, index):
        """
        Get the value at a specific index.

        Args:
            index: The index to get

        Returns:
            The data at the index

        Raises:
            IndexError: If index is out of bounds
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next

        return current.data

    def reverse(self):
        """Reverse the linked list in place."""
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def length(self):
        """Return the length of the list."""
        return self.size

    def clear(self):
        """Clear all nodes from the list."""
        self.head = None
        self.size = 0

    def to_list(self):
        """
        Convert the linked list to a Python list.

        Returns:
            list: List containing all elements
        """
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result

    def __str__(self):
        """String representation of the linked list."""
        if self.head is None:
            return "Empty List"

        result = []
        current = self.head

        while current:
            result.append(str(current.data))
            current = current.next

        return " -> ".join(result)

    def __len__(self):
        """Return the length of the list."""
        return self.size


class DoublyNode:
    """Node class for DoublyLinkedList."""

    def __init__(self, data):
        """
        Initialize a doubly linked node with data.

        Args:
            data: The data to store in the node
        """
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Doubly Linked List implementation.
    """

    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """
        Add a node at the end of the list.

        Args:
            data: The data to add
        """
        new_node = DoublyNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def prepend(self, data):
        """
        Add a node at the beginning of the list.

        Args:
            data: The data to add
        """
        new_node = DoublyNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def delete_value(self, value):
        """
        Delete the first node with the specified value.

        Args:
            value: The value to delete

        Returns:
            bool: True if value was found and deleted, False otherwise
        """
        current = self.head

        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -= 1
                return True

            current = current.next

        return False

    def reverse(self):
        """Reverse the doubly linked list in place."""
        current = self.head
        self.head, self.tail = self.tail, self.head

        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def length(self):
        """Return the length of the list."""
        return self.size

    def __str__(self):
        """String representation of the doubly linked list."""
        if self.head is None:
            return "Empty List"

        result = []
        current = self.head

        while current:
            result.append(str(current.data))
            current = current.next

        return " <-> ".join(result)

    def __len__(self):
        """Return the length of the list."""
        return self.size
