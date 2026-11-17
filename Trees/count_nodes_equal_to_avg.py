# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        #(subtreesum, nr_of_nodes, nodes_equal_to_avg)

        def solve(root):
            if not root:
                return (0, 0, 0)
            
            subtreesum_left, nr_of_nodes_left, nodes_equal_to_avg_left = solve(root.left)
            subtreesum_right, nr_of_nodes_right, nodes_equal_to_avg_right = solve(root.right)

            subtreesum = subtreesum_left + subtreesum_right + root.val
            nr_of_nodes = nr_of_nodes_left + nr_of_nodes_right + 1

            avg = math.floor(subtreesum / nr_of_nodes)

            if avg == root.val:
                nodes_equal_to_avg = nodes_equal_to_avg_left + nodes_equal_to_avg_right + 1
            else:
                nodes_equal_to_avg = nodes_equal_to_avg_left + nodes_equal_to_avg_right

            return (subtreesum, nr_of_nodes, nodes_equal_to_avg)

        return solve(root)[2]