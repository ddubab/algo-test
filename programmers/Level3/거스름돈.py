def solution(n, money):
  
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for mon in money:
        for i in range(mon,n+1):
            dp[i] +=dp[i-mon]
    
    return dp[n]

'''
dp[i]의 값을 i값을 만들 수 있는 조합의 개수로 설정.
dp는 확실히 그리면서 하면 훨씬 빨리 이해할 수 있음 ! 

이 문제에서는 money를 순회하며 i 조합 개수를 구하기 위해서 i-mon 개수의 조합을 계속 더해준다. 설명을 어케할지 모르겠네 ㅎㅎㅎ

'''
