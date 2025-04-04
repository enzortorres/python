from itertools import count

c1 = count(10, 8) # > Start: 10; Step: 8;
r1 = range(10, 100, 8) # > Start: 10; Stop: 100; Step: 8;

print('c1', hasattr(c1, "__iter__"))
print('c1', hasattr(c1, "__next__"))

print('range', hasattr(range, "__iter__"))
print('range', hasattr(range, "__next__"))

print('\ncount')
for i in c1:
    if i > 100:
        break
    
    print(i)
    
print('\nrange')
for i in r1:
    print(i)
