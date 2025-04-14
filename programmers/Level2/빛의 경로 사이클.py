from collections import deque
def solution(grid):
    answer = []
    visited = dict()

    n = len(grid)
    m = len(grid[0])
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    awd_cnt = []
    idx = 0
    for ii in range(n):
        for jj in range(m):
            for i in range(4):
                q = deque()
                q.append([ii,jj,i])
                cnt = 0

                while q:    
                    x,y,di = q.popleft()
                    if (x,y) not in visited:
                        visited[(x,y)] = set()
                        visited[(x,y)].add(di)
                    else:
                        if di in visited[(x,y)]:
                            break
                        else:
                            visited[(x,y)].add(di)
            
                    if grid[x][y] == 'L':
                        di -=1
                        if di<0:
                            di = 3
                
                    elif grid[x][y] == 'R':
                        di +=1
                        if di>3:
                            di = 0
                    
                    nx = x+dx[di]
                    ny = y+dy[di]
                    if nx<0:
                        nx = n-1
                    elif nx>=n:
                        nx = 0
                    if ny<0:
                        ny = m-1
                    elif ny>=m:
                        ny = 0
            
                    q.append([nx,ny,di])
                    cnt+=1
                        
                if cnt!=0:
                    awd_cnt.append(cnt)
    
    awd_cnt.sort()
    return awd_cnt

'''
좌표마다 네 가지 방향으로 출발하는 경우를 고려해줬다. 
처음에는 경우마다 visited를 초기화 해 줘서 시간초과가 떠서 visited를 어떻게 처리하면 좋을지 고민했다.

시작점이 달라도 결국 같은 사이클이 되려면 지나가는 좌표와 방향이 같아야 됨을 깨닫고 굳이 경우마다 visited를 업데이트 해 주지 않아도 됨을 깨달았다. (다른 사이클이면 같은 좌표,같은 방향을 지나갈 수 없음.)
visited를 계속 초기화해주지 않고 visited가 겹칠 때(이미 지나갔던 사이클이면 while문 한 번도 돌지 않고 바로 빠져나온다) 바로 while문을 빠져나오니 시간초과 문제가 해결되었다.

처음에는 0,0 좌표에서 네 가지 방향의 출발점만 고려해줬는데 모든 방향에서 고려해줘야 하는 걸 나중에 알았다. 문제해석력도 역시 중요하다;;

visited 처리를 어떻게 해 줄지가 관건인 문제였다.

'''
