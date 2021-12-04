from dataclasses import dataclass
from enum import Enum
from functools import reduce

class CommandType(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"

@dataclass
class Command:
    command_type: CommandType
    value: int

@dataclass
class State:
    horizontal: int = 0
    depth: int = 0

def read_command(line) -> Command:
    type_str, value_str = line.strip().split(" ")
    return Command(
        command_type=CommandType(type_str),
        value=int(value_str),
    )

def apply_command(state: State, command: Command) -> State:
    horizontal = state.horizontal
    depth = state.depth

    if command.command_type == CommandType.FORWARD:
        horizontal += command.value
    elif command.command_type == CommandType.DOWN:
        depth += command.value
    elif command.command_type == CommandType.UP:
        depth -= command.value
    else:
        raise RuntimeError(f"Unsupported command {command.command_type}")

    return State(horizontal=horizontal, depth=depth)

import fileinput

commands = map(read_command, fileinput.input())
final_state = reduce(apply_command, commands, State())
print(final_state.horizontal * final_state.depth)
