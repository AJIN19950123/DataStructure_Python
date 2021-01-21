# python中的等号是把对象的地址指向赋给新的标签
# a = 10 是指10整数存储的地址指向给了a这个标签，并不是把值给了a
# next = node2 是把下一个节点的地址指向给了next
# 在python中给的都是地址，所以可以实现 a, b = b, a

class Node(object):
    """节点类，有元素储存空间和地址储存空间 node = Node(100)"""

    def __init__(self, elem=None):
        self.elem = elem
        self.next = None

class SingleLinklist(object):
    """单链表类，实现存储数据和查找基本属性,均考虑空链表情况"""

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
        node.next = self.__head
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
        while cur != None:
            if cur.elem == item:
                # 删除操作
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    prior.next = cur.next
                return True
            else:
                prior = cur
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
    sll = SingleLinklist()
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
    print(sll.remove(200))
    sll.travel()








