try:
    print('start code')
    print(10/0)
    print('No error')
except (NameError, ZeroDivisionError):
    print("Oops, there's an error in our project!")
print('Code after capsule')