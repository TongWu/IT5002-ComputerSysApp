## Number System

- 1s complement: Flip all bits
- 2s complement: Flip all bits then add 1
- Ns complement: 
- 
- Fixed point representation: `010.11(2)` = $0\times2^2+1\times 2^1+0\times 2^0+1\times 2^{-1}+1\times2^{-2}=2.75$
- Floating point representation: 
  - Use scientific notation to convert binary numbers to $1.\text{fraction}\times2^{\text{exponent}}$
  - Sign bit (1): 1 for negative, 0 for positive
  - Exponent bit (E): the exponent value of the radix, for example $1.\text{fraction}\times2^{\text{4}}$, the exponent is 4, where the exponent bit is $0100_2$
  - Mantissa bit (M): the fractional part, since IEEE 754 has one hidden bit, so the integer part is ignored. Truncate if the number of fractional parts is greater than the specified value. If it is less than the specified value, write it and then continue from the beginning
  - Excess: 





## Datapath:

- R-format: 
  - `add $8, $9, $10`: `rd = 8 (destination register)` `rs = 9 (first operand)` `rt = 10 (second operad)`
  - `sll $8, $9, 4`: `rd = 8`, `rt = 9`, `shamt = 4`

- I-format: 
  - `addi $8, $8, 10`: `rs = rt = $8`, `immediate = 10`

![image-20231016191613707](https://images.wu.engineer/images/2023/10/16/image-20231016191613707.png)

- Execution cycle: Fetch -> Decode -> Operand Fetch -> Execute (ALU) -> Result Write
- Fetch Stage: Fetch instruction from memory (Program Counter)
- Decode Stage: Use register file to read all necessary data
  - Register file Input:
    - Read register 1 (RR1): read `rs` (operand 1)
    - Read register 2 (RR2): read `rt` (operand 2)
    - Write Register (WR): read `rd` (destination register) for R-format, `rt` for I-format
    - Write Data (WD): the ALU output, for R format `sub $25, $20, $5`, WD should be `[$20]-[$5]`
  - Register file output:
    - Read data 1: content of `rs`
    - Read data 2: content of `rt` for R-format, `immediate` for I-format
  - Control Signal `RegWrite` to control the writing of register
  - Control Signal `RegDst` for WR side MUX to indicate I-J or R format, 0 for R format
  - Control Signal `ALUSrc` for RD2 side MUX to indicate I or R-J format, 0 for R-J format
- ALU stage: implement arithmetic and logical operations
  - ALU input:
    - `Opr1`: content of `rs` (`[rs]`)
    - `Opr2`: according to control signal `ALUSrc`, content of `rt` for R, `immediate` for I
  - ALU output:
    - `isZero`: For branch instruction to handle equal/not equal check
    - `ALU result`: result of operation
  - ALU control signal `ALUcontrol`: 4-bit signal, to control the operation function (`AND`, `OR`, `add`, `sub`…)
- Memory Stage: store and load ALU stage result to memory (for read/load operation only like `lw`, `sw`. Other instruction like `add`, `or` keep idle)
  - Data Memory Input:
    - `Address`: the output of ALU result (ALU computes address)
    - `Write Data`: if the action is write, import from `rt` (RD2)
  - Data Memory Output:
    - `Read Data`: if the action is read, output the memory address
  - Data Memory Control Signal: `MemWrite` and `MemRead`
  - For Non-memory instruction (`add` `or` `sub`), the output of ALU stage and RD2’s output `rt` is inputted to a MUX, controlled by `MemReg`, indicate whether result come from memory or ALU.
- Register Write Stage: write result of computation into register for instructions `add`, `or`, `sub`
  - The output of this stage is the input of WD in register file (Decode Stage)

- Other control signal:
  - `PCSrc`: Select the next PC value
    - For regular instruction, the next PC value should be PC+4
    - For branch instruction but not enter the branch, the next PC value also PC+4
    - For branch instruction that enter the branch, the next PC value should be `PC+4+(immediate*4)`
- Critical path:
  - `SUB` instruction: Inst-Mem -> Reg.File -> MUX(ALUSrc) -> ALU -> MUX(MemToReg) -> Reg.File
  - `LW` instruction: Inst-Mem -> Reg.File -> ALU -> Data-Mem -> MUX(MemToReg) -> Reg.File
  - `BEQ` instruction: Inst-Mem -> Reg.File -> MUX(ALUSrc) -> ALU -> AND -> MUX(PCSrc)



## Cache

