import string
import sys
from heapq import merge

import math
# from math import sqrt, inf


class Point:
    def __init__(self, x_coord, y_coord):
        self.x_coord = int(x_coord)
        self.y_coord = int(y_coord)

    def __repr__(self):
        return repr((self.x_coord, self.y_coord))

    def dist(self, other):
        dx = self.x_coord - other.x_coord
        dy = self.y_coord - other.y_coord
        return math.sqrt(dx**2 + dy**2)


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
        point = Point(coords[0], coords[1])
        point_list.append(point)
    return point_list


def print_point_list(point_list):
    for point in point_list:
        print("(" + str(point.x_coord) + ", " + str(point.y_coord) + ")")


def brute_force_check(point_set):
    dist_p0p1 = point_set[0].dist(point_set[1])
    if len(point_set) == 3:
        dist_p0p2 = point_set[0].dist(point_set[2])
        dist_p1p2 = point_set[1].dist(point_set[2])
        if dist_p0p1 <= dist_p0p2 and dist_p0p1 <= dist_p1p2:
            return point_set[0], point_set[1], dist_p0p1
        elif dist_p0p2 <= dist_p1p2:
            return point_set[0], point_set[2], dist_p0p2
        else:
            return point_set[1], point_set[2], dist_p1p2
    else:
        return point_set[0], point_set[1], dist_p0p1


def closest_pair_in_body(x_sorted, y_sorted):
    list_length = len(x_sorted)
    if list_length <= 1:
        return x_sorted[0], None, math.inf
    elif list_length <= 3:
        return brute_force_check(x_sorted)
    else:
        mid = len(x_sorted) // 2
        x_sorted_left = x_sorted[:mid]
        x_sorted_right = x_sorted[mid:]
        y_sorted_left, y_sorted_right = [], []
        mid_x_val = x_sorted_left[len(x_sorted_left)-1].x_coord
        for point in y_sorted:
            if point.x_coord <= mid_x_val:
                y_sorted_left.append(point)
            else:
                y_sorted_right.append(point)
        (left_candidate_pt1, left_candidate_pt2, delta_left) = closest_pair_in_body(x_sorted_left, y_sorted_left)
        (right_candidate_pt1, right_candidate_pt2, delta_right) = closest_pair_in_body(x_sorted_right, y_sorted_right)
        if delta_left <= delta_right:
            candidate = closest_pair_over_edges(left_candidate_pt1, left_candidate_pt2, delta_left, y_sorted)
        else:
            candidate = closest_pair_over_edges(right_candidate_pt1, right_candidate_pt2, delta_right, y_sorted)
        


def closest_pair_over_edges(point1, point2, delta_p1p2, y_sorted):
    close_points = []
    for point in y_sorted:
        if abs(point.x_coord - mid_x_val) < candidate[2]:
            close_points.append(point)
    num_closer_pts = len(close_points)


# todo: finish timer
# def algo_timer(point_list):
#     n = len(point_list)
#     print('For input size n = ' + str(n) + ', the algorithm took  ' + str()


def closest_pair(n):
    if n == 10:
        point_list = read_file_into_list("10points.txt")
    elif n == 100:
        point_list = read_file_into_list("100points.txt")
    elif n == 1000:
        point_list = read_file_into_list("1000points.txt")
    else:
        print("Invalid number entered, enter 10, 100, or 1000 next time. ")
        print("We'll use the 10 point list this time. ")
        point_list = read_file_into_list("10points.txt")
    x_sorted = sorted(point_list, key=lambda point: point.x_coord)
    y_sorted = sorted(point_list, key=lambda point: point.y_coord)
    (point1, point2, delta_p1p2) = closest_pair_in_body(x_sorted, y_sorted)
    print("Closest Points are " + str(point1) + " and " + str(point2) +
          ", which are separated by distance " + str(delta_p1p2))


def main():
    # point_list = read_file_into_list("10points.txt")
    # sorted_by_x = sorted(point_list, key=lambda point: point.x_coord)
    # sorted_by_y = sorted(point_list, key=lambda point: point.y_coord)
    closest_pair(10)


    # print("brute force check vals: " + str(sorted_by_y[0:3]))
    # print("brute force check: " + str(brute_force_check(sorted_by_y[0:3])))


if __name__ == "__main__":
	sys.exit(main())
