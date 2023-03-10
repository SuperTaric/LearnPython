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
    def __init__(self, alpha = 0.75):
        self.root = None
        self.alpha = alpha
        self.nodes = []

    def _insert_helper(self, node: TreeNode, val):
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert_helper(node.left, val)
            node.left.parent = node
        elif val > node.val:
            node.right = self._insert_helper(node.right, val)
            node.right.parent = node
        node.size += 1
        node.f_size += 1
        self.check(self.root, node)
        return node

    def insert(self, val):
        """
        插入：和BST一样，只是在最后加一个判断树是否平衡
        """
        if self.root is None:
            self.root = TreeNode(val)
            return
        self.root = self._insert_helper(self.root, val)

    def remove(self, val):
        """
        删除：（惰性删除），先给要删除的节点打一个删除的标记
        实际大小就是没有被打入标记的节点数量，删除后要判断是
        否需要重构
        """
        r_node = self.find(val)
        if r_node is None:
            return False
        r_node.exits = False
        r_node.f_size -= 1
        self.check(self.root, r_node)
            

    def check(self, node: TreeNode, end_node: TreeNode):
        """
        判断是否需要重构：从根节点开始查找，找到需要重构的节点
        就，暴力重构子树
        需要重构的条件是当前节点的左子树或右子树的大小大于当前
        节点的大小乘一个平衡因子（0.5 ~ 1），一般是0.75或者
        以当前节点为根的子树内被删除的节点数量大于树大小的30%，
        """
        if node.val == end_node.val:
            return
        if self.size(node.left) > self.size(node) * self.alpha or self.size(node.right) > self.size(node) * self.alpha or self.size(node) - node.f_size > self.size(node) * 0.3 :
            self.rebuild(node)
            self.update(self.root, node)
        self.check(node.right, end_node) if node.val < end_node.val else self.check(node.left, end_node)
    
    def ldr(self, node: TreeNode):
        """
        中序遍历
        """
        if node is None:
            return
        self.ldr(node.left)
        if node.exits:
            self.nodes.append(node)
        self.ldr(node.right)

    def lift(self, start, end, parent: TreeNode):
        """
        分治重构
        为左右子树和父节点赋值，重新计算大小，然后递归执行
        """
        if start > end:
            return
        mid = (start + end) // 2
        # 值相同时候位置左移
        while start < mid and self.nodes[start].val == self.nodes[mid]:
            mid -= 1
        node: TreeNode = self.nodes[mid]
        if parent is None:
            self.root = node
        else:
            node.parent = parent
        node.left = self.lift(start, mid - 1, node)
        node.right = self.lift(mid + 1, end, node)
        node.size = self.size(node.left) + self.size(node.right) + 1
        node.f_size = self.size(node.left) + self.size(node.right) + 1
        return node

    def rebuild(self, node: TreeNode):
        """
        暴力重构：把当前子树进行中序遍历，然后用分治重构
        """
        self.nodes.clear()
        self.ldr(node)
        if len(self.nodes) == 0:
            return
        new_node = self.lift(0, len(self.nodes), node.parent)
        # 重构完的子树挂接到父节点
        if node.parent.left > new_node.val:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        node.parent.size = self.size(node.parent.left) + self.size(node.parent.right) + 1
        node.parent.f_size = self.size(node.parent.left) + self.size(node.parent.right) + 1

    def update(self, s_node: TreeNode, e_node: TreeNode):
        """
        重构完子树更新重构节点上边的size
        """
        if s_node is None:
            return
        if s_node.val > e_node:
            self.update(s_node.left, e_node)
        else:
            self.update(s_node.right, e_node)
        s_node.size = self.size(s_node.left) + self.size(s_node.right) + 1
        
    def find(self, val):
        node = self.root
        while node is not None:
            if val == node.val:
                return node
            elif val > node.val:
                node = node.right
            else:
                node = node.left

    def size(self, node):
        if node is None:
            return 0
        return node.size
    
