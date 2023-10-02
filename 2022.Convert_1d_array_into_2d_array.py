def construct2DArray(original, m: int, n: int):
    
    # return empty array if conversion not possible
    if (m * n) != len(original):
        return []

    # initialize two-dimensional array
    # tda = [[0] * n for _ in range(m)]              
    # count = 0

    # # populate 2D array using original
    # for i in range(m):
    #     for j in range(n):
    #         tda[i][j] = original[count]
    #         count += 1

    # return tda

    ans = []
    for i in range(0, len(original), n):
        ans.append(original[i:i+n])

    return ans


original = [1,2,3,4]
m = 2
n = 2
# [1,2,3]
# 1
# 3
# [1,2]
# 1
# 1
construct2DArray(original, m, n)