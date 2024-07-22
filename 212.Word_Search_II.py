class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # add all words to Trie
        root = TrieNode()
        for w in words:
            root.add_word(w)


        # do dfs from every cell, if found a word, add to res

        def dfs(row, col, node, curr_word):
            # checks
            if (
                row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                board[row][col] not in node.children or 
                (row, col) in visit
            ):
                return

            curr_word += board[row][col]
            node = node.children[board[row][col]]

            # if reached end of word
            if node.end_of_word:
                res.add(curr_word)
 

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                visit.add((row, col))
                dfs(row + dr, col + dc, node, curr_word)
                visit.remove((row, col))

        res, visit = set(), set()
        ROWS, COLS = len(board), len(board[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)