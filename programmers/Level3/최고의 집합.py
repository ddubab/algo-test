def solution(n, s):
    best_union = []
    
    if n>s:
        return [-1]

    num = s//n
    namege = s%n
    best_union = [num for _ in range(n)]
    
    idx = n-1
    while namege>0:
        best_union[idx] += 1
        namege-=1
        idx-=1
        
    return best_union

'''
그냥. . 수학 문제~
'''
