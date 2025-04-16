def solution(e, starts):
    store = [1 for _ in range(e+1)]
    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            store[j] += 1
    
    min_value = min(starts)
    dp = [0 for _ in range(e+1)]  
    value = 0
    maxI = 0 
    for i in range(e,min_value-1,-1):
        if value<=store[i]:
            value = store[i]
            maxI = i
            dp[i] = maxI
        else:
            dp[i] = maxI

    
    return [dp[s] for s in starts]
  
'''
약수를 효과적으로 구하는 게 키포인트 !!!
하나의 수에 약수를 구하는 게 아니라, 배수 방식으로 약수를 구하는 방식을 사용.

파이썬 억까가 심한 문제였다.
store같은 리스트를 만들 때 n 크기 딱 맞춰서 store를 생성하고, 인덱스 접근 시 인덱스 -1 해주면서 계산하는 방식보다 
n+1 크기의 리스트를 만들고 인덱스 계산 방식 없이 바로 접근하는 게 시간적으로 훨씬 이득임을 알게 되었다.. ㅎㅎ
'''
