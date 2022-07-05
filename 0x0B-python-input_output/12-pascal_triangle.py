#!/usr/bin/env python3
"""Calculate Pascal's Triangle"""
import sys

def get_triangle(num):
    """return 2D list of triangle"""
    ret = [[1]]
    for i in range(1, num + 1):
        sys.stdout.write('\rrow: '+str(i))
        row = []
        for j in range(0, i+1):
            if j == 0 or j == i:
                row.append(1) # first or last position
            else:
                res = ret[i-1][j-1]+ret[i-1][j]
                row.append(res)

        ret.append(row)
    sys.stdout.write('\n')
    return ret

def main():
    """Get number of rows to calculate from the user and
    show a pretty triangle"""
    try:
        num = int(input('Number of rows: '))
    except ValueError:
        print('Please input an integer')
        exit(1)
    triangle = get_triangle(num)
    length = len(triangle) - 1
    if length > 100:
        return print('too large, not displaying')
    for i in range(0, length):
        row = triangle[i]
        print(' '*(length-i)+(' '.join(str(j) for j in row)))

if __name__ == '__main__':
    main()
