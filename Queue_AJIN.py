# 单端队列结构

class Queue(object):

    def __init__(self):
        """数据存储结构"""
        self.__list = []

    def is_empty(self):
        if self.size() == 0:
            print("Queue is empty")
        else:
            print("Queue is not empty")

    def has_elem(self):
        if self.size() == 0:
            return 0
        else:
            return 1

    def size(self):
        return len(self.__list)

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        return self.__list.pop(0)

    def travel(self):
        print(self.__list)

if __name__ == "__main__":
    q = Queue()
    q.is_empty()
    print(q.size())

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.is_empty()
    print(q.size())
    q.travel()
    print(q.dequeue())
    print(q.dequeue())
    q.travel()



