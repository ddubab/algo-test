def solution(matrix_sizes):
    answer = 0
    
    n = len(matrix_sizes)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    #dp[i][j] -> i~j까지 최소행렬곱셈
    for i in range(n-1):
        dp[i][i+1] = matrix_sizes[i][0]*matrix_sizes[i][1]*matrix_sizes[i+1][1]
    
    for i in range(n-2,-1,-1):
        for j in range(i+2,n):
            dp[i][j] = 10e9
            for k in range(i,j):
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+matrix_sizes[i][0]*matrix_sizes[j][1]*matrix_sizes[k][1])
                
            
    return dp[0][n-1]

'''
2차원 dp를 이용했다.
i,j의 최소값을 계속 구해줘서 마지막엔 0,n-1의 최솟값을 구하는 문제였다.

예를 들어 n이 3일 때, 최종적으로 구해야 하는 것은 0-2(0부터 시작하는 인덱스라 가정)까지의 최솟값을 구해야 하는데
이 때 경우의 수가 1,(2,3) or (1,2),3 가 있다. 어느 순서부터 해야 될 지 모르니까 모든 경우의 수를 구해야 한다. 이 때 앞에서 구한 최솟값을 뒤에서 활용하는 dp를 이용해 문제를 풀었다
'''
