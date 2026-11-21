"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def BFS(root):
            if not root:
                return

            q = deque([root])

            while q:
                current_level = []

                for i in range(len(q)):
                    curr_node = q.popleft()
                    current_level.append(curr_node)

                    if curr_node.left:
                        q.append(curr_node.left)
                    if curr_node.right:
                        q.append(curr_node.right)
                
                for i in range(len(current_level) - 1):
                    current_level[i].next = current_level[i + 1]
                current_level[-1].next = None        
        BFS(root)
        return root
        