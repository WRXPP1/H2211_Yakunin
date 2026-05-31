class BuildingError(Exception):
    def __str__(self):
        return f"With this amount of materials the house can't be build!"


def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return "Enough material"
    else:
        raise BuildingError(amount_of_material)



rock = 5000
check_material(rock, 1200)