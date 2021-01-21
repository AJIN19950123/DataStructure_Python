# 单项循环列表就是单向链表的尾节点连接到头节点行成一个循环

class Node(object):
    """节点类，有元素储存空间和地址储存空间 node = Node(100)"""

    def __init__(self, elem=None):
        self.elem = elem
        self.next = None

class SingleCycleLinklist(object):
    """单循环链表类,均考虑空链表情况"""

    def __init__(self, node=None):
        self.__head = node
        # 尾节点指向节点自己,且确定传递了节点才可操作
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """返回链表长度"""
        # cur作为当前状态上的游标，表示当前节点 / count作为计数器，表示当前节点之前的个数
        # cur=None 和 cur.next=None 不一样，cur.next=None停在最后一个节点上,不进入节点，cur=None表示当前状态节点为空
        # 私有变量双下划线
        cur = self.__head
        count = 1
        # 考虑空链表
        if self.is_empty():
            return 0
        else:
            # 已经无法采用cur != None这种判断条件，应采用cur.next,且尾结点无法被计算到
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        """遍历整个链表，把数字都打印出来"""
        cur = self.__head
        if self.is_empty():
            print("Empty List")
            return
        else:
            while cur.next != self.__head:
                # 如果不需要换行，加入一个参数end=" ", 即可按行输出
                print(cur.elem, end=" ")
                cur = cur.next
        # 如果需要换行，直接print(""),就可以按列输出
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素，头插法，需要找到尾结点"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        """链表尾部添加元素,尾插法,不是加节点，内部包装好"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            node.next = cur.next
            cur.next = node


    def insert(self, pos, item):
        """指定位置添加元素"""
        #游标无法操作上一个节点，所以prior定位在指定pos的上一个节点上
        prior = self.__head
        count = 0
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            # 在等于这个符号上要计算一下，如果等于就进入循环体
            while count < (pos-1):
                count += 1
                prior = prior.next
            node.next = prior.next
            prior.next = node

    def remove(self, item):
        """移除指定元素,双游标联动"""
        cur = self.__head
        prior = None
        # 空链表情况
        if self.is_empty():
            print("Empty List")
            return
        else:
            while cur.next != self.__head:
                if cur.elem == item:
                    # 头结点删除操作
                    if cur == self.__head:
                        # 找尾结点的游标
                        rear = self.__head
                        while rear.next != self.__head:
                            rear = rear.next
                        self.__head = cur.next
                        rear.next = cur.next
                    # 中间节点删除操作
                    else:
                        prior.next = cur.next
                    return True
                else:
                    prior = cur
                    cur = cur.next
            if cur.elem == item:
                # 有两种可能，一种是尾结点，还有一种是仅有一个头结点
                if cur == self.__head:
                    # 仅有一个头结点
                    self.__head = None
                else:
                    # 尾节点删除操作
                    prior.next = cur.next
            return False

    def search(self, item):
        """查找指定元素,返回下标"""
        cur = self.__head
        count = 0
        if self.is_empty():
            return False
        else:
            while cur.next != self.__head:
                if cur.elem == item:
                    return count
                else:
                    cur = cur.next
                    count += 1
            # 尾节点上没有进行比较
            if cur.elem == item:
                return count
            else:
                return False

"""重要！！！  测试模块编写方法"""
if __name__ == "__main__":
    sll = SingleCycleLinklist()
    print(sll.is_empty())
    print(sll.length())

    sll.add(1)
    sll.add(20)
    sll.travel()
    sll.append(3)
    sll.travel()
    sll.insert(-1,100)
    sll.travel()
    sll.insert(100,30)
    sll.travel()

    print(sll.is_empty())
    print(sll.length())

    print(sll.search(20))
    print(sll.search(30))
    sll.remove(20)
    sll.travel()
    sll.remove(5)
    sll.travel()
    sll.remove(100)
    sll.travel()
    sll.remove(30)
    sll.travel()
    sll.remove(3)
    sll.travel()
    sll.remove(1)
    sll.travel()
    sll.add(0)
    sll.travel()






