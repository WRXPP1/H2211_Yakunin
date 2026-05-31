def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have a problem {exc}")
        else:
            print(f"No problem. Result - {result}")
    return checker

def calculate(expr):
    return eval(expr)

calculate = checker(calculate)
calculate("2+2")