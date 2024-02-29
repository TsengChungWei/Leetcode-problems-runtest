# 938. Range Sum of BST

# Description
"""
https://leetcode.com/problems/range-sum-of-bst/description/

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


Example 1:
    https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg
    |       10
    |     ／  ＼　
    |    5     15
    |  ／ ＼　   ＼
    | 3    7      18
    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32
    Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
    https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg
    |           10
    |        ／    ＼
    |       5       15
    |     ／ ＼    ／  ＼
    |    3    7  13     18
    |  ／    ／ 
    | 1 `   6
    Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    Output: 23
    Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
    

Constraints:
● The number of nodes in the tree is in the range [1, 2 * 10^4].
● 1 <= Node.val <= 10^5
● 1 <= low <= high <= 10^5
● All Node.val are unique.
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        if root is None:
            return 0
        if root.val < low:
            result += self.rangeSumBST(root.right, low, high)
        elif low <= root.val and root.val <= high:
            result += root.val
            result += self.rangeSumBST(root.left, low, high)
            result += self.rangeSumBST(root.right, low, high)
        elif high < root.val:
            result += self.rangeSumBST(root.left, low, high)

        return result

# Testcase
class Testcase:
    Case = [
        [[10,5,15,3,7,None,18], 7, 15],
        [[10,5,15,3,7,13,18,1,None,6], 6, 10],
        [[10,5,15,4,6,14,16], 6, 15]
    ]

    Expected = [
        32,
        23,
        45
    ]
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
    
# Submisstions
for i, case in enumerate(Testcase.Case):
    Sol = Solution()
    solution  = Sol.rangeSumBST(root = list_to_treenode(case[0]), low = case[1], high = case[2])
    input = f"root = {case[0]}, low = {case[1]}, high = {case[2]}"
    # expected = Testcase.Expected[i]
    expected = Testcase.SolutionAlgorithm(list_to_treenode(case[0]), case[1], case[2])
    if solution == expected:
        print(f"Case {i+1}:\n  Input : {input}\n  Output: {solution} (expectly)\n")
    else:
        print(f"Case {i+1}:\n  Input : {input}\n  Output: {solution} (wrong)-->\nExpected: {expected}\n")
print("--------------------------------------------------------")
