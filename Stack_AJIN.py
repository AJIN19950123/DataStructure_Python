# 链表就是一种存储数据的结构，而栈和队列为方法实现方式（取数据的方法）
# 栈 Last In First Out 单端 / 队列 First In First Out 双端

class Stack(object):

    def __init__(self):
        """需要一个储存数据的结构"""
        self.__list = []

    def size(self):
        """栈内元素个数"""
        print(len(self.__list))

    def is_empty(self):
        """判断是否为空栈"""
        if len(self.__list) == 0:
            print("Stack is empty")
        else:
            print("Stack is not empty")

    def push(self, item):
        """压元素入栈，list结构尾节点快"""
        self.__list.append(item)

    def pop(self):
        """弹元素出栈"""
        self.__list.pop()

    def peek(self):
        """访问栈顶元素"""
        print(self.__list[-1])

    def travel(self):
        print(self.__list)

if __name__ == "__main__":
    s = Stack()
    s.push(100)
    s.push(200)
    s.push(300)
    s.travel()
    s.pop()
    s.travel()
    s.is_empty()
    s.size()
    s.peek()
