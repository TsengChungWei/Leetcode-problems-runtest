
from collections import deque
import time
import random


class compare:
    def f1(input):
        return
    

    def SolutionAlgorithm(input):
        return

def list_to_treenode(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    k = 1
    while k < len(arr):
        currnode = queue.popleft()
        if arr[k]:
            currnode.left = TreeNode(arr[k])
            queue.append(currnode.left)
        k += 1
        if k < len(arr) and arr[k]:
            currnode.right = TreeNode(arr[k])
            queue.append(currnode.right)
        k += 1
    return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Constraints:

"""
def TestExample(max_length = 0, max_num = 0):
    inputInList = None
    return inputInList

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

inputInList = TestExample()
input = list_to_treenode(inputInList)
Ans = compare.SolutionAlgorithm(input)

print("\nThe Efficiency Comparison of Various Algorithms through Time Testing :\n")
RuntimeTester("Solution", compare.SolutionAlgorithm, input, Answer = True)
RuntimeTester("f1", compare.f1, input, Ans)
