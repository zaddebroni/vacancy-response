class PersistentStack:

    def __init__(self):
        self.versions = [[None, None, 0]]
        self.currentNode = 0

    def push(self, obj):
        self.versions.append([obj, self.currentNode, self.versions[self.currentNode][2] + 1])
        self.currentNode += 1

    def peek(self):
        assert self.versions[self.currentNode][2] != 0
        toReturn = self.versions[self.currentNode][1]
        return toReturn

    def pop(self):
        assert self.versions[self.currentNode][2] != 0
        toReturn = self.versions[self.currentNode][1]
        newElement = self.versions[self.versions[self.currentNode][1]]
        self.versions.append(newElement)
        self.currentNode += 1
        return toReturn

    def clear(self):
        self.versions.append([None, None, 0])
        self.currentNode += 1

    def size(self) -> int:
        return self.versions[self.currentNode][2]


class CycledFIFOBufferUsingPersistentStack:

    def __init__(self, n: int):
        self.maxSize = n
        self.left = PersistentStack()
        self.right = PersistentStack()

    def transfusion(self):
        while self.right.size() != 0:
            self.left.push(self.right.pop())

    def size(self) -> int:
        return self.right.size() + self.left.size()

    def push(self, obj):
        if self.size() == self.maxSize:
            self.pop()
        self.right.push(obj)

    def pop(self):
        assert self.size() != 0
        if self.left.size() == 0:
            self.transfusion()
        toReturn = self.left.pop()
        return toReturn

    def peek(self):
        assert self.size() != 0
        if self.left.size() == 0:
            self.transfusion()
        toReturn = self.left.peek()
        return toReturn
