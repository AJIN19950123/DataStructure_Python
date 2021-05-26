import numpy as np
if __name__ == "__main__":
    alist = [1, 2, 3, -8, 2, 3, 4, -1, 2, 3, -9, 2]
    sum_num = 0
    max_num = float('-inf')
    left = 0
    right = 0

    for index, value in enumerate(alist):
        sum_num += value
        if sum_num < 0:
            sum_num = 0
            left = index + 1
        if max_num < sum_num:
            max_sum = sum_num
            right = index+1
    print(alist[left:right])
    print("Masterpiece")




