input_location = './input/day7.txt'

#Part 1
rules = {}
with open(input_location) as f:
    chunks = f.read().split('\n')
    for rule in chunks:
        rule_id, conditions = rule.split('contain')
        rule_id = rule_id.strip().replace(' bags','')
        if rule_id not in rules:
            rules[rule_id] = {}
        for condition in conditions.split(','):
            cType = condition.strip().split(' ')
            if len(cType) == 3:
                rules[rule_id] = None
            else:
                num, adj, color, bag = condition.strip().split(' ')
                rules[rule_id][' '.join((adj,color))] = num

def can_hold_gold(rule):
    if not rules[rule]:
        return 0
    else:
        res = 0
        for sub_rule in rules[rule]:
            if sub_rule == 'shiny gold':
                res += 1
            else:
                res += can_hold_gold(sub_rule)
        return res > 0            

def sum_bags(rule):
    res = 1
    if not rules[rule]:
        return res
    else:
        for sub_rule in rules[rule]:
            factor = int(rules[rule][sub_rule])
            prev = sum_bags(sub_rule)
            res += prev * factor
        return res    

total1 = 0
total2 = -1
# Part 1
for rule in rules:
    total1 += can_hold_gold(rule)
total2 += sum_bags('shiny gold') # Part 1 uses can_hold_gold
print (total1)
print (total2)