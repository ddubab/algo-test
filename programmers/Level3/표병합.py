graph = [['EMPTY' for _ in range(50)] for _ in range(50)]
parent = [[[r,c] for c in range(50)] for r in range(50)]

def find(r,c):
    if [r,c] == parent[r][c]:
        return r,c
    pr,pc = parent[r][c]
    parent[r][c] = list(find(pr,pc))
    return parent[r][c]
  
def update(st,end):
    for r in range(50):
        for c in range(50):
            if [r,c] == parent[r][c]:
              if graph[r][c] == st:
                  graph[r][c] = end

def merge(r1,c1,r2,c2):

    pr1,pc1 = find(r1,c1)
    pr2,pc2 = find(r2,c2)
    
    if pr1==pr2 and pc1==pc2 :
        return
    
    if graph[pr1][pc1] != 'EMPTY':
        parent[pr2][pc2] = parent[pr1][pc1]
        
    else:
        parent[pr1][pc1] = parent[pr2][pc2]
        
def unmerge(r,c):
    pr,pc = find(r,c)
    value = graph[pr][pc]
    
    un_list = []
    for i in range(50):
        for j in range(50):
            ppr,ppc = find(i,j)
            if pr == ppr and pc == ppc:
                un_list.append([i,j])
                #parent[i][j] = [i,j]
                #graph[i][j] = 'EMPTY'
    for i, j in un_list :
        parent[i][j] = [i, j]
        graph[i][j] = "EMPTY" if (i, j) != (r, c) else value

    #graph[r][c] = value
    
    
def solution(commands):
    answer = []
    
    for com in commands:
        com = com.split()
        if com[0] == 'UPDATE':
            if len(com)==4:
                pr,pc = find(int(com[1])-1,int(com[2])-1)
                graph[pr][pc] = com[3]
            else:
                update(com[1],com[2])
        elif com[0] == 'MERGE':
            r1,c1 = int(com[1])-1,int(com[2])-1
            r2,c2 = int(com[3])-1,int(com[4])-1
            merge(r1,c1,r2,c2)
        elif com[0] == 'UNMERGE':
            r,c = int(com[1])-1,int(com[2])-1
            unmerge(r,c)
        else:
            r = int(com[1])-1
            c = int(com[2])-1
            pr,pc = find(r,c)
            answer.append(graph[pr][pc])
            
                
    return answer

'''
구현 문제 !!!!!!
어딘가에서 삐그덕 대는데 찾질 못해서 답 보고도 이틀 동안 붙잡았던 문제 ;; 윽

문제점 1
주석 처리해준 (unmerge 함수) 부분에서 계속 틀리던 거였다.
완탐하면서 나는 조건 맞으면 바로바로 수정해줬는데 
바로 수정해주면서 뒷 부분 탐색할 때 영향을 준 것 같다 .. 

문제점 2
find함수 구현해주면서 parent 업데이트 해 주기
return 값 확인 잘 하기~

다른 사람 답도 봤는데 깔끔쓰하게 짜 가지고 배워야겠다고 생각했다.
나도 구현 예쁘게 풀어야지~!~!
'''
