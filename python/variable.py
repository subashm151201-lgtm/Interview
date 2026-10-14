# 1. Instance variable
# Belongs to a particular object. Each object can have its own value.

# 2. Class variable
# Shared at the class level by instances, unless an instance shadows it with its own attribute.

# 3. Global variable
# Defined outside a function or class at the module level. Functions can read it, and global allows them to reassign it.

# 4. Static variable
# Usually refers to a class variable in Python. It is associated with the class rather than an individual object.

# 5. Local variable
# Defined inside a function and normally available only within that function.

# 1. Instance variables
# Instance variables store data specific to each object .

class Student:
    def __init__(self,name,standard):
        self.name = name
        self.standard = standard

    def func1(self):
        print(self.name)
        print(self.standard)

st = Student("Subash" ,10)
st1 = Student("Kittu" ,9)

# st.fun1()
# st1.fun1()


st.func1()
st1.func1()
 