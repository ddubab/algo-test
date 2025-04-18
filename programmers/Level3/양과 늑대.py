def solution(info, edges):
    answer = 0
    n = len(info)
    visited = [0 for _ in range(n)]
    
    def dfs(yang,wolf,visited):
        nonlocal answer
        answer = max(answer,yang)
        for edge in edges:
            if visited[edge[0]] == 1 and visited[edge[1]] == 0:
                who = info[edge[1]]
                visited[edge[1]] = 1
                if who == 0:
                    dfs(yang+1,wolf,visited)
                else:
                    if yang>wolf+1:
                        dfs(yang,wolf+1,visited)
                visited[edge[1]] = 0
    
    visited[0] = 1
    dfs(1,0,visited)
    return answer

'''
문제의 핵심은 노드의 최대 갯수가 작다는 것과, edges의 길이는 노드 개수-1 이라는 것 같다.

문제를 풀며 dfs 방식과 bfs 방식을 고민했다.
트리의 자식노드를 따라가며 dfs 방식으로 풀자니 안 되는 경우가 발생하였고, 트리의 깊이 기준 bfs로도 못 풀 것 같았다.

풀이에서는 트리의 자식노드를 따라가지 않았다. 방문 함수를 만들어서 그 때 그 때 방문 가능한 노드들을 dfs로 전부 방문해 주었다.
여기서 그 때 그 때 방문 가능한 노드들은 부모 노드는 방문했지만 자식 노드는 방문하지 않은 경우로 이 조건을 통과하면, 양과 늑대의 개수를 고려하여 dfs를 들어갈 것인가 판단해 주었다.

dfs를 어느 순서로 방문할 것인가에 대한 고민이 있었다. 어떻게 모든 경우의 수를 탐색할까 했는데 트리 형식을 보면 무조건 부모 노드부터 시작해 자식 노드를 가는 경우만 생각했는데 앞으로는 조건을 충족하는 경우의 수를 기준으로 생각하면 좋을 것 같다.

뭔가 bfs+dfs 느낌으로 풀어야 할 것 같았는데 풀이를 보니 얼추 생각은 비슷하게 들어간 것 같다..
'''
