input_location = './input/day2.txt'
with open(input_location) as f:
    strings = [line.strip() for line in f.readlines()]
total = 0
for p_string in strings:
    p_range, letter, password = p_string.split(' ')
    x, y = p_range.split('-')
    letter = letter.split(':')[0]
    # Start Part 1
    count = len(list(filter(lambda x: x==letter, password)))
    total += (int(x) <= count <= int(y)) # End Part 1
    # Start Part 2
    # total += (password[int(x)-1]==letter) + (password[int(y)-1]==letter) == 1 # End Part 2

print (total)
