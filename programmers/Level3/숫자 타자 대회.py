def solution(numbers):
    weight = [[1,7,6,7,5,4,5,3,2,3],
             [7,1,2,4,2,3,5,4,5,6],
            [6,2,1,2,3,2,3,5,4,5],
            [7,4,2,1,5,3,2,6,5,4],
            [5,2,3,5,1,2,4,2,3,5],
            [4,3,2,3,2,1,2,3,2,3],
            [5,5,3,2,4,2,1,5,3,2],
            [3,4,5,6,2,3,5,1,2,4],
            [2,5,4,5,3,2,3,2,1,2],
            [3,6,5,4,5,3,2,4,2,1]]
    
    n = len(numbers)
    dp = [[[10e9 for _ in range(10)] for _ in range(10)] for _ in range(n+1)]
    
    dp[0][4][6] = 0
    
    for idx in range(1,n+1):
        num = int(numbers[idx-1])
        for i in range(10):
            for j in range(10):
                pre = dp[idx-1][i][j]
                if i==j or pre>=10e9:
                    continue
                dp[idx][num][j] = min(pre+weight[i][num],dp[idx][num][j])
                dp[idx][i][num] = min(pre+weight[j][num],dp[idx][i][num])
    
    answer = 10e9
    for i in range(10):
        for j in range(10):
            answer = min(answer,dp[n][i][j])
                   
        
    return answer

'''
처음에 Dp를 고려 안 했던 건 아닌데 왼손과 오른손을 어떻게 따로 고려 할 수 있을까 했는데 3중 배열로 하는 거였다..
풀이를 봤는데 혼자 힘으로 풀 수 있을까 싶다.
'''
