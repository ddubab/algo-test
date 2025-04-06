def solution(topping):
    answer = 0
    length = len(topping)
    
    front = [0 for _ in range(length)]
    end = [0 for _ in range(length)]
    
    store = set()
    for i in range(length):
        front[i] = len(store)
        store.add(topping[i])
        
    store = set()
    for i in range(length-1,-1,-1):
        store.add(topping[i])
        end[i] = len(store)
    
    for i in range(length):
        if end[i] == front[i]:
            answer+=1
    
    return answer

'''
topping의 최대 길이가 100만이라 이중 포문은 불가했다.

케이크를 잘랐을 때 앞 조각의 토핑 종류의 개수를 저장하는 front와 뒷 조각의 토핑 종류 개수를 저장하는 end를 따로 만들어 주었다.
같은 곳을 잘랐을 때 front와 end의 저장된 값을 비교하여 그 값이 같으면 공평하게 케이크를 자른 것이다.

토핑의 길이가 백만일 때 총 백만*3번의 반복문을 돌게 된다.
'''
