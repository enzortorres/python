d1 = {
    'c1': 1,
    'c2': 2,
}

d2 = d1
d2['c1'] = 4 
print(d1)
print(d2)

d3 = d1.copy()

print(d3)
print(d3['c2'])
