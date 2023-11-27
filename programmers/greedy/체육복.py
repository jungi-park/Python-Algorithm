# 내답 정확성 86.7
def solution(n, lost, reserve):
  answer = 0

  for i in lost:
      if i in reserve:
          lost.remove(i)
          reserve.remove(i)

  for i in lost:
      if i-1 in reserve:
              reserve.remove(i-1)
              continue
      elif i+1 in reserve:
              reserve.remove(i+1)
              continue
      answer += 1


  return n-answer

# 추천답 정확성: 93.3
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)