from itertools import chain

input_location = './input/day5.txt'

def get_pos(arr, chars, pos):
    if len(arr) > 1:
        if chars[pos] in ['F', 'L']:
            return get_pos(arr[:len(arr)//2], chars, pos+1)
        else:
            return get_pos(arr[len(arr)//2:], chars, pos+1)
    else:
        return arr[0]

with open(input_location) as f:
    seats = [seat.strip() for seat in f.readlines()]

rows = [i for i in range(0,128)]
cols = [i for i in range(0,8)]
plane = [[0 for x in range(0,8)] for x  in range(0,128)]
for seat in seats:
    row = get_pos(rows, seat, 0)
    col = get_pos(cols, seat, 7)
    plane[row][col] = row*8+col

flat = list(chain(*plane))
print(max(flat))

for i, seat in enumerate(flat):
    if seat == 0 and flat[i-1] and flat[i+1]:
        print (i)