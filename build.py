import numpy as np
def solution(row,column):
    """Enter Code Here"""

    if row-1 % 2 == 0:
        mid_row = (row-1)/2
    else:
        mid_row = (row+1)/2

    pattern = ""
    for r in range(row):
        for c in range(column):
            if r == 0 or r == row-1:
                if c == 0 or c == column-1:
                    pattern = pattern + " "
                else:
                    pattern = pattern + "*"
            else:
                if r == mid_row:
                    if c == 1:
                        pattern = pattern + " "
                    else:
                        pattern = pattern + "*"
                elif r < mid_row and r == mid_row-1:
                    if c == 0:
                        pattern = pattern + "*"
                    else:
                        pattern = pattern + " "
                elif r < mid_row or r > mid_row:
                    if c == 0 or c == column-1:
                        pattern = pattern + "*"
                    else:
                        pattern = pattern + " "
        pattern = pattern + "\n"
    return pattern

solution(8,5)
