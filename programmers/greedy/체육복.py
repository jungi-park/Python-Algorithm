def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost1 = [l for l in lost if l not in reserve]
    _lost2 = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost1:
            _lost1.remove(f)
        elif b in _lost1:
            _lost1.remove(b)
            
    for r in _reserve:
        f = r - 1
        b = r + 1
        if b in _lost2:
            _lost2.remove(b)
        elif f in _lost2:
            _lost2.remove(f)
    
    return max(n - len(_lost1),n - len(_lost2))