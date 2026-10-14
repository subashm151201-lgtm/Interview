# Given a string, find the first non-repeating character.
# Example:
# Input:
# "swiss"

# Output:
# "w"
# n = input("please eneter the string")
# n = sorted(n)
# count = 0
# for i in range(len(n)):
#     for j in range(1,len(n)):
#         if n[i] == n[j]:
#             count += 1
#         else:
#             print(n[i])
text = input("Please enter a string: ")

counts = {}

for char in text:
    counts[char] = counts.get(char, 0) + 1

first_unique = None

for char in text:
    if counts[char] == 1:
        first_unique = char
        break

if first_unique is not None:
    print(first_unique)
else:
    print("No non-repeating character found")