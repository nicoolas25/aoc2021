import fileinput

inputs = [int(line.strip()) for line in fileinput.input()]
increment_count = sum(
    b > a
    for a, b in zip(inputs, inputs[1:])
)
print(increment_count)
