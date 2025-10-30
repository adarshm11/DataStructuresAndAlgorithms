from Tree import BinaryTree, BinaryTreeNode


class BinarySearchTree(BinaryTree):
    """
    Binary Search Tree (BST) implementation that inherits from BinaryTree.

    A BST is a binary tree where for each node:
    - All values in the left subtree are less than the node's value
    - All values in the right subtree are greater than the node's value
    """

    def __init__(self, root_data=None):
        """
        Initialize a Binary Search Tree with an optional root.

        Args:
            root_data: Data for the root node (optional)
        """
        super().__init__(root_data)

    def insert(self, data):
        """
        Insert a value into the BST maintaining the BST property.

        Args:
            data: The data to insert

        Returns:
            bool: True if inserted successfully, False if duplicate
        """
        if self.root is None:
            self.root = BinaryTreeNode(data)
            return True

        return self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """
        Helper method to recursively insert data into the BST.

        Args:
            node: Current node being examined
            data: Data to insert

        Returns:
            bool: True if inserted successfully, False if duplicate
        """
        if data == node.data:
            # Duplicate value, typically not allowed in BST
            return False
        elif data < node.data:
            if node.left is None:
                node.left = BinaryTreeNode(data)
                return True
            else:
                return self._insert_recursive(node.left, data)
        else:  # data > node.data
            if node.right is None:
                node.right = BinaryTreeNode(data)
                return True
            else:
                return self._insert_recursive(node.right, data)

    def search(self, data):
        """
        Search for a value in the BST.

        Args:
            data: The data to search for

        Returns:
            BinaryTreeNode: The node containing the data, or None if not found
        """
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        """
        Helper method to recursively search for data in the BST.

        Args:
            node: Current node being examined
            data: Data to search for

        Returns:
            BinaryTreeNode: The node containing the data, or None if not found
        """
        if node is None or node.data == data:
            return node

        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def find_min(self, node=None):
        """
        Find the minimum value in the BST.

        Args:
            node: Starting node (defaults to root)

        Returns:
            The minimum value, or None if tree is empty
        """
        if node is None:
            node = self.root

        if node is None:
            return None

        while node.left is not None:
            node = node.left

        return node.data

    def find_max(self, node=None):
        """
        Find the maximum value in the BST.

        Args:
            node: Starting node (defaults to root)

        Returns:
            The maximum value, or None if tree is empty
        """
        if node is None:
            node = self.root

        if node is None:
            return None

        while node.right is not None:
            node = node.right

        return node.data

    def delete(self, data):
        """
        Delete a value from the BST.

        Args:
            data: The data to delete

        Returns:
            bool: True if deleted successfully, False if not found
        """
        self.root, deleted = self._delete_recursive(self.root, data)
        return deleted

    def _delete_recursive(self, node, data):
        """
        Helper method to recursively delete data from the BST.

        Args:
            node: Current node being examined
            data: Data to delete

        Returns:
            tuple: (new subtree root, whether deletion was successful)
        """
        if node is None:
            return None, False

        deleted = False

        if data < node.data:
            node.left, deleted = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right, deleted = self._delete_recursive(node.right, data)
        else:
            # Found the node to delete
            deleted = True

            # Case 1: Node has no children (leaf node)
            if node.left is None and node.right is None:
                return None, deleted

            # Case 2: Node has only right child
            elif node.left is None:
                return node.right, deleted

            # Case 3: Node has only left child
            elif node.right is None:
                return node.left, deleted

            # Case 4: Node has both children
            # Find the inorder successor (minimum in right subtree)
            successor_data = self.find_min(node.right)
            node.data = successor_data
            # Delete the successor
            node.right, _ = self._delete_recursive(node.right, successor_data)

        return node, deleted

    def is_valid_bst(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        """
        Check if the tree is a valid Binary Search Tree.

        Args:
            node: Starting node (defaults to root)
            min_val: Minimum allowed value for this node
            max_val: Maximum allowed value for this node

        Returns:
            bool: True if valid BST, False otherwise
        """
        if node is None:
            node = self.root

        if node is None:
            return True

        # Check if current node violates BST property
        if node.data <= min_val or node.data >= max_val:
            return False

        # Recursively check left and right subtrees
        return (self.is_valid_bst(node.left, min_val, node.data) and
                self.is_valid_bst(node.right, node.data, max_val))

    def find_successor(self, data):
        """
        Find the inorder successor of a given value.

        Args:
            data: The value whose successor to find

        Returns:
            The successor value, or None if not found or no successor exists
        """
        node = self.search(data)
        if node is None:
            return None

        # Case 1: Node has right subtree
        if node.right is not None:
            return self.find_min(node.right)

        # Case 2: No right subtree, find ancestor
        successor = None
        current = self.root

        while current is not None:
            if data < current.data:
                successor = current.data
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                break

        return successor

    def find_predecessor(self, data):
        """
        Find the inorder predecessor of a given value.

        Args:
            data: The value whose predecessor to find

        Returns:
            The predecessor value, or None if not found or no predecessor exists
        """
        node = self.search(data)
        if node is None:
            return None

        # Case 1: Node has left subtree
        if node.left is not None:
            return self.find_max(node.left)

        # Case 2: No left subtree, find ancestor
        predecessor = None
        current = self.root

        while current is not None:
            if data > current.data:
                predecessor = current.data
                current = current.right
            elif data < current.data:
                current = current.left
            else:
                break

        return predecessor

    def range_query(self, min_val, max_val):
        """
        Find all values in the BST within a given range [min_val, max_val].

        Args:
            min_val: Minimum value (inclusive)
            max_val: Maximum value (inclusive)

        Returns:
            list: Sorted list of values in the range
        """
        result = []
        self._range_query_recursive(self.root, min_val, max_val, result)
        return result

    def _range_query_recursive(self, node, min_val, max_val, result):
        """
        Helper method to recursively find values in range.

        Args:
            node: Current node
            min_val: Minimum value (inclusive)
            max_val: Maximum value (inclusive)
            result: List to store results
        """
        if node is None:
            return

        # If current node is greater than min, search left subtree
        if node.data > min_val:
            self._range_query_recursive(node.left, min_val, max_val, result)

        # If current node is in range, add it
        if min_val <= node.data <= max_val:
            result.append(node.data)

        # If current node is less than max, search right subtree
        if node.data < max_val:
            self._range_query_recursive(node.right, min_val, max_val, result)

    def __str__(self):
        """String representation of the BST."""
        return f"BinarySearchTree with root: {self.root.data if self.root else None}"


# Example usage and testing
if __name__ == "__main__":
    # Create a new BST
    bst = BinarySearchTree()

    # Insert values
    print("Inserting values: 50, 30, 70, 20, 40, 60, 80")
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)

    print(f"\n{bst}")

    # Test traversals (inherited from BinaryTree)
    print("\nInorder traversal (should be sorted):", bst.inorder_traversal())
    print("Preorder traversal:", bst.preorder_traversal())
    print("Postorder traversal:", bst.postorder_traversal())
    print("Level order traversal:", bst.level_order_traversal())

    # Test search
    print("\nSearching for 40:", "Found" if bst.search(40) else "Not found")
    print("Searching for 100:", "Found" if bst.search(100) else "Not found")

    # Test min/max
    print("\nMinimum value:", bst.find_min())
    print("Maximum value:", bst.find_max())

    # Test BST validation
    print("\nIs valid BST?", bst.is_valid_bst())

    # Test successor/predecessor
    print("\nSuccessor of 30:", bst.find_successor(30))
    print("Predecessor of 30:", bst.find_predecessor(30))

    # Test range query
    print("\nValues in range [25, 65]:", bst.range_query(25, 65))

    # Test delete
    print("\nDeleting 30...")
    bst.delete(30)
    print("Inorder traversal after deletion:", bst.inorder_traversal())

    print("\nDeleting 50 (root)...")
    bst.delete(50)
    print("Inorder traversal after deletion:", bst.inorder_traversal())
    print(f"{bst}")

    # Test height and size (inherited from BinaryTree)
    print("\nTree height:", bst.height())
    print("Tree size:", bst.size())
    print("Is balanced?", bst.is_balanced())
