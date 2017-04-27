import string
import sys
from heapq import merge


class Point:
    def __init__(self, x_coord, y_coord):
        self.x_coord = int(x_coord)
        self.y_coord = int(y_coord)

    def __repr__(self):
        return repr((self.x_coord, self.y_coord))


# Takes a list, list_a, and returns a sorted list.
def merge_sort(list_a, index):
    if len(list_a) < 2:
        return list_a
    mid = len(list_a) // 2
    left = list_a[:mid]
    right = list_a[mid:]
    left = merge_sort(left, index)
    right = merge_sort(right, index)
    return list(merge(left, right, index))


# def merge(left, right, index):
#     if len(left) == 0:
#         return right
#     elif len(right) == 0:
#         return left
#
#     merged_list = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i][index] < right[j][index]:
#             merged_list.append(left[i])
#             i += 1
#         else:
#             merged_list.append(right[j])
#             j += 1
#         if i == len(left):
#             return merged_list.extend(left[i:])
#         elif j == len(right):
#             return merged_list.extend(right[j:])
#         else:
#             return list("something went wrong", "real wrong")


def read_file_into_list(filename):
    file = open(filename, 'r')
    point_list = []
    for line in file:
        coords = line.split()
        # point = Point(coords[0], coords[1])
        point = (int(coords[0]), int(coords[1]))
        point_list.append(point)
    return point_list


def print_point_list(point_list):
    for point in point_list:
        # print("(" + str(point.x_coord) + ", " + str(point.y_coord) + ")")
        print("(" + str(point[0]) + ", " + str(point[1]) + ")")


def main():
    point_list = read_file_into_list("10points.txt")
    # sorted_by_x = sorted(point_list, key=lambda point: point.x_coord)
    # sorted_by_y = sorted(point_list, key=lambda point: point.y_coord)

    sorted_by_x = sorted(point_list, key=lambda point: point[0])
    sorted_by_y = sorted(point_list, key=lambda point: point[1])
    print_point_list(point_list)
    print("Now for the sorted_by_x list")
    print_point_list(sorted_by_x)
    print("Now for the sorted_by_y list")
    print_point_list(sorted_by_y)



if __name__ == "__main__":
	sys.exit(main())
