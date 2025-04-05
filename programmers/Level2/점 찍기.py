import math
def solution(k, d):
    answer = 0
    std = math.pow(d,2)
    
    for i in range(0,d+1,k):
        n = math.sqrt(std-math.pow(i,2))
        n = math.floor(n)
        answer += n//k + 1
    
    return answer 
