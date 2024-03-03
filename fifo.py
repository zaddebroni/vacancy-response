class CycledFIFOBuffer:

    def __init__(self, n: int):
        self.array = [None] * n
        self.indexFirst = 0
        self.indexLast = 0
        self.length = 0

    def push(self, obj):
        self.array[self.indexLast] = obj
        self.indexLast += 1
        if self.indexLast == len(self.array):
            self.indexLast = 0
        self.length += 1

    def pop(self):
        assert self.length != 0
        toReturn = self.array[self.indexFirst]
        self.array[self.indexFirst] = None
        self.indexFirst += 1
        if self.indexFirst == len(self.array):
            self.indexFirst = 0
        return toReturn

    def peek(self):
        assert self.length != 0
        return self.array[self.indexFirst]

    def clear(self):
        self.__init__(len(self.array))
