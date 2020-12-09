input_location = './input/day8.txt'
import copy
ops = []

with open(input_location) as f:
    chunks = f.read().split('\n')
    for i , op in enumerate(chunks):
        command, value = op.split(' ')
        ops.append([command, int(value)])

for i in range(0, len(ops)-1):
    ops_c = copy.deepcopy(ops)
    index = 0
    acc = 0
    if ops_c[i][0] == 'jmp':
        ops_c[i][0] = 'nop'
    elif ops_c[i][0] == 'nop':
        ops_c[i][0] = 'jmp'
    while True:
        if not ops_c[index]:
            break
        else:
            command = ops_c[index][0]
            next_index = index
            if command == 'nop':
                next_index+=1
            elif command == 'acc':
                acc += ops_c[next_index][1]
                next_index+=1
            elif command == 'jmp':
                next_index+=ops_c[next_index][1]
            if next_index >= len(ops_c):
                print(acc)
                exit()
            ops_c[index] = None
            index = next_index % len(ops_c)