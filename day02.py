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

# Answer to part 1
print("Valids:", valid)

### My approach

ans = 0
counter = 0

data_list = inputs.strip().split()

ranges = data_list[::3]

# Getting the first char and excluding the colon ':'
char = [x[0] for x in data_list[1::3]]

password = data_list[2::3]

low = [int(x.split('-')[0]) for x in ranges]
high = [int(x.split('-')[1]) for x in ranges]


for i, p in enumerate(password):
    counter = p.count(char[i])
    if low[i] <= counter <= high[i]:
        ans += 1

print("My solution:", ans)


### PART 2


