def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    for sk in skill:
        t, r1, c1, r2, c2, degree = sk
        
        #공격
        if t==1:
            degree = -degree
        dp[r1][c1] += degree
        
        if c2+1 < m:
            dp[r1][c2+1] += (-degree)
        if r2 + 1 < n:
            dp[r2+1][c1] += (-degree)
        if r2+1 < n and c2+1 < m:
            dp[r2+1][c2+1] += degree

    for i in range(1,m):
        dp[0][i] += dp[0][i-1] 
    for j in range(1,n):
        dp[j][0] += dp[j-1][0]
    
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]   
    
    for i in range(n):
        for j in range(m):
            board[i][j] += dp[i][j]
            if board[i][j] > 0:
                answer+=1
    
        
        
    return answer

'''
2차원 dp
'''
