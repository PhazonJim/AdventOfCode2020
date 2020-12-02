nums = []
with open('./input/day1.txt') as f:
    for line in f.readlines():
        nums.append(int(line.strip()))
for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums):
        if i != j and (num1 + num2) == 2020:
            print(num1 * num2)