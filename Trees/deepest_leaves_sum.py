# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        def find_depth(root):
            if not root:
                return 0
            
            return max(find_depth(root.left), find_depth(root.right)) + 1

        max_depth = find_depth(root)

        def find_sum(root, curr_depth):
            if not root or curr_depth == max_depth:
                return 0 if not root else root.val
            
            return find_sum(root.left, curr_depth + 1) + find_sum(root.right, curr_depth + 1)
        
        return find_sum(root, 1)

