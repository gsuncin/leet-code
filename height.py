def height(root, c=0):
    if not root:
        return c -1
    c+=1
    left = height(root.left, c)
    right = height(root.right, c)
    return max(left, right)