def calc_factorial(n):
    if n <= 1:
        return 1

    return n * calc_factorial(n - 1)


n = int(input())

print(calc_factorial(n))


# Variant 2 with no recursion

# def factorial(n):
#     factorial_num = 1

#     for i in range(n, 0, -1):
#         factorial_num *= i

#     return factorial_num


print(factorial(int(input())))
