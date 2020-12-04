import re
input_location = './input/day4.txt'
vals = {
    'byr': r'^19[2-9][0-9]|200[0-2]$',
    'iyr': r'^20(1[0-9]|20)$',
    'eyr': r'^20(2[0-9]|30)$', 
    'hgt': r'1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in', 
    'hcl': r'#[\da-f]{6}', 
    'ecl': r'amb|blu|brn|gry|grn|hzl|oth', 
    'pid': r'\d{9}'
}
with open(input_location) as f:
    chunks = f.read().split('\n\n')
    documents = [{k: v for (k,v) in [kv.split(':') for kv in chunk.split()]} for chunk in chunks]
total = 0
for document in documents:
    good = True
    for field in vals.keys():
        if field not in document.keys():
            good = False
        else:
            if not re.fullmatch(vals[field], document[field]):
                good = False
    if good:
        total+=1
print (total)