class TrieNode():
    def __init__(self):
        self.children = {}
        self.eow = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c]=TrieNode()
                cur = cur.children[c]
            cur.eow = True
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        result = set()

        def dfs(r,c,root,word):
            if r<0 or c<0 or r>=ROWS or c>=COLS or not root or (r,c) in visited:
                return
            if board[r][c] not in root.children:
                return
            
            visited.add((r,c))
            
            node = root.children[board[r][c]]
            word+=board[r][c]
            if node.eow:
                result.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visited.remove((r,c))
            return

        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(result)
