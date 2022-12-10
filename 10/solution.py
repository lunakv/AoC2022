POLL_FREQUENCY = 40
POLL_START = 20

def signal_strength(x, cycle):
    return x * cycle

clock = 0
total_strength = 0
x = 1
display = ''

to_add = None
try:
    while True:
        if abs(x - (clock % POLL_FREQUENCY)) <= 1:
            display += '#'
        else:
            display += '.'

        clock += 1 
        if clock == POLL_START or (clock - POLL_START) % POLL_FREQUENCY == 0:
            total_strength += x * clock

        if to_add is not None:
            x += to_add
            to_add = None
        else:
            instruction = input().split()
            if instruction[0] == "noop":
                pass
            elif instruction[0] == "addx":
                to_add = int(instruction[1])
            else:
                raise ValueError(f'Invalid instruction "{instruction}"')

except EOFError:
    print(total_strength)
    for i in range(0, len(display), 40):
        print(display[i:i+40])

