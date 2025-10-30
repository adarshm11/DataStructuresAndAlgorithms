"""
Tree Traversal Algorithms

Various ways to traverse binary trees and general trees.
All traversals are O(N) time complexity where N is number of nodes.
"""

from collections import deque


class TreeNode:
    """Binary tree node."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Depth-First Traversals

def inorder_recursive(root, result=None):
    """
    Inorder traversal: Left -> Root -> Right
    Returns sorted order for BST
    """
    if result is None:
        result = []

    if root:
        inorder_recursive(root.left, result)
        result.append(root.val)
        inorder_recursive(root.right, result)

    return result


def inorder_iterative(root):
    """Inorder traversal using stack (iterative)."""
    result = []
    stack = []
    current = root

    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Process node
        current = stack.pop()
        result.append(current.val)

        # Move to right subtree
        current = current.right

    return result


def preorder_recursive(root, result=None):
    """
    Preorder traversal: Root -> Left -> Right
    Useful for creating a copy of the tree
    """
    if result is None:
        result = []

    if root:
        result.append(root.val)
        preorder_recursive(root.left, result)
        preorder_recursive(root.right, result)

    return result


def preorder_iterative(root):
    """Preorder traversal using stack (iterative)."""
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def postorder_recursive(root, result=None):
    """
    Postorder traversal: Left -> Right -> Root
    Useful for deleting tree or calculating heights
    """
    if result is None:
        result = []

    if root:
        postorder_recursive(root.left, result)
        postorder_recursive(root.right, result)
        result.append(root.val)

    return result


def postorder_iterative(root):
    """Postorder traversal using two stacks (iterative)."""
    if not root:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    result = []
    while stack2:
        result.append(stack2.pop().val)

    return result


# Breadth-First Traversals

def level_order(root):
    """
    Level order traversal (BFS).
    Returns list of values level by level.
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def level_order_by_levels(root):
    """
    Level order traversal grouped by levels.
    Returns list of lists, each inner list is one level.
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

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


def zigzag_level_order(root):
    """
    Zigzag (spiral) level order traversal.
    Alternates direction for each level.
    """
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        current_level = deque()

        for _ in range(level_size):
            node = queue.popleft()

            # Add to current level based on direction
            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(current_level))
        left_to_right = not left_to_right

    return result


def vertical_order(root):
    """
    Vertical order traversal.
    Groups nodes by vertical columns.
    """
    if not root:
        return []

    # Dictionary to store nodes at each horizontal distance
    column_table = {}
    # Queue stores (node, horizontal_distance)
    queue = deque([(root, 0)])
    min_col = max_col = 0

    while queue:
        node, col = queue.popleft()

        if col not in column_table:
            column_table[col] = []
        column_table[col].append(node.val)

        min_col = min(min_col, col)
        max_col = max(max_col, col)

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    # Build result from left to right columns
    result = []
    for col in range(min_col, max_col + 1):
        result.extend(column_table[col])

    return result


def boundary_traversal(root):
    """
    Boundary traversal: left boundary -> leaves -> right boundary
    """
    if not root:
        return []

    result = []

    def is_leaf(node):
        return node and not node.left and not node.right

    def add_left_boundary(node):
        """Add left boundary (excluding leaves)."""
        while node:
            if not is_leaf(node):
                result.append(node.val)
            node = node.left if node.left else node.right

    def add_leaves(node):
        """Add all leaves."""
        if not node:
            return
        if is_leaf(node):
            result.append(node.val)
            return
        add_leaves(node.left)
        add_leaves(node.right)

    def add_right_boundary(node):
        """Add right boundary (excluding leaves) in reverse."""
        stack = []
        while node:
            if not is_leaf(node):
                stack.append(node.val)
            node = node.right if node.right else node.left
        result.extend(reversed(stack))

    if not is_leaf(root):
        result.append(root.val)

    add_left_boundary(root.left)
    add_leaves(root)
    add_right_boundary(root.right)

    return result


def morris_inorder(root):
    """
    Morris inorder traversal (no stack, no recursion).
    Time: O(N), Space: O(1) - modifies tree temporarily
    """
    result = []
    current = root

    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            # Find inorder predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if not predecessor.right:
                # Create link
                predecessor.right = current
                current = current.left
            else:
                # Remove link
                predecessor.right = None
                result.append(current.val)
                current = current.right

    return result


# Example usage
if __name__ == "__main__":
    # Build sample tree
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("Tree Traversals Demo\n")

    print("DFS Traversals:")
    print(f"Inorder (recursive):   {inorder_recursive(root)}")
    print(f"Inorder (iterative):   {inorder_iterative(root)}")
    print(f"Preorder (recursive):  {preorder_recursive(root)}")
    print(f"Preorder (iterative):  {preorder_iterative(root)}")
    print(f"Postorder (recursive): {postorder_recursive(root)}")
    print(f"Postorder (iterative): {postorder_iterative(root)}")

    print("\nBFS Traversals:")
    print(f"Level order:           {level_order(root)}")
    print(f"Level order by levels: {level_order_by_levels(root)}")
    print(f"Zigzag level order:    {zigzag_level_order(root)}")
    print(f"Vertical order:        {vertical_order(root)}")

    print("\nSpecial Traversals:")
    print(f"Boundary:              {boundary_traversal(root)}")
    print(f"Morris inorder:        {morris_inorder(root)}")
