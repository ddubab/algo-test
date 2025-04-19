from collections import deque
def solution(a, edges):

    q = deque()
    n = len(a)
    graph = [set() for _ in range(n)]
    
    for ed1,ed2 in edges:
        graph[ed1].add(ed2)
        graph[ed2].add(ed1)
    
    sum = 0

    for i,value in enumerate(a):
        sum+=value
        if len(graph[i]) == 1:
            q.append(i)
    
    if sum !=0:
        return -1


    cnt = 0
    
    while q:
        now = q.popleft()
        
        for edge in graph[now]:
            re = edge
            graph[edge].remove(now)
            cnt += abs(a[now])
            a[edge] += a[now]
            a[now] = 0
            if len(graph[edge]) == 1:
                q.append(edge)
                
    return cnt
