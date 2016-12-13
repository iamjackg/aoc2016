registers = {name: 0 for name in 'abcd'}
registers['c'] = 1
p_c = 0

test_input = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""

instructions = [instr.strip() for instr in open('input.txt', 'r').readlines()]


def unpack(first, *rest):
    return first, rest


def copy(operands):
    try:
        registers[operands[1]] = int(operands[0])
    except ValueError:
        registers[operands[1]] = registers[operands[0]]


def inc(operands):
    registers[operands[0]] += 1


def dec(operands):
    registers[operands[0]] -= 1


def jnz(operands):
    global p_c
    try:
        true = registers[operands[0]] != 0
    except KeyError:
        true = int(operands[0]) != 0

    if true:
        p_c += int(operands[1]) - 1

operations = {
    'cpy': copy,
    'inc': inc,
    'dec': dec,
    'jnz': jnz
}


while p_c < len(instructions):
    label, parameters = unpack(*instructions[p_c].split())
    operations[label](parameters)
    p_c += 1

print registers
