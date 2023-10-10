
def spiralOrder(matrix):
    
    ## T(N): O(M * N)
    ## Space: O(1)

    out = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    
    while left < right and top < bottom:            
        # get every i in the top row
        for i in range(left, right):
            out.append(matrix[top][i])
        top += 1  # shifting top by 1

        # get every i in the right col
        for i in range(top, bottom):
            out.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # get every i in the bottom row
        for i in range(right - 1, left - 1, -1):
            out.append(matrix[bottom - 1][i])
        bottom -= 1

        # get every i in the left col
        for i in range(bottom - 1, top - 1, -1):
            out.append(matrix[i][left])
        left += 1


    return out