def draw_figure(n):
    if n == 0:
        return

    print("*" * n)    # Pre-action
    draw_figure(n - 1)    # Calling the recursion
    print("#" * n)    # Post-action


n = int(input())
draw_figure(n)


# Variant 2 with no recursion


# def draw_symbols(n):
#     result = ""
#
#     for i in range(n, 0, -1):
#         result += "*" * i + "\n"
#
#         n -= 1
#
#     return result.strip()
#
#
# def draw_symbols_new(n):
#     result = ""
#
#     for i in range(1, n + 1):
#         result += "#" * i + "\n"
#
#         n += 1
#
#     return result.strip()
#
#
# n = int(input())
# print(draw_symbols(n))
# print(draw_symbols_new(n))