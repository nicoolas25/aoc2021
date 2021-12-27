from part1 import Octopus, OctopusesMap, Position, step

if __name__ == "__main__":
    import fileinput

    octopuses: OctopusesMap = {
        Position(i, j): Octopus(energy_level=int(cell))
        for i, line in enumerate(fileinput.input())
        for j, cell in enumerate(line.strip())
    }


    flash_count = 0
    def on_flash():
        nonlocal flash_count
        flash_count += 1

    step_count = 0
    while True:
        octopuses = step(octopuses, on_flash)
        step_count += 1
        if flash_count == len(octopuses):
            print(step_count)
            break
        else:
            flash_count = 0
