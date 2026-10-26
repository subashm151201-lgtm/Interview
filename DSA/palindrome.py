n = input("please enter the  string  :")
m = "".join(reversed(n))

print(m)

if n  == m :
    print(" It is a palindrome")
else:
    print(" It is not a palindrome .")


# Find the second-largest number.

n = [1, 4, 5, 4, 5, 12, 3, 5]

# unique_numbers = sorted(set(n))
n.sort()

print(n)

print(n[len(n)-2])
# if len(unique_numbers) >= 2:
#     print("Second-largest:", unique_numbers[-2])
# else:
#     print("There is no second-largest distinct number.")

# Remove duplicates while preserving order.

n = [1, 4, 5, 4, 5, 12, 3, 5]

m = set(n)

print(list(m))
