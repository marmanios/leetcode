import sys

def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    pair = [[p,s] for p, s in zip(position, speed)]
    earliest_arrival = -1 * (sys.maxsize - 1)
    groups = 0 

    for p, s in sorted(pair)[::-1]:
        arrival_time = (target - p) / s
        if arrival_time > earliest_arrival:
            earliest_arrival = arrival_time
            groups += 1
        else:
            continue
    
    return groups
            
carFleet(100, [0,2,4], [4,2,1])