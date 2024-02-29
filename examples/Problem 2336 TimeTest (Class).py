
import heapq
import time
import random


class compare1:
    def __init__(self):
        self.min = 1
        self.add = []
        
    def popSmallest(self) -> int:
        if self.add:
            return self.add.pop(0)
        self.min += 1
        return self.min-1
        
    def addBack(self, num: int) -> None:
        if num < self.min and num not in self.add:
            self.add.append(num)
            self.add.sort()
        return None

    

class SolutionAlgorithm():
    def __init__(self):
        self.cur_integer = 1
        self.added = []
        self.present = set()

    def popSmallest(self) -> int:
        if self.added:
            answer = heapq.heappop(self.added)
            self.present.remove(answer)
        else:
            answer = self.cur_integer
            self.cur_integer += 1
        return answer

    def addBack(self, num: int) -> None:
        if num >= self.cur_integer or num in self.present:
            return
        heapq.heappush(self.added, num)
        self.present.add(num)


"""
Constraints:
● 1 <= num <= 1000
● At most 1000 calls will be made in total to popSmallest and addBack.
"""
def TestExample(max_num = 1000):
    length = max_num
    Model = ["Class"]*length
    Value = [[]]*length
    for i in range(1, length):
        k = random.randint(1, max_num)
        r = random.randint(0, 1)
        if r == 0:
            Model[i] = "popSmallest"
        else:
            Model[i] = "addBack"
            Value[i] = [k]
    ModelValue = [Model, Value]
    return ModelValue

def RunClass(cls, ModelValue):
    Ans = [None]
    for model, value in zip(ModelValue[0][1:], ModelValue[1][1:]):
        if model == "popSmallest":
            sol = cls.popSmallest()
        elif model == "addBack":
            sol = cls.addBack(value[0])
        Ans.append(sol)
    return Ans

def RuntimeTester(name, cls, ModelValue, Answer, round_point = None, times = 10):
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
