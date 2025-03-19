import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2],
}

d2 = copy.deepcopy(d1)

d2['c1'] = 100
d2['l1'][1] = 99999999999

print(d1)
print(d2)