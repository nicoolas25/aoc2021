from part1 import parse, UnexpectedClosingError

def score(line: str) -> int:
    try:
        total = 0
        for closing_char in parse(line):
            total = total * 5 + _scores[closing_char]
        return total
    except UnexpectedClosingError:
        return 0

_scores = { ")": 1, "]": 2, "}": 3, ">": 4 }

if __name__ == "__main__":
    import fileinput
    all_scores = (score(str(line.strip())) for line in fileinput.input())
    non_zero_scores = [non_zero_score for non_zero_score in all_scores if non_zero_score != 0]
    print(sorted(non_zero_scores)[int(len(non_zero_scores) / 2)])
