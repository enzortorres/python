def fat(n):
    if n > 1:
        return n * fat(n-1) # > 2x1 | 3x2 | 4x6 | 5x24
    return n

print(fat(6))