class TreeNode:
    """Node class for general tree."""

    def __init__(self, data):
        """
        Initialize a tree node with data.

        Args:
            data: The data to store in the node
        """
        self.data = data
        self.children = []

    def add_child(self, child_node):
        """
        Add a child node to this node.

        Args:
            child_node: The child node to add
        """
        self.children.append(child_node)

    def remove_child(self, child_node):
        """
        Remove a child node from this node.

        Args:
            child_node: The child node to remove
        """
        self.children = [child for child in self.children if child != child_node]


class Tree:
    """
    General Tree data structure implementation.
    A tree where each node can have any number of children.
    """

    def __init__(self, root_data=None):
        """
        Initialize a tree with an optional root.

        Args:
            root_data: Data for the root node (optional)
        """
        self.root = TreeNode(root_data) if root_data is not None else None

    def traverse_preorder(self, node=None, result=None):
        """
        Traverse the tree in preorder (root, children).

        Args:
            node: Starting node (defaults to root)
            result: List to store results

        Returns:
            list: List of node data in preorder
        """
        if result is None:
            result = []

        if node is None:
            node = self.root

        if node is None:
            return result

        result.append(node.data)
        for child in node.children:
            self.traverse_preorder(child, result)

        return result

    def traverse_postorder(self, node=None, result=None):
        """
        Traverse the tree in postorder (children, root).

        Args:
            node: Starting node (defaults to root)
            result: List to store results

        Returns:
            list: List of node data in postorder
        """
        if result is None:
            result = []

        if node is None:
            node = self.root

        if node is None:
            return result

        for child in node.children:
            self.traverse_postorder(child, result)

        result.append(node.data)
        return result

    def traverse_level_order(self):
        """
        Traverse the tree level by level (breadth-first).

        Returns:
            list: List of node data in level order
        """
        if self.root is None:
            return []

        result = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            result.append(node.data)
            queue.extend(node.children)

        return result

    def height(self, node=None):
        """
        Calculate the height of the tree.

        Args:
            node: Starting node (defaults to root)

        Returns:
            int: Height of the tree
        """
        if node is None:
            node = self.root

        if node is None or not node.children:
            return 0

        max_height = 0
        for child in node.children:
            max_height = max(max_height, self.height(child))

        return max_height + 1

    def size(self, node=None):
        """
        Count the total number of nodes in the tree.

        Args:
            node: Starting node (defaults to root)

        Returns:
            int: Number of nodes
        """
        if node is None:
            node = self.root

        if node is None:
            return 0

        count = 1
        for child in node.children:
            count += self.size(child)

        return count

    def __str__(self):
        """String representation of the tree."""
        return f"Tree with root: {self.root.data if self.root else None}"


class BinaryTreeNode:
    """Node class for binary tree."""

    def __init__(self, data):
        """
        Initialize a binary tree node with data.

        Args:
            data: The data to store in the node
        """
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary Tree data structure implementation.
    A tree where each node has at most two children.
    """

    def __init__(self, root_data=None):
        """
        Initialize a binary tree with an optional root.

        Args:
            root_data: Data for the root node (optional)
        """
        self.root = BinaryTreeNode(root_data) if root_data is not None else None

    def insert_left(self, node, data):
        """
        Insert a left child for a node.

        Args:
            node: The parent node
            data: Data for the new node
        """
        if node.left is None:
            node.left = BinaryTreeNode(data)
        else:
            new_node = BinaryTreeNode(data)
            new_node.left = node.left
            node.left = new_node

    def insert_right(self, node, data):
        """
        Insert a right child for a node.

        Args:
            node: The parent node
            data: Data for the new node
        """
        if node.right is None:
            node.right = BinaryTreeNode(data)
        else:
            new_node = BinaryTreeNode(data)
            new_node.right = node.right
            node.right = new_node

    def inorder_traversal(self, node=None, result=None):
        """
        Traverse the tree inorder (left, root, right).

        Args:
            node: Starting node (defaults to root)
            result: List to store results

        Returns:
            list: List of node data in inorder
        """
        if result is None:
            result = []

        if node is None:
            node = self.root

        if node is None:
            return result

        self.inorder_traversal(node.left, result)
        result.append(node.data)
        self.inorder_traversal(node.right, result)

        return result

    def preorder_traversal(self, node=None, result=None):
        """
        Traverse the tree preorder (root, left, right).

        Args:
            node: Starting node (defaults to root)
            result: List to store results

        Returns:
            list: List of node data in preorder
        """
        if result is None:
            result = []

        if node is None:
            node = self.root

        if node is None:
            return result

        result.append(node.data)
        self.preorder_traversal(node.left, result)
        self.preorder_traversal(node.right, result)

        return result

    def postorder_traversal(self, node=None, result=None):
        """
        Traverse the tree postorder (left, right, root).

        Args:
            node: Starting node (defaults to root)
            result: List to store results

        Returns:
            list: List of node data in postorder
        """
        if result is None:
            result = []

        if node is None:
            node = self.root

        if node is None:
            return result

        self.postorder_traversal(node.left, result)
        self.postorder_traversal(node.right, result)
        result.append(node.data)

        return result

    def level_order_traversal(self):
        """
        Traverse the tree level by level.

        Returns:
            list: List of node data in level order
        """
        if self.root is None:
            return []

        result = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def height(self, node=None):
        """
        Calculate the height of the tree.

        Args:
            node: Starting node (defaults to root)

        Returns:
            int: Height of the tree
        """
        if node is None:
            node = self.root

        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return max(left_height, right_height) + 1

    def size(self, node=None):
        """
        Count the total number of nodes in the tree.

        Args:
            node: Starting node (defaults to root)

        Returns:
            int: Number of nodes
        """
        if node is None:
            node = self.root

        if node is None:
            return 0

        return 1 + self.size(node.left) + self.size(node.right)

    def is_balanced(self, node=None):
        """
        Check if the tree is balanced (height difference <= 1 for all nodes).

        Args:
            node: Starting node (defaults to root)

        Returns:
            bool: True if balanced, False otherwise
        """
        if node is None:
            node = self.root

        if node is None:
            return True

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.is_balanced(node.left) and self.is_balanced(node.right)

    def __str__(self):
        """String representation of the tree."""
        return f"BinaryTree with root: {self.root.data if self.root else None}"
