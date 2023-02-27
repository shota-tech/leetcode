# https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        old_to_new = {}

        def dfs(node: 'Node') -> 'Node':
            if node in old_to_new:
                return old_to_new[node]

            new = Node(node.val)
            old_to_new[node] = new

            for neighbor in node.neighbors:
                new.neighbors.append(dfs(neighbor))

            return new

        return dfs(node)
