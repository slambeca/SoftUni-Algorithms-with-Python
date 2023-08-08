def get_operations_count(n):
    counter = 0    # One operation here

    for i in range(n):    # This will be executed n times
        for j in range(n):    # This will be executed n times
            counter += 1    # We have 2 operations here, counter = something and counter + something

    return counter    # One operation here


print(get_operations_count(4))    # 16