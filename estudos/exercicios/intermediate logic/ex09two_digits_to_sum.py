def two_sum(numbers: list, target: int) -> list:
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
numbers = [1,2,3,4,5,6,7,8,9]

print(two_sum(numbers, 15))