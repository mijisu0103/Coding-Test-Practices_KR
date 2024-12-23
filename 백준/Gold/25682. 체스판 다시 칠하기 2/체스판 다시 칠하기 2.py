def min_repaints(N, M, K, board):
    
    mismatch1 = [[0] * (M + 1) for _ in range(N + 1)]
    mismatch2 = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(M):
            expected1 = 'W' if (i + j) % 2 == 0 else 'B'
            expected2 = 'B' if (i + j) % 2 == 0 else 'W'
            mismatch1[i + 1][j + 1] = mismatch1[i + 1][j] + mismatch1[i][j + 1] - mismatch1[i][j] + (board[i][j] != expected1)
            mismatch2[i + 1][j + 1] = mismatch2[i + 1][j] + mismatch2[i][j + 1] - mismatch2[i][j] + (board[i][j] != expected2)

    
    min_paint = float('inf')
    for i in range(K, N + 1):
        for j in range(K, M + 1):
            cost1 = mismatch1[i][j] - mismatch1[i - K][j] - mismatch1[i][j - K] + mismatch1[i - K][j - K]
            cost2 = mismatch2[i][j] - mismatch2[i - K][j] - mismatch2[i][j - K] + mismatch2[i - K][j - K]
            min_paint = min(min_paint, cost1, cost2)

    return min_paint


N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]


print(min_repaints(N, M, K, board))
