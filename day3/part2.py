import fileinput

ONE = "1"
ZERO = "0"

def get_most_common_bit(inputs, index):
    balance = sum(
        1 if line[index] == ONE else -1
        for line in inputs
    )
    return ONE if balance >= 0 else ZERO


def find_by(inputs, filter_fn) -> str:
    filtered_inputs = inputs
    for index in range(len(inputs[0])):
        most_common_bit = get_most_common_bit(filtered_inputs, index)
        filtered_inputs = [
            line
            for line in filtered_inputs
            if filter_fn(line[index], most_common_bit)
        ]
        if len(filtered_inputs) == 1:
            break
    return filtered_inputs[0]

inputs = [line.strip() for line in fileinput.input()]
oxygen = find_by(inputs, lambda bit, most_common_bit: bit == most_common_bit)
co2 = find_by(inputs, lambda bit, most_common_bit: bit != most_common_bit)
print(int(oxygen, 2) * int(co2, 2))
