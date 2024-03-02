# Given code
def isEven(value):
    return value % 2 == 0


# My code
def isEven2(value: int) -> bool:
    return not value ^ 1
