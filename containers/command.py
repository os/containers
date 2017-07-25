import re

from containers.utilities import solve


PATTERN_INPUT_CONTAINER_TYPES = re.compile(r'^\s*\d+(\s*,\s*\d+)*\s*$')
PATTERN_INPUT_LOAD = re.compile(r'^\s*\d+\s*$')
PATTERN_INTEGER = re.compile(r'\d+')


def main():
    input_container_types = input('containers: ')

    # Validate container types
    while not PATTERN_INPUT_CONTAINER_TYPES.match(input_container_types):
        print('Invalid containers value')
        input_container_types = input('containers: ')

    container_types = [
        int(i) for i in re.findall(PATTERN_INTEGER, input_container_types)
    ]

    while True:
        input_system_load = input('load: ')

        # Validate load
        if not PATTERN_INPUT_LOAD.match(input_system_load):
            print('Invalid load value')
            continue

        system_load = int(PATTERN_INTEGER.search(input_system_load).group())
        solution = sorted(solve(container_types, system_load), reverse=True)
        print('> {}'.format(solution))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
