from functools import cache

@cache
def count(days, number):
    return (
        1 if days <= number
        else count(days - number, 7) + count(days - number, 9)
    )

import fileinput

first_line = str(next(fileinput.input()).strip())
numbers = [int(i) for i in first_line.split(",")]
print(sum(count(256, number) for number in numbers))
