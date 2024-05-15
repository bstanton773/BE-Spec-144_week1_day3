def my_func(n): # O(n * n)
    num_ops = 0
    for i in range(n): # O(n)
        for j in range(n): # O(n)
            num_ops += 1
            print(i, j)
    print('Num Ops', num_ops)

my_func(4)