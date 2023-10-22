# 7 - The Processor: Datapath

## 7.1 Brief Recap

![image-20231017000614838](https://images.wu.engineer/images/2023/10/16/image-20231017000614838.png)

![image-20231017000620991](https://images.wu.engineer/images/2023/10/16/image-20231017000620991.png)

![image-20231017000631746](https://images.wu.engineer/images/2023/10/16/image-20231017000631746.png)

![image-20231017000637504](https://images.wu.engineer/images/2023/10/16/image-20231017000637504.png)

## 7.2 From C to Execution

- We play the role of Programmer, Compiler, Assembler, and Processor

  - Program:

    ```c
    if (x != 0) {
    	a[0] = a[1] + x;
    }
    ```

  - Programmer: Show the workflow of compiling, assembling, and executing C program

  - Compiler: Show how the program is compiled into MIPS

  - Assembler: Show how the MIPS is translated into binaries

  - Processor: Show how the datapath is activated in the processor

### 7.2.1 Writing C Program

![image-20231017000853064](https://images.wu.engineer/images/2023/10/16/image-20231017000853064.png)

### 7.2.2 Compiling to MIPS

#### Key Idea

- Key Idea #1:

  Compilation is a structed process

  ```c
  if (x != 0) {
  	a[0] = a[1] + x;
  }
  ```

  Each structure can be compiled independently

![image-20231017000959098](https://images.wu.engineer/images/2023/10/16/image-20231017000959098.png)

- Key Idea #2:

  Variable-to-Register Mapping

  Let the mapping be:

![image-20231017001028769](https://images.wu.engineer/images/2023/10/16/image-20231017001028769.png)

#### Common Technique

- Common Technique #1:

  Invert the condition for shorter code

  ![image-20231017001105217](https://images.wu.engineer/images/2023/10/16/image-20231017001105217.png)

- Common Technique #2:

  Break complex operations, use temp register

  ![image-20231017001134356](https://images.wu.engineer/images/2023/10/16/image-20231017001134356.png)

- Common Technique #3:

  Array access is `lw`, array update is `sw`

  ![image-20231017001200731](https://images.wu.engineer/images/2023/10/16/image-20231017001200731.png)

#### Common Error

- Common Error #1:

  Assume that the address of the next word can be found by incrementing the address in a register by 1 instead of by the word size in bytes

  Example:

  `$t1 = a[1]`

  is translated to:

  `lw $8, 4($17)`

  instead of

  `lw $s8, 1($17)`

#### Finalize

- Last Step:

  Combine the two structures logically

  ![image-20231017001412054](https://images.wu.engineer/images/2023/10/16/image-20231017001412054.png)

### 7.2.3 Assembling to Binaries

- Instruction Types Used:
  1. R-Format:`opcode $rd, $rs, $rt`
     ![image-20231017002853051](https://images.wu.engineer/images/2023/10/16/image-20231017002853051.png)
	
	2. I-Format: `opcode $rt, $rs, immediate`
	
	   ![image-20231017003025678](https://images.wu.engineer/images/2023/10/16/image-20231017003025678.png)
	
	3. Branch:
	
	   - Use I-format
	   - PC = (PC+4) + (`immediate` x 4)
	
	4. `beq $16, $0, Else`
	
	   - Compute immediate value
	      - `immediate` = 3
	   - Fill in fields
	
	   ![image-20231017004833819](https://images.wu.engineer/images/2023/10/16/image-20231017004833819.png)
	
	   - Convert to binary
	
	   ![image-20231017004850682](https://images.wu.engineer/images/2023/10/16/image-20231017004850682.png)
	
	   ![image-20231017144403434](https://images.wu.engineer/images/2023/10/17/image-20231017144403434.png)
	
	5. `lw $8, 4($17)`
	
	   - Filled in fields (Refer to MIPS Reference data)
	
	   ![image-20231017144446750](https://images.wu.engineer/images/2023/10/17/image-20231017144446750.png)
	
	   - Convert to binary
	
	   ![image-20231017144510923](https://images.wu.engineer/images/2023/10/17/image-20231017144510923.png)
	
	   ![image-20231017144521728](https://images.wu.engineer/images/2023/10/17/image-20231017144521728.png)
	
	6. `add $8, $8, $16`
	
	   - Filled in fields
	
	   ![image-20231017144559595](https://images.wu.engineer/images/2023/10/17/image-20231017144559595.png)
	
	   - Convert to binary
	
	   ![image-20231017144621445](https://images.wu.engineer/images/2023/10/17/image-20231017144621445.png)
	
	   ![image-20231017144630267](https://images.wu.engineer/images/2023/10/17/image-20231017144630267.png)
	
	7. `sw $8, 0($17)`
	
	   - Filled in fields
	
	   ![image-20231017144657949](https://images.wu.engineer/images/2023/10/17/image-20231017144657949.png)
	
	   - Convert to binary
	
	   ![image-20231017144724854](https://images.wu.engineer/images/2023/10/17/image-20231017144724854.png)
	
	   ![image-20231017144749758](https://images.wu.engineer/images/2023/10/17/image-20231017144749758.png)

### 7.2.4 Execution (Datapath)

- Given the binary

  - Assume two possible executions
    1. `$16 == $0` (shorter)
    2. `$16 != $0` (larger)

  - Convention:

  ![image-20231017161007418](https://images.wu.engineer/images/2023/10/17/image-20231017161007418.png)

  ![image-20231017161040487](https://images.wu.engineer/images/2023/10/17/image-20231017161040487.png)

  ![image-20231017161114190](https://images.wu.engineer/images/2023/10/17/image-20231017161114190.png)

![image-20231017161125183](https://images.wu.engineer/images/2023/10/17/image-20231017161125183.png)

![image-20231017161145770](https://images.wu.engineer/images/2023/10/17/image-20231017161145770.png)

![image-20231017161206140](https://images.wu.engineer/images/2023/10/17/image-20231017161206140.png)