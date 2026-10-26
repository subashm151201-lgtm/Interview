# Input:  arr = [10, 20, 30, 40, 50]
#       target = 30

# Output: 2

arr = [10, 20, 30, 40, 50]
target = 30

for i in range(len(arr)):
    if target == arr[i]:
        print(f"target value {target} and its index  {arr[i]}")
        break

# Given an array and a target value, count how many times the target appears in the array.

# Input:  arr = [2, 5, 2, 8, 2, 9]
 # target = 2

# Output: 3

arr = [2, 5, 2, 8, 2, 9]
target = 2
count = 0

for i in range(len(arr)):
    if target == arr[i]:
        count += 1
        
print(f" In {arr} {target } is repeating {count} times . ")
        

    
# Given an array of integers, find the largest element without using the built-in max() function.

# Example:
# Input:  [12, 45, 7, 89, 23]

# Output: 89

arr = [12, 45, 7 , 89 , 23]

arr.sort()
print(arr[len(arr)-1])

print(arr[0])

# Given an array and a target value, find all indices where the target occurs.

# Example:
# Input:  arr = [4, 2, 7, 2, 9, 2]
#         target = 2

# Output: [1, 3, 5]    


arr = [4, 2, 7, 2, 9, 2]

target = 2

indices = []

for i in range(len(arr)):
    if target == arr[i]:
        indices.append(i)

print(indices)

# Given an array and a target value, determine whether the target exists in the array.

# Return True if it exists; otherwise, return False.

# Example:
# Input:  arr = [11, 22, 33, 44]
#         target = 33

# Output: True

arr = [11, 22, 33, 44]

target = 33

for i in range(len(arr)) :
    if target == arr[i]:
        True
    else:
        False
