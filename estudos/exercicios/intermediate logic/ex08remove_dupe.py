def remove_dupe(numbers: list) -> list:
    no_dupe_numbers = []
    seen = set()
    for num in numbers:
        if num not in seen:
            no_dupe_numbers.append(num)
            seen.add(num)

    return no_dupe_numbers

print(remove_dupe([1,2,2,5,4,2,2]))