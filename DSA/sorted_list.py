# Medium: Merge Two Sorted Lists
# Given two sorted lists of integers, merge them into one sorted list.
# a = [1, 4, 7, 10]
# b = [2, 3, 8, 11]
# output : [1, 2, 3, 4, 7, 8, 10, 11]

a = [1, 4, 7, 10]
b = [2, 3, 8, 11]

output = a + b

output.sort()

print(f"output {output}")


#  Time complxetity  
a = [1, 4, 7, 10]
b = [2, 3, 8, 11]

i = 0
j = 0

output = []

while i < len(a) and j < len(b) :
    if a[i] <= b[j]:
        output.append(a[i])
        i += 1
    else:
        output.append(b[j])
        j += 1

output.extend(a[i :])
output.extend(b[j :])

print(output)