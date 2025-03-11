from itertools import combinations
def solution(n, q, ans):
    def compare(com,q_li):
        cnt = 0
        idx = 0
        for i in range(5):
            for j in range(idx,5):
                if com[i] == q_li[j]:
                    idx = j+1
                    cnt+=1
                    break
        return cnt
    
    li = [i for i in range(1,n+1)]
    answer = 0
    
    for com in combinations(li,5):
        check = True
        for i,q_li in enumerate(q):
            cnt = compare(com,q_li)
            if cnt!=ans[i]:
                check = False
                break
        if check:
            answer+=1
            
            
    return answer

'''
그냥 콤비네이션 때리면 됨 ..ㅎㅎ
'''
