"""导入模块， from 模块名称（即.py的名称） import 函数名/类名称/*（全部导入）"""
from Queue_AJIN import Queue

"""继承单向队列，复用代码功能，已经把 is_empty 和 size 功能去掉"""
class DoubleEndQueue(Queue):

    def __init__(self):
        """在继承的时候，要把父类的初始化和需要参数传输进去，super().父类的函数名称(所需参数)"""
        super().__init__()
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0,item)

    def add_rear(self, item):
        self.__list.append(item)

    def remove_front(self):
        return self.__list.pop(0)

    def remove_rear(self):
        return self.__list.pop()

    def travel(self):
        print(self.__list)


if __name__ == "__main__":
    q = DoubleEndQueue()
    q.is_empty()
    print(q.size())

    q.add_front(1)
    q.add_front(2)
    q.add_rear(3)
    q.is_empty()
    print(q.size())
    q.travel()
    print(q.remove_front())
    q.travel()
    print(q.remove_rear())
    q.travel()