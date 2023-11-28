def solution(sizes):
    h = []
    w = []
    for size in sizes:
        h.append(max(size))
        w.append(min(size))
    return max(h) * max(w)