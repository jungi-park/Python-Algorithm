def solution(s):
    s_s = s.split(' ')
    temp = []
    for i in s_s:
        i = i.capitalize()
        temp.append(i)
    return ' '.join(temp)