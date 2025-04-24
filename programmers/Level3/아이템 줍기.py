from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    q = deque()
    
    for r in rectangle:
        r1,c1,r2,c2 = map(lambda x:x*2,r)
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if r1 <i<r2 and c1<j<c2:
                    graph[i][j] = 0
                elif graph[i][j] !=0:
                    graph[i][j] = 1
    
    characterX,characterY = characterX*2,characterY*2
    itemX,itemY = itemX*2,itemY*2
    
    q.append([characterX,characterY,0])
    visited = [[0 for _ in range(102)] for _ in range(102)]
    
    while q:
        x,y,c = q.popleft()
        if x == itemX and y == itemY:
            return c//2
        
        visited[x][y] = 1
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if visited[nx][ny] == 0 and graph[nx][ny] ==1:
                q.append([nx,ny,c+1])

'''

'''
