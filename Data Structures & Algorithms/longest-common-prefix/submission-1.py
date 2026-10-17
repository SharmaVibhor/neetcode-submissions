class TrieNode:
    def __init__(self):
        self.trie = {} # c->TrieNode
        self.eow = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.root = TrieNode()
        res = ""

        for w in strs:
            node = self.root
            for i in range(len(w)):
                if w[i] not in node.trie:
                    node.trie[w[i]] = TrieNode()
                node = node.trie[w[i]]
            node.eow = True
        
        while len(self.root.trie) == 1 and self.root.eow == False:
            c = list(self.root.trie.keys())[0]
            res += c
            self.root = self.root.trie[c]
        
        return res

        


        