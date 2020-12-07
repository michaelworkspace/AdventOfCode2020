from typing import List


def find_product(inputs: List[int]) -> int:
    """Given a list of integers, if the sum of two element is 2020, return it's product."""

     # This is the classic Two Sum problem
     # This is not good solution because it is O(n^2)
#    for x in INPUTS:
#        for y in INPUTS:
#            if x + y == 2020:
#                ans = x * y
#    return ans


    # This is the optimal solution because its time complexity is O(n)
    needs = {2020 - x for x in inputs}

    for num in inputs:
        if num in needs:
            ans = num * (2020-num)
    return ans

"""--- PART 2 --- """


def find_product_part2(inputs: List[int]) -> int:
    """Given a list of integers, if the sum of three element is 2020, return it's product."""


    n = len(inputs)
    # This is the classic Three Sum problem
    # Naive run time is O(n^3) cube which is not very efficient
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if inputs[i] + inputs[j] + inputs[k] == 2020:
                    ans = inputs[i] * inputs[j] * inputs[k]
    return ans


with open("Inputs/day01.txt") as f:
    inputs = [int(line.strip()) for line in f]
    print(find_product(inputs))
    print(find_product_part2(inputs))
