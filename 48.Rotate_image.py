def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """

    ## T(N): O(N * N)
    ## Space: O(1), in-place, required in question

    left, right = 0, len(matrix)-1

    while left < right:
        # for i in range(left, right):  #can't be this bcz every time l and r moves we need range like 0,1,2 not 1,2,3 or 2,3,4

        # need i to process every ele in a row
        for i in range(right - left):
            top, bottom = left, right

            # save top left
            topLeft = matrix[top][left+i]

            # moving counter clockwise
            # a) move bottom left into top left
            matrix[top][left+i] = matrix[bottom-i][left]

            # b) move bottom right into bottom left
            matrix[bottom-i][left] = matrix[bottom][right-i]

            # c) move top right into bottom right
            matrix[bottom][right-i] = matrix[top+i][right]

            # move top left into top right
            matrix[top+i][right] = topLeft

        left += 1
        right -= 1
