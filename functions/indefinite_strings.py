"""
Define a function that takes an indefinite number of strings as parameters and returns a list containing all the strings in UPPERCASE and sorted alphabetically. For example, if I called your function with foo("snow", "glacier", "iceberg") it should return ["GLACIER", "ICEBERG", "SNOW"].
"""


def indefinite(*args):
    return sorted([name.upper() for name in args])


print(indefinite("snow", "glacier", "iceberg"))
