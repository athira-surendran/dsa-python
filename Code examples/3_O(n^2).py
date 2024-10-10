## The time complexity of this function is O(n^2)
def print_items(n):
    for i in range(0,n):
        for j in range(0,n):
            print(i,j)
  
# Time increases exponentially to n in order of 2
print_items(10)