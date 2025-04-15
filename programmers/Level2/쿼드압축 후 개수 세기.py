def solution(arr):
    length = len(arr)
    
    cnt_0 = 0
    cnt_1 = 0
    
    def dfs(x,y,n):
        nonlocal cnt_0
        nonlocal cnt_1
        
        check = True
        s = arr[x][y]

        for i in range(x,x+n):
            for j in range(y,y+n):
                if s!=arr[i][j]:
                    dfs(x,y,n//2)
                    dfs(x,y+n//2,n//2)
                    dfs(x+n//2,y,n//2)
                    dfs(x+n//2,y+n//2,n//2)
                    check = False
                    break
            if not check:
                break
        if check:
            if s==0:
                cnt_0 +=1
            else:
                cnt_1 +=1
        
        
        
    
    dfs(0,0,length)
    
    return [cnt_0,cnt_1]

'''
global -> 전역변수 참조 
nonlocal -> 가장 가까운 바깥 함수의 변수 참조
'''
