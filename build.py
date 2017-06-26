def solution():
    r = 7
    c = 5
    for row in range(r):
        for col in range(c):
            if row == 0 or row == r-1:
                if col == 0 or col == c-1:
                    print " ",
                else:
                    print "*",
                if row == 1 or row == r-2 or row == r-3:
                    if col == 0 or col == c - 1:
                        print "*",
                    else:
                        print " ",
                if row == 2:
                    if col == 0:
                        print "*",
                else:
                        print " ",
                if row == 3:
                    if col == 1:
                        print " ",
                else:
                    print "*",
        print("\r")
