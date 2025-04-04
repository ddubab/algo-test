from collections import deque
    
def solution(maps):
    q = deque()
    answer = -1
    
    n=len(maps)
    m=len(maps[0])
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    x,y=0,0

    for i in range(n):
        for j in range(m):
            if maps[i][j]=='S':
                x,y=i,j

    visited=[[0]*m for _ in range(n)]
    visited_lever = False
    
    q.append((x,y,0))
    
    while q:        
        now_x,now_y,time = q.popleft()
        
        if not visited_lever and maps[now_x][now_y] == 'L':
            visited_lever = True
            visited = [[0]*m for _ in range(n)]
            q = deque()
            visited[now_x][now_y] = 1
            q.append((now_x,now_y,time))
            continue
        if visited_lever and maps[now_x][now_y] == 'E':
            answer = time 
            break
            
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maps[nx][ny] == 'X' or visited[nx][ny] == 1:
                continue
            
            visited[nx][ny] = 1
            q.append((nx,ny,time+1))
    
            
    
    return answer 

'''
레버방문전까지 visited 업데이트해주고 
레버 방문 시 visited 리셋 해 준 다음에 다시 업데이트 해 주면 된당
'''
