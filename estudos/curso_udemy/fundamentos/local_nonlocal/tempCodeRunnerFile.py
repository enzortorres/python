def fat(n):
    if n > 1:
        return n * fat(n-1)
    else: 
        return n
    
print(fat(5))