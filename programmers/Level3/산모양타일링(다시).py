def solution(n, tops):

    first = [0 for _ in range(n)]
    second = [0 for _ in range(n)]
    
    if tops[0] == 1:
        first[0] = 3
        second[0] = 1
    else:
        first[0] = 2
        second[0] = 1
    
    
    for i in range(1,len(tops)):
        if tops[i] == 1:
            first[i] = first[i-1] * 3 + second[i-1] *2 % 10007
            second[i] = first[i-1] + second[i-1] % 10007
        else:
            first[i] = first[i-1] * 2 + second[i-1] % 10007
            second[i] = first[i-1]  + second[i-1] % 10007
    
            
        
    #print(first)
    #print(second)
    return (first[n-1] +second[n-1]) % 10007 

'''
문제 : https://school.programmers.co.kr/learn/courses/30/lessons/258705
아직 dp적 사고가 부족하다 그래서 답 보고 풀음 ㅎㅎ
처음에는 규칙으로 풀려고 했는데 예외처리를 어케 해 줄지 고민하다가 답을 봐 버렸다.

dp 의심 포인트
1. 계산마다 10007로 나눠주기
2. 가능한 경우의 수를 미리 줌 -> 순차적으로 앞에서부터 가능한 경우의 수 고려해서 dp로 풀라는 거 아닐까..?

풀이
1. 4개의 작은 삼각형으로 이루어진 큰 삼각형을 기준으로 dp 테이블을 계산하여준다.
2. 큰 삼각형을 구성할 수 있는 4가지 경우의 수가 있는데, 4개의 작은 삼각형 / 오른쪽으로 기울어진 마름모 / 왼쪽으로 기울어진 마름모 / 마름모 총 네 가지 경우이다. (편하게 11,22,33,44번 경우의 수라 칭함)
3. i번째 연산에서 33번을 선택했을 때에는 i+1번째 연산에서 33번 빼고는 모든 경우의 수를 선택할 수 없다. (겹치기 때문)
4. 따라서 i-1번째 연산을 기준으로 i번째 dp 테이블을 업데이트 시켜주면 되는데 11,22,44번을 선택할 때의 테이블과 33번을 선택할 때의 경우를 나누어 두 개의 테이블로 계산을 진행한다. (문제에서는 first,second로 나눔)
'''
