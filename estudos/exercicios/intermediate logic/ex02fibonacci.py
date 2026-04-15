def fibonacci_1(num: int) -> list:
    fib_numbers = [0, 1]
    prev, curr = fib_numbers

    if num == 1:
        return [0]
    
    while (len(fib_numbers) < num):
        next_number = prev + curr
        fib_numbers.append(next_number)
        prev, curr = curr, next_number
    
    return fib_numbers

print(fibonacci_1(10))

def fibonacci_2(num: int) -> list:
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    
    fib_numbers = [0,1]
    
    while (len(fib_numbers) < num):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

    return fib_numbers

print(fibonacci_2(10))