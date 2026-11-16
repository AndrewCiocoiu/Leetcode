# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        #(curr_path_size, max_path_size)
        def solve(root):
            if not root:
                return (0, 0)
            
            currPathL, maxPathL = solve(root.left)
            currPathR, maxPathR = solve(root.right)

            leftPath = currPathL + 1 if root.left and root.left.val == root.val else 0
            rightPath = currPathR + 1 if root.right and root.right.val == root.val else 0
            
            max_path_size = max(leftPath, rightPath, leftPath + rightPath, maxPathL, maxPathR)

            return (max(leftPath, rightPath), max_path_size)
        
        return solve(root)[1]
        