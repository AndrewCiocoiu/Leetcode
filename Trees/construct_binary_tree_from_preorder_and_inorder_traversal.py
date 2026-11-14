# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        root_pos = defaultdict(int)
        for idx, el in enumerate(inorder):
            root_pos[el] = idx

        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            mid = root_pos[root_val]
            left_size = mid - in_left

            root.left = helper(pre_left + 1, pre_left + left_size, in_left, mid - 1)
            root.right = helper(pre_left + left_size + 1, pre_right, mid + 1, in_right)

            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
