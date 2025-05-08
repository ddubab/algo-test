def solution(n, costs):
    root_node = [i for i in range(n)]
    costs.sort(key = lambda x:x[2])
    answer = 0
    
    num = 0
    for c in costs:
        n1,n2,cost = c
        #루트 노드 확인
        #루트 노드가 같지 않으면 루트 노드 바꾸고 num+=1
        if root_node[n1] == root_node[n2]:
            continue
        root = min(root_node[n1],root_node[n2])
        change_root = max(root_node[n1],root_node[n2])
        for i,r in enumerate(root_node):
            if r==change_root:
                root_node[i] = root
                        
        answer += cost
        num+=1
        if num==n-1:
            break
        
    return answer

'''
크루스칼 알고리즘 - 모든 노드를 최단거리로 잇는 경로 구하는 알고리즘
포인트 : 모든 정점을 잇는 간선의 개수는 n-1개다, 루트 노드를 업데이트해 줘서 노드가 순환되지 않게 한다.

처음에 루트 노드를 계속 업데이트 해 주지 않고 경우의 수를 나눠서 특정 경우에만 루트 노드에 속해 있는 노드들을 순회하며 업데이트 해 주었다.
업데이트 해 주어야 하는 경우에도 업데이트 해 주지 않아서 틀려서 좀 헤맸다! 한 번 더 풀어보는 걸로~

'''
