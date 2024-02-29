# ● 

# Description
"""

"""

# Code
from typing import List, Optional

class Solution:
    def LeetcodeExample(self, __: type) -> type:
        return


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
    solution  = Sol.LeetcodeExample(__ = case)
    input = f"__ = {case}"
    expected = Testcase.Expected[i]
    # expected = Testcase.SolutionAlgorithm(case)
    if solution == expected:
        print(f"Case {i+1}:\n  Input : {input}\n  Output: {solution} (expectly)\n")
    else:
        print(f"Case {i+1}:\n  Input : {input}\n  Output: {solution} (wrong)-->\nExpected: {expected}\n")
print("--------------------------------------------------------")
