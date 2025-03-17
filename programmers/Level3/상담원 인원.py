from itertools import combinations_with_replacement

min_time = 10e9

def find_min_time(k,com,reqs):
    global min_time
    dic = dict()
    for i in range(1,k+1):
        dic[i] = 1
    for co in com:
        dic[co] +=1
    
    wait_time = 0
    store = [[] for _ in range(k+1)]
    for di in dic:
        while dic[di]>0:
            store[di].append(list())
            dic[di] -= 1
    
    for req in reqs:
        c = req[2]
        start = req[0]
        length = req[1]
        
        l = len(store[c])
        min_value = 10e9
        min_idx = -1
        for i in range(l):
            if len(store[c][i]) == 0:
                store[c][i].append(start+length)
                min_idx = -1
                break
            if(store[c][i][0]-start<min_value) :
                min_value = store[c][i][0]-start
                min_idx = i
        if min_idx != -1:
            if min_value>0:
                wait_time += min_value
                store[c][min_idx][0] += length
            else:
                store[c][min_idx][0] = start+length
        if wait_time>min_time:
            break
    
    min_time = min(min_time,wait_time)
                  
    
def solution(k, n, reqs):
    global min_time
    list_ = [i for i in range(1,k+1)]
            
    n-=k
       
    for com in combinations_with_replacement(list_,n):
        find_min_time(k,com,reqs)
    
    
    return min_time

'''
문제 : https://school.programmers.co.kr/learn/courses/30/lessons/214288

뭔가 dp로 풀어야 될 줄 알고 지레 겁먹었는데 도저히 생각 안 나서 완탐으로 푼 문제 근데 통과 됨 ㅎㅋㅎㅋ 


풀이
상담 유형만큼 일단 최소 한 명씩 상담원을 배치해야 되니 n에서 k개만큼은 상담원을 배치해주고 
나머지 배치가능 인력을 itertools의 combinations_with_replacement 함수를 사용해 중복 조합을 구했다.
조합을 사용해 각 상담원이 배치될 수 있는 모든 경우의 수로 reqs 체크해주었다.
reqs 돌면서 최종 답이 될 min_time보다 이미 최솟값이 초과된 경우에는 탐색을 멈추고 반환시켜 주어서 탐색 시간을 줄였다.

'''
