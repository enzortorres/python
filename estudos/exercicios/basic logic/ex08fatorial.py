def fat(n):
    if n <= 1:
        return 1
    return n * fat(n - 1)

print(fat(5))