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