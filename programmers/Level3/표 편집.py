def solution(n, k, cmd):
    prev = [i-1 for i in range(n)]
    next = [i+1 for i in range(n)]
    
    next[n-1] = 0
    length = n-1
    
    now = k
    delete_list = []

    for c in cmd:
        command = c.split(" ")
        if command[0] == 'U':
            kk = int(command[1])
            for i in range(kk):
                now = prev[now]
        elif command[0] == 'D':
            kk = int(command[1])
            for i in range(kk):
                now = next[now]
        elif command[0] == 'C':
            delete_list.append(now)
            temp = now
            if now!=length:
                next[prev[now]] = next[now]
                prev[next[now]] = prev[now]
                now = next[now]
                if now == 0:
                    next[prev[temp]] = 0
                    now = prev[temp]
                
            else:
                next[prev[now]] = 0
                now = prev[now]
            
        elif command[0] == 'Z':
            d = delete_list.pop()
            prev[next[d]] = d
            next[prev[d]] = d



    answer = ['O' for _ in range(n)]
    for de in delete_list:
        answer[de] = 'X'
    return ''.join(answer)

'''
처음에는 delete_list와 별개로 n 크기의 배열을 만들어서 삭제된 행인지 검사해주었다.
delete_list로 인덱스를 저장했는데 배열을 또 따로 저장해 준 이유는 인덱스로 배열에 접근해서 O(1) 시간으로 현재 인덱스가 삭제된 행인지 체크해 주려고 했다. ('U' 또는 'D' 명령어 때 중간 행들을 체크해주는 용도로)
얼추 다 통과했는데 몇 개에서 시간 초과로 통과 못 했다.
도저히 생각 안 나서 지피티한테 시간 최적화해달라고 했더니 이 방법을 알려주었다.
prev 배열과 next배열을 만들어서 각 인덱스 다음값과 이전 값을 저장하고 업데이트 시켜주는 방식이다.
이 방식을 사용하면 기존 U,D 명령어 때 인덱스를 하나하나 훑고 가며 검사했던 방식 말고 현재 인덱스의 next,prev 배열만 한 번씩만 타고 가면 돼서 접근해야 하는 배열이 훨씬 작아진다.
지피티 이즈 지니어스..

지피티가 의외로 코테 정확하게 못 푸는데 맞는 방식으로 풀고 시간 최적화 해 달라고 하면 그건 또 기가 막히게 잘 함

'''
