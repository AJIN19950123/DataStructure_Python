# 时间复杂度带规模参数 a+b+c = N T(N) = N**3*2
# 大O记法


# List的四种生成方式
# 1. Li = Li1 +Li2
# 2. Li = [i for i in range(1000)]
# 3. Li = list(range(1000))
# 4. Li = []
# 	 for i in range(1000):
# 	 	Li.append(i)
# List 常用函数
# append(元素) 只能添加一个元素，在list尾部添加
# insert(位置，元素) 只能添加一个元素，可指定位置添加，队尾效率远大于队头
# extend([元素,]) 可以添加一整个List和可迭代对象
# pop(位置) 默认队尾弹出元素

# 计时器 class Timer("function name statement", "import function")
import timeit
from timeit import Timer

def test1():
	li = []
	for i in range(10000):
		li.append(i)

def test2():
	li = []
	for i in range(10000):
		li = li + [i]

def test3():
	li = [i for i in range(10000)]

def test4():
	li = list(range(10000))

def test5():
	li = []
	for i in range(10000):
		li.extend([i])

def test6():
	li = []
	for i in range(10000):
		li.insert(0,i)

timer1 = Timer("test1()", "from __main__ import test1")
print("append:", timer1.timeit(1000))

timer2 = Timer("test2()", "from __main__ import test2")
print("+:", timer2.timeit(1000))

timer3 = Timer("test3()", "from __main__ import test3")
print("[i for i in range]", timer3.timeit(1000))

timer4 = Timer("test4()", "from __main__ import test4")
print("list(range())", timer4.timeit(1000))

timer5 = Timer("test5()", "from __main__ import test5")
print("extend:", timer5.timeit(1000))

timer6 = Timer("test6()", "from __main__ import test6")
print("insert:", timer6.timeit(1000))