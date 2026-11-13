# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        # To know the max path sum at node x we need to know the max path sum on the left, the max path sum on on the right and to be able to calculate the max path sum at the current node aka we need the max 1 way down sum on the left and max 1 way down path sum on the righnt

        # => x = (down, max_path_sum)
        def solve(root):
            if not root:
                return (0, float("-inf"))

            left = solve(root.left)
            right = solve(root.right)

            best_left = max(0, left[0])
            best_right = max(0, right[0])

            down = max(best_left, best_right) + root.val
            max_sum = max(left[1], right[1], best_left + best_right + root.val)

            return (down, max_sum)
        
        return solve(root)[1]

            