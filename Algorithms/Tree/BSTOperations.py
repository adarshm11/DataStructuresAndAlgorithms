"""
Advanced Binary Search Tree Operations

Additional algorithms and operations for BST beyond basic insert/search/delete.
Time complexities assume balanced tree unless noted otherwise.
"""


class TreeNode:
    """Binary tree node."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_kth_smallest(root, k):
    """
    Find the kth smallest element in BST.
    Time: O(H + k) where H is height

    Args:
        root: Root of BST
        k: Position (1-indexed)

    Returns:
        Value of kth smallest element, or None if not found
    """
    stack = []
    current = root
    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        count += 1

        if count == k:
            return current.val

        current = current.right

    return None


def find_kth_largest(root, k):
    """
    Find the kth largest element in BST.
    Time: O(H + k)

    Args:
        root: Root of BST
        k: Position (1-indexed)

    Returns:
        Value of kth largest element, or None if not found
    """
    stack = []
    current = root
    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.right  # Go right first for reverse inorder

        current = stack.pop()
        count += 1

        if count == k:
            return current.val

        current = current.left

    return None


def lowest_common_ancestor(root, p, q):
    """
    Find lowest common ancestor of two nodes in BST.
    Time: O(H)

    Args:
        root: Root of BST
        p: First value
        q: Second value

    Returns:
        LCA node
    """
    while root:
        # If both values are greater, LCA is in right subtree
        if p > root.val and q > root.val:
            root = root.right
        # If both values are smaller, LCA is in left subtree
        elif p < root.val and q < root.val:
            root = root.left
        # Found the split point
        else:
            return root

    return None


def is_valid_bst_range(root, min_val=float('-inf'), max_val=float('inf')):
    """
    Validate if tree is a valid BST using range method.
    Time: O(N)

    Args:
        root: Root of tree
        min_val: Minimum allowed value
        max_val: Maximum allowed value

    Returns:
        bool: True if valid BST
    """
    if not root:
        return True

    if root.val <= min_val or root.val >= max_val:
        return False

    return (is_valid_bst_range(root.left, min_val, root.val) and
            is_valid_bst_range(root.right, root.val, max_val))


def inorder_successor(root, target):
    """
    Find inorder successor of a target value.
    Time: O(H)

    Args:
        root: Root of BST
        target: Target value

    Returns:
        Successor node or None
    """
    successor = None

    while root:
        if target < root.val:
            successor = root
            root = root.left
        else:
            root = root.right

    return successor


def inorder_predecessor(root, target):
    """
    Find inorder predecessor of a target value.
    Time: O(H)

    Args:
        root: Root of BST
        target: Target value

    Returns:
        Predecessor node or None
    """
    predecessor = None

    while root:
        if target > root.val:
            predecessor = root
            root = root.right
        else:
            root = root.left

    return predecessor


def floor_value(root, target):
    """
    Find floor value (largest value <= target) in BST.
    Time: O(H)

    Args:
        root: Root of BST
        target: Target value

    Returns:
        Floor value or None
    """
    floor = None

    while root:
        if root.val == target:
            return root.val
        elif root.val < target:
            floor = root.val
            root = root.right
        else:
            root = root.left

    return floor


def ceil_value(root, target):
    """
    Find ceil value (smallest value >= target) in BST.
    Time: O(H)

    Args:
        root: Root of BST
        target: Target value

    Returns:
        Ceil value or None
    """
    ceil = None

    while root:
        if root.val == target:
            return root.val
        elif root.val > target:
            ceil = root.val
            root = root.left
        else:
            root = root.right

    return ceil


def bst_to_sorted_array(root):
    """
    Convert BST to sorted array.
    Time: O(N)

    Args:
        root: Root of BST

    Returns:
        list: Sorted array of values
    """
    result = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result


def sorted_array_to_bst(arr):
    """
    Convert sorted array to balanced BST.
    Time: O(N)

    Args:
        arr: Sorted array

    Returns:
        Root of balanced BST
    """
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid + 1:])

    return root


def count_nodes_in_range(root, low, high):
    """
    Count nodes with values in range [low, high].
    Time: O(N) worst case, but can prune subtrees

    Args:
        root: Root of BST
        low: Lower bound (inclusive)
        high: Upper bound (inclusive)

    Returns:
        int: Count of nodes in range
    """
    if not root:
        return 0

    # If current node is in range
    if low <= root.val <= high:
        return (1 +
                count_nodes_in_range(root.left, low, high) +
                count_nodes_in_range(root.right, low, high))

    # If current node is smaller than low, ignore left subtree
    elif root.val < low:
        return count_nodes_in_range(root.right, low, high)

    # If current node is greater than high, ignore right subtree
    else:
        return count_nodes_in_range(root.left, low, high)


def trim_bst(root, low, high):
    """
    Remove nodes outside the range [low, high].
    Time: O(N)

    Args:
        root: Root of BST
        low: Lower bound
        high: Upper bound

    Returns:
        Root of trimmed BST
    """
    if not root:
        return None

    # If root is less than low, trim left subtree
    if root.val < low:
        return trim_bst(root.right, low, high)

    # If root is greater than high, trim right subtree
    if root.val > high:
        return trim_bst(root.left, low, high)

    # Root is in range, recursively trim children
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)

    return root


def find_mode(root):
    """
    Find the most frequent value(s) in BST.
    Time: O(N), Space: O(1) if we don't count output

    Args:
        root: Root of BST

    Returns:
        list: List of most frequent values
    """
    def inorder(node):
        nonlocal current_val, current_count, max_count, modes

        if not node:
            return

        inorder(node.left)

        # Process current node
        if node.val == current_val:
            current_count += 1
        else:
            current_val = node.val
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            modes = [current_val]
        elif current_count == max_count:
            modes.append(current_val)

        inorder(node.right)

    current_val = None
    current_count = 0
    max_count = 0
    modes = []

    inorder(root)
    return modes


# Example usage
if __name__ == "__main__":
    # Build sample BST
    #       8
    #      / \
    #     3   10
    #    / \    \
    #   1   6   14
    #      / \  /
    #     4  7 13

    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)

    print("BST Operations Demo\n")

    # Kth smallest/largest
    print(f"3rd smallest: {find_kth_smallest(root, 3)}")  # 4
    print(f"3rd largest: {find_kth_largest(root, 3)}")    # 10

    # LCA
    lca = lowest_common_ancestor(root, 4, 7)
    print(f"\nLCA of 4 and 7: {lca.val}")  # 6

    # Validation
    print(f"\nIs valid BST: {is_valid_bst_range(root)}")

    # Successor/Predecessor
    succ = inorder_successor(root, 6)
    pred = inorder_predecessor(root, 6)
    print(f"\nSuccessor of 6: {succ.val if succ else None}")    # 7
    print(f"Predecessor of 6: {pred.val if pred else None}")    # 4

    # Floor/Ceil
    print(f"\nFloor of 5: {floor_value(root, 5)}")    # 4
    print(f"Ceil of 5: {ceil_value(root, 5)}")       # 6

    # Range operations
    print(f"\nNodes in range [4, 10]: {count_nodes_in_range(root, 4, 10)}")

    # Convert to array
    arr = bst_to_sorted_array(root)
    print(f"\nBST to sorted array: {arr}")

    # Create balanced BST from array
    new_root = sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])
    new_arr = bst_to_sorted_array(new_root)
    print(f"Balanced BST from [1,2,3,4,5,6,7]: {new_arr}")
