import fileinput

ONE = "1"
ZERO = "0"

def get_counter(inputs):
    counter = [0] * len(inputs[0])
    for line in inputs:
        for index, bit in enumerate(line):
            counter[index] += 1 if bit == ONE else -1
    return counter

counter = get_counter([line.strip() for line in fileinput.input()])
gamma = int("".join(ONE if index >= 0 else ZERO for index in counter), 2)
epsilon = int("".join(ONE if index < 0 else ZERO for index in counter), 2)
print(gamma * epsilon)
