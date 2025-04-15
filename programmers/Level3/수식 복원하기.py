
def find(X:str,Y:str,awd:str,formula):
    X = X[::-1]
    Y = Y[::-1]
    awd = awd[::-1]

    for i in range(2,10):
        string = []
        
        x_decimal = 0
        y_decimal = 0
        a_decimal = 0
        square = 0
        for x in X:
            x_decimal += int(x)*i**(square)
            square+=1
            
        square = 0
        for y in Y:
            y_decimal += int(y)*i**(square)
            square+=1
        
        square = 0
        for a in awd:
            a_decimal += int(a)*i**(square)
            square+=1
        
        if formula == '+':
            if x_decimal + y_decimal == a_decimal:
                return i
        else:
            if x_decimal - y_decimal == a_decimal:
                return i   
        
        
            
        
        
def cal(x:str,y:str,formula,de):
    X = x[::-1]
    Y = y[::-1]
    awd = ''
    
    square = 0
    int_x = 0
    int_y = 0
    for x in X:
        int_x += int(x)*de**(square)
        square+=1
    square = 0
    for y in Y:
        int_y += int(y)*de**(square)
        square+=1
    
    answer = 0
    if formula == '+':
        answer = int_x + int_y
    else:
        answer = int_x - int_y
    if answer ==0:
        return '0'
    
    while answer>0:
        awd += str(answer%de)
        answer = answer//de
    awd = awd[::-1]
    return awd
                
        
        
        
def solution(expressions):
    answer = []
    
    min_candi = 2
    last_candi = 0
    store = []
    for ex in expressions:
        X,formula,Y,equal,awd = ex.split(" ")
        
        
        for x in X:
            x = int(x)
            min_candi = max(x+1,min_candi)
        for y in Y:
            y = int(y)
            min_candi = max(y+1,min_candi)
        
        if awd == 'X':
            store.append(ex)
            continue
        if last_candi!=0:
            continue
        
        for a in awd:
            a = int(a)
            min_candi = max(a+1,min_candi)

        x = int(X)
        y = int(Y)

        if formula == '+':
            if x+y != int(awd):
                last_candi = find(X,Y,awd,formula)
        elif formula == '-':
            if x-y != int(awd):
                last_candi = find(X,Y,awd,formula)
                
            
    if min_candi == 9:
        last_candi = 9
    for s in store:
        aw = set()
        X,formula,Y,equal,awd = s.split(" ")
        a= '?'
        
        if last_candi!=0:
            a = cal(X,Y,formula,last_candi)
            a_str = X +" " +formula+" " +Y+" " +equal+" " +a
            answer.append(a_str)
            continue
        
        
        if formula == '+':
            for candi in range(min_candi,10):
                a = cal(X,Y,formula,candi)
                aw.add(a)   
        else:
            for candi in range(min_candi,10):
                a = cal(X,Y,formula,candi)
                aw.add(a) 
        
        if len(aw) > 1:
            a= '?'
        else:
            a = aw.pop()

        a_str = X +" " +formula+" " +Y+" " +equal+" " +a
        answer.append(a_str)
        
            
    return answer


'''
min_candi : 가능한 최소 진수값
last_candi : 확정된 진수값

각 숫자들을 자리수마다 순회하며 각 자리수의 최대값+1로 min_candi를 업데이트해주었다.
답이 나와있는 식 중에서 더하거나 뺄 때 일의 자릿수가 십의 자릿수에 영향을 주거나 그 반대의 경우 (예를 들어, 51 - 4 = 47)는 진법검사를 통해 몇진법인지 알아낼 수 있다. 따라서 이런 경우 last_candi를 업데이트해주었다.

마지막으로 구해야 되는 식에 이제까지 구한 정보를 이용해 ? 또는 정답을 추가해 문자열로 바꿔주면 된다.
여기서 최종적으로 몇진법인지 정확하지 않을 때는 가능한 진법의 경우를 모두 계산해주어 하나의 답이 나오면 그 답을 반환하여 주고 두 개 이상의 답이 나오면 ?를 반환해주었다.

처음에는 모든 경우의 수를 구하지 않고 다음과 같이 내 나름의 규칙을 생각해 계산해 주었다.

+인 경우, x의 일의 자릿수 + y의 일의 자릿수 >= min_candi -> ? 반환
        x의 이의 자릿수 + y의 이의 자릿수 >= min_candi -> ? 반환
-인 경우, x의 일의 자릿수 > y의 일의 자릿수 -> ? 반환

근데 이렇게 하니까 절반 정도는 틀렸다.. ㅎㅎ 아직까지 무슨 반례가 있는지는 사실 잘 모르겠지만 
기존의 답은 내가 모르는 무엇인가 있을 수 있다는 생각이고(확신이 없고)
최종적으로 수정한 답이 비효율이지만 확실한 방법인 것 같다. ----> 코테 풀 때는 무조건 확실한 답으로 !!!


'''
