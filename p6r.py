class PeopleError(Exception):
    def __str__(self):
        return f"Access denied! There's Vasya!"


def check_material(name, bad_name):
    if name == bad_name:
        raise PeopleError()
    else:
        "Access allowed!"



for i in range(3):
    check(input("Enter name"))
check_material("Vasya")