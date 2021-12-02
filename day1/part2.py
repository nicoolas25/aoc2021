import fileinput

inputs = [int(line.strip()) for line in fileinput.input()]
group_sums = [
    sum(group)
    for group in zip(inputs, inputs[1:], inputs[2:])
]
increment_count = sum(
    b > a
    for a, b in zip(group_sums, group_sums[1:])
)
print(increment_count)
