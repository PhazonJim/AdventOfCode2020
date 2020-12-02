from itertools import combinations
from functools import reduce
nums = []
pair_length = 3
target = 2020
input_location = './input/day1.txt'
with open(input_location) as f:
    nums = [int(line.strip()) for line in f.readlines()]
magic_number = [reduce((lambda a, b: a*b), x) for x in combinations(nums,pair_length) if sum(x) == target]
print(magic_number)