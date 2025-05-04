def str_to_int(str_time):
    hour_min = str_time.split(":")
    return int(hour_min[0])*60 + int(hour_min[1])

def int_to_str(int_time):
    hour = str(int_time//60)
    min = str(int_time%60)
    if len(hour) == 1:
        hour = '0' + hour
    if len(min) == 1:
        min = '0'+min
    return hour+":"+min

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    start = 540
    get_bus = [[] for _ in range(n)]
    idx = 0
    cnt = 0
    for time in timetable:
        time = str_to_int(time)
        while time>start or cnt == m:
            cnt = 0
            idx+=1
            start += t
            if idx==n:
                break     
        if idx == n:
            break
        if time<=start:
            get_bus[idx].append(time)
            cnt +=1

    if len(get_bus[n-1]) < m:
        answer = int_to_str(540 + (n-1)*t)
    else:
        last_time = get_bus[n-1][-1]
        answer = int_to_str(last_time-1)
        
    return answer

'''
1. timetable에서 각 시간대별 버스에 탈 수 있는 크루들을 넣어줬다.
2-1. 콘은 최대한 늦은 시간에 버스를 타야 되기 때문에 마지막 시간대 버스가 m명보다 덜 탔으면 마지막 버스가 출발하는 시각에 버스를 타면 되고,
2-2. 마지막 버스가 꽉 찼으면 마지막에 버스를 탑승하는 사람보다 1분 더 빨리 줄을 서면 된다.

풀면서 헤맸던 점 : 
처음 풀 때는 for문 안에 while문을 쓰지 않고 if문을 써서 버스 출발 시간보다 탑승할 시간이 늦을 경우를 한 번만 걸러줬다.(버스 출발 간격 시간(t)을 한 번만 더해줬다.)
while문으로 바꿔줘서 2번 이상 시간 차이가 날 때를 고려해서 통과됐다.

'''
