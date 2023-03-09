"""
暴力重构维持平衡的树
构造函数需要存储的信息：
    1、左右子树编号
    2、当前节点的值
    3、以当前节点为根的树的大小和实际大小
    4、删除标记
"""

class TreeNode():
    def __init__(self, k) -> None:
        self.parent = None
        self.left = None
        self.right = None
        self.val = k
        self.size = 1
        self.f_size = 1
        self.exits = True

class ScapegoatTree():
    def __init__(self, alpha):
        self.root = None
        self.alpha = alpha

    def _insert_helper(self, node: TreeNode, val):
        if node is None:
            return TreeNode(val)
        node.size += 1
        node.f_size += 1
        if val < node.val:
            node.left = self._insert_helper(node.left, val)
            node.left.parent = node
        elif val > node.val:
            node.right = self._insert_helper(node.right, val)
            node.right.parent = node
        return node

    def insert(self, val):
        """
        插入：和二叉搜索树一样，只是在最后加一个判断树是否平衡
        """
        if self.root is None:
            self.root = TreeNode(val)
            return
        self.root = self._insert_helper(self.root, val)
        self.check()

    def remove(self, val):
        """
        删除：（惰性删除），先给要删除的节点打一个删除的标记
        实际大小就是没有被打入标记的节点数量，删除后要判断是
        否需要重构
        """

    def check(self, node):
        """
        判断是否需要重构：从根节点开始查找，找到需要重构的节点
        就，暴力重构子树
        需要重构的条件是当前节点的左子树或右子树的大小大于当前
        节点的大小乘一个平衡因子（0.5 ~ 1），一般是0.75或者
        以当前节点为根的子树内被删除的节点数量大于树大小的30%，
        """

    def rebuild(self, node):
        """
        暴力重构：把当前子树进行中序遍历拉成直线，然后用分治拎起来
        """

    def find(self, val):
        

    def size(self, node):
        if node is None:
            return 0
        return node.size
    
