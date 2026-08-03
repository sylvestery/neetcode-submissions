"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodeMapping = {
            node: Node(node.val)
        }
        q = deque([node])
        while q:
            curr = q.popleft()
            for kid in curr.neighbors:
                if kid not in nodeMapping:
                    nodeMapping[kid] = Node(kid.val)
                    q.append(kid)
                nodeMapping[curr].neighbors.append(nodeMapping[kid])
        


        return nodeMapping[node]