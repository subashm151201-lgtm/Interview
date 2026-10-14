# Difference between == and is
# == (Equality operator): Checks whether two objects have the same value.
# is (Identity operator): Checks whether two variables refer to the exact same object in memory.


a = [10, 20, 30]
b = [10, 20, 30]

print(a == b)
print(a is b)
print(a is a)