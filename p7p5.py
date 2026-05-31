from unittest import result


def raise_to_degrees(number):
    i = 0
    while True:
        result = number ** i
        yield result
        if result > 100 ** 20:
            return
        i += 1



res = raise_to_degrees(34)
# print(res)
for el in res:
    print(el)