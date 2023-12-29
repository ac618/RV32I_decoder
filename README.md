# RISC-V32I Instruction Decoder

## Description

The Python script translates hexadecimal RISC-V instructions into human-readable assembly code. It is designed to assist in the debugging process of the NTUEE Computer Architecture Fall 2023 final project.

## Features

- Decodes RISC-V instructions in hexadecimal format to assembly code.
- Supports a subset of RISC-V instruction formats and can the further extended.
- Outputs decoded instructions to a text file.

## Usage

1. Add hexadecimal RISC-V instructions to the `inst_hex.txt` file in /files.
2. Run the script `RV32I_decoder.py` to decode the instructions.
3. View the decoded instructions in the output file `/files/riscv_inst.txt`.

## Customization

- Extend the `decode_riscv` function to add support for additional RISC-V instructions.

## Requirements

- Python 3.x
- `bitstring` library