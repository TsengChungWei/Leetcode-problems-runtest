
import time
import random


class compare:
    def f1(input):
        return
    

    def SolutionAlgorithm(input):
        return

"""
Constraints:

"""
def TestExample(max_length = 0, max_num = 0):
    input = None
    return input

def RuntimeTester(name, func, input, Answer, times = 10):
    temp = time.time()
    ans = func(input)
    for _ in range(times-1):
        _ = func(input)
    t = 1000*(time.time()-temp)
    t /= times
    ms, mus = int(t), round(1000*(t-int(t)), 3)

    if Answer is True:
        print("{}: {} ms, {} µs".format(name, ms, mus))
    elif Answer == ans:
        print("{}: {} ms, {} µs, (Exact answer)".format(name, ms, mus))
    else:
        print("{}: {} ms, {} µs, (Wrong answer)".format(name, ms, mus))

input = TestExample()
Ans = compare.SolutionAlgorithm(input)

print("\nThe Efficiency Comparison of Various Algorithms through Time Testing :\n")
RuntimeTester("Solution", compare.SolutionAlgorithm, input, Answer = True)
RuntimeTester("f1", compare.f1, input, Ans)
