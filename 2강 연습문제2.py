def solution(L, x):
    idxlst = []
    while(True):
        try:
            idxlst.append(L.index(x))
            L.pop(x)
            
        except:
            if len(idxlst) == 0:
                idxlst.append(-1)
        break
    return L

print(solution([64, 72, 83, 72, 54], 72))