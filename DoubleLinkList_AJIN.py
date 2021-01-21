# 双向链表，多了一个储存位置储存前向node的地址
# 注意有些到None就不能进行prev操作

class Node(object):
    """节点类，有元素储存空间和地址储存空间 node = Node(100)"""

    def __init__(self, elem=None):
        self.elem = elem
        self.next = None
        # 多一个前向储存空间prev
        self.prev = None

class DoubleLinklist(object):
    """双向链表类，节点都是双向操作的，均考虑空链表情况，可以直接继承SingleLinkList"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """返回链表长度"""
        # cur作为当前状态上的游标，表示当前节点 / count作为计数器，表示当前节点之前的个数
        # cur=None 和 cur.next=None 不一样，cur.next=None停在最后一个节点上,不进入节点，cur=None表示当前状态节点为空
        # 私有变量双下划线
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表，把数字都打印出来"""
        cur = self.__head
        while cur != None:
            # 如果不需要换行，加入一个参数end=" ", 即可按行输出
            print(cur.elem, end=" ")
            cur = cur.next
        # 如果需要换行，直接print(""),就可以按列输出
        print("")

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, item):
        """链表尾部添加元素,尾插法,不是加节点，内部包装好"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur


    def insert(self, pos, item):
        """指定位置添加元素"""
        # 不需要另外一个游标操作上一个节点
        cur = self.__head
        count = 0
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            # 在等于这个符号上要计算一下，如果等于就进入循环体
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """移除指定元素,双游标联动"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    # 头元素
                    self.__head = cur.next
                    # 仅一个头节点不需要连接回来
                    if cur.next:
                        cur.next.prev = None
                else:
                    # 中间元素
                    cur.prev.next = cur.next
                    # 尾节点不需要连接回来,用条件语句控制
                    if cur.next:
                        cur.next.prev = cur.prev
                return True
            else:
                cur = cur.next
        return False

    def search(self, item):
        """查找指定元素,返回下标"""
        cur = self.__head
        count = 0
        while cur != None:
            if cur.elem == item:
                return count
            else:
                cur = cur.next
                count += 1
        return False

"""重要！！！  测试模块编写方法"""
if __name__ == "__main__":
    sll = DoubleLinklist()
    print(sll.is_empty())
    print(sll.length())

    sll.add(1)
    print(sll.is_empty())
    print(sll.length())

    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    sll.travel()

    sll.add(7)
    sll.travel()
    sll.insert(2,100)
    sll.travel()
    sll.insert(-2,200)
    sll.travel()
    sll.insert(100,3000)
    sll.travel()

    print(sll.search(3000))
    print(sll.search(200))

    print(sll.remove(1000))
    sll.travel()
    print(sll.remove(100))
    sll.travel()