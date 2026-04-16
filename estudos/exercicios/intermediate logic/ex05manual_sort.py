def bubble_sort(numbers: list) -> list:
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
        if not swapped:
            break

    return numbers

numbers = [3,1,2,5,4,5,10,2]

print(bubble_sort(numbers))