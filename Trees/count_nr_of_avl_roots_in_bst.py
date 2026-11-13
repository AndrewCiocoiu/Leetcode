def count_nr_of_avl_roots_in_bst(root):
    # To calculate nr of avl roots we need to know if the left child is a vlid avl tree and if the right child is a valid avl tree, the height of left and right child and the count of valid avl trees on the left and right side.
    # => (height, is_valid_tree tree_count)    
    def solve(root):
        if not root:
            return (0, True, 0)

        left = solve(root.left)
        right = solve(root.right)
        h = max(left[0], right[0]) + 1

        if left[1] and right[1] and abs(left[0] - right[0]) <= 1:
            return (h, True, left[2] + right[2] + 1)
        else:
            return (h, False, left[2] + right[2])

    return solve(root)[2]