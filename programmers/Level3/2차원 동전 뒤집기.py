
def solution(beginning, target):
    n = len(beginning)
    m = len(beginning[0])
    
    
    def col_reverse(y):
        for i in range(n):
            if middle[i][y] == 1:
                middle[i][y] = 0
            else:
                middle[i][y] = 1
                
    def row_reverse(x):
        for i in range(m):
            if middle[x][i] == 1:
                middle[x][i] = 0
            else:
                middle[x][i] = 1
        
    def make_middle():
        for i in range (n):
            for j in range (m):
                middle[i][j] = beginning[i][j]
    
    def check_middle():
        for i in range(n):
            for j in range(m):
                if middle[i][j]!=target[i][j]:
                    return False
        return True
                
    answer = 0
    dx = []
    dy = []
    middle = [[_ for _ in range(m)] for _ in range(n)]
    result = 10e9
    
    dx = [0,n-1,0,n-1]
    dy = [0,0,m-1,m-1]
  
    for i in range(4):
        nx = dx[i]
        ny = dy[i]
        answer = 0
        make_middle()
        for x in range(n):
            if middle[x][ny]!=target[x][ny]:
                answer +=1 
                row_reverse(x)
        for y in range(m):
            if middle[nx][y]!=target[nx][y]:
                answer +=1 
                col_reverse(y)
        if check_middle():
            result = min(answer,result)
            
    for i in range(4):
        nx = dx[i]
        ny = dy[i]
        answer = 0
        make_middle()
        for y in range(m):
            if middle[nx][y]!=target[nx][y]:
                answer +=1 
                col_reverse(y)
        for x in range(n):
            if middle[x][ny]!=target[x][ny]:
                answer +=1 
                row_reverse(x)
        if check_middle():
            result = min(answer,result)
    

    if result == 10e9:
        result = -1
    return result


"""
문제풀이 접근방식 
처음 풀 때는 각 행의 첫 열과, 각 열의 첫 행을 타겟과 비교하여 다를 시 각 행,열을 뒤집어 주었다.
결론적으로 타겟과 일치하게 뒤집을 수는 있지만 최대 효율은 아니었다.

순차적으로 행 검사나 혹은 열 검사는 각 실행이 독립적이라고 생각하였다. (예를 들어 1,2,3 행 검사를 할 때는 1,2,3 어느 것부터 검사를 해도 영향을 받지 않음.)
이를 바탕으로 행 검사를 첫 번째 열에서 시작할지, 마지막 열에서 시작할지 / 행 검사부타 할지, 열 검사부터 할지를 조건으로 두고 검사를 진행하였다.

총 8가지의 순서가 나올 수 있음 (for문 4번 *2로 실행)

n : target의 행 길이
m : target의 열 길이
행 검사(row_reverse) : 하나의 열을 기준으로(0 혹은 m-1) 첫 행부터 마지막 행까지 순회하며 타겟값과 미들값이 다를 시 그 행 전체를 뒤집어줌 
열 검사(col_reverse) : 하나의 행을 기준으로(0 혹은 n-1) 첫 열부터 마지막 열까지 순회하며 타겟값과 미들값이 다를 시 그 열 전체를 뒤집어줌 

"""
