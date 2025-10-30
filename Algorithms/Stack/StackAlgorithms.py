"""
Stack-Based Algorithms

Common algorithms that use stack data structure.
"""


def is_balanced_parentheses(s):
    """
    Check if parentheses are balanced.
    Time: O(N), Space: O(N)

    Args:
        s: String with parentheses

    Returns:
        bool: True if balanced
    """
    stack = []
    matching = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in matching:
            stack.append(char)
        elif char in matching.values():
            if not stack or matching[stack.pop()] != char:
                return False

    return len(stack) == 0


def evaluate_postfix(expression):
    """
    Evaluate postfix (RPN) expression.
    Time: O(N), Space: O(N)

    Args:
        expression: List of tokens (numbers and operators)

    Returns:
        Result of evaluation

    Example:
        ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) = 9
    """
    stack = []

    for token in expression:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Integer division

    return stack[0]


def infix_to_postfix(expression):
    """
    Convert infix expression to postfix.
    Time: O(N), Space: O(N)

    Args:
        expression: Infix expression string

    Returns:
        Postfix expression as list

    Example:
        "2+3*4" -> ["2", "3", "4", "*", "+"]
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    i = 0

    while i < len(expression):
        char = expression[i]

        # Skip whitespace
        if char.isspace():
            i += 1
            continue

        # If operand, add to output
        if char.isdigit():
            num = ''
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            output.append(num)
            continue

        # If opening parenthesis, push to stack
        elif char == '(':
            stack.append(char)

        # If closing parenthesis, pop until opening
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()  # Remove '('

        # If operator
        elif char in precedence:
            while (stack and stack[-1] != '(' and
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[char]):
                output.append(stack.pop())
            stack.append(char)

        i += 1

    # Pop remaining operators
    while stack:
        output.append(stack.pop())

    return output


def evaluate_infix(expression):
    """
    Evaluate infix expression.
    Time: O(N), Space: O(N)

    Args:
        expression: Infix expression string

    Returns:
        Result of evaluation
    """
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)


def next_greater_element(arr):
    """
    Find next greater element for each element in array.
    Time: O(N), Space: O(N)

    Args:
        arr: Input array

    Returns:
        Array where result[i] is next greater element for arr[i]
        or -1 if no greater element exists
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # Stack stores indices

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result


def next_smaller_element(arr):
    """
    Find next smaller element for each element in array.
    Time: O(N), Space: O(N)

    Args:
        arr: Input array

    Returns:
        Array of next smaller elements
    """
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result


def largest_rectangle_histogram(heights):
    """
    Find largest rectangle in histogram.
    Time: O(N), Space: O(N)

    Args:
        heights: Array of bar heights

    Returns:
        Maximum rectangle area
    """
    stack = []
    max_area = 0
    i = 0

    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            area = heights[top] * width
            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        width = i if not stack else i - stack[-1] - 1
        area = heights[top] * width
        max_area = max(max_area, area)

    return max_area


def stock_span(prices):
    """
    Calculate stock span for each day.
    Span is number of consecutive days before current day
    where price was less than or equal to current price.
    Time: O(N), Space: O(N)

    Args:
        prices: Array of stock prices

    Returns:
        Array of spans
    """
    n = len(prices)
    spans = [1] * n
    stack = []  # Stack stores indices

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        spans[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    return spans


def simplify_path(path):
    """
    Simplify Unix-style file path.
    Time: O(N), Space: O(N)

    Args:
        path: Unix path string

    Returns:
        Simplified path

    Example:
        "/a/./b/../../c/" -> "/c"
    """
    stack = []
    components = path.split('/')

    for component in components:
        if component == '..' and stack:
            stack.pop()
        elif component and component != '.' and component != '..':
            stack.append(component)

    return '/' + '/'.join(stack)


def decode_string(s):
    """
    Decode string with pattern k[encoded_string].
    Time: O(N), Space: O(N)

    Args:
        s: Encoded string

    Returns:
        Decoded string

    Example:
        "3[a2[c]]" -> "accaccacc"
    """
    stack = []
    current_num = 0
    current_string = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_num))
            current_string = ''
            current_num = 0
        elif char == ']':
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * num
        else:
            current_string += char

    return current_string


def valid_parentheses_removal(s):
    """
    Remove minimum invalid parentheses to make string valid.
    Time: O(N), Space: O(N)

    Args:
        s: String with parentheses

    Returns:
        Valid string after removal
    """
    # First pass: remove invalid closing parentheses
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                # Mark for removal
                s = s[:i] + '*' + s[i+1:]

    # Second pass: remove invalid opening parentheses
    while stack:
        idx = stack.pop()
        s = s[:idx] + '*' + s[idx+1:]

    return s.replace('*', '')


def min_stack_operations():
    """
    Demonstrate a stack that supports getMin() in O(1).
    """
    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []

        def push(self, val):
            self.stack.append(val)
            if not self.min_stack or val <= self.min_stack[-1]:
                self.min_stack.append(val)

        def pop(self):
            if self.stack:
                val = self.stack.pop()
                if val == self.min_stack[-1]:
                    self.min_stack.pop()
                return val

        def top(self):
            return self.stack[-1] if self.stack else None

        def get_min(self):
            return self.min_stack[-1] if self.min_stack else None

    return MinStack


# Example usage
if __name__ == "__main__":
    print("Stack Algorithms Demo\n")

    # Test balanced parentheses
    print("--- Balanced Parentheses ---")
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for test in test_cases:
        print(f"{test}: {is_balanced_parentheses(test)}")

    # Test postfix evaluation
    print("\n--- Postfix Evaluation ---")
    postfix = ["2", "1", "+", "3", "*"]
    print(f"Postfix {postfix}: {evaluate_postfix(postfix)}")

    # Test infix to postfix
    print("\n--- Infix to Postfix ---")
    infix = "2+3*4"
    postfix_result = infix_to_postfix(infix)
    print(f"Infix: {infix}")
    print(f"Postfix: {postfix_result}")
    print(f"Result: {evaluate_infix(infix)}")

    # Test next greater element
    print("\n--- Next Greater Element ---")
    arr = [4, 5, 2, 10, 8]
    nge = next_greater_element(arr)
    print(f"Array: {arr}")
    print(f"NGE:   {nge}")

    # Test largest rectangle in histogram
    print("\n--- Largest Rectangle in Histogram ---")
    heights = [2, 1, 5, 6, 2, 3]
    print(f"Heights: {heights}")
    print(f"Max area: {largest_rectangle_histogram(heights)}")

    # Test stock span
    print("\n--- Stock Span ---")
    prices = [100, 80, 60, 70, 60, 75, 85]
    spans = stock_span(prices)
    print(f"Prices: {prices}")
    print(f"Spans:  {spans}")

    # Test path simplification
    print("\n--- Simplify Path ---")
    paths = ["/home/", "/a/./b/../../c/", "/a/../"]
    for path in paths:
        print(f"{path} -> {simplify_path(path)}")

    # Test decode string
    print("\n--- Decode String ---")
    encoded = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]
    for s in encoded:
        print(f"{s} -> {decode_string(s)}")

    # Test MinStack
    print("\n--- Min Stack ---")
    MinStack = min_stack_operations()
    min_stack = MinStack()
    operations = [(min_stack.push, 5), (min_stack.push, 3), (min_stack.push, 7),
                  (min_stack.get_min, None), (min_stack.pop, None), (min_stack.get_min, None)]

    for op, arg in operations:
        if arg is not None:
            op(arg)
            print(f"Push {arg}, Min: {min_stack.get_min()}")
        elif op == min_stack.get_min:
            print(f"Get Min: {op()}")
        else:
            val = op()
            print(f"Pop {val}, Min: {min_stack.get_min()}")
