"""
236. 二叉树的最近公共祖先
"""
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q: return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if not left: return right
    if not right: return left
    return root