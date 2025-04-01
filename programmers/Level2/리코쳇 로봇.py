from collections import deque
def solution(board):
    answer = 0
    q = deque()
    set_list = set()
    n = len(board)
    m = len(board[0])
    
    sx,sy = -1,-1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                sx,sy = i,j
                break
    # 상좌하우
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    for i in range(4):
        nx = dx[i] + sx
        ny = dy[i] + sy
        if nx>=n or nx<0 or ny>=m or ny<0 :
            continue
        if board[nx][ny] == 'D':
            continue
        q.append([sx,sy,1,i])

        
    check = True
    while q:
        x,y,cnt,di = q.popleft()
        if (x,y,di) in set_list:
            continue
        set_list.add((x,y,di))
        
        while True:
            x += dx[di]
            y += dy[di]
            
            if x<0 or y<0 or x>=n or y>=m:
                x-= dx[di]
                y-= dy[di]
                if board[x][y] == 'D':
                    x -= dx[di]
                    y -= dy[di]
                break
            if board[x][y] == 'D':
                x -= dx[di]
                y -= dy[di]
                break

        if board[x][y] == 'G':
            answer = cnt
            break
        for i in range(4):
            if di%2 == 0 and i%2==0:
                continue
            if di%2==1 and i%2==1:
                continue
            nx = dx[i] + x
            ny = dy[i] + y
            if nx>=n or nx<0 or ny>=m or ny<0 :
                continue
            if board[nx][ny] == 'D':
                continue
            q.append([x,y,cnt+1,i])

            
    if answer == 0:
        answer = -1
    return answer


'''
로봇이 길을 찾지 못했을 때 처리해주는 방법이 키 포인트
set으로 이전에 갔던 길을 다시 갈 때 무시하도록 처리하였다.
'''
