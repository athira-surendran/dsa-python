def print_numbers(n):
    for i in range(0,n):
        for j in range(0,n):
            print(i,j) # O(n^2)

    for k in range(0,n):
        print(k) # O(n)

print_numbers(10) # O(n^2 + n) ==> O(n^2)