
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        ## APPROACH: create a map of old -> new nodes and use dfs to fill that
        ## TIME: O(n + e)
        ## SPACE: O(n), maybe

        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                # returns the value of this node
                # key: value
                # orginal node: copy node
                # returns a new node i.e copy, that has been added
                return old_to_new[node]
            
            # if incoming node doesn't exist in map
            # then add
            copy = Node(node.val)       # create a new node
            old_to_new[node] = copy     # add this new node as a value with key being old node

            # call dfs on the neighbours of orginal node
            for nei in node.neighbors:
                # append neighbors to a newly created copy
                copy.neighbors.append(dfs(nei))

            return copy
        
        return dfs(node) if node else None
    