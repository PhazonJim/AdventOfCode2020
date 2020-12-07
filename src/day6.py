from functools import reduce
input_location = './input/day6.txt'

#Part 1
groups = []
with open(input_location) as f:
    chunks = f.read().split('\n\n')
    groups = [set(chunk.replace('\n','')) for chunk in chunks]

print(reduce(lambda count, l: count + len(l), groups, 0))

#Part 2
groups = []
with open(input_location) as f:
    chunks = f.read().split('\n\n')
    groups = [[set(person) for person in chunk.split()] for chunk in chunks]

groups = [set(group[0]).intersection(*group) for group in groups]
print(reduce(lambda count, l: count + len(l), groups, 0))
