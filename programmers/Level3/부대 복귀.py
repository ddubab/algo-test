from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    q = deque()
    graph = [[] for _ in range(n+1)]
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    
    distance = [10e9 for _ in range(n+1)]
    distance[destination] = 0
    
    q.append(destination)
    while q:
        now = q.popleft()
        
        for node in graph[now]:
            if distance[now] + 1 < distance[node]:
                distance[node] = distance[now] + 1
                q.append(node)
    
    for source in sources:
        if distance[source] == 10e9:
            answer.append(-1)
            continue
        answer.append(distance[source])
    return answer


'''
목적지가 정해져 있는 문제였기 때문에 목적지를 기준으로 도달 가능한 곳 전부의 최단 거리를 구하였다.
'''
