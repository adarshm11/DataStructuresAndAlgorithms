"""
Trie-Based Algorithms

Algorithms using Trie (Prefix Tree) data structure.
"""


class TrieNode:
    """Node in a Trie."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None  # Store complete word at end node


class Autocomplete:
    """
    Autocomplete system using Trie.
    Supports prefix-based word suggestions.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert word into trie.
        Time: O(M) where M is word length
        """
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True
        node.word = word

    def search(self, word):
        """
        Search for exact word.
        Time: O(M)
        """
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        Check if any word starts with prefix.
        Time: O(M)
        """
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

    def get_suggestions(self, prefix, max_suggestions=10):
        """
        Get word suggestions for a prefix.
        Time: O(M + N) where N is total nodes in subtree

        Args:
            prefix: Prefix string
            max_suggestions: Maximum number of suggestions

        Returns:
            List of suggested words
        """
        node = self.root

        # Navigate to prefix node
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # DFS to find all words with this prefix
        suggestions = []

        def dfs(current_node):
            if len(suggestions) >= max_suggestions:
                return

            if current_node.is_end_of_word:
                suggestions.append(current_node.word)

            for child in current_node.children.values():
                dfs(child)

        dfs(node)
        return suggestions

    def get_all_words(self):
        """Get all words in trie."""
        words = []

        def dfs(node):
            if node.is_end_of_word:
                words.append(node.word)
            for child in node.children.values():
                dfs(child)

        dfs(self.root)
        return words


class WordDictionary:
    """
    Dictionary with support for wildcard search.
    '.' matches any character.
    """

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        """Add word to dictionary."""
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True

    def search(self, word):
        """
        Search with wildcard support.
        Time: O(M * 26^K) where K is number of wildcards
        """
        def dfs(node, i):
            if i == len(word):
                return node.is_end_of_word

            char = word[i]

            if char == '.':
                # Try all possible characters
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)

        return dfs(self.root, 0)


def longest_common_prefix(words):
    """
    Find longest common prefix using Trie.
    Time: O(S) where S is sum of all characters

    Args:
        words: List of words

    Returns:
        Longest common prefix string
    """
    if not words:
        return ""

    # Build trie
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Find longest common prefix
    prefix = []
    node = root

    while True:
        # If node has != 1 child or is end of word, stop
        if len(node.children) != 1 or node.is_end_of_word:
            break

        char = list(node.children.keys())[0]
        prefix.append(char)
        node = node.children[char]

    return ''.join(prefix)


def word_break(s, word_dict):
    """
    Check if string can be segmented into dictionary words.
    Time: O(N^2 + M*K) where M is dict size, K is avg word length

    Args:
        s: Input string
        word_dict: List of valid words

    Returns:
        bool: True if can be segmented
    """
    # Build trie from dictionary
    root = TrieNode()
    for word in word_dict:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        # Try all possible starting positions
        for j in range(i):
            if dp[j]:
                # Check if s[j:i] is in trie
                node = root
                found = True

                for k in range(j, i):
                    if s[k] not in node.children:
                        found = False
                        break
                    node = node.children[s[k]]

                if found and node.is_end_of_word:
                    dp[i] = True
                    break

    return dp[n]


def find_all_concatenated_words(words):
    """
    Find all words that are concatenation of other words.
    Time: O(N * M^2) where N is number of words, M is max length

    Args:
        words: List of words

    Returns:
        List of concatenated words
    """
    # Build trie
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def can_form(word, start, count):
        """Check if word[start:] can be formed."""
        if start == len(word):
            return count >= 2

        node = root
        for i in range(start, len(word)):
            if word[i] not in node.children:
                return False

            node = node.children[word[i]]

            if node.is_end_of_word:
                if can_form(word, i + 1, count + 1):
                    return True

        return False

    result = []
    for word in words:
        if can_form(word, 0, 0):
            result.append(word)

    return result


def replace_words(dictionary, sentence):
    """
    Replace words with their shortest root in dictionary.
    Time: O(D*K + S) where D is dict size, K is avg length, S is sentence length

    Args:
        dictionary: List of root words
        sentence: Sentence string

    Returns:
        Modified sentence
    """
    # Build trie
    root = TrieNode()
    for word in dictionary:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def find_root(word):
        """Find shortest root for word."""
        node = root
        for char in word:
            if char not in node.children:
                return word
            node = node.children[char]
            if node.is_end_of_word:
                return node.word
        return word

    words = sentence.split()
    return ' '.join(find_root(word) for word in words)


def max_xor_pair(nums):
    """
    Find maximum XOR of two numbers using Trie.
    Time: O(N * 32) = O(N)

    Args:
        nums: List of integers

    Returns:
        Maximum XOR value
    """
    class TrieNode:
        def __init__(self):
            self.children = {}

    root = TrieNode()

    # Insert all numbers as binary into trie
    for num in nums:
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    max_xor = 0

    # For each number, find its best XOR partner
    for num in nums:
        node = root
        current_xor = 0

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Try to go opposite bit for max XOR
            opposite = 1 - bit

            if opposite in node.children:
                current_xor |= (1 << i)
                node = node.children[opposite]
            else:
                node = node.children[bit]

        max_xor = max(max_xor, current_xor)

    return max_xor


# Example usage
if __name__ == "__main__":
    print("Trie Algorithms Demo\n")

    # Test autocomplete
    print("--- Autocomplete ---")
    autocomplete = Autocomplete()
    words = ["apple", "application", "apply", "app", "banana", "band"]
    for word in words:
        autocomplete.insert(word)

    print(f"Words: {words}")
    print(f"Search 'apple': {autocomplete.search('apple')}")
    print(f"Starts with 'app': {autocomplete.starts_with('app')}")
    print(f"Suggestions for 'app': {autocomplete.get_suggestions('app')}")
    print(f"Suggestions for 'ban': {autocomplete.get_suggestions('ban')}")

    # Test wildcard dictionary
    print("\n--- Wildcard Dictionary ---")
    word_dict = WordDictionary()
    words = ["bad", "dad", "mad"]
    for word in words:
        word_dict.add_word(word)

    test_patterns = ["pad", "bad", ".ad", "b.."]
    for pattern in test_patterns:
        print(f"Search '{pattern}': {word_dict.search(pattern)}")

    # Test longest common prefix
    print("\n--- Longest Common Prefix ---")
    words_list = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interstellar", "internet", "internal"]
    ]
    for words in words_list:
        lcp = longest_common_prefix(words)
        print(f"{words} -> '{lcp}'")

    # Test word break
    print("\n--- Word Break ---")
    s = "leetcode"
    word_dict_list = ["leet", "code"]
    print(f"String: '{s}', Dictionary: {word_dict_list}")
    print(f"Can break: {word_break(s, word_dict_list)}")

    # Test replace words
    print("\n--- Replace Words ---")
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    result = replace_words(dictionary, sentence)
    print(f"Original: {sentence}")
    print(f"Replaced: {result}")

    # Test max XOR
    print("\n--- Maximum XOR Pair ---")
    nums = [3, 10, 5, 25, 2, 8]
    max_xor_val = max_xor_pair(nums)
    print(f"Numbers: {nums}")
    print(f"Maximum XOR: {max_xor_val}")
