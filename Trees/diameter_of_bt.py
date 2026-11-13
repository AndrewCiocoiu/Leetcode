# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return (0, 0)
            
            left = solve(root.left)
            right = solve(root.right)

            h = max(left[0], right[0]) + 1
            d = max(left[1], right[1], left[0] + right[0])

            return (h, d)
            
        # diam at x = max(lefth + righth + 1, diam_left, diam_right) => we need to hold (diam, h)

        return solve(root)[1]

