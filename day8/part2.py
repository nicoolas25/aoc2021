from itertools import permutations
from typing import Callable, List, Tuple

Digit = str
Digits = List[Digit]

REF_WIRES_TO_DIGIT = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

def sorted_str(s: str) -> str:
    return "".join(sorted(s))

def generate_parser_fn(samples: Digits) -> Callable[[Digits], int]:
    trans = next(
        translation
        for translation in (
            str.maketrans("".join(translation_key), "abcdefg")
            for translation_key in permutations("abcdefg")
        )
        if all(
            sorted_str(sample.translate(translation)) in REF_WIRES_TO_DIGIT
            for sample in samples
        )
    )

    def parser_fn(digits: Digits) -> int:
        return int("".join([
            str(REF_WIRES_TO_DIGIT[sorted_str(digit.translate(trans))])
            for digit in digits
        ]))

    return parser_fn

def read_input(line) -> Tuple[Digits, Digits]:
    samples, digits = [part.split() for part in line.split(" | ")]
    return (samples, digits)

if __name__ == "__main__":
    import fileinput

    total = 0
    for line in fileinput.input():
        samples, digits = read_input(line.strip())
        total += generate_parser_fn(samples)(digits)
    print(total)
