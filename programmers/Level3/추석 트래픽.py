# 문자열 시간을 ms 단위로 바꿔주는 함수
def time_to_second(time):
    h,m,s = time.split(":")
    return int(h)*3600000+int(m)*60000+int(float(s)*1000)

def solution(lines):
    answer = 0
    array = [0 for _ in range(24*60*60*1000+1)]
    min_time = 10e9
    max_time = 0
    
    start_time = []
    for line in lines:
        x,time,duration = line.split(" ")
        t = time_to_second(time)
        d = int(float(duration.split("s")[0])*1000)
        pre_time = t-d-998
        if pre_time<0:
            pre_time = 0

        array[pre_time] += 1
        array[t+1] += (-1)
        
        min_time = min(min_time,pre_time)
        max_time = max(max_time,t+1)
        start_time.append(pre_time)
    
    answer = array[min_time]

    idx = min_time+1
    start_time.sort()
    start_idx = 0
    
    while idx<max_time+1:
        array[idx] += array[idx-1]
        answer = max(answer,array[idx])
        while start_time[start_idx]<idx:
            start_idx+=1
            if start_idx == len(start_time):
                start_idx-=1
                break
        if array[idx]==0 and start_time[start_idx]>idx:
            idx = start_time[start_idx]
            continue
        idx+=1
        

    return answer

'''
초 단위를 신경쓰는 데 주의해야 한다. 나는 ms 단위로 시간을 바꿔서 계산했다. 1초동안 최대 요청 개수를 반환하면 되는데 이 때 일초는 999ms로 계산해주어야 한다.

for문을 이용해 lines를 한 번 돌면서 누적합의 시작 포인트와 끝 포인트를 배열에 저장해 주었다.
그리고 while문을 이용해 최소 인덱스부터 최대 인덱스까지 누적합해주며 최댓값을 계산하였다.

처음에는 while문이 아니라 for문을 돌며 인덱스를 하나씩 올려주며 계산했더니 배열이 너무 커서 시간 초과가 발생하였다.
이에 시작 인덱스만 따로 저장해주어 누적합을 해 주지 않아도 되는 값 0인 구간을 건너뛰었다.
'''
