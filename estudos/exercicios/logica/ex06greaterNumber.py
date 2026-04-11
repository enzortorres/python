def greaterNumber(numbers: list):
    greater = 0
    for num in numbers:
        if num > greater:
            greater = num

    return greater

print(greaterNumber([1,4,2,10,5]))
