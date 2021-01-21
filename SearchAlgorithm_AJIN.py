

"""搜索算法"""

"""Binary Search二分查找算法，必须在有序序列且有下标查找方法里用，时间复杂度O(log(n))"""
"""1.把序列取中间值的索引 2.比较中间值和目标值 3.判断取左半边还是右半边 4.更改索引对的起始点 5.重新对半查找"""

# 递归方法
def BinarySearchRecusion(alist, item):

    n = len(alist)
    # 递归结束条件
    if n > 0:
        # 取序列的中间值索引 (0+n)//2
        mid = n // 2
        # 查找到目标值的情况
        if item == alist[mid]:
            return True
        # 左半边查找，返回查找情况
        elif item < alist[mid]:
            return BinarySearchRecusion(alist[:mid], item)
        # 右半边查找，返回查找情况
        else:
            return BinarySearchRecusion(alist[mid+1:], item)
    return False

# 非递归方法
def BinarySearchNonrecusion(alist, item):

    # 定义起始点位置
    n = len(alist)
    first = 0
    last = n - 1
    # 循环体，等号的时候存在一个元素
    while first <= last:
        # 更新mid
        mid = (first + last) // 2
        # 判断大小，改变下标的数值缩小判断空间
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


"""
树的概念
1.节点的度：即节点拥有子节点的个数
2.树的度：整个树的节点里面拥有最大的度
3.叶节点：度为0的节点
4.父节点：可以拥有多个子节点
5.子节点：只能拥有一个父节点
6.节点的层次：所在节点往根节点追的个数（包括自己）
7.树的深度&深度：所有节点中拥有的最大层次
8.森林：m>=0个互不相交的树

树的种类
1.二叉树：节点的最大度为2
2.完全二叉树：除了最底层（叶），其他层的节点的度都达到最大的度（为2）
3.满二叉树：全部节点的度为2
4.平衡二叉树（AVL）：任何节点的两个子树的深度差不大于1
5.排序二叉树：节点之间为有序的树
6.霍夫曼树：带权路径最短的二叉树

二叉树数学规律**
1.在二叉树的第i层上至多有2^(i-1)个节点(i>0)
2.深度为k的二叉树至多有2^k-1个节点(k>0)
3.任何一个二叉树，叶节点数为N0，而度数为2的节点总数为N2，则N0=N2+1
4.具有n个节点的完全二叉树的深度必为log2(n+1)
5.对完全二叉树，若从上到下，从左到右编号，编号为i的节点，其左孩子编号必为2i，右孩子编号必为2i+1;双亲的编号必为i/2

队列作为树的基础结构：
1.加入元素，queue = [A]
2.弹出元素，判断A的左右子树，queue = []
3.把左右子树加进队列，queue = [B, C]
4.弹出B判断左右子树，queue = [C]，加进队列，queue = [C, D, E]
5.弹出C判断左右子树，queue = [D, E]，加进队列，queue = [D, E, F, G]
6.继续循环
所以需要支持先进先出的数据结构，即为队列结构
"""


"""Binary Tree二叉树数据结构"""

# 采用队列结构作为树的基础数据结构
from Queue_AJIN import Queue

"""节点类"""
class Node(object):

    def __init__(self, elem=None):
        # 节点上数据的储存空间
        self.elem = elem
        # 左右树的节点地址储存空间
        self.lchild = None
        self.rchild = None

    def add(self, elem):
        self.elem = elem

"""树结构类"""
class BinaryTree(object):

    def __init__(self, node=None):
        # 初始节点挂在__root上
        self.__root = node

    def root(self):
        return self.__root

    # 加入新的树节点（广度遍历方法）
    def add(self, item):
        node = Node(item)
        # 没有初始节点挂在__root上结束
        if self.__root == None:
            self.__root = node
            return
        # 调用队列结构,存入已经有的root节点
        queue = Queue()
        queue.enqueue(self.__root)

        # 只要队列里有元素且没找到位置，就持续循环下去
        while queue.has_elem():
            # 从队列中取出现在的节点
            cur_node = queue.dequeue()
            # 从左子树判断新加入节点位置,加入后直接退出
            if cur_node.lchild == None:
                cur_node.lchild = node
                return
            else:
                queue.enqueue(cur_node.lchild)
            # 再判断右子树的节点，加入后直接退出
            if cur_node.rchild == None:
                cur_node.rchild = node
                return
            else:
                queue.enqueue(cur_node.rchild)

    """广度遍历（层次遍历）
    队列作为树的基础结构：
    1.加入元素，queue = [A]
    2.弹出元素，判断A的左右子树，queue = []
    3.把左右子树加进队列，queue = [B, C]
    4.弹出B判断左右子树，queue = [C]，加进队列，queue = [C, D, E]
    5.弹出C判断左右子树，queue = [D, E]，加进队列，queue = [D, E, F, G]
    6.继续循环
    所以需要支持先进先出的数据结构，即为队列结构"""
    def BreadthFirstTravel(self):
        queue = Queue()
        if self.__root == None:
            print("Tree is empty")
            return
        queue.enqueue(self.__root)
        while queue.has_elem():
            cur_node = queue.dequeue()
            print(cur_node.elem, end=" ")
            if cur_node.lchild != None:
                queue.enqueue(cur_node.lchild)
            if cur_node.rchild != None:
                queue.enqueue(cur_node.rchild)
        print("")
        print("finish")
        return

    """深度遍历（三种方法），每次顺序都按一颗完整的树来取值，然后再拓展树（把根往下移），再取值"""
    """采用递归方法，简单，要传入参数"""
    def DepthFirstTravel_preorder(self, cur_root):
        # 先序遍历（根左右）
        # 退出递归的条件为当前节点为空
        if cur_root == None:
            return
        else:
            # 运用递归的方法，先根节点打印，再左子树，右子树，把根的权限一点点往下移动
            # 内部递归要用self
            print(cur_root.elem, end=" ")
            self.DepthFirstTravel_preorder(cur_root.lchild)
            self.DepthFirstTravel_preorder(cur_root.rchild)

    def DepthFirstTravel_inorder(self, cur_root):
        # 中序遍历（左根右）
        # 退出递归的条件为当前节点为空
        if cur_root == None:
            return
        else:
            # 运用递归的方法，先左子树打印，再根，右子树，把根的权限一点点往下移动
            # 内部递归要用self
            self.DepthFirstTravel_inorder(cur_root.lchild)
            print(cur_root.elem, end=" ")
            self.DepthFirstTravel_inorder(cur_root.rchild)

    def DepthFirstTravel_postorder(self, cur_root):
        # 后序遍历（左右根）
        # 退出递归的条件为当前节点为空
        if cur_root == None:
            return
        else:
            # 运用递归的方法，先左子树打印，再右子树，最后根，把根的权限一点点往下移动
            # 内部递归要用self
            self.DepthFirstTravel_postorder(cur_root.lchild)
            self.DepthFirstTravel_postorder(cur_root.rchild)
            print(cur_root.elem, end=" ")

    """通过遍历结果可以复现一棵树结构：
       至少需要两个序列，且一定要有中序序列：中序序列可以把左右子树分开，先序+中序 / 中序+后序 都可以复现结构
       1.先用根把中序的左右子树分开
       2.用先序后序确定根
       3.用中序确认左右子树的顺序
       4.以此类推"""




"""测试程序"""
if __name__ == "__main__":

    node = Node(0)
    tree = BinaryTree(Node(0))
    tree.BreadthFirstTravel()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.BreadthFirstTravel()
    tree.DepthFirstTravel_preorder(tree.root())
    print("")
    tree.DepthFirstTravel_inorder(tree.root())
    print("")
    tree.DepthFirstTravel_postorder(tree.root())

