class Node:

    def __init__(self, char='', isWord=False):

        self.char = char
        self.isWord = isWord

        self.children = dict()

class Trie:

    def __init__(self, words) -> None:

        self.main = Node()

        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:

        main = self.main

        for char in word:

            if char not in main.children:

                main.children[char] = Node(char=char)

            main = main.children[char]

        main.isWord = True

    def dfsWords(self, node: Node, words, word):

        word.append(node.char)

        for child in node.children:
            self.dfsWords(node.children[child], words, word)


        if node.isWord:
            words.append(''.join(word))

        if word:
            word.pop()

    def search(self, letter, node, prefix=""):

        if not node:
            node = self.main

        if letter in node.children:
            node = node.children[letter]
            words = list()
            self.dfsWords(node, words, [])
            words = sorted([prefix + word for word in words])[0:3]
            return words, node

        else:
            return [], Node()

class Solution:

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        T = Trie(products)
        output = list()
        node = None

        for index, letter in enumerate(searchWord):
            out, node = T.search(letter, node, searchWord[0:index])
            output.append(out)

        return output
