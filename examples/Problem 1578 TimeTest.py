
import time
import random


class compare:
    def f1(colors, neededTime):
        def non_max_sum(array):
            max_num, sum_nums = 0, 0
            for num in array:
                if max_num > num:
                    sum_nums += num
                else:
                    sum_nums += max_num
                    max_num = num
            return sum_nums
        compare_time = [neededTime[0]]
        result = 0
        for i in range(1, len(neededTime)):
            if colors[i-1] == colors[i]:
                compare_time.append(neededTime[i])
            else:
                result += non_max_sum(compare_time)
                compare_time = [neededTime[i]]
        result += non_max_sum(compare_time)
        return result
        
    def f2(colors, neededTime):
        max_num = neededTime[0]
        result = sum(neededTime)
        for i in range(1, len(neededTime)):
            if colors[i-1] == colors[i]:
                if max_num < neededTime[i]:
                    max_num = neededTime[i]
            else:
                result -= max_num
                max_num = neededTime[i]
        result -= max_num
        return result
    
    def f3(colors, neededTime):
        max_num = neededTime[0]
        result = neededTime[0]
        for i in range(1, len(neededTime)):
            result += neededTime[i]
            if colors[i-1] == colors[i]:
                if max_num < neededTime[i]:
                    max_num = neededTime[i]
            else:
                result -= max_num
                max_num = neededTime[i]
        result -= max_num
        return result


    def SolutionAlgorithm(colors, neededTime):
        sum_cost = 0
        curr = colors[0]
        max_time = neededTime[0]
        for i in range(1, len(neededTime)):
            if curr == colors[i]:
                if neededTime[i] > max_time:
                    sum_cost += max_time
                    max_time = neededTime[i]
                else:
                    sum_cost += neededTime[i]
            else:
                curr = colors[i]
                max_time = neededTime[i]
        return sum_cost 

"""
Constraints:
● n == colors.length == neededTime.length
● 1 <= n <= 10^5
● 1 <= neededTime[i] <= 10^4
● colors contains only lowercase English letters.
"""
def TestExample(max_length = 10**5, max_time = 10**4):
    en = "abcdefghijklmnopqrstuvwxyz"
    colors = [random.choice(en) for _ in range(max_length)]
    neededTime = [random.randint(1, max_time) for _ in range(max_length)]
    return colors, neededTime

def RuntimeTester(name, func, colors, neededTime, Answer, times = 10):
    temp = time.time()
    ans = func(colors, neededTime)
    for _ in range(times-1):
        _ = func(colors, neededTime)
    t = 1000*(time.time()-temp)
    t /= times
    ms, mus = int(t), round(1000*(t-int(t)), 3)

    if Answer is True:
        print("{}: {} ms, {} µs".format(name, ms, mus))
    elif Answer == ans:
        print("{}: {} ms, {} µs, (Exact answer)".format(name, ms, mus))
    else:
        print("{}: {} ms, {} µs, (Wrong answer)".format(name, ms, mus))

colors, neededTime = TestExample()
Ans = compare.SolutionAlgorithm(colors, neededTime)

print("\nThe Efficiency Comparison of Various Algorithms through Time Testing :\n")
RuntimeTester("Solution", compare.SolutionAlgorithm, colors, neededTime, Answer = True)
RuntimeTester("f1", compare.f1, colors, neededTime, Ans)
RuntimeTester("f2", compare.f2, colors, neededTime, Ans)
RuntimeTester("f3", compare.f3, colors, neededTime, Ans)
