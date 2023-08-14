def print_multiplication_table(n, m):
    for i in range(1, 11):
        for j in range(1, 11):
            print(i*n, "x", j*m, "=", i*n*j*m)
        print()
            

print_multiplication_table(2, 3)