def solution(rows, columns, queries):
    answer = []
    
    graph = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for query in queries:
        x1,y1,x2,y2 = query[0]-1,query[1]-1,query[2]-1,query[3]-1
        
        x,y = x1,y1
        di = 0
        temp = graph[x][y]
        min_value = temp
        
        while 1:
            min_value = min(min_value,graph[x][y])
            
            if y == y2 and di ==0:
                di +=1
            if x == x2 and di ==1:
                di +=1
            if y == y1 and di ==2:
                di +=1
            if x == x1 and di ==3:
                break
            
            x += dx[di]
            y += dy[di]
            
            pre_temp = graph[x][y]
            graph[x][y] = temp
            temp = pre_temp
            

        answer.append(min_value)
        
        
    return answer

'''
시계 방향으로 회전하며 문제에서 요구하는 것들을 구현
'''
