from collections import Counter
def solution(weights):
    answer = 0
    
    counter = Counter(weights)
    
    weights.sort()
    
    for i in range(100,1001):
        if counter[i] >0:
            answer += counter[i] * (counter[i]-1) / 2
            answer += counter[i] * counter[i*3/2]
            answer += counter[i] * counter[i*2]
            answer += counter[i] * counter[i*4/3]

               
    return answer

'''
리스트 범위를 보고 힌트를 알아차릴 것 ..
답 보고 풀었으니 다시 풀고 해설을 적어보기로 한다 ~ 
'''
