import copy
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
            self.root_node = p
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
    
    def find_max_node(self, node):
        """
        查找左子树中最大的节点
        """
        n = node
        if n == None:
            return None
        while n.right != None:
            n = n.right
        return n
    
    def find_min_node(self, node):
        """
        查找右子树中最小的节点
        """
        n = node
        if n == None:
            return None
        while n.left != None:
            n = n.left
        return n
    
    def is_leaf(self, node: TreeNode):
        return True if node.left == None and node.right == None else False
    
    def remove(self, node: TreeNode):
        """
        删除节点
        1、叶子节点直接删除
        2、先查找右子树最小值，若没有找左子树最大值
            （1）、找到的节点是直接子树，直接子节点替换父节点
            （2）、找到的节点不是直接子树，先替换，然后递归执行子节点删除操作
        """
        if self.is_leaf(node):
            self.remove_leaf(node)
        else:
            replace_node = self.find_min_node(node.right) if node.right != None else self.find_max_node(node.left)
            replace_node_copy = copy.copy(replace_node)

            if node == replace_node.parent:
                if node.val < node.parent.val:
                    node.parent.left = replace_node
                else:
                    node.parent.right = replace_node
                replace_node.parent = node.parent

                # 因为先从右边开始查的继承关系节点，所以不用管右边子树
                if replace_node != node.left:
                    replace_node.left = node.left
                    node.left.parent = replace_node
            else:
                # 连接删除节点的父节点和当前节点
                if node.parent != None:
                    if node.val < node.parent.val:
                        node.parent.left = replace_node
                    else:
                        node.parent.right = replace_node
                else:
                    self.root_node = replace_node
                replace_node.parent = node.parent

                # 连接删除节点的子树和当前节点
                replace_node.left = node.left
                replace_node.right = node.right
                # 左右子树都没有的话会前边直接走逻辑，这里只会走一个if
                if node.left != None:
                    node.left.parent = replace_node
                if node.right != None:
                    node.right.parent = replace_node
                
                self.remove(replace_node_copy)

    def remove_leaf(self, node: TreeNode):
        """
        删除叶子节点
        """
        cur_parent = node.parent
        # 将节点和父节点关联删除即删除了该节点
        if cur_parent != None:
            if node.val < cur_parent.val:
                cur_parent.left = None
            else:
                cur_parent.right = None
        else:
            # 删除的是根节点
            self.root_node = None


if __name__ == '__main__':
    bs_tree = BST(16)
    bs_tree.insert(9)
    bs_tree.insert(24)
    bs_tree.insert(12)
    bs_tree.insert(6)
    bs_tree.insert(20)
    bs_tree.insert(30)
    pre_res = bs_tree.pre_tree_walk(bs_tree.root_node, [])
    mid_res = bs_tree.mid_tree_walk(bs_tree.root_node, [])
    next_res = bs_tree.next_tree_walk(bs_tree.root_node, [])
    print(bs_tree)
    print(pre_res)
    print(mid_res)
    print(next_res)
    remove_node = bs_tree.find(9)
    bs_tree.remove(remove_node)
    pre_res = bs_tree.pre_tree_walk(bs_tree.root_node, [])
    mid_res = bs_tree.mid_tree_walk(bs_tree.root_node, [])
    next_res = bs_tree.next_tree_walk(bs_tree.root_node, [])
    print(pre_res)
    print(mid_res)
    print(next_res)
