class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''
    # 입력 S 를 한번 순회하면서 처리
    for i in S:
        # 닫는 괄호인 경우 ")"
        if i == ")":
            while opStack.peek() != "(":
                answer += opStack.pop()
            opStack.pop()
        
        elif i == "(":
            opStack.push(i)    

        # 연산자인 경우
        elif i in prec:
            # opStack이 비었을 경우 opStack에 원소를 넣고 다음 순회
            if opStack.isEmpty():
                opStack.push(i)
                continue
            # 아닐 경우 우선순위를 서로 비교.
            s = prec[i]  # 입력된 것의 우선순위
            t = prec[opStack.peek()]  # 스택 맨 위의 우선순위

            # 우선 순위를 비교했을 때 stack원소가 크거나 같으면, stack 원소를 answer에 append하고 입력된 거를 스택에 push
            if t >= s:
                while not opStack.isEmpty() and prec[opStack.peek()] >= s: # 여기서 많이 헤맸음. prec[opStack.peek()]를 계속 업데이트 해줘야 하니까. 업데이트 안 하면 확인을 못함. 그리고 opStack.isEmpty()가 앞에 나와야 먼저 판단을 함 (Computer Science 적 내용 ("And"))
                    answer += opStack.pop()
                opStack.push(i)
                        

            # 우선 순위를 비교했을 떄, 입력된 것의 우선순위가 높거나 같으면 입력된 것을 스택에 push
            else:
                opStack.push(i)
                
        # 둘 다 아닌 경우 -> 변수인 경우
        else:
            answer += i

    # 순회 끝, 스택이 0 이 아닌 경우, 스택을 pop해줌
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer

S = input()
print(solution(S))