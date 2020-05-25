"""
Implement a trie with insert, search, and startsWith methods.

Example:

    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // returns true
    trie.search("app");     // returns false
    trie.startsWith("app"); // returns true
    trie.insert("app");
    trie.search("app");     // returns true

Note:
    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.
"""
import collections


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = set()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.hash.add(word)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.hash


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for word in self.hash:
            if word.startswith(prefix):
                return True
        return False


class Node:

    def __init__(self,value):
        self.value=value
        self.childs = {}
        self.end_word = False

    def isChild(self,value):
        if value in self.childs:
            return True
        return False

    def addChild(self,value):
        self.childs[value] = Node(value)

    def getChild(self,value):
        return self.childs[value]

    def setEnd(self):
        self.end_word = True

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inserted_words = collections.defaultdict(int) # stores the words for quick lookup
        self.root = Node("-") # create null node

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.inserted_words[word] = 1
        current_node = self.root
        for c in word:
            if current_node.isChild(c)==False:
                current_node.addChild(c)
            current_node = current_node.getChild(c)
        current_node.setEnd()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return True if self.inserted_words[word]!=0 else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        for c in prefix:
            if current_node.isChild(c)==False:
                return False
            current_node = current_node.childs[c]
        return True

trie = Trie();
trie.insert("apple");
print(trie.search("apple"));
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app");
print(trie.search("app"))
