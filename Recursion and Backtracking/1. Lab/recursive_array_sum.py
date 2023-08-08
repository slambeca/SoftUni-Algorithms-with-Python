# With recursion


def sum_numbers(array, idx):
    if idx == len(array) - 1:
        return array[idx]
    return array[idx] + sum_numbers(array, idx + 1)


numbers = [int(x) for x in input().split()]

print(sum_numbers(numbers, 0))


numbers = [int(x) for x in input().split()]

# Variant 2 with no recursion
print(sum([int(x) for x in input().split()]))    # [1, 2, 3, 4]

result = sum(numbers)

print(result)

# Variant 3 - the shortest
print(sum([int(x) for x in input().split()]))