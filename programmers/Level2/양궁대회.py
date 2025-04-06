from itertools import combinations_with_replacement
from collections import Counter
def solution(n, info):
    answer = []
    num  = [i for i in range(11)]
    result = [0 for _ in range(11)]
    
    dif = 0
    last_sum = 0
    
    for com in combinations_with_replacement(num,n):
        counter = Counter(com)
        sum = 0
        info_sum = 0
        now_result = [0 for _ in range(11)]
        for i in range(11):
            if i in counter:
                if counter[i] > info[i]:
                    sum += 10-i
                    now_result[i] = counter[i]
                elif info[i] !=0 :
                    info_sum += 10-i
                    now_result[i] = counter[i]
            elif info[i] != 0:
                info_sum += 10-i
        
        
        if sum>info_sum:
            if sum-info_sum > dif:
                dif = sum-info_sum
                last_sum = sum
                result = now_result[:]
            if sum-info_sum == dif:
                for j in range(10,-1,-1):
                    if result[j]<now_result[j]:
                        result = now_result[:]
                        break
                    elif result[j]>now_result[j]:
                        break

    
    if dif ==0:
        return [-1]
        
    return result


'''
중복조합을 이용해서 가능한 경우의 수를 다 탐색하여 조건에 맞는 값을 구해 주었다.
중복 조합의 개수가 최대일 때, 20C10으로 184756이다. (n+r-1 C r,  여기서 n은 뽑힐 후보(0~10-> 11개)의 개수이고 r(문제로 봤을 때 변수 n)은 뽑을 개수이다.)
'''
