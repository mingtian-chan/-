class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        # head 이면서 tail 인 경우
        if pos == 1 and pos == self.nodeCount:
            curr = self.getAt(1)
            self.head = None
            self.tail = None

            # 노드카운트 1 감소
            self.nodeCount -= 1
            return curr.data

        # head 의 경우
        elif pos == 1:
            curr = self.getAt(1)
            self.head = self.getAt(2)

            # 노드카운트 1 감소
            self.nodeCount -= 1
            return curr.data

        # tail 의 경우
        elif pos == self.nodeCount:
            curr = self.getAt(self.nodeCount)
            self.tail = self.getAt(self.nodeCount - 1)
            self.tail.next = None

            # 노드카운트 1 감소
            self.nodeCount -= 1
            return curr.data

        else:
            prev = self.getAt(pos-1)
            curr = prev.next
            prev.next = curr.next

            # 노드카운트 1 감소
            self.nodeCount -= 1
            return curr.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0