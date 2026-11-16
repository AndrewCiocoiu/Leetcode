class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        def solve(node):
            if not node:
                return (-1, -1, 0)
            
            _, left_then_right, max_l = solve(node.left)
            right_then_left, _, max_r = solve(node.right)

            go_left = left_then_right + 1
            go_right = right_then_left + 1

            overall_max = max(go_left, go_right, max_l, max_r)

            return (go_left, go_right, overall_max)
        
        return solve(root)[2]