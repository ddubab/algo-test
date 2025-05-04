def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    n = len(B)
    idx = 0
    
    for a in (A):
        while a>=B[idx]:
            idx+=1
            if idx == n:
                break
        if idx == n:
            break
        if a<B[idx]:
            idx+=1
            answer +=1
            if idx == n:
                break
            
    return answer

'''
sort가 관건
'''
