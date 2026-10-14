# Given a number, return the sum of its digits.
# Example:
# Input: 27
# Output: 9
# n =int(input("Please eneter the number :"))
# n.sorted()
# sum = 0
# for i in range(0,len(n)+1):
#     sum = sum + n[i]
# print(f'The sum of the {n} is {sum}')

number = input("Please enter a number: ")

digit_sum = 0
for digit in number:
    digit_sum += int(digit)

print(f"The sum of the digits in {number} is {digit_sum}")
