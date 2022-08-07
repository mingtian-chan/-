L = [0,1,3,4,5]
print(L[2])

L.insert(0,10)
print(L)

print(L.index(0))

def solution(L,x): # def로 함수를 정의 할 때는 ":"를 넣어주도록하자.

    for i in L:
        if x < i:
            L.insert(L.index(i),x)
            break
        if x > L[-1]:
            L.append(x)
    return(L)