try:
    print("xyz"+1)
    a="Thor"
    print(int(a))
except Exception as error:
    print(error)
def square(x):
    """This function returns the square of input"""
    return x**2
print(square.__doc__)
for i in range (1,11):
    print(square(i))
