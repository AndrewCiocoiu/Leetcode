class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        def find_depth(node):
            if not node:
                return 0
            return max(find_depth(node.left), find_depth(node.right)) + 1
        
        depth = find_depth(root)

        def get_left_val(node, curr_depth):
            if not node:
                return None
            if curr_depth == depth:
                return node.val
            
            left = get_left_val(node.left, curr_depth + 1)
            if left is not None:
                return left
            
            return get_left_val(node.right, curr_depth + 1)
        
        return get_left_val(root, 1)