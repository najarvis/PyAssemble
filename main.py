memory = []
pointer = 0x00
registers = {0x00: 0,
             0x01: 0,
             0x02: 0,
             0x03: 0} # Registers A - D

FLAG_FINISHED = False

def NOP():
    global pointer, memory
    pointer += 0x01

def ADD():
    global pointer, memory
    return memory[pointer] + memory[pointer + 1]

def MOV():
    """ SET [value] [memory address]"""
    global pointer, memory, registers
    registers[memory[pointer + 2]] = memory[pointer + 1]
    pointer += 0x03

def OUT():
    """ OUT [register] """
    global pointer, memory, registers
    print( chr( registers[memory[pointer + 1]] ) )
    pointer += 0x02

def END():
    global pointer, memory, FLAG_FINISHED
    FLAG_FINISHED = True

def run():
    global pointer, memory, FLAG_FINISHED
    memory = [0x00 for i in range(0x100)]
    pointer = 0x00

    command_map = {0x00: NOP,
                   0x01: OUT,
                   0x02: ADD,
                   0x03: MOV,
                   0x0f: END}

    # MOV 'A' A
    # OUT A
    # END
    memory = load_program("""
                          03 41 00
                          01 00
                          0f
                          """)
    print()
    pretty_print_memory()
    print()

    FLAG_FINISHED = False

    print("Code Output:")
    while not FLAG_FINISHED:
        # print(command_map[memory[pointer]].__name__)
        command_map[memory[pointer]]()

        if pointer == len(memory):
            FLAG_FINISHED = True

    print()
    print("DONE")

    print()
    pretty_print_memory()
    print()

def load_program(program: str):
    memory = [0x00 for i in range(0x100)]
    program_list = list(program)
    for bit in program_list[:]:
        if bit not in '0123456789abcdef':
            program_list.remove(bit)

    # Can't overflow our memory!
    if len(program_list) > len(memory):
        raise ValueError

    # Turns ['0', '1', '0', '1', '1', '1', '0', '1', '0', '1'...] into [0b01001101, '0b01...']
    final_list = ["".join(program_list[i:i+2]) for i in range(0, len(program_list), 2)]

    for bit_index in range(len(final_list)):
        memory[bit_index] = int(final_list[bit_index], 16)

    return memory

def pretty_print_memory():
    global memory, registers
    print ("CURRENT MEMORY")
    for i in range(len(memory)):
        print('{0:4}'.format(hex(memory[i])), end=' ')
        if (i + 1) % 0x10 == 0:
            print()

    print()
    print("REGISTERS")
    print("A: " + str(registers[0x00]))
    print("B: " + str(registers[0x01]))
    print("C: " + str(registers[0x02]))
    print("D: " + str(registers[0x03]))


if __name__ == "__main__":
    run()
