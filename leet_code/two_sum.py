import time
import sys


def two_sum_nlgn(array, target, count=0):
    array.sort()
    index_l = 0
    index_h = len(array) - 1
    count += 4
    while (index_l < index_h):
        if array[index_l] + array[index_h] == target:
            count += 2
            return index_l, index_h, count
        elif array[index_l] + array[index_h] > target:
            count += 3
            index_h -= 1
        else:
            count += 4
            index_l += 1
    return None, None, count


def fun_timer(func, array, target):
    if func == 1:
        func_name = "O(n*lg(n))"
        start = time.time()
        (index_l, index_h, count) = two_sum_nlgn(array, target)
        end = time.time()
    else:
        print("Invalid function. Next time, enter a valid function Code")
        print("Code) Function ")
        print("   1) O(n*lg(n))")
        print("   2) O(n^2)")

    if index_l:
        print("The " + str(func_name) + " function took " + str(end - start) +
              " seconds to run and performed " + str(count) + " operations")


def main():
    # array = [5, 8, 2, 7, 12, 9, 123, 71, 32, 1, 3, 91, 14, 17, 23]
    # fun_timer(1, array, 12)
    a = [0, 1]
    print(len(a))


if __name__ == "__main__":
    sys.exit(main())
