import sys

from math import floor
from heapq import merge


# Takes a list
def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def naive(a, b, c=0):
    x = a
    y = b
    z = 0
    while x > c:
        z = z + y
        x = x - 1
    return z


def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print(y)


def clique(n):
    k = 0
    print("in a clique...")
    for j in range(n):
        print("eval'd range j")
        for i in range(j):
            print("eval'd range i")
            print(i, "is friends with", j)
            k += 1
    return k


def russian(a, b, c=0):
    x = a; y = b; z = 0
    while x > c:
        if x % 2 == 1:
            z += y
            y = y << 1
            x = x >> 1
    return z


def recursive_max(A):
    if (len(A) == 1):
        return A[0]
    elif (len(A) == 2):
        if (A[0] > A[1]):
            return A[0]
        else:
            return A[1]
    else:
        mid = floor(len(A)/2)
        half1 = recursive_max(A[0:mid])
        half2 = recursive_max(A[mid+1:len(A)])
        return recursive_max([half1, half2])


def quicksort(a):
    left = []
    pivots = []
    right = []
    if len(a) <= 1:
        return a
    else:
        pivot = a[len(a)-1]
        for i in a:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                pivots.append(i)
        left = quicksort(left)
        right = quicksort(right)
        return left + pivots + right


def main():
    A = [1,54,56,23,7,63514,125,852,3,4,9,21,-65]
    # A_max = recursive_max(A)
    # print("max in list is " + str(A_max))

    # print(A[0:2])
    m = [6, 4, 9, 8, 5, 10, 1, 3]
    # sorted_m = merge_sort(m, 0)
    sorted_m = quicksort(m)
    print(str(m) + " is sorted to " + str(sorted_m))






if __name__ == "__main__":
	sys.exit(main())
