from typing import List


with open("Inputs/day02.txt") as f:
    inputs = f.read()

valid = 0
lines = inputs.splitlines()

def compute(line):
    x = line.split(" ")
    amounts = [int(i) for i in x[0].split("-")]
    char = x[1][0]
    password = x[2]

    count = 0
    for i in password:
        count += i == char

    return amounts[0] <= count <= amounts[1]

for line in lines:
    valid += compute(line)


print(valid)
