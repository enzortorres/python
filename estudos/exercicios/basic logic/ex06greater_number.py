def greater_number(numbers: list):
    if not numbers:
        return None
    greater = numbers[0]
    for num in numbers:
        if num > greater:
            greater = num

    return greater

print(greater_number([1,4,2,10,5]))
