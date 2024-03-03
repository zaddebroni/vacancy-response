from fifo import CycledFIFOBuffer
from fifoUsingStack import CycledFIFOBufferUsingPersistentStack
import timeit


def test1(size, cnt):
    g = CycledFIFOBuffer(size)
    for i in range(cnt):
        g.push(i)


def test2(size, cnt):
    g = CycledFIFOBufferUsingPersistentStack(size)
    for i in range(cnt):
        g.push(i)


for size in range(4, 7):
    for cnt in range(4, 7):
        start_time = timeit.default_timer()
        test1(10 ** size, 10 ** cnt)
        res1 = timeit.default_timer() - start_time

        start_time = timeit.default_timer()
        test2(10 ** size, 10 ** cnt)
        res2 = timeit.default_timer() - start_time

        print(f"For 10^{size} size and 10^{cnt} cnt: ")
        print(res2 - res1)
        print(res2 / res1)
        print()
