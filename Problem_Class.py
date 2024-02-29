# ● 

# Description
"""

"""

# Code
from typing import List, Optional

class ClassName:
    def __init__(self) -> None:
        self.null = None
    def function1(self) -> type:
        return

# Testcase
class Testcase:
    Case = [
        [
            ["ClassName", "function1"], 
            [[], []]
        ]
    ]
    Expected = [
        [None, None]
    ]
    

# Submisstions
def RunClass(cls, operation, content):
    solution = [None]
    for model, value in zip(operation[1:], content[1:]):
        if model == "function1":
            sol = cls.function1()
        solution.append(sol)
    return solution

for i, case in enumerate(Testcase.Case):
    operation, content = case[0], case[1]
    input = f"\n  {operation}\n  {content}"
    solution = RunClass(ClassName(), operation, content)
    # expected = Expected[i]
    expected = RunClass(ClassName(), operation, content)    
    if solution == expected:
        print(f"Case {i+1}:\n  Input : {input}\n\n  Output: {solution} (expectly)\n")
    else:
        print(f"Case {i+1}:\n  Input : {input}\n\n  Output: {solution} (wrong)-->\nExpected: {expected}\n")
print("--------------------------------------------------------")
