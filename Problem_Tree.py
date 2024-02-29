# ● 
# ╱╲　／＼　↑　↓  ←　→　↖　↗　↙　↘

# Description
"""

"""

# Code
from collections import deque
from typing import List, Optional


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
class Solution:
    def LeetcodeExample(self, __: Optional[TreeNode]) -> type:
        pass

# Testcase
class Testcase:
    Case = [
        None
    ]
    Expected = [
        None
    ]
    # def SolutionAlgorithm(__):
    #     return 
    
# Submisstions
for i, case in enumerate(Testcase.Case):
    Sol = Solution()
    solution  = Sol.LeetcodeExample(__ = list_to_treenode(case))
    input = f"__ = {case}"
    expected = Testcase.Expected[i]
    # expected = Testcase.SolutionAlgorithm(list_to_treenode(case))
    if solution == expected:
        print(f"Case {i+1}:\n  Input : {input}\n  Output: {solution} (expectly)\n")
    else:
        print(f"Case {i+1}:\n  Input : {input}\n  Output: {solution} (wrong)-->\nExpected: {expected}\n")
print("--------------------------------------------------------")
