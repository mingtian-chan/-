def solution(L, x):
    lower = 0
    upper = len(L)-1
    #middle = int ((lower + upper) // 2) # 여기서 만약에 middle 을 정의하면 아래에서 middle은 고정된 값이라 
    # 에러가 나지요! 
    idx = -1
    while upper >= lower:
        middle = int((lower + upper)// 2) # 여기서 middle 의 값이 바뀌니까 여기서 mid 를 정의하는게 맞다. 
        if x == L[middle]: # x 는 값(value), middle 은 순서(index)! 
            idx = middle
            break
        elif x < L[middle] :
            upper = middle - 1
        else:
            lower = middle + 1
        
    return idx