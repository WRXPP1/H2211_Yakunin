def checker(function, *args, **kwargs):
    try:
        result = function(*args, **kwargs)
    except Exception as exc:
        print(f"We have a problem {exc}")
    else:
        print(f"No problem. Result - {result}")


def calculate(expr):
    return eval(expr)

checker(calculate, "2+2")