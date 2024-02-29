# 2336. Smallest Number in Infinite Set

# Description
"""
https://leetcode.com/problems/smallest-number-in-infinite-set/

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:
● SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
● int popSmallest() Removes and returns the smallest integer contained in the infinite set.
● void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 

Example 1:
    Input
    ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
    [[], [2], [], [], [], [1], [], [], []]
    Output
    [null, null, 1, 2, 3, null, 1, 4, 5]

    Explanation
    SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
    smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
    smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
    smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
    smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
    smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
    smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                    // is the smallest number, and remove it from the set.
    smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
    smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
 

Constraints:
● 1 <= num <= 1000
● At most 1000 calls will be made in total to popSmallest and addBack.
"""

# Code
import heapq
from typing import List, Optional

class SmallestInfiniteSet:
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


# Testcase
class Testcase:
    Case = [
        [
            ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"],
            [[], [2], [], [], [], [1], [], [], []]
        ]
    ]

    Expected = [
        [None, None, 1, 2, 3, None, 1, 4, 5]
    ]

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
    

# Submisstions
def RunClass(cls, operation, content):
    solution = [None]
    for model, value in zip(operation[1:], content[1:]):
        if model == "addBack":
            sol = cls.addBack(value[0])
        elif model == "popSmallest":
            sol = cls.popSmallest()
        solution.append(sol)
    return solution

for i, case in enumerate(Testcase.Case):
    operation, content = case[0], case[1]
    input = f"\n  {operation}\n  {content}"
    solution = RunClass(SmallestInfiniteSet(), operation, content)
    # expected = Testcase.Expected[i]
    expected = RunClass(SolutionAlgorithm(), operation, content)
    if solution == expected:
        print(f"Case {i+1}:\n  Input : {input}\n\n  Output: {solution} (expectly)\n")
    else:
        print(f"Case {i+1}:\n  Input : {input}\n\n  Output: {solution} (wrong)-->\nExpected: {expected}\n")
print("--------------------------------------------------------")
