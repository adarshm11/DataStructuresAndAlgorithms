"""
Linked List Algorithms

Common algorithms for linked list manipulation and analysis.
"""


class ListNode:
    """Singly linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list_iterative(head):
    """
    Reverse a linked list iteratively.
    Time: O(N), Space: O(1)

    Args:
        head: Head of linked list

    Returns:
        New head of reversed list
    """
    prev = None
    current = head

    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    return prev


def reverse_linked_list_recursive(head):
    """
    Reverse a linked list recursively.
    Time: O(N), Space: O(N) for call stack

    Args:
        head: Head of linked list

    Returns:
        New head of reversed list
    """
    if not head or not head.next:
        return head

    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head


def detect_cycle(head):
    """
    Detect if linked list has a cycle (Floyd's algorithm).
    Time: O(N), Space: O(1)

    Args:
        head: Head of linked list

    Returns:
        bool: True if cycle exists
    """
    if not head:
        return False

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def find_cycle_start(head):
    """
    Find the node where cycle begins.
    Time: O(N), Space: O(1)

    Args:
        head: Head of linked list

    Returns:
        Node where cycle starts, or None
    """
    if not head:
        return None

    slow = fast = head
    has_cycle = False

    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # Find start of cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def find_middle(head):
    """
    Find middle node of linked list.
    Time: O(N), Space: O(1)

    Args:
        head: Head of linked list

    Returns:
        Middle node
    """
    if not head:
        return None

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def find_nth_from_end(head, n):
    """
    Find nth node from end of list.
    Time: O(N), Space: O(1)

    Args:
        head: Head of linked list
        n: Position from end (1-indexed)

    Returns:
        nth node from end, or None
    """
    if not head:
        return None

    fast = slow = head

    # Move fast pointer n steps ahead
    for _ in range(n):
        if not fast:
            return None
        fast = fast.next

    # Move both pointers until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next

    return slow


def merge_two_sorted_lists(l1, l2):
    """
    Merge two sorted linked lists.
    Time: O(N + M), Space: O(1)

    Args:
        l1: Head of first sorted list
        l2: Head of second sorted list

    Returns:
        Head of merged sorted list
    """
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach remaining nodes
    current.next = l1 if l1 else l2

    return dummy.next


def remove_duplicates(head):
    """
    Remove duplicates from sorted linked list.
    Time: O(N), Space: O(1)

    Args:
        head: Head of sorted linked list

    Returns:
        Head of list without duplicates
    """
    if not head:
        return None

    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


def remove_duplicates_unsorted(head):
    """
    Remove duplicates from unsorted linked list.
    Time: O(N), Space: O(N) for hash set

    Args:
        head: Head of unsorted linked list

    Returns:
        Head of list without duplicates
    """
    if not head:
        return None

    seen = set()
    seen.add(head.val)
    current = head

    while current.next:
        if current.next.val in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.val)
            current = current.next

    return head


def is_palindrome(head):
    """
    Check if linked list is a palindrome.
    Time: O(N), Space: O(1)

    Args:
        head: Head of linked list

    Returns:
        bool: True if palindrome
    """
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second_half = reverse_linked_list_iterative(slow)

    # Compare both halves
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


def rotate_list(head, k):
    """
    Rotate linked list to the right by k places.
    Time: O(N), Space: O(1)

    Args:
        head: Head of linked list
        k: Number of rotations

    Returns:
        Head of rotated list
    """
    if not head or not head.next or k == 0:
        return head

    # Find length and connect to form circle
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Connect tail to head
    tail.next = head

    # Find new tail (length - k % length - 1)
    k = k % length
    steps_to_new_tail = length - k - 1

    new_tail = head
    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head


def partition_list(head, x):
    """
    Partition list around value x.
    Nodes < x come before nodes >= x.
    Time: O(N), Space: O(1)

    Args:
        head: Head of linked list
        x: Partition value

    Returns:
        Head of partitioned list
    """
    before_head = ListNode(0)
    after_head = ListNode(0)
    before = before_head
    after = after_head

    current = head
    while current:
        if current.val < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next

    after.next = None
    before.next = after_head.next

    return before_head.next


def intersection_of_lists(headA, headB):
    """
    Find intersection point of two linked lists.
    Time: O(N + M), Space: O(1)

    Args:
        headA: Head of first list
        headB: Head of second list

    Returns:
        Intersection node, or None
    """
    if not headA or not headB:
        return None

    pA, pB = headA, headB

    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA


# Helper functions for testing

def create_linked_list(values):
    """Create linked list from list of values."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linked_list_to_list(head):
    """Convert linked list to Python list."""
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


def print_linked_list(head, name="List"):
    """Print linked list."""
    print(f"{name}: {linked_list_to_list(head)}")


# Example usage
if __name__ == "__main__":
    print("Linked List Algorithms Demo\n")

    # Test reverse
    list1 = create_linked_list([1, 2, 3, 4, 5])
    print_linked_list(list1, "Original")
    reversed_list = reverse_linked_list_iterative(list1)
    print_linked_list(reversed_list, "Reversed")

    # Test cycle detection
    print("\n--- Cycle Detection ---")
    list2 = create_linked_list([1, 2, 3, 4])
    print(f"Has cycle: {detect_cycle(list2)}")

    # Create cycle
    list2.next.next.next.next = list2.next  # 4 -> 2
    print(f"After creating cycle: {detect_cycle(list2)}")

    # Test middle
    print("\n--- Find Middle ---")
    list3 = create_linked_list([1, 2, 3, 4, 5])
    middle = find_middle(list3)
    print(f"Middle value: {middle.val}")

    # Test nth from end
    print("\n--- Nth from End ---")
    nth = find_nth_from_end(list3, 2)
    print(f"2nd from end: {nth.val}")

    # Test merge
    print("\n--- Merge Sorted Lists ---")
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    merged = merge_two_sorted_lists(l1, l2)
    print_linked_list(merged, "Merged")

    # Test remove duplicates
    print("\n--- Remove Duplicates ---")
    list4 = create_linked_list([1, 1, 2, 3, 3, 4])
    list4 = remove_duplicates(list4)
    print_linked_list(list4, "After removing duplicates")

    # Test palindrome
    print("\n--- Palindrome Check ---")
    list5 = create_linked_list([1, 2, 3, 2, 1])
    print(f"Is palindrome: {is_palindrome(list5)}")

    # Test rotate
    print("\n--- Rotate List ---")
    list6 = create_linked_list([1, 2, 3, 4, 5])
    rotated = rotate_list(list6, 2)
    print_linked_list(rotated, "Rotated by 2")
