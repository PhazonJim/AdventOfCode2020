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
    # for regex in regexes:
    #     if (re.search(regexes[regex], flair)):
    #         return regex
with open(input_location) as f:
    data = f.read()
mlist = data.split('\n\n')
total = 0
for item in mlist:
    mdict = {}
    for el in item.split():
        key, val = el.split(':')
        mdict[key] = val
    good = True
    for field in vals.keys():
        if field not in mdict.keys():
            good = False
        else:
            res = re.fullmatch(vals[field], mdict[field])
            if not res:
                print(field)
                print(mdict[field]+'\n')
                good = False
            
    if good:
        total+=1
print (total)