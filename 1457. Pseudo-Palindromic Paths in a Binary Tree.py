# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    '''
    APPROACH-1: check path len and check odd/even occurances
    APPROACH-2: check odd occurances, should be <= 1 for valid pseudo-palindromic path
    APPROACH-3: bitwise XOR

    '''
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        table = {}          # num -> occurance
        count = 0

        def dfs(node, levels):
            nonlocal count

            if not node:         # terminating condition
                return

            table[node.val] = table.get(node.val, 0) + 1
            
            # check if it's a leaf node
            if not node.left and not node.right:
                
                # check if len is odd
                if levels % 2:
                    odd_count, even_count = 0, 0
                    for occ in table.values():
                        if occ % 2:
                            odd_count += 1
                        else:
                            even_count += 1
                    
                    # there should only be one key with odd occurance, every other key should have even occurance
                    if odd_count == 1 and len(table) - even_count == 1:
                        count += 1
                
                # check if len is even
                else:
                    print("$$$$$$$")
                    even_count = 0
                    for occ in table.values():
                        if not occ % 2:
                            even_count += 1

                    # every key should have even occurance
                    if len(table) == even_count:
                        count += 1

            dfs(node.left, levels + 1)
            dfs(node.right, levels + 1)
            table[node.val] -= 1

        dfs(root, 1)
        return count

        ## OBSERVATION:
        # it doesn't matter that if the path len is even or odd
        # i.e path_len (levels) doesn't even matter
        # if there are 2 or more digits with odd occurances, it can't be a psedo-palindromic path
        # a valid pseudo-palindromic path is one with only 0 or 1 digit with odd occurances

        # VALID
        # 232 or 23332      1 digit with odd occurance
        # 3223 or 22        0 digit with odd occurance

        # INVALID
        # 1233 OR 123       2 or 2+ digits with odd occurances
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        table = {}          # num -> occurance
        count = 0

        def dfs(node):
            nonlocal count

            if not node:         # terminating condition
                return

            table[node.val] = table.get(node.val, 0) + 1
            
            # check if it's a leaf node
            if not node.left and not node.right:
                odd_count = 0
                for v in table.values():
                    if v % 2:
                        odd_count += 1

                if odd_count <= 1:
                    count += 1

            dfs(node.left)
            dfs(node.right)
            table[node.val] -= 1        # very important to backtrack, remove the key

        dfs(root)
        return count