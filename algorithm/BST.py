"""
二叉搜索树：
1、若左子树非空，则左子树上的所有节点的值均小于根节点的值.
2、若右子树非空，则右子树上的所有节点的关键字值均大于根节点的关键字值。
3、左、右子树本身也分别是一棵二叉查找树（二叉排序树）。
"""

# 定义 BST 的节点对象
class TreeNode():
    def __init__(self, x = None) -> None:
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self) -> str:
        return str(self.val)
    
class BST():
    """
    设置根节点
    """
    def __init__(self, node = None) -> None:
        node = TreeNode(node)
        self.root_node = node

    def insert(self, x):
        """
        插入操作
        """
        if self.is_exit(x):
            return
        p = TreeNode(x)
        if self.root_node == None:
            self.root_nooe = p
        else:
            cur = self.root_node
            pre = None
            while cur != None:
                pre = cur
                if cur.val < x:
                    cur = cur.right
                else:
                    cur = cur.left
            p.parent = pre
            if pre.val < x:
                pre.right = p
            else:
                pre.left = p

    def is_exit(self, k):
        """
        判断是否存在
        """
        cur = self.find(k)
        return True if cur != None else False
    
    def find(self, k):
        """
        查找
        """
        cur = self.root_node
        while cur != None and cur.val != k:
            if k < cur.val:
                cur = cur.left
            else:
                cur =  cur.right
        return cur

    def pre_tree_walk(self, n, arr):
        """
        前序遍历
        """
        if n != None:
            arr.append(n.val)
            self.pre_tree_walk(n.left, arr)
            self.pre_tree_walk(n.right, arr)
        return arr

    def mid_tree_walk(self, n, arr):
        """
        中序遍历
        """
        if n != None:
            self.mid_tree_walk(n.left, arr)
            arr.append(n.val)
            self.mid_tree_walk(n.right, arr)
        return arr

    def next_tree_walk(self, n, arr):
        """
        后序遍历
        """
        if n != None:
            self.next_tree_walk(n.left, arr)
            self.next_tree_walk(n.right, arr)
            arr.append(n.val)
        return arr
    
if __name__ == '__main__':
    bs_tree = BST(16)
    bs_tree.insert(9)
    bs_tree.insert(24)
    bs_tree.insert(20)
    pre_res = bs_tree.pre_tree_walk(bs_tree.root_node, [])
    mid_res = bs_tree.mid_tree_walk(bs_tree.root_node, [])
    next_res = bs_tree.next_tree_walk(bs_tree.root_node, [])
    print(bs_tree)
    print(pre_res)
    print(mid_res)
    print(next_res)
