# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        def BFS(root):
            q = deque([root])

            if not root:
                return 0

            last_sum = 0

            while q:
                curr_level = []
                for i in range(len(q)):
                    curr_node = q.popleft()
                    curr_level.append(curr_node.val)

                    if curr_node.left:
                        q.append(curr_node.left)
                    if curr_node.right:
                        q.append(curr_node.right)
                
            
            return sum(curr_level)
        
        return BFS(root)