# 双端队列结构

class DoubleEndQueue(object):

    def __init__(self):
        """数据存储结构"""
        self.__list = []

    def is_empty(self):
        if self.size() == 0:
            print("Queue is empty")
        else:
            print("Queue is not empty")

    def size(self):
        return len(self.__list)

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