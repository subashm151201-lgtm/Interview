# Find Duplicate Elements
# Given a list of integers, find all duplicate values without returning the same duplicate more than once.
# Input: nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]
# output : [2, 1, 3]

nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]
output = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            output.append(nums[i]) # here we are appending the data .
print(f'output : {output}')

#  Decreasing time  time complexity .

nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]

counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1

output = []
added = set()

for num in nums:
    if counts[num] > 1 and num not in added:
        output.append(num)
        added.add(num)

print(f"output: {output}")