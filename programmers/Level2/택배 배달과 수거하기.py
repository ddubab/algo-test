def solution(cap, n, deliveries, pickups):
    answer = 0
    
    del_end = 0
    pick_end = 0
    
    for i in range(n-1,-1,-1):
        if deliveries[i] !=0 :
            del_end = i
            break
    for i in range(n-1,-1,-1):
        if pickups[i] !=0 :
            pick_end = i
            break


    del_cap = cap
    pick_cap = cap

    while pick_end>=0 or del_end >= 0:
        del_cap = cap
        pick_cap = cap
        if del_end <=0 and pick_end <=0 :
            if deliveries[0] == 0 and pickups[0] == 0:
                break
        answer += (max(del_end,pick_end)+1)*2

        while del_cap != 0:
            if del_end<0:
                break
            if deliveries[del_end] <= del_cap:
                t = deliveries[del_end]
                deliveries[del_end] -= del_cap
                del_cap -= t
                del_end -= 1
            else:
                deliveries[del_end] -= del_cap
                del_cap = 0

        while pick_cap!=0:
            if pick_end <0:
                break
            if pickups[pick_end] < pick_cap:
                t = pickups[pick_end]
                pickups[pick_end] -= pick_cap
                pick_cap -= t
                pick_end -=1
            else:
                pickups[pick_end] -= pick_cap
                pick_cap = 0
        while 1 : 
            if deliveries[del_end] == 0 and del_end>=1:
                del_end-=1
            else:
                break
        while 1 : 
            if pickups[pick_end] == 0 and pick_end>=1:
                pick_end-=1
            else:
                break


    return answer

'''

최대 효율을 내기 위해서는 한 번 이동할 때 cap 만큼의 배달과 수거를 해야 한다고 생각했다. 배달과 수거의 경우를 따로 생각해도 cap개수만 지켜주면 된다고 생각하여 del_cap(배달캡), pick_cap(수거캡)을 따로 두었다.
한 번의 턴(while)을 cap의 개수가 다할때까지로 정했다. 배열 뒤에서부터 배달과 수거를 따로 생각하여 cap 개수만큼 빼 주면서 배달 인덱스와 수거 인덱스를 업데이트해주었다.
배달 인덱스와 수거 인덱스 중 더 멀리 있는 인덱스 값을 두 배 하여 answer에 더해 주었다.
'''
