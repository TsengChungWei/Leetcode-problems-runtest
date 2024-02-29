# 1578. Minimum Time to Make Rope Colorful

# Description
"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is 
the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, 
so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. 
You are given a 0-indexed integer array neededTime where neededTime[i] is the time 
(in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.


Example 1:
    https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg
    |    a   b   a   a   c
    |            ⇩
    |    a   b       a   c
    Input: colors = "abaac", neededTime = [1,2,3,4,5]
    Output: 3
    Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
    Bob can remove the blue balloon at index 2. This takes 3 seconds.
    There are no longer two consecutive balloons of the same color. Total time = 3.

Example 2:
    https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg
    |    a   b   c
    |        ⇩
    |    a   b   c
    Input: colors = "abc", neededTime = [1,2,3]
    Output: 0
    Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

Example 3:
    https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg
    |    a   a   b   a   a
    |            ⇩
    |        a   b   a    
    Input: colors = "aabaa", neededTime = [1,2,3,4,1]
    Output: 2
    Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
    There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
 

Constraints:
● n == colors.length == neededTime.length
● 1 <= n <= 10^5
● 1 <= neededTime[i] <= 10^4
● colors contains only lowercase English letters.
"""

# Code
from typing import List, Optional

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # ---------------- method1 ----------------
        # def non_max_sum(array):
        #     max_num, sum_nums = 0, 0
        #     for num in array:
        #         if max_num > num:
        #             sum_nums += num
        #         else:
        #             sum_nums += max_num
        #             max_num = num
        #     return sum_nums
        
        # compare_time = [neededTime[0]]
        # result = 0
        # for i in range(1, len(neededTime)):
        #     if colors[i-1] == colors[i]:
        #         compare_time.append(neededTime[i])
        #     else:
        #         result += non_max_sum(compare_time)
        #         compare_time = [neededTime[i]]
        # result += non_max_sum(compare_time)
        # return result

        # ---------------- method2 ----------------
        # max_num = neededTime[0]
        # result = sum(neededTime)
        # for i in range(1, len(neededTime)):
        #     if colors[i-1] == colors[i]:
        #         if max_num < neededTime[i]:
        #             max_num = neededTime[i]
        #     else:
        #         result -= max_num
        #         max_num = neededTime[i]
        # result -= max_num
        # return result
    
        # ---------------- method3 ----------------
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

# Testcase
class Testcase:
    Case = [
        ["abaac", [1,2,3,4,5]],
        ["abaaa", [1,2,3,1,5]],
        ["aabaaa", [1,2,4,3,1,5]],
        ["aabaaaa", [1,2,4,3,1,5,6]],
        ["abc", [1,2,8]],
        ["aabaa", [1,2,3,4,1]],
        ["aaa", [1,1,1]]
    ]

    Expected = [
        3,
        4,
        5,
        10,
        0,
        2,
        2
    ]
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
    

# Submisstions
for i, case in enumerate(Testcase.Case):
    Sol = Solution()
    solution  = Sol.minCost(colors = case[0], neededTime = case[1])
    input = f"colors = {case[0]}, neededTime = {case[1]}"
    expected = Testcase.Expected[i]
    # expected = Testcase.SolutionAlgorithm(case[0], case[1])
    if solution == expected:
        print(f"Case {i+1}:\n  Input : {input}\n  Output: {solution} (expectly)\n")
    else:
        print(f"Case {i+1}:\n  Input : {input}\n  Output: {solution} (wrong)-->\nExpected: {expected}\n")
print("--------------------------------------------------------")
