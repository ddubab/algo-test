def solution(land):
    row = len(land)
    
    dp = [[0,0,0,0] for _ in range(row)]
    dp[0] = land[0]
    
    for i in range(1,row):
        for j in range(4):
            max_value = 0
            for k in range(4):
                if j==k:
                    continue
                max_value = max(dp[i-1][k],max_value)
            dp[i][j] = max_value + land[i][j]
    
    answer = max(dp[len(dp)-1])
    return answer

'''
간단한 dp 문제
'''
