import statistics as stat

"""
Define a function that takes an indefinite number of numbers as arguments and returns their average. If I called your function with foo(10, 20, 30, 40) it should return the 25, the average of those numbers.
"""


def indefinite(*args):
    return stat.mean(args)


print(indefinite(10, 20, 30, 40))
