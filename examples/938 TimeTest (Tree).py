
import time
import random


class compare:
    def f1(root, low, high):
        result = 0
        if root is None:
            return 0
        if root.val < low:
            result += compare.f1(root.right, low, high)
        elif low <= root.val and root.val <= high:
            result += root.val
            result += compare.f1(root.left, low, high)
            result += compare.f1(root.right, low, high)
        elif high < root.val:
            result += compare.f1(root.left, low, high)
        return result
    
    def f2(root, low, high):
        if root is None:
            return 0
        result = 0
        if low <= root.val <= high:
            result += root.val
        if root.val > low:
            result += compare.f2(root.left, low, high)
        if root.val < high:
            result += compare.f2(root.right, low, high)
        return result
    

    def SolutionAlgorithm(root, low, high):
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if node and low <= node.val <= high:
                ans += node.val
            if node and low< node.val:
                stack.append(node.left)
            if node and node.val< high:
                stack.append(node.right)
        return ans        


def list_to_treenode(arr):
    if not arr: return None
    root = TreeNode(arr[0])
    queue = [root]
    k = 1
    while k < len(arr):
        current_node = queue.pop(0)
        if arr[k] is not None:
            current_node.left = TreeNode(arr[k])
            queue.append(current_node.left)
        k += 1
        if k < len(arr) and arr[k] is not None:
            current_node.right = TreeNode(arr[k])
            queue.append(current_node.right)
        k += 1
    return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Constraints:
● A binary search tree
● The number of nodes in the tree is in the range [1, 2 * 10^4].
● 1 <= Node.val <= 10^5
● 1 <= low <= high <= 10^5
● All Node.val are unique.
"""
def TestExample(max_length = 2*10**4):
    # 2^16 < 10**5 and 2**17 > 10**5
    # 2^16 + 2^15 + 2^14 + ... + 2 + 1 = 2^17-1 > 2*10^4
    k = 16
    n = 2**k
    array = [2*i+1 for i in range(n)]
    arr = array
    for _ in range(k):
        arr = [(arr[i]+arr[i+1])//2 for i in range(0, n, 2)]
        array = arr + array
        n //= 2
    inputInList = array[:2*10**4]
    low = 1
    high = inputInList[-1]
    return inputInList, low, high

def RuntimeTester(name, func, root, low, high, Answer, times = 8):
    temp = time.time()
    ans = func(root, low, high)
    for _ in range(times-1):
        _ = func(root, low, high)
    t = 1000*(time.time()-temp)
    t /= times
    ms, mus = int(t), round(1000*(t-int(t)), 3)

    if Answer is True:
        print("{}: {} ms, {} µs".format(name, ms, mus))
    elif Answer == ans:
        print("{}: {} ms, {} µs, (Exact answer)".format(name, ms, mus))
    else:
        print("{}: {} ms, {} µs, (Wrong answer)".format(name, ms, mus))

inputInList, low, high = TestExample()
root = list_to_treenode(inputInList)
Ans = compare.SolutionAlgorithm(root, low, high)

print("\nThe Efficiency Comparison of Various Algorithms through Time Testing :\n")
RuntimeTester("Solution", compare.SolutionAlgorithm, root, low, high, Answer = True)
RuntimeTester("f1", compare.f1, root, low, high, Ans)
RuntimeTester("f2", compare.f2, root, low, high, Ans)