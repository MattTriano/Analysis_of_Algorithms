import sys


def pascal_dynamic(i,j):
    triangle = [[0 for r in range(i)] for c in range(i)]
    for row in range(i):
        for col in range(row+1):
            if (col == 0) or (row == col):
                triangle[row][col] = 1
            else:
                triangle[row][col] = triangle[row-1][col] + triangle[row-1][col-1]
            if (row == i - 1) and (col == j - 1):
                return triangle


def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    arrows = [['  ' for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
                arrows[i + 1][j + 1] = "NW"
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    result_printer(lengths)
    result_printer(arrows)
    return result


def subset_sum(list_a, target):
    n = len(list_a)
    table = [[0 for row in range(target)] for col in range(n)]
    for i in range(n):
        table[i][0] = 1
        for s in range(1, target):
            if list_a[i] <= target:
                if table[i-1][s] == 1:
                    table[i][s] = 1
                else:
                    table[i][s] = max(table[i-1][s], table[i-1][s-list_a[i]])
    return table

def val_in_subset_sum(table, val):
    for i in range(len(table)):
        if table[i][val-1] == 1:
            return "TRUE"
    return "FALSE"


def result_printer(result):
    for line in result:
        print(str(line))


def table_printer(result):
    i_len = len(result)
    s_len = len(result[0])
    header = []
    for s in range(s_len+1):
        buffer = '| '
        if s >= 9:
            buffer = '|'
        header.append(str(s) + buffer)
    print(''.join(header))
    for i in range(i_len):
        row = [str(i) + '| ']
        for s in range(s_len):
            row.append(str(result[i][s]) + '| ')
        print(''.join(row))


def main():
    # triangle = pascal_dynamic(6, 4)
    # print("Pascal's Triangle at 6,4 is " + str(triangle[5][3]))
    # res = lcs("ACTCCTGAT", "TCAGGACT")
    # print(res)
    S = [1, 2, 4, 10, 20, 25]
    val = 18
    table = subset_sum(S, val)
    table_printer(table)
    print(str(val) + ' in this subset? ' + str(val_in_subset_sum(table, val)))


if __name__ == "__main__":
    sys.exit(main())