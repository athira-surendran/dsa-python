## The time complexity of this function is O(n)
def print_items(n):
    for i in range(0,n):
        print(i)
    for j in range(0,n):
        print(j)

# The bigger the value of n, bigger the time it takes to execute
print_items(10)

# The first loop runs n times
# The second loop runs n time
# So in total the time complexity is O(n+n) = O(2n) = O(n)
# We can drop the constant 2 here while calculating the time complexity of this 