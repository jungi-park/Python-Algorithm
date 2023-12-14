def solution(data, ext, val_ext, sort_by):
    standerd = {
        "code":0,
        "date":1,
        "maximum":2,
        "remain":3
    }
    data = [d for d in data if int(d[standerd[ext]]) < int(val_ext)]
    data.sort(key = lambda x : x[standerd[sort_by]])
    return data