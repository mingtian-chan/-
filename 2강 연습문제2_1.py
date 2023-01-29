def solution(L, x):
    idx = []
    for i in range(len(L)): # 인덱스를 나타내는건 i부터 시작한다 라는 반복문
        if L[i] == x:
            idx.append(i)
    if len(idx) == 0: # 반복문이 끝났을때 idx가 0이면 -1 추가 
        idx.append(-1)
    return idx
