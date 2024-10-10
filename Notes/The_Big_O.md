# The Big O
- Big O is the way of comparing two sets of code mathematically,
telling how efficiently they run

# Time complexity
- Say we have code 1 and code 2
Code 1 takes 15 seconds to run on a system
Code 2 takes 60 seconds to run on the same system
We can conclude that code 1 is better than code 2
This is called Time Complexity

- The thing about time complexity that is interesting is that it is NOT measured in time.
Because if you took the same code and ran it on a computer that runs twice as fast, it would complete twice as fast. It doesn't make the code any better. It just means the computer is better.

- So it is measured in the "number of operations that it takes to complete something".

# Space Complexity
- In addition to time complexity, we measure space complexity.
So let's say that code one.
While it runs very fast comparatively, let's say it takes up a lot of memory when it runs.
And maybe code two, even though that takes much longer to finish.
Maybe it takes up less memory.

- If preserving memory space is your most important priority and you don't mind having some extra time
complexity, maybe code two is better.

============================================================================

# Big O: Worst Case
- So when we dealing with time complexity and space complexity, there are three Greek letters that you will see and they are omega (Ω), theta (Θ) and Omicron (O).
- Omicron is better known as O, as in big O.
- Let's say you have a list with seven items in it, and you're going to build a for loop to iterate through this list to find a specific number.

[1,2,3,4,5,6,7]

- So let's say you're looking for the number one.This is your best case scenario. You're going to find this in one operation.

- But if you're looking for the number seven that is your worst case scenario. You have to iterate through the entire list to be able to get to it.

- If you're looking for the number four, that's your average case. So when someone talks about the best case scenario for running a piece of code that is Omega, the average case is theta and worst case is Omicron or O.

- Technically when you talk about big O you are always talking about worst case.

============================================================================

# Big O - O(n)
- In a graph where x is n and y is number of operations O(n) forms a straight line.
- Code example:

def print_items(n):
    for i in range(0,n):
        print(i)

print_items(10)

- The time complexity of this code snippet is O(n)

============================================================================

# Big O: Drop the constants
- Drop the constants while calculating Big O
- Code example:

def print_items(n):
    for i in range(0,n):
        print(i)

    for j in range(0,n):
        print(j)

print_items(10)

- The first loop runs n times
- The second loop runs n time
- So in total the time complexity is O(n+n) = O(2n) = O(n)

============================================================================

# Big O - O(n^2)
- In a graph where x is n and y is number of operations O(n) forms a exponential graph.
- Code example:

def print_items(n):
    for i in range(0,n):
        for j in range(0,n):
            print(i,j)

print_items(10)

Output:
00
01
02
.
.
.
97
98
99

n*n = n^2 outputs

- The time complexity of this code snippet is O(n^2)

============================================================================

# Drop the Non-Dominants

Say we have this code,

def print_numbers(n):
    for i in range(0,n):
        for j in range(0,n):
            print(i,j) # O(n^2)

    for k in range(0,n):
        print(k) # O(n)

print_numbers(10) # O(n^2 + n) ==> O(n^2)

- The time complexity of this code will be
- O(n^2) + O(n) = O(n^2 + n) ---> which can be approximated to O(n^2)
- Here, O(n) will be a non-determinant

- Say n = 100
- O(n^2 + n) = O(100*100 + 100) = O(10000 + 100) = O(100100) ==> O(10000)

===================================================================

# Big O - O(1) --- Constant time

- This code takes a constant time to execute - O(1)

def add(a,b):
    return a+b

print(add(10,20))

- The time this program takes to execute is not dependant on its inputs

- In a graph where x is n and y is number of operations O(1) forms a straight line parallel to x axis.

=====================================================================================

# Big O - O(log n) [DEVIDE & CONQUER]

- Say we have a sorted list (n = 8)
1,2,3,4,5,6,7,8

Say I want to find number 1. I will devide the list by half and check in each half
1,2,3,4

1,2

1

- Hence I took "3" steps to find 1
- log of 8 base 2 = 3 --> log2(8) = 3 ==> O(log n) 

======================================================

# Most efficient a sorting algorithm can get is O(n log n)

=========================================================

# Big O - Lists
=================
- List 0[11], 1[3], 2[23], 3[7]

- Append 17
List 0[11], 1[3], 2[23], 3[7], 4[17]
my_list.append(17)
# O(1) 

- Pop last
List 0[11], 1[3], 2[23], 3[7]
my_list.pop()
# O(1)

- Pop at 0
List 0[11], 1[3], 2[23], 3[7]
my_list.pop(0)

Remove -  1[3], 2[23], 3[7]
Re Index -  0[3], 1[23], 2[7]

# 0(n)

- Insert at 0 or beginning
List  0[3], 1[23], 2[7]
my_list.insert(0,11)

Insert -   0[11], 0[3], 1[23], 2[7]
Re Index -  0[11], 1[3], 2[23], 3[7]

# 0(n)

- Insert at end
List  0[3], 1[23], 2[7]
my_list.insert(77)

Insert - 0[3], 1[23], 2[7], 3[77]

# 0(1)

- Insert in random position or middle 
# O(n)

- Search by value
# O(n)

- Get value by index
# O(1)

================================================
# Big-O Complexity Chart
https://www.bigocheatsheet.com/







