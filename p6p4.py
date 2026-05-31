def checker(var1):
    if type(var1) != str:
        raise TypeError(f"Sorry, we can't work with {type(var1)}, only str used")
    else:
        return var1


f_var = "Vasya"
s_var = 6

checker(f_var)
checker(s_var)