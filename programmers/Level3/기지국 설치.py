def solution(n, stations, w):
    answer = 0

    lights = [[1]]
    idx = 0

    for station in stations:
        start = station-w

        if start<1:
            start = 1
        end = station+w
        if end>=n:
            end = n
        lights[idx].append(start-1)
        lights.append([end+1])
        idx+=1
    lights[idx].append(n)
    
    ra = 2*w+1
    for light in lights:
        start,end = light
        if end<start:
            continue
        cnt = end-start+1
        if cnt%ra == 0:
            answer += cnt//ra
        else:
            answer += (cnt//ra)+1


    return answer

'''
설치된 기지국 구간을 제외하고 안 설치된 곳의 시작 인덱스와 끝 인덱스를 찾고, 설치해야 될 기지국 개수를 구해준다.
두 번째 for문 돌 때 제외 구간 설정을 end<=start로 해서 조금 헤맸다. end랑 start가 같아도 하나 설치해줘야 되는데.. 맞는 로직인 것 같은데 몇 개 안 되면 구간설정을 맞게 해 줬나 잘 보자~

코드 개선하면 좋을 점
1. lights 리스트에 [start,end]를 따로 저장히자 않고 바로바로 처리해 줘도 됨.


'''
