from __future__ import print_function
def solution():
    """Enter Code Here"""
    matrix = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]
    for row in matrix:
        for elm in row:
            if elm == 1:
                print("*", end="")
            elif elm == 0:
                print(" ", end="")
        print("\r")
