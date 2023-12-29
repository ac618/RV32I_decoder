import os
from bitstring import BitArray

dir = os.path.dirname(os.path.abspath(__file__))
input_file = 'inst_hex.txt'
output_file = 'riscv_inst.txt'

def decode_riscv(instruction):
    opcode = instruction[-7:]
    funct3 = instruction[-15:-12]
    funct7 = instruction[-32:-25]
    rd = int(instruction[-12:-7], 2)
    rs1 = int(instruction[-20:-15], 2)
    rs2 = int(instruction[-25:-20], 2)
    imm_i = int(instruction[-32:-20], 2)
    imm_s = int(instruction[-32:-25] + instruction[-12:-7], 2)
    imm_b = int(instruction[-32] + instruction[-8] +
                instruction[-31:-25] + instruction[-12:-8] + '0', 2)
    imm_u = int(instruction[-32:-12] + '0' * 12, 2)
    imm_j = int(instruction[-32] + instruction[-20:-12] +
                instruction[-21] + instruction[-31:-21] + '0', 2)

    # identify instructions
    if opcode == "0110011": # R type
        if funct3 == "000" and funct7 == "0000000":
            return f"add x{rd}, x{rs1}, x{rs2}"
        elif funct3 == "000" and funct7 == "0100000":
            return f"sub x{rd}, x{rs1}, x{rs2}"
        elif funct3 == "111" and funct7 == "0000000":
            return f"and x{rd}, x{rs1}, x{rs2}"
        elif funct3 == "100" and funct7 == "0000000":
            return f"xor x{rd}, x{rs1}, x{rs2}"
        elif funct3 == "000" and funct7 == "0000001":
            return f"mul x{rd}, x{rs1}, x{rs2}"
    	
    elif opcode == "0010011": # normal I type
        if funct3 == "000":
            return f"addi x{rd}, x{rs1}, {imm_i}"
        elif funct3 == "001":
            return f"slli x{rd}, x{rs1}, {imm_i}"
        elif funct3 == "010":
            return f"slti x{rd}, x{rs1}, {imm_i}"
        elif funct3 == "101":
            return f"srai x{rd}, x{rs1}, {imm_i}"
    
    elif opcode == "0000011": # lw
        if funct3 == "010":
            return f"lw x{rd}, {imm_i}(x{rs1})"
        
    elif opcode == "1100111": # jalr
        return f"jalr x{rd}, {imm_i}(x{rs1})"
    
    elif opcode == "1110011": # ecall
        return f"ecall"

    elif opcode == "1100011": # B type
        if funct3 == "000":
            return f"beq x{rs1}, x{rs2}, {imm_b}"
        elif funct3 == "001":
            return f"bne x{rs1}, x{rs2}, {imm_b}"
        elif funct3 == "100":
            return f"blt x{rs1}, x{rs2}, {imm_b}"
        elif funct3 == "101":
            return f"bge x{rs1}, x{rs2}, {imm_b}"

    elif opcode == "1101111": # J type
        return f"jal x{rd}, {imm_j}"
    
    elif opcode == "0100011": # S type
        if funct3 == "010":
            return f"sw x{rs2}, {imm_s}(x{rs1})"
    
    elif opcode == '0010111': # auipc
        return f"auipc x{rd}, {imm_u}"
    
    # Add more instruction formats as needed
    return "Unknown instruction"

# read instructions
insts = []
with open(os.path.join(dir, 'files', input_file), 'r') as f:
    for line in f:
        insts.append(line[:-1])

# decode RV32I instructions
insts_dec = []
for inst in insts:
    instruction_binary = BitArray(hex=inst).bin
    decoded_instruction = decode_riscv(instruction_binary)
    insts_dec.append(decoded_instruction)
    print(f"{inst}: {decoded_instruction}")

# write results
with open(os.path.join(dir, 'files', output_file), 'w') as f:
    for inst in insts_dec:
        f.write(inst+'\n')