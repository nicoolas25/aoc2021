from dataclasses import dataclass
from functools import singledispatch

@dataclass
class State:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0

    def incr(self, /, horizontal = 0, depth = 0, aim = 0):
        return State(
            self.horizontal + horizontal,
            self.depth + depth,
            self.aim + aim,
        )

@dataclass
class Command:
    value: int
class Forward(Command):
    pass
class Down(Command):
    pass
class Up(Command):
    pass

@singledispatch
def apply_command(command: Command, state: State) -> State:
    raise NotImplementedError(f"Implementation is missing for {command}")

@apply_command.register
def apply_forward(command: Forward, state: State) -> State:
    return state.incr(horizontal=command.value, depth=command.value * state.aim)

@apply_command.register
def apply_down(command: Down, state: State) -> State:
    return state.incr(aim=command.value)

@apply_command.register
def apply_up(command: Up, state: State) -> State:
    return state.incr(aim=-command.value)

# =====

import fileinput

def read_command(line) -> Command:
    name, value = line.strip().split(" ")
    if name == "forward":
        return Forward(value=int(value))
    elif name == "down":
        return Down(value=int(value))
    elif name == "up":
        return Up(value=int(value))
    else:
        raise ValueError(f"Unknown '{name}' command")

state = State()
for line in fileinput.input():
    command = read_command(line)
    state = apply_command(command, state)

print(state.horizontal * state.depth)
