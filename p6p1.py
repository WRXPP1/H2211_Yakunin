try:
    print('start code')
    print(10/0)
    print('No error')
except NameError:
    print("Oops, there's an error in our project!")
except ZeroDivisionError:
    print("Oops, there's impossible division by zero!")
print('Code after capsule')