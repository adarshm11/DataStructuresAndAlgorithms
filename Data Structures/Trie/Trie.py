class TrieNode:
    """Node class for Trie."""

    def __init__(self):
        """Initialize a trie node."""
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Trie (Prefix Tree) data structure implementation.
    Efficient for storing and searching strings with common prefixes.
    """

    def __init__(self):
        """Initialize an empty trie."""
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the trie.

        Args:
            word (str): The word to insert
        """
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True

    def search(self, word):
        """
        Search for a complete word in the trie.

        Args:
            word (str): The word to search for

        Returns:
            bool: True if word exists, False otherwise
        """
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        Check if any word in the trie starts with the given prefix.

        Args:
            prefix (str): The prefix to search for

        Returns:
            bool: True if prefix exists, False otherwise
        """
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

    def delete(self, word):
        """
        Delete a word from the trie.

        Args:
            word (str): The word to delete

        Returns:
            bool: True if word was deleted, False if word not found
        """
        def _delete_helper(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False

                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            child_node = node.children[char]
            should_delete_child = _delete_helper(child_node, word, index + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word

            return False

        return _delete_helper(self.root, word, 0)

    def get_all_words(self):
        """
        Get all words stored in the trie.

        Returns:
            list: List of all words in the trie
        """
        words = []

        def _traverse(node, prefix):
            if node.is_end_of_word:
                words.append(prefix)

            for char, child_node in node.children.items():
                _traverse(child_node, prefix + char)

        _traverse(self.root, "")
        return words

    def get_words_with_prefix(self, prefix):
        """
        Get all words that start with the given prefix.

        Args:
            prefix (str): The prefix to search for

        Returns:
            list: List of words with the given prefix
        """
        node = self.root

        # Navigate to the end of the prefix
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # Collect all words from this point
        words = []

        def _traverse(node, current_word):
            if node.is_end_of_word:
                words.append(current_word)

            for char, child_node in node.children.items():
                _traverse(child_node, current_word + char)

        _traverse(node, prefix)
        return words

    def count_words(self):
        """
        Count the number of words in the trie.

        Returns:
            int: Number of words
        """
        count = 0

        def _count(node):
            nonlocal count
            if node.is_end_of_word:
                count += 1

            for child_node in node.children.values():
                _count(child_node)

        _count(self.root)
        return count

    def is_empty(self):
        """
        Check if the trie is empty.

        Returns:
            bool: True if empty, False otherwise
        """
        return len(self.root.children) == 0

    def clear(self):
        """Clear all words from the trie."""
        self.root = TrieNode()

    def longest_common_prefix(self):
        """
        Find the longest common prefix among all words in the trie.

        Returns:
            str: The longest common prefix
        """
        node = self.root
        prefix = ""

        while len(node.children) == 1 and not node.is_end_of_word:
            char = list(node.children.keys())[0]
            prefix += char
            node = node.children[char]

        return prefix

    def __contains__(self, word):
        """
        Check if a word is in the trie using 'in' operator.

        Args:
            word (str): The word to check

        Returns:
            bool: True if word exists, False otherwise
        """
        return self.search(word)

    def __str__(self):
        """String representation of the trie."""
        words = self.get_all_words()
        return f"Trie({len(words)} words: {words[:10]}{'...' if len(words) > 10 else ''})"
