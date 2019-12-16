#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime complexity is O(n). 
```python
a = 0 # O(1)
while (a < n * n * n): # O(3n)
    a = a + n * n # O(2n)

 # O(1) + O(3n) + O(2n) = O(5n) = O(n)
 # Despite the function being a multiple of N the performance is still a linear increase in relation to the input
```

b) Runtime complexity is O(n^2).
```python
sum = 0 # O(1)
for i in range(n): # O(n) 
    j = 1 # O(1)
    while j < n: # O(n*n)
        j *= 2 # O(1)
        sum += 1 # O(1)
# O(1) + O(n) + O(n^2) + O(1) + O(1) = O(3n+n^2) = O(n^2)
# Runtime complexity increases exponentially because of the nested loops
```


c) Runtime complexity is O(n). The number of recursive function calls is in direct proportion to the size of N.

## Exercise II
```
PROBLEM ANALYSIS - ASSUMPTIONS
1. Can I restate the problem in my own words?
Determine which floor of the building is high enough to break an egg if dropped from that floor
2. What are the input that go into the problem?
	- Confirm required data types (string, integers, floats, arrays, objects) POSITVE INTEGERS GREATER THAN 0
	- Can negative numbers be included? NO
  - Confirm upper/lowercase enforcement N/A
	- Confirm whitespace and punctuation N/A
	- Confirm if each argument must be the same length (strings and arrays) N/A
	- Confirm upper and lower bound limits of integers and floating points LOWER LIMIT: 0
3. What are the outputs that should come from the solution to the problem? POSITIVE INTEGER
4. Can the outputs be determined from the inputs? WE WOULD NEED INPUT THAT PROVIDES THE STATUS OF A DROPPED EGG
5. Any time or space constraints with the solution? O(N)
6. How should I label the important pieces of data that are part of the problem?
n = Number of floors
f = lowest floor where a dropped egg will break
not_broken = True/False 
```

```
ALGORITHM
1. Check for any edge cases. Confirm the proper data type of lower/upper limits are being passed to the function
2. Declare a variable `broken_eggs` and set it to 0 to track number of broken eggs
3. Declare variable `f` and set it to 1 to track the floor we're on
4. Create a loop block that continues while there are no broken eggs
    It increments the `f` value by 1 with each iteration and checks to see if a dropped egg is broken
5. Once an egg breaks then the loop terminates and returns the value of `f`
```
```python
# Pseudo Code
def findFloor(n):
    not_broken = True
    f = 1

    while not_broken == 0:
        f += 1
    
    return 1
```
```
RUNTIME COMPLEXITY: O(n)
``

