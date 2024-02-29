
import time
import random


class compare1:
    def __init__(self) -> None:
        self.null = None
    def function1(self) -> type:
        return
    

class SolutionAlgorithm():
    def __init__(self) -> None:
        self.null = None
    def function1(self) -> type:
        return

"""
Constraints:

"""
def TestExample(max_length = 0, max_num = 0):
    ModelValue = [
            ["Class", "function1"], 
            [[], []]
        ]
    return ModelValue

def RunClass(cls, ModelValue):
    Ans = [None]
    for model, value in zip(ModelValue[0][1:], ModelValue[1][1:]):
        if model == "function1":
            sol = cls.function1()
        Ans.append(sol)
    return Ans

def RuntimeTester(name, cls, ModelValue, Answer, times = 10):
    temp = time.time()
    ans = RunClass(cls, ModelValue)
    for _ in range(times-1):
        _ = RunClass(cls, ModelValue)
    t = 1000*(time.time()-temp)
    t /= times
    ms, mus = int(t), round(1000*(t-int(t)), 3)

    if Answer is True:
        print("{}: {} ms, {} µs".format(name, ms, mus))
    elif Answer==ans:
        print("{}: {} ms, {} µs, (Exact answer)".format(name, ms, mus))
    else:
        print("{}: {} ms, {} µs, (Wrong answer)".format(name, ms, mus))



ModelValue = TestExample()
Ans = RunClass(SolutionAlgorithm(), ModelValue)

print("\nThe Efficiency Comparison of Various Algorithms through Time Testing :\n")
RuntimeTester("Solution", SolutionAlgorithm(), ModelValue, Answer = True)
RuntimeTester("f1", compare1(), ModelValue, Ans)
