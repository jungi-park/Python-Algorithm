from collections import deque
def solution(priorities, location):
    process = 0
    priorities = [[val,index] for index , val in enumerate(priorities)]
    qu = deque(priorities)
    while qu:
        process += 1
        val,index = qu.popleft()
        if qu and max([data[0] for data in qu]) > val:
            qu.append([val,index])
            process -=1
        else:
            if index == location:
                return process