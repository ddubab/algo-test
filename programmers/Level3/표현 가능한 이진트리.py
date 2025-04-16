'''
to2 : 십진수를 이진수로 바꿔주는 함수
'''
def to2(num:int):
    bi_num = ''
    while num>0:
        bi_num += str(num%2)
        num = num//2
    bi_num = bi_num[::-1]
    return bi_num

'''
check : 이진수가 포화이진트리 형태로 표현 가능한지 체크하는 함수
1. 이진수의 길이를 포화이진트리 형태로 맞게 바꿔줌. (1, 1+2, 1+2+4, 1+2+4+8 등의 길이 가능)
2. 포화이진트리의 형태로 바꿔준 이진수가 가능한것인지 체크 -> check 2 함수

check2 : 포화이진트리 형태가 가능한지 체크해주는 재귀 함수
이진수의 정중앙 값을 체크 해 줌으로써 포화이진트리가 가능하면 0을 반환, 불가능하면 1을 반환
포화이진트리 형태가 불가능한 경우 -> 트리의 정중앙 값이 0인데 그 밑 노드들이 1이 나오는 경우

check3 : 트리의 중앙값이 0일 때 그 밑 노드들의 수를 확인해주는 함수 
'''
def check(binary):
    n = len(binary)
    
    std = 0
    di = 0
    while n>std:
        std += 2**(di)
        di+=1
    
    if n<std:
        s = '0'*(std-n)
        binary = s+binary

    return check2(binary)

def check2(bi):
    if len(bi) == 1:
        return 1
    if bi[len(bi)//2] == '0':
        return check3(bi)
    else:
        a = check2(bi[:len(bi)//2])
        b = check2(bi[len(bi)//2+1:])
        return min(a,b)
    
def check3(bi):
    num = int(bi)
    if num!=0:
        return 0
    return 1

def solution(numbers):
    answer = []
    
    for num in numbers:
        binary = to2(num)
        ch = check(binary)
        answer.append(ch)

    return answer


