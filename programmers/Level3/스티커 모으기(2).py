def solution(sticker):
    answer = 0
    n = len(sticker)
    
    if n<=3:
        for sti in sticker:
            answer = max(answer,sti)
        return answer
    
    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]
    
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for i in range(2,n):
        dp1[i] = max(sticker[i]+dp1[i-2],dp1[i-1])
    
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2,n):
        dp2[i] = max(sticker[i]+dp2[i-2],dp2[i-1])


    return max(dp1[-2],dp2[-1])


'''
원형 배열이기 때문에 첫 번째 인덱스르 무조건 선택해주느냐 vs 선택하지 않는 경우로 dp1,dp2로 나누어서 계산했다.

고려점 
dp1과 dp2로 나누면서 앞 쪽 0,1 인덱스 값을 채울 때 주의하여야 한다. dp[idx]의 의미는 idx에서 그 때까지의 최댓값임에 유의하자.
dp1[1]의 값을 sticker[1]로도 해 보고 0으로도 했었는데 인덱스 0 을 선택했을 때는 인덱스1의 최댓값은 dp1[0]의 값이다. dp2[0]의 값이 0이라고 헷갈리지 말자~
'''
