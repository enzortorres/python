def is_primo(num: int) -> bool:
    if num <= 1:
        return False
    total_div = 0
    for i in range(1, num+1):
        if (num % i == 0):
            total_div += 1
            if total_div > 2:
                return False
    return True

for i in range(1, 12):
    print(f"i is primo? {is_primo(i)}")