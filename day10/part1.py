from dataclasses import dataclass
from typing import List

OPENING_TO_CLOSING_CHAR = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}",
}

@dataclass(frozen=True)
class UnexpectedClosingError(Exception):
    found: str

def parse(line: str) -> List[str]:
    closing_stack = []
    for char in line:
        if char in OPENING_TO_CLOSING_CHAR:
            closing_stack.insert(0, OPENING_TO_CLOSING_CHAR[char])
        elif closing_stack and closing_stack[0] == char:
            del closing_stack[0]
        else:
            raise UnexpectedClosingError(found=char)
    return closing_stack

def score(line: str) -> int:
    try:
        parse(line)
        return 0
    except UnexpectedClosingError as error:
        return _scores[error.found]

_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

if __name__ == "__main__":
    import fileinput
    print(
        sum(
            score(str(line.strip()))
            for line in fileinput.input()
        )
    )
