# 1 - Introduction

## 1.1 Programming Language

- Programming language: a formal language that specifies a set of instructions for a computer to implement specific algorithms to solve problems

![image-20230923211215183](https://images.wu.engineer/images/2023/09/23/image-20230923211215183.png)

- 1st Generation languages: 
  - Machine language
  - Directly executable by machine
  - Machine dependent
  - Efficient code but difficult to write
- 2nd generation languages:
  - Assembly language
  - Need to be **translated(assembled)** into machine code for execution
  - Efficient code, easier to write than machine code
- 3rd generation language:
  - Closer to English
  - Need to be **translated (complied or interpreted)** into machine code for execution
  - Example: FORTRAN, COBOL, C, BASIC
- 4th generation language:
  - Require fewer instructions than 3GL
  - Used with databases (query languages, report generators, forms designers)
  - Example: SQL, PostScript, Mathematica
- 5th generation language:
  - Used mainly AI research
  - Declarative languages
  - Functional languages (Lisp, Scheme, SML)
  - Logic programming (Prolog)
- “Generational” classification of high level languages (3GL and later) was never fully precise
- A different classification is based on paradigm

![image-20230923211754385](https://images.wu.engineer/images/2023/09/23/image-20230923211754385.png)

### 1.1.1 C Programming Language

- C is an **imperative procedural language (命令式程序语言)**
- C provides constructs that map efficiently to typical machine instructions
- C is a high-level language very close to the machine level, hence sometimes it is called “mid-level”

![image-20230923212016669](https://images.wu.engineer/images/2023/09/23/image-20230923212016669.png)

## 1.2 Abstraction

![image-20230923212034228](https://images.wu.engineer/images/2023/09/23/image-20230923212034228.png)

![image-20230923212047740](https://images.wu.engineer/images/2023/09/23/image-20230923212047740.png)

![image-20230923212116541](https://images.wu.engineer/images/2023/09/23/image-20230923212116541.png)

# 2 - Number Systems

## 2.1 Data Representation

- Basic data types in C:
  - `int`, with variants `short`, `long`
  - `float`
  - `double`
  - `char`
- How data is represented depends on its type:

![image-20230923212837454](https://images.wu.engineer/images/2023/09/23/image-20230923212837454.png)

- Data are internally represented as sequence of bits (binary digits). A bit is either 0 or 1
- Other units:
  - Byte = 8 bits
  - Nibble = 4 bits
  - Word = Multiple of bytes (eg: 1 byte, 2 bytes, 4 bytes, etc) depending on the computer architecture
- N bits can represent up to $2^n$ values
  - 2 bits represent up to 4 values (00, 01, 10, 11)
- To represent M values, $\lceil log_2M \rceil$ bits required
  - 32 values requires 5 bits; 1000 values require 10 bits

## 2.2 Decimal (base 10) Number System

- A weighted-positional number system
- Base (also called radix) is 10
- Symbols/digits = ${0,1,2,3,4,5,6,7,8,9}$
- Each position has a weight of power of 10
  - $(7594.36)_{10} = (7\times10^3)+(5\times10^2)+(9\times10^1)+(4\times10^0)+(3\times10^{-1})+(6\times10^{-2})$

## 2.3 Other Number Systems

- In some programming languages/software, special notations are used to represent numbers in certain bases
  - In C
    - prefix 0 for octal. Eg: `032` represents the octal number $(32)_8$
    - prefix 0x for hexadecimal. Eg: `0x32` represents the hexadecimal number $(32)_{16}$
  - In QTSpim (a MIPS simulator)
    - prefix 0x for hexadecimal.
  - In Verilog, the following values are the same
    - `8'b11110000`: an 8-bit binary value 11110000
    - `8'hF0`: an 8-bit binary value represented in hexadecimal F0
    - `8'd240`: an 8-bit binary value represented in decimal 240

## 2.4 Base-R to Decimal Conversion

- $1101.101_2 = 1\times 2^3 + 1\times 2^2 + 1\times 2^0 + 1 \times 2^{-1} + 1\times 2^{-3}=8+4+1+0.5+0.125=13.625_{10}$
- $572.6_8 = 5\times8^2+7\times8^1+2\times8^0+6\times8^{-1}=320+56+2+0.75=378.75_8$
- $2A.8_{16}=2\times16^1+10\times16^0+8\times16^{-1}=32+10+0.5=42.5_{10}$

## 2.5 Decimal to Binary Conversion

- For whole numbers
  - Repeated Division-by-2 method
- For fractions
  - Repeated Multiplication-by-2 method

### 2.5.1 Repeated Division-by-2

**Repeated Divide**

- To convert a whole number to binary, use **successive division by 2** until the quotient is 0. The remainders from the answer, with the first remainder as the Least Significant Bit (LSB) and the last as the Most Significant Bit (MSB)

![image-20230925150617246](https://images.wu.engineer/images/2023/09/25/image-20230925150617246.png)

> **Repeated Division-by-2**: 这种方法经常被用于将十进制数转换为二进制数。
>
> 步骤如下：
>
> 1. 用2除以给定的十进制数，记录商和余数。 
>
> 2. 再用2除以上一步得到的商，再次记录商和余数。
>
> 3. 重复上述步骤，直到商变为0为止。 
>
> 4. 从上到下读取余数，就得到了对应的二进制表示。
>
> 例如，将十进制数13转换为二进制：
>
> ```
> Copy code13 ÷ 2 = 6 商 1 余数
> 6 ÷ 2 = 3 商 0 余数
> 3 ÷ 2 = 1 商 1 余数
> 1 ÷ 2 = 0 商 1 余数
> 
> 从上到下读取余数得到：1101，所以13的二进制表示是1101。
> ```

### 2.5.2 Repeated Multiplication-by-2

**Repeated Multiply**

- To convert **decimal fractions** to binary, **repeated multiplication by 2** is used, until the fractional product is 0 (or until the desired number of decimal places). The carried digits, or *carries*, produce the answer, with the first carry as the MSB, and the last as the LSB.

![image-20230925150851946](https://images.wu.engineer/images/2023/09/25/image-20230925150851946.png)

> **Repeated Multiplication-by-2**: 这种方法经常被用于将二进制小数转换为十进制小数。
>
> 步骤如下：
>
> 1. 将给定的二进制小数的最高位（最左边的位）乘以2。 
> 2. 记录该乘积的整数部分。 
> 3. 将乘积的小数部分再乘以2。 
> 4. 重复上述步骤，直到得到的小数部分为0或达到所需的精度。
>
> 例如，将二进制小数0.101转换为十进制：
>
> ```
> rustCopy code0.101 × 2 = 1.01  -> 记录整数部分 1
> 0.01 × 2  = 0.02  -> 记录整数部分 0
> 0.02 × 2  = 0.04  -> 记录整数部分 0 (如果需要更多精度则继续，否则可以停止)
> 
> 从上到下读取整数部分得到：100，表示二进制的0.101等于十进制的0.5。
> ```

## 2.6 Conversion Between Decimal and Other Bases

- **Base-R to decimal:** multiply digits with their corresponding weights
- **Decimal to binary (base 2)**
  - For whole numbers: repeated division-by-2 (2.5.1)
  - For fraction numbers: repeated multiplication-by-2 (2.5.2)
- **Decimal to base-R**
  - For whole numbers: repeated division-by-R
  - For fraction numbers: repeated multiplication-by-R

> 总结:
>
> 不管是什么进制，均可使用2.5章内使用的方法，将除以2或乘以2替换进制数字

## 2.7 Conversion Between Bases

- In general, conversion between bases can be done via decimal:

![image-20230925151637586](https://images.wu.engineer/images/2023/09/25/image-20230925151637586.png)

## 2.8 Binary to Octal/Hexadecimal Conversion

- Binary -> Octal: partition in groups of 3
  - $(10\ \ 111\ \ 011\ \ 001\ .\ 101\ \ 110)_2=(2731.56)_8$
- Octal -> Binary: reverse
  - $(2731.56)_8=(10\ \ 111\ \ 011\ \ 001\ .\ 101\ \ 110)_2$
- Binary -> Hexadecimal: partition in groups of 4
  - $(101\ \ 1101\ \ 1001\ .\ 1011\ \ 1000)_2=(5D9.B8)_{16}$
- Hexadecimal -> Binary: reverse
  - $(5D9.B8)_{16} = (101\ \ 1101\ \ 1001\ .\ 1011\ \ 1000)_2$

## 2.9 ASCII Code

- **ASCII code** and **Unicode** are used to represent characters `('a', 'C', '?', '\0')`
- ASCII
  - American Standard Code for Information Interchange
  - 7 bits, plus 1 parity bit (odd or even parity)

![image-20230925153442761](https://images.wu.engineer/images/2023/09/25/image-20230925153442761.png)

![image-20230925153601908](https://images.wu.engineer/images/2023/09/25/image-20230925153601908.png)

- Integers (0 to 127) and characters are ‘somewhat’ interchangeable in C

![image-20230925153702075](https://images.wu.engineer/images/2023/09/25/image-20230925153702075.png)

> ```c
> int main() {
>     int i, n = 2147483640;
>     for (i=1; i<=10; i++) {
>         n = n + 1;
>     }
>     printf("n = %d\n", n);
> }
> ```
>
> 对于这一段代码，其输出是什么？
>
> 这段代码中, `int` 数据类型的整数会溢出。在多数计算机系统中，一个 `int` 数据类型通常占据4个字节（32位），其范围是从 `-2,147,483,648`（即 `-2^31`）到 `2,147,483,647`（即 `2^31 - 1`）。
>
> 当 `n` 的值是 `2,147,483,640`，并在循环中加了10次，它的值会变为 `2,147,483,650`。这个值超出了 `int` 的最大值 `2,147,483,647`。
>
> 因此，当加1到 `2,147,483,647`，它会溢出并回绕到 `int` 的最小值 `-2,147,483,648`，然后再从这个值开始增加。
>
> ```markdown
> 2,147,483,640 + 1 = 2,147,483,641
> 2,147,483,641 + 1 = 2,147,483,642
> ...
> 2,147,483,646 + 1 = 2,147,483,647  // 这是int的最大值
> 2,147,483,647 + 1 = -2,147,483,648 // 溢出，变成int的最小值
> -2,147,483,648 + 1 = -2,147,483,647
> -2,147,483,647 + 1 = -2,147,483,646
> ```

## 2.10 Negative Numbers

- Unsigned numbers: only non-negative values
- Signed numbers: include all values (positive and negative)
- There are 3 common representations for signed binary numbers:
  - Sign-and-magnitude
  - 1s Complement
  - 2s Complement

### 2.10.1 Sign-and-Magnitude

- The sign is represented by a ‘sign bit’
  - `0` for +
  - `1` for -
- For example: a 1-bit sign and 7-bit magnitude format

![image-20230925154458173](https://images.wu.engineer/images/2023/09/25/image-20230925154458173.png)

- Example:

  - `00110100` -> $+110100_2=+52_{10}$

  - `10010011` -> $-10011_2=-19_{10}$

- For 8-bit binary number:
  - Largest value: `01111111`, $127_{10}$
  - Smallest value: `11111111`, $-127_{10}$
  - Zeros:
    - `00000000`, $+0_{10}$
    - `10000000`, $-0_{10}$
  - Range (for 8-bit): $-127_{10}$ to $+127_{10}$
- For n-bit sign-and-magnitude representation, the range of values should be:
  - $-2^{n-1}+1$ to $2^{n-1}-1$
- Negate a number, just **invert the sign bit**
  - Examples:
    - Negate $00100001_2$ (decimal 33)
      - $10100001_2$ (decimal -33)
    - Negate $10000101_2$ (decimal -5)
      - $00000101_2$ (decimal 5)

### 2.10.2 1s Complement 一进制补码

- Given a number `x` which can be expressed as an n-bit binary number, its **negated value** can be obtained in **1’s-complement** representation using:

$$
-x=2^n-x-1
$$

- Example: With an 8-bit number `00001100` (or $12_{10}$), its negated value expressed in 1’s-complement is:

$$
\begin{aligned}
-00001100_2 &= 2^8 -12 -1 \\
&= 243 \\
&= 11110011_{1s}
\end{aligned}
$$

- (This means that $-12_{10}$ is written as `11110011` in 1s-complement representation)
- Technique to negate a value: **invert all the bits**
- Largest value: `0111 1111` = $+127_{10}$
- Smallest value: `1000 0000` = $-127_{10}$
- Zeros:
  - `0000 0000` = $+0_{10}$
  - `1111 1111` = $-0_{10}$
- Range (for 8 bits): $-127_{10}$ to $+127_{10}$
- Range (for n bits): $-(2^{n-1}-1)$ to $2^{n-1}-1$
- The *most significant bit (MSB)* still represents the sign: 0 for positive, 1 for negative
- Examples:
  - $(14_{10})=(00001110)_2=(00001110)_{1s}$
  - $-(14)_{10}=-(00001110)_2=(11110001)_{1s}$

> - 对于一个二进制数，它的1's complement是将该数中的每一位都取反。换句话说，将所有的0变为1，所有的1变为0。
> - 例如，考虑一个8位二进制数 `1101 0101`。它的1's complement是 `0010 1010`。

### 2.10.3 2s Complement

- Given a number *x* which can be expressed as an n-bit binary number, its *negated value* can be obtained in **2s-complement** representation using:

$$
-x=2^n-x
$$

- Example: With an 8-bit number `00001100` (or $12_{10}$), its negated value expressed in 2s-complement is:

$$
\begin{aligned}
-00001100_2 &= 2^8 - 12 \\
&= 244 \\
&= ((11110011)_{1s} + 1)_{2s} \\
&= 11110100_{2s}
\end{aligned}
$$

- This means that $-12_{10}$ is written as `1111 0100` in 2s-complement representation
- Technique to negate a value: **invert all the bits, then add 1**
- Largest value: `0111 1111` = $+127_{10}$
- Smallest value: `1000 0000` = $-128_{10}$
- Zero: `0000 0000` = $+0_{10}$
- Range (for 8 bits): $-128_{10}$ to $+127_{10}$
- Range (for n bits): $-(2^{n-1})$ to $2^{n-1}-1$
- The *most significant bit (MSB)* still represents the sign: 0 for positive, 1 for negative
- Examples:
  - $(14)_{10}=(00001110)_2=(00001110)_{2s}$
  - $-(14)_{10}=-(00001110)_2=(11110010)_{2s}$

### 2.10.4 Comparisons

![image-20230926014751133](https://images.wu.engineer/images/2023/09/25/image-20230926014751133.png)

### 2.10.5 Complement on Fractions

- We can extend the idea of complement on fractions
- Examples:
  - Negate `0101.01` in 1s-complement
    - Answer: `1010.10`
  - Negate `111000.101` in 1s-complement
    - Answer: `000111.010`
  - Negate `0101.01` in 2s-complement
    - Answer: `1010.11`

### 2.10.6 2s Complement Addition/Subtraction

- Algorithm for addition of integers, $A+B$:

  1. Perform binary addition on the two numbers
  2. Ignore the carry out of the MSB
  3. Check for overflow. Overflow occurs if the ‘carry in’ and ‘carry out’ of the MSB are different, or if result is opposite sign of A and B

- Algorithm for subtraction of integers, $A-B$:
  $$
  A-B=A+(-B)
  $$

  1. Take 2s-complement of B
  2. Add the 2s-complement of B to A

#### Overflow

- Signed numbers are of a fixed range
- If the result of addition/subtraction goes beyond this range, an **overflow** occurs
- Overflow can be easily detected:
  - positive add positive -> negative
  - negative add negative -> positive
- Example: 4-bit 2s-complement system
  - Range of value: $-8_{10}$ to $7_{10}$
  - $0101_{2s} + 0110_{2s} = 1011_{2s}$
    $5_{10}+6_{10}=-5_{10}$ (Overflow!)
  - $1001_{2s} + 1101_{2s} = 10110_{2s} \text{ (discard end-carry)} = 0110_{2s}$
    $-7_{10}+-3_{10}=6_{10}$ (Overflow!)

![image-20230926020057101](https://images.wu.engineer/images/2023/09/25/image-20230926020057101.png)

![image-20230926020214093](https://images.wu.engineer/images/2023/09/25/image-20230926020214093.png)

> 在二进制的2's-complement加减法中，判断溢出的情况是基于加法的结果与两个操作数的关系来确定的。下面我将为您解释如何判断正溢出和负溢出。
>
> 1. **正溢出**：
>    - 当两个正数相加得到一个负数结果时，就发生了正溢出。
>    - 具体判断方式为：两个操作数的最高位（符号位）都是0，但结果的最高位是1。
> 2. **负溢出**：
>    - 当两个负数相加得到一个正数结果时，就发生了负溢出。
>    - 具体判断方式为：两个操作数的最高位都是1，但结果的最高位是0。
>
> 加减法的关系：减法可以看作加上一个数的2's complement。所以，如果你知道如何检测加法的溢出，你也可以应用这个知识来检测减法的溢出。

### 2.10.7 1s Complement Addition/Subtraction

- Algorithm for addition of integers, $A+B$:

  1. Perform binary addition on the two numbers
  2. If there is a carry out of the MSB, add 1 to the result
  3. Check for overflow. Overflow occurs if result is opposite sign of A and B

- Algorithm for subtraction of integers, $A-B$:
  $$
  A-B=A+(-B)
  $$

  1. Take 1s-complement of B
  2. Add the 1s-complement of B to A

![image-20230926020545253](https://images.wu.engineer/images/2023/09/25/image-20230926020545253.png)

> 在二进制加减法中，判断溢出是否发生取决于你是否在执行有符号的运算。溢出的概念主要适用于有符号数，通常是使用2's complement表示法。
>
> 对于加法：
>
> 1. **正溢出**：当你将两个正数相加并得到一个负结果时，发生正溢出。
> 2. **负溢出**：当你将两个负数相加并得到一个正结果时，发生负溢出。
>
> 对于减法： 由于减法可以被视为加法（减去一个数等同于加上它的负数），因此溢出条件与上述相同。
>
> 判断溢出的实际方法：
>
> 1. 检查操作数的符号和结果的符号。
> 2. 如果两个正操作数的加法得到一个负结果，或者两个负操作数的加法得到一个正结果，则发生溢出。
> 3. 更具体地说，可以检查进位到符号位和从符号位的进位。如果它们不同，就发生了溢出。例如，对于8位数，如果从第7位到第8位有进位，但从第8位向上没有进位（或相反），则发生溢出。
>
> 这种基于进位的方法在硬件加法器中更为实用，因为可以直接从加法器的输出中获得进位信号，用于溢出检测。

### 2.10.8 Excess Notation (Excess Representation)

- Besides sign-and-magnitude and complement schemes, the **excess representation** is another scheme
- It allows the range of values to be distributed **evenly** between the positive and negative values, by a simple translation (addition/subtraction)
- Example: Excess+4 (Excess-(-4)) representation on 3-bit numbers. See table below

![image-20230926020849749](https://images.wu.engineer/images/2023/09/25/image-20230926020849749.png)

- Example: Excess+8 (Excess-(-7)) representation on 4-bit numbers

![image-20230926021250881](https://images.wu.engineer/images/2023/09/25/image-20230926021250881.png)

## 2.11 Real Numbers

- Many applications involve computations not only on integers but also on real numbers
- How are real numbers represented in a computer system?
- Due to the finite number of bits, real number are often represented in their approximate values

### 2.11.1 Fixed-point Representation

- In **fixed-point representation**, the number of bits allocated for the whole number part and fractional part are fixed
- For example, given an 8-bit representation, 6 bits are for whole number part and 2 bits for fractional parts

![image-20230926021907280](https://images.wu.engineer/images/2023/09/25/image-20230926021907280.png)

- If 2s-complement is used, we can represent values like:
  $011010.11_{2s}=26.75_{10}$
  $111110.11_{2s}=-000001.01_2=-1.25_{10}$

### 2.11.2 Floating-point Representation

- Floating-point representation has limited range
- Alternative: **Floating points numbers** allow us to represent very large or very small numbers
- Examples:
  - $0.23\times10^{23}$ (very large positive number)
  - $0.5\times10^{-37}$ (very small positive number)
  - $-0.2397\times10^{-18}$ (very small negative number)
- 3 components: **sign, exponent and mantissa (fraction)**
- The base (radix) is assumed to be 2
- Two formats:
  - Single-precision (32-bit): 1-bit sign, 8-bit exponent with bias 127 (excess-127), 23-bit mantissa
  - Double-precision (64-bit): 1-bit sign, 11-bit exponent with bias 1023 (excess-1023), 53-bit mantissa

![image-20230926022523051](https://images.wu.engineer/images/2023/09/25/image-20230926022523051.png)

- Sign bit: 0 for positive, 1 for negative

- Mantissa is **normalized** with an implicit leading bit 1
  - $110.1_2$ -> normalized -> $1.101_2\times2^2$ -> only $101$ is stored in the mantissa field
  - $0.00101101_2$ -> normalized -> $1.01101_2 \times 2^{-3}$ -> only $01101$ is stored in the mantissa field

![image-20230926022742727](https://images.wu.engineer/images/2023/09/25/image-20230926022742727.png)

# 3 - MIPS Assembly I

### 3.0 Recap



### 3.1 Instruction Set Architecture (ISA)

> 指令集架构（Instruction Set Architecture, ISA）定义了一个计算机系统可以执行的低级机器语言指令集，也就是计算机硬件能够理解和执行的指令。
>
> 指令集架构涵盖了以下几个方面：
>
> 1. **操作和指令**：定义了计算机能够执行的基本操作，如加法、减法、乘法、逻辑操作等。
> 2. **寄存器**：描述了计算机中的数据存储位置，通常分为通用寄存器、状态寄存器等。
> 3. **地址模式**：定义了如何计算数据和指令的存储位置。
> 4. **数据类型**：描述了支持的数据的种类和大小，如整数、浮点数等。
> 5. **异常和中断处理**：定义了当某些事件（如算术溢出、缺页中断）发生时计算机应该如何响应。
>
> 不同的指令集架构会导致计算机的性能、功耗、代码密度等方面的差异。有一些著名的ISA，如x86（由Intel和AMD使用）、ARM（用于大多数移动设备）、MIPS等。
>
> ISA是计算机架构的一个层次，通常分为三个层次：
>
> 1. **高级语言层**：如Python、Java等。
> 2. **汇编语言和指令集架构层**：这里就是ISA所在的层次。
> 3. **微架构或实现层**：这是具体硬件的实现细节，比如Intel的Core、Pentium等或AMD的Ryzen系列。
>
> ISA定义了软件与硬件之间的接口，使得软件开发者可以不必关心底层硬件的具体实现细节，而只需要关心指令集来编写程序。

- Instruction Set Architecture (ISA) (指令集架构)

  - An abstraction on the interface between the hardware and the low-level software
    - Software: To be translated to the instruction set
    - Hardware: Implementing the instruction set

  - ISA Allows computer designers to talk about functions independently from the hardware that performs them

    - > 允许计算机设计师在不考虑特定硬件实现的情况下，讨论和设计计算机功能。以指令集架构为例，设计师可以定义一个指令来完成特定的操作，例如加法，而不需要指定这个加法是如何在硬件上实现的。这样，ISA就充当了软件和硬件之间的桥梁，为高级编程语言提供了一个稳定的接口。

  - This abstraction allows many implementations of varying cost and performance to run identical software

    - > 由于存在上述的抽象，同一个指令集架构可以有多种不同的硬件实现。这些实现可能在成本和性能上有所不同。例如，高性能的服务器处理器和低功耗的移动设备处理器可能都遵循相同的ISA，但它们在微架构（即具体的硬件实现）上会有所不同。尽管如此，由于它们共享相同的ISA，它们仍然可以运行相同的软件。这种抽象确保了软件的兼容性和长期稳定性。

### 3.2 Machine Code vs. Assembly Language

- Machine Code

  - Instructions are represented in **Binary**
  - Hard and tedious for programmer

- Assembly Language

  - Symbolic version of machine code

  - Human readable

    - **1000110010100000** in binary and `add A,B` in assembly language

  - **Assembler **translates from assembly language to machine code

  - Assembly can provide ‘**pseudo-instructions**’ as **syntactic sugar**

    - > "伪指令"（pseudo-instructions）
      >
      > - 在汇编语言中，伪指令不是实际的机器语言指令，但它们在汇编器中有特定的含义。汇编器在处理伪指令时会将它们转换为一个或多个实际的机器指令，或执行特定的操作。例如，某些伪指令可能用于数据分配或指定一个内存地址。
      >
      > "语法糖"（syntactic sugar）
      >
      > - 语法糖是指在编程语言中，为了使代码更易读、更易写而添加的某种语法。这种语法并没有为语言增加新的功能，但它为编程师提供了一种更加方便、更加直观的方式来表示某个操作或结构。
      >
      > 汇编语言提供的伪指令可以被视为一种语法糖，因为它们为程序员提供了一种更简单、更直观的方式来编写汇编代码，尽管这些伪指令在最终转换为机器代码时可能会被替换为实际的指令或执行一系列操作。简言之，伪指令使得汇编代码更易读和更易写，但它们并不直接对应于实际的硬件指令。

  - When considering performance, only read instructions are counted, pseudo-instructions are not counted

### 3.3 Walkthrough

#### The components

![image-20230822160545623](https://images.wu.engineer/images/2023/08/22/image-20230822160545623.png)

- Assume a simple computing-storage platform, including a processor, bus and a memory
  - Processor processing instructions
  - Bus transmit the data between memory and processor
  - Memory store the instructions and temp data

#### The code in Action

```c
for (i=1; i<10; i++) {
    res = res + i;
}
```

```assembly
res <- res + i
i <- i + 1
if i < 10, repeat 
```

![image-20230822160818336](https://images.wu.engineer/images/2023/08/22/image-20230822160818336.png)

![image-20230822161503259](https://images.wu.engineer/images/2023/08/22/image-20230822161503259.png)

- The instructions and variables are stored in the **memory**

- The variable, `i` and `res` has been transmitted to **processor** through **bus**

  - The data of two variables and the instruction has been stored in **CPU register**, in order to get faster speed

  - > - The register (寄存器) is inside in the CPU, which is using to store the processing data and instruction
    > - The register can provide data and instruction quickly to the ALU
    > - The size of register determines the bit of the CPU, like 32 bit or 64 bit CPU
    >
    > - THE REGISTER IS NOT L1, L2, and L3 CAHCE
    > - L1, L2 and L3 cache is bigger, but slower than register. It provides a buffer between the memory and the processor register, mainly to decrease the distance between these two, from the physically abstraction.

#### Memory Instructions

![image-20230822161615095](https://images.wu.engineer/images/2023/08/22/image-20230822161615095.png)

- The machine needs instruction to move data from memory to the register
  - `r0 <- load i` is in the memory
  - This instruction has been transmitted to the processor through bus
  - Then the register `0` is **loaded** the data of variable `i`
- Then the same process for variable `res`

#### Reg-to-Reg Arithmetic

![image-20230822161825387](https://images.wu.engineer/images/2023/08/22/image-20230822161825387.png)

- After moving all needed variables into the register, the ALU can load all need variables from the register, but not memory. Which is much faster

- Sometimes the arithmetic operation uses a constant value instead of register value

  - `r0 <- r0 + 1`, `1` is the constant value

  - > 常数被称为"立即数"（Immediate Value）。立即数是直接编码在机器指令中的常数值。
    >
    > 所以，当ALU要执行加法操作时，它不需要从寄存器或内存中加载立即数，因为这个值已经直接包含在指令中了。这意味着CPU可以在执行指令的同时，直接从指令本身获取这个常数值，并在ALU中与寄存器中的值进行计算。

#### Execution Sequence (Loop)

![image-20230822162619136](https://images.wu.engineer/images/2023/08/22/image-20230822162619136.png)

- What happened when the machine want to process the loop?

  - ```assembly
    res <- res + i
    i <- i + 1
    if i < 10, repeat
    ```

- We need instructions to change the **control flow** based on condition:

  - Repetition (loop) and Selection (if-else) can both support

- Since the condition succeeded, execution will repeat from the indicated position

  - The execution will continue sequentially
  - Until we see another control flow instruction

#### Memory Instructions (Finish Computing, output the result)

![image-20230822162853849](https://images.wu.engineer/images/2023/08/22/image-20230822162853849.png)

- Finally, move the computed value out from the register, store it into the memory

#### Summary

- The stored-memory concept:
  - Both **instruction** and **data** are stored in memory

- **The load-store model:**
  - Limit memory operations and relies on registers for storage during execution

- **The major types of assembly instruction:**

  - **Memory:** Move values between memory and registers

  - **Calculation:** Arithmetic and other operations

  - **Control flow:** Change the sequential execution

### 3.4 General Purpose Registers

> General Purpose Registers（GPR，通用寄存器）是中央处理器（CPU）内部的一组寄存器，这些寄存器不是为某个特定的任务或操作而设计，而是为了存储临时数据或在指令执行过程中用作操作数。通常，汇编语言编程或机器语言编程中的指令可以直接访问和操作这些寄存器。
>
> GPR的特点和用途
>
> 1. **多功能**：与专用寄存器（如浮点寄存器或状态寄存器）相比，通用寄存器可以用于多种任务，如算术运算、数据移动、逻辑操作等。
> 2. **速度**：访问通用寄存器的速度非常快，因为它们是CPU内部的存储单元。这使得它们成为临时存储操作数和结果的理想选择。
> 3. **数量**：现代处理器通常具有多个GPR。例如，x86架构提供了EAX、EBX、ECX、EDX等寄存器（在64位模式下，这些寄存器分别被称为RAX、RBX、RCX、RDX）；而ARM架构提供了R0到R15的寄存器。
> 4. **扩展性**：随着处理器架构的发展，GPR的数量和大小可能会发生变化。例如，早期的x86处理器使用16位的AX、BX、CX和DX作为其GPR，而现代的x86-64处理器则使用64位的RAX、RBX、RCX和RDX。
> 5. **任务**：尽管这些寄存器被称为"通用"，但在某些指令或情境下，它们可能有特定的用途或约定。例如，在某些架构中，某些GPR可能首选或专用于函数调用的返回值或作为参数传递。

- Not all CPU register are GPR
  - CPU寄存器是一个广泛的类别，涵盖了处理器内的所有寄存器。这包括GPR，但也包括其他专用或特定功能的寄存器。
  - GPR是处理器中的寄存器，可以用于多种通用计算和数据传输任务。它们并没有为特定功能（如浮点运算）专门设计。
- Data are transferred from memory to registers for faster processing
- A typical architecture has 16 to 32 registers
- GPR has no data type



- There are **32 registers** in MIPS assembly language
  - Can be referred by a number ($0, \$1,…, \$31) OR
  - referred by name (\$a0, \$t1)

![image-20230822163647369](https://images.wu.engineer/images/2023/08/22/image-20230822163647369.png)

> - \$at (register 1) is reserved for the assembler
> - \$k0-\$k1 (register 26-27) are reserved for the operation system

### 3.5 MIPS Assembly Language

> MIPS assembly language 是 MIPS 架构的汇编语言。MIPS（Microprocessor without Interlocked Pipeline Stages）是一种基于RISC（Reduced Instruction Set Computer）原则的微处理器架构，旨在简化指令集以提高性能。以下是有关MIPS汇编语言的一些关键点：
>
> 1. **指令集**：MIPS 指令集被设计得相对简单，并与其硬件管道设计紧密相连。这使得MIPS能高效地执行指令，同时简化了硬件实现。
> 2. **寄存器**：MIPS架构具有32个通用寄存器，标记为`$0`到`$31`。其中，`$0`寄存器总是存储值0，其他寄存器用于不同的目的。例如，`$sp`是堆栈指针，`$ra`是返回地址寄存器。
> 3. **指令格式**：MIPS指令有几种格式，最常见的是R型、I型和J型。不同的格式支持不同的操作，例如算术运算、数据传输和跳转。
> 4. **指令示例**：以下是一些常见的MIPS汇编指令示例：
>    - `add $t0, $t1, $t2`：将 `$t1` 和 `$t2` 中的值加在一起，并将结果存储在 `$t0` 中。
>    - `lw $t0, 4($sp)`：从堆栈指针 `$sp` 加上偏移量 4 的位置加载一个字（word）到 `$t0`。
>    - `beq $t0, $t1, label`：如果 `$t0` 和 `$t1` 的值相等，则跳转到 `label`。

- Each instruction executes a simple command
  - Usually has a counterpart in high level programming language like C/C++, Java
- Each line of assembly code contains at most 1 instruction
- \# (hex-sign) is used for comments
  - Anything from \# to end of line is a comment and will be ignored by the assembler

![image-20230822164006111](https://images.wu.engineer/images/2023/08/22/image-20230822164006111.png)

#### General Instruction Syntax

![image-20230822164050549](https://images.wu.engineer/images/2023/08/22/image-20230822164050549.png)

- Naturally, most of the MIPS arithmetic/logic operations have three operands: 2 sources and 1 destination

#### Arithmetic Operation: Addition

![image-20230822164151284](https://images.wu.engineer/images/2023/08/22/image-20230822164151284.png)

- The value `a`, `b` and `c` are loaded into the CPU register `\$s0`, `\$s1` and `\$s2`
	- This procession is called **variable mapping**
> MIPS arithmetic operations are mainly **reg-to-reg**

#### Arithmetic Operation: Subtraction

![image-20230822164206893](https://images.wu.engineer/images/2023/08/22/image-20230822164206893.png)

- Similar variable mapping processing than addition
	- The position of `\$s1` and `\$s2` is important for subtraction

#### Complex Expression

![image-20230822164225150](https://images.wu.engineer/images/2023/08/22/image-20230822164225150.png)

- A single MIPS instruction can only handle at most two source operands.
	- In this case, we should break this expression into two separate expressions, one is addition and another is subtraction.

![image-20230822164231794](https://images.wu.engineer/images/2023/08/22/image-20230822164231794.png)

#### Constant/Immediate Operands

![image-20230822164257017](https://images.wu.engineer/images/2023/08/22/image-20230822164257017.png)

- Immediate value are also called: “constant value”
- The instruction is “Add immediate” (`addi`), differ from the default addition `add`

#### Register zero (\$0)

![image-20230822164318774](https://images.wu.engineer/images/2023/08/22/image-20230822164318774.png)

- The number zero (0) is **constantly** assigned at register zero (`\$0` or `\$zero`)
- The above assignment is equivalent to the pseudo instruction (move)
	- `add \$s0, \$s1, \$zero`
	- `move \$s0, \$s1`

### 3.6 Logical Operations

#### Overview

- Arithmetic instructions view the content of a register as a single quantity (singed or unsigned integer)
- The logical operations allows the ALU to view register as 32 raw bits rather than a single 32-bit number

![image-20230822164349029](https://images.wu.engineer/images/2023/08/22/image-20230822164349029.png)

- Truth table of logical operations

![image-20230822164357395](https://images.wu.engineer/images/2023/08/22/image-20230822164357395.png)

#### Shifting

![image-20230822164436083](https://images.wu.engineer/images/2023/08/22/image-20230822164436083.png)

![image-20230822164420472](https://images.wu.engineer/images/2023/08/22/image-20230822164420472.png)

- Left shift: `sll`
- The above code let the value in register `\$s0` **left shift** 4 bits, then store into the register `\$t2`

![image-20230822164441727](https://images.wu.engineer/images/2023/08/22/image-20230822164441727.png)

- Right shift: `srl`

#### Bitwise AND

![image-20230822164505002](https://images.wu.engineer/images/2023/08/22/image-20230822164505002.png)

- Bitwise AND: `and`
	- Do AND operation on the register `\$t1` and `\$t2` **bit by bit**, then store the result to register `\$t0`
	- It can be used for *masking operation*

#### Bitwise OR

![image-20230822164528057](https://images.wu.engineer/images/2023/08/22/image-20230822164528057.png)

- Bitwise OR: `or`

- Similar usage with the Bitwise AND operator
	- Also can be used to *mask*

#### Bitwise NOR

![image-20230822164543076](https://images.wu.engineer/images/2023/08/22/image-20230822164543076.png)

- Bitwise NOR: `nor`
- Similar usage with the Bitwise AND, OR operator
- There is no NOT instructions in MIPS to toggle bits 1->0, 0->1
	- However, the `nor` instruction can achieve the NOT operation
		- `nor \$t0, \$t0, \$zero`
		- This instruction turn all 0 to 1, and all 1 to 0 in register `\$t0`

- There DO NOT exist `nori` instruction

#### Bitwise XOR

![image-20230822164607052](https://images.wu.engineer/images/2023/08/22/image-20230822164607052.png)

- Bitwise XOR: `xor`
- To get `not` operation through `xor`:
	- `xor \$t0, \$t0, \$t2`

- There DO exist `xori`



### 3.7 Large Constant: Case Study



# 4 - MIPS II

## 4.1 Memory Organization

- The main memory can be viewed as a large, single-dimension array of memory locations
- Each location of the memory has an address, which is an index into the array
  - Given a `k`-bit address, the address space is of size $2^k$
- The memory map on the below contains one byte (8 bits) in every location/address.
  - This is called **byte addressing**

![image-20231013130128495](https://images.wu.engineer/images/2023/10/13/image-20231013130128495.png)

> **Byte Addressing 字节寻址**
> Byte addressing（字节寻址）是指在计算机内存中，每个字节都有其独特的地址。这意味着，即使一个数据项（例如32位整数）需要多个字节来存储，我们仍然可以分别访问这些字节。
>
> 为了更加清晰地说明，我们可以拿一个32位整数来做例子：
>
> 假设我们有一个32位的整数，它需要4个字节来存储（因为32位等于4字节）。在byte addressing系统中，这4个字节会被存放在连续的内存地址中。假设该整数的第一个字节存储在地址0x1000处，那么：
>
> - 第一个字节的地址是：0x1000
> - 第二个字节的地址是：0x1001
> - 第三个字节的地址是：0x1002
> - 第四个字节的地址是：0x1003
>
> 这就是byte addressing的核心思想，即每个字节在内存中都有唯一的地址。这种方式使得硬件和软件可以非常灵活地访问内存，但与此同时，也需要在内存管理方面投入更多的精力，以确保有效地使用这种精细级别的寻址机制。

### 4.1.1 Memory: Transfer Unit

- Using distinct memory address, we can access:
  - a single byte (byte addressable) or
  - a single word (word addressable)
- Word is:
  - Usually $2^n$ bytes
  - The common unit of transfer between processor and memory
  - Also commonly coincide with the register size, the integer size and instruction size in most architecture

> Word的大小通常与寄存器大小相同，例如32位架构中，通常由32位的寄存器（4字节），一个word就是32位


### 4.1.2 Memory: Word Alignment

- **Word alignment**:
  - Words are aligned in memory if they begin at a byte address that is a multiple of the number of bytes in the word
- Example: If a word consists of 4 bytes, then:

![image-20231013131721427](https://images.wu.engineer/images/2023/10/13/image-20231013131721427.png)

> "Word Alignment"（或简称 "Alignment"）是计算机存储和内存管理中的一个概念，它指的是数据项在内存中的开始地址应该是其大小（通常是数据项大小或特定架构的word大小）的某个倍数。
>
> 为什么需要对齐？
>
> 1. **性能**：在许多架构上，访问对齐的数据比非对齐的数据要快。当数据对齐时，数据可能完全位于一个或多个缓存行内，从而减少了需要访问的缓存行数量。
> 2. **硬件要求**：一些处理器不支持非对齐的数据访问，或者在尝试这样做时可能导致性能损失或异常。
>
> 以32位系统为例，其中word的大小为4字节（32位）：
>
> - 如果一个32位的整数地址为0x1004或0x1008，那么这个整数是对齐的，因为这些地址都是4的倍数。
> - 但是，如果这个32位的整数的地址为0x1005或0x1006，那么它就不是对齐的，因为这些地址不是4的倍数。
>
> 为了确保对齐，编译器和内存分配器通常会自动处理数据对齐的问题，为变量分配适当对齐的地址。但在低级编程或嵌入式系统开发中，程序员可能需要更加关注对齐的问题，因为它可能会影响性能或正确性。
>
> 如果是64位系统，则应该是8的倍数。

## 4.2 MIPS Memory Instructions

- MIPS is a load-store register architecture
  - 32 registers, each 32-bit (4 bytes) long
  - Each word contains 32-bit (4 bytes)
  - Memory addresses are 32-bit long

| Name                  | Examples                                                     | Comments                                                     |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 32 registers          | \$s0-\$s7, \$t0-\$t9, \$zero, \$a0-\$a3, \$v0-\$v1, \$gp, \$fp, \$sp, \$ra, \$at | Fast processor storage for data.<br />In MIPS, data must be in registers to perform arithmetic. |
| $2^{30}$ memory words | `Mem[0]`, `Mem[1]`, …, `Mem[4294967292]`                     | Accessed only by data transfer instructions.<br />MIPS uses **byte addresses**, so consecutive words differ by 4.<br />Memory holds data structures, such as arrays, and spilled registers, such as those saved on procedure calls |

> - 32 registers:
>   1. `$0` 或 `$zero`：这个寄存器始终包含值0，任何尝试向其写入的操作都会被忽略。
>   2. `$1` 或 `$at`：为汇编器预留的临时寄存器。
>   3. `$2-$3` 或 `$v0-$v1`：用于返回函数值的寄存器。
>   4. `$4-$7` 或 `$a0-$a3`：用于传递函数参数的寄存器。
>   5. `$8-$15`、`$24-$25` 或 `$t0-$t7` 和 `$t8-$t9`：临时寄存器，函数调用不会保存它们。
>   6. `$16-$23` 或 `$s0-$s7`：保存的寄存器，函数调用会保存它们。
>   7. `$26-$27` 或 `$k0-$k1`：为操作系统预留的寄存器。
>   8. `$28` 或 `$gp`：全局指针。
>   9. `$29` 或 `$sp`：堆栈指针。
>   10. `$30` 或 `$fp`：帧指针（在某些约定中使用）。
>   11. `$31` 或 `$ra`：返回地址。
>
> - memory words
>   - 指内存中的数据单元。一个 "word" 在 MIPS 中通常指代一个固定大小的数据块，其大小在传统的 MIPS 架构中为 32 位，或 4 字节。
>   - 如果 MIPS 系统有 $2^{30}$ 个 "memory words"，这意味着这个系统有 $2^{30}$ 个独立的 32 位数据块。换句话说，该系统的总内存大小是 $2^{30}$×32 位，或 $2^{30}$×4 字节 (4GB)。
> - Words and Memory words
>   - **Word**：是指数据的大小。在 32 位 MIPS 架构中，一个 word 是 32 位或 4 字节。
>   - **Memory Words**：是指内存中的 word 单元的数量。如果一个系统有 $2^{30}$ 个 memory words，那么它具有 $2^{30}$ 个独立的 32 位数据单元。

### 4.2.1 Memory Instruction: Load Word

- `lw $t0, 4($t0)`

![image-20231013133159243](https://images.wu.engineer/images/2023/10/13/image-20231013133159243.png)

- Steps:
  1. Memory Address = `$s0 + 4 = 8000 + 4 = 8004`
  2. Memory word at `Mem[8004]` is loaded into `$t0`

> 1. `lw`：这是 "load word" 的指令，意味着从内存中加载一个 32 位的数据块。
> 2. `$t0`：这是目标寄存器，指示数据从内存加载到哪个寄存器中。
> 3. `4($t0)`：这是源操作数，表示内存的地址。这个地址是通过取 `$t0` 寄存器中的值，并加上偏移量 `4` 来计算的。这里的偏移量是以字节为单位的，因此 `4` 实际上是 4 字节的偏移量。
>
> 所以，整体上，这条指令的意思是： 从地址为 `$t0 + 4` 的位置加载一个 word（32 位的数据块）到 `$t0` 寄存器中。
>
> 例如，假设 `$t0` 中原来的值是 `0x8000`，那么这条指令会从内存地址 `0x8004` 加载一个 word 到 `$t0` 寄存器中。

### 4.2.2 Memory Instruction: Store Word

- `sw $t0, 12($s0)`

![image-20231013134302246](https://images.wu.engineer/images/2023/10/13/image-20231013134302246.png)

- Steps:
  1. Memory Address = `$t0 + 12 = 8000 + 12 = 8012`
  2. Content of `$t0` is stored into word at `Mem[8012]`

> 1. `sw`：这是 "store word" 的指令，意味着将一个 32 位的数据块存储到内存中。
> 2. `$t0`：这是源寄存器，它表示要存储到内存中的数据来源于哪个寄存器。
> 3. `12($s0)`：这是目标操作数，表示内存的地址。这个地址是通过取 `$s0` 寄存器中的值，并加上偏移量 `12` 来计算的。这里的偏移量是以字节为单位的，所以 `12` 实际上是 12 字节的偏移量。
>
> 因此，整体上，这条指令的意思是： 将 `$t0` 寄存器中的 word（32 位的数据块）存储到地址为 `$s0 + 12` 的内存位置。
>
> 例如，假设 `$s0` 中的值是 `0x8000`，那么这条指令会将 `$t0` 寄存器中的内容存储到内存地址 `0x8012` 的位置。

### 4.2.3 Load and Store Instructions

- Only `load` and `store` instructions can access data in memory
- Example: Each array element occupies a word

| C Code             | MIPS Code                                                    |
| ------------------ | ------------------------------------------------------------ |
| `A[7] = h + A[10]` | `lw $t0, 40($s3)`<br />`add $t0, $s2, $t0`<br />`sw $t0, 28($s3)` |

- Each array element occupies a word(4 bytes)
- `$s3` contains the base address (address of first element, `A[0]` ) of array A. Variable `h` is mapped to `$s2`

### 4.2.4 Memory Instructions: Others

- Other than load word (`lw`) and store word (`sw`), there are other variants, example:
  - load byte (`lb`)
  - store byte (`sb`)
- Similar in format:
  - `lb $t1, 12($s3)`
  - `lb $t2, 13($s3)`
- Similar in working except that one byte, instead of one word, is loaded or stored
  - Note that the offset no longer needs to be a multiple of 4
- MIPS disallows loading/storing unaligned word using `lw`/`sw`
  - Pseudo-Instructions *unaligned load word `ulw` and unaligned store word `usw`* are provided for this purpose
- Other memory instructions:
  - `lh` and `sh`: load and store halfword
  - `lwl`, `lwr`, `swl`, `swr`: load word left/right, store word left/right

### 4.2.5 Example: Array

![image-20231013145548786](https://images.wu.engineer/images/2023/10/13/image-20231013145548786.png)

> 1. **C Statement to translate**：我们要转换的 C 语句是 `A[3] = h + A[1];`。这个语句表示要将变量 `h` 与数组 `A` 的第二个元素（索引为1的元素）相加，然后将结果存储在数组 `A` 的第四个元素中（索引为3的元素）。
> 2. **Variables Mapping**：这部分为我们提供了 C 语句中变量与 MIPS 寄存器之间的映射关系。即变量 `h` 映射到寄存器 `$s2`，而数组 `A` 的基地址（第一个元素的地址）映射到寄存器 `$s3`。
> 3. **MIPS Instructions**：
>    - `lw $t0, 4($s3)`: 这条指令从数组 `A` 中加载第二个元素（由于每个元素占 4 字节，所以索引为1的元素的偏移是 4 字节）到临时寄存器 `$t0` 中。
>    - `add $t0, $s2, $t0`: 这条指令将寄存器 `$s2`（存储变量 `h` 的值）与寄存器 `$t0` 中的值相加，并将结果存储在 `$t0` 中。
>    - `sw $t0, 12($s3)`: 这条指令将 `$t0` 中的值存储到数组 `A` 的第四个元素（由于每个元素占 4 字节，所以索引为3的元素的偏移是 12 字节）。
> 4. **Memory Representation**：这部分展示了数组 `A` 在内存中的表示方式。从基地址 `$s3` 开始，每个格子表示数组的一个元素。每个元素都是一个 word，这里假设一个 word 的大小是 4 字节。

### 4.2.6 Common Questions

#### Address vs Value

> Registers do NOT have types

- A register can hold any 32-bit number:
  - The number has no implicit data type and is interpreted according to the instruction that use it
- Examples:
  - `add $t2, $t1, $t0`
    - `$t0` and `$t1` should contain data values
  - `lw $t2, 0($t0)`
    - `$t0` should contain a memory address

#### Byte vs Word

> Consecutive word addresses in machines with byte-addressing do not differ by 1

- Common error:
  - Assume that the address of the next word can be found by incrementing the address in a register by 1 instead of by the word size in bytes
- For both `lw` and `sw`:
  - The sum of base address and offset must be a multiple of 4 (i.e. to adhere to word boundary)

### 4.2.7 Example: Swapping Elements

![image-20231013150059666](https://images.wu.engineer/images/2023/10/13/image-20231013150059666.png)

> 交换数组中两个连续元素的值（C和MIPS）
>
> - 我们要转换的C函数是swap，函数的主要逻辑是交换数组 `v` 中索引为 `k` 和 `k+1` 的两个连续元素。
> - **Variables Mapping**：这部分为我们提供了 C 函数中变量与 MIPS 寄存器之间的映射关系。即参数 `k` 映射到寄存器 `$5`，数组 `v` 的基地址映射到寄存器 `$4`，局部变量 `temp` 映射到寄存器 `$15`。
> - **Example**：提供了一个具体的例子，即当 `k=3` 时，交换数组 `v` 的第四和第五个元素（`v[3]` 和 `v[4]`）。假设数组的基地址是 2000。
> - **MIPS Instructions**：
>   - `sll $2, $5, 2`: 这条指令是将 `k`（存储在 `$5` 中）乘以 4（因为每个整数大小是4字节），结果保存在 `$2`。这是为了计算数组中索引为 `k` 的元素的偏移量。
>   - `add $2, $4, $2`: 将基地址（存储在 `$4`）和偏移量（存储在 `$2`）相加，计算出 `v[k]` 的地址，并将其保存在 `$2` 中。
>   - `lw $15, 0($2)`: 加载 `v[k]` 的值到 `$15`。
>   - `lw $16, 4($2)`: 加载 `v[k+1]` 的值到 `$16`。
>   - `sw $16, 0($2)`: 将 `v[k+1]` 的值存储到 `v[k]` 的位置。
>   - `sw $15, 4($2)`: 将 `v[k]` 的值存储到 `v[k+1]` 的位置。

## 4.3 Making Decisions

- Decision make in high-level language:
  - `if` and `goto` statement
  - MIPS decision making instructions are similar to `if` statement with a `goto`
- Decision making instructions
  - Alter the control flow of the program
  - Change the next instruction to be executed

- Two types of decision-making statements in MIPS
  - Conditional (branch)
    `bne $t0, $t1, label`
    `beq $t0, $t1, label`
  - Unconditional (jump)
    `j label`

- A label is an anchor in the assembly code to indicate point of interest, usually as branch target
  - Labels are NOT instructions


> 1. **Decision make in high-level language**:
>    - 当我们在高级编程语言（如 C、Java 或 Python）中进行决策时，通常使用的是 `if` 语句和 `goto` 语句。
>    - MIPS 的决策制定指令与高级编程语言中的 `if` 语句相似，并经常与 `goto` 语句一起使用，以决定程序的执行流程。
> 2. **Decision making instructions**:
>    - 这些指令用于改变程序的控制流程。
>    - 它们会改变下一条要执行的指令，从而使程序可能跳转到不同的部分执行。

### 4.3.1 Conditional Branch: `beq` and `bne`

- Processor follows the branch only when the condition is satisfied (True)
- `beq $r1, $r2, L1`
  - Go to statement labeled `L1` if the value in register `$r1` equals the value in register `$r2`
  - `beq` is “branch if equal”
  - C code: `if (a==b) goto L1`
- `bne $r1, $r2, L1`
  - Go to statement labeled `L1` if the value in register `$r1` does not equal the value in register `$r2`
  - `bne` is “branch if not equal”
  - C code: `if (a != b) goto L1`

### 4.3.2 Unconditional Jump: `j`

- Processor always follows the branch
- `j L1`
  - Jump to label `L1` unconditionally
  - C code: `goto L1`
- Technically equivalent to such statement
  `beq $s0, $s0, L1`

### 4.3.3 IF statement

![image-20231014210747922](https://images.wu.engineer/images/2023/10/14/image-20231014210747922.png)

> The right one is more efficient

![image-20231014211003957](https://images.wu.engineer/images/2023/10/14/image-20231014211003957.png)

> Re-write to `beq`
>
> ```assembly
> beq $s3, $s4, Else
> sub $s0, $s1, $s2
> j Exit
> Else: add $s0, $s1, $s2
> Exit:
> ```

### 4.3.4 Exercise #1: IF statement

![image-20231014212747843](https://images.wu.engineer/images/2023/10/14/image-20231014212747843.png)

## 4.4 Loops

![image-20231014232318823](https://images.wu.engineer/images/2023/10/14/image-20231014232318823.png)

### 4.4.1 Exercise #2: FOR loop



### 4.4.2 Inequalities

- We have `beq` and `bne`, what about branch-if-less-than?
  - There is no real `blt` instruction in MIPS
- Use `slt` (set on less than) or `slti`

```assembly
slt $t0, $s1, $s2
```

```c
if ($s1 < $s2)
	$t0 = 1;
else
	$t0 = 0;
```

- To build a `blt $s1, $s2, L` in instruction

```assembly
slt $t0, $s1, $s2
bne $t0, $zero, L
```

```c
if ($t1 < $t2)
	goto L;
```

- This is another example of pseudo-instruction
  - Assembler translates (`blt`) instruction in an assembly program into the equivalent MIPS(two) instructions

## 4.5 Array and Loop

- Typical example of accessing array elements in a loop:



> Count the number of zeros in an Array A
>
> - A is word array with 40 elements
> - Address of A[] -> \$t0, Result -> \$t8
>
> **C code:**
>
> ```c
> result = 0
> i = 0
> while (i<40) {
> 	if (A[i] == 0)
> 		result++;
> 	i++
> }
> ```
>
> ```assembly
> addi $t8, $zero, 0				# Assign variable "result" with value 0
> addi $t1, $zero, 0				# Assign variable "i" with value 0
> addi $t2, $zero, 160			# Assign a temp anoymous variable with value 160, point to endpoint of array
> loop: bge $t1, $t2, end			# Comparing address
> 	  lw  $t3, 0($t1)			# $t3 <- A[i]
> 	  bne $t3, $zero, skip		# if A[i] != 0, then skip
> 	  addi $t8, $t8, 1			# result++
> skip: addi $t1, $t1, 4			# move to the next item
> 	  j loop
> end:
> ```
>
> 

## 4.6 Exercises



# 5 - MIPS Instruction

## 5.1 Overview and Motivation

- Recap: Assembly instructions will be translated to machine code for actual execution
  - This section shows how to translate MIPS assembly code into binary patterns
- Explains some of the “target facts” from earlier:
  - Why is *immediate* limited to 16 bits
  - Why is *shift* amount only 5 bits

## 5.2 MIPS Encoding: Basics

- Each MIPS instruction has a fixed-length of 32 bits
  - All relevant information for an operation must be encoded with these bits
- Additional challenge:
  - To reduce the complexity of processor design, the instruction encodings should be as regular as possible
    - Small number of formats, i.e. as few variations as possible

> 每条 MIPS 指令都有固定的32位长度。
>
> - 所有操作必须在这32位内编码。这意味着每条指令，无论其功能如何，都被设计为具有相同的长度。

## 5.3 MIPS Instruction Classification

- Instructions are classified according to their operands:
  - Instructions with same operand types have same encoding

> R-Format (Register format: `op $r1, $r2, $r3`)
>
> - Instructions which use 2 source registers and 1 destination register
> - e.g. `add`, `sub`, `and`, `or`, `nor`, `slt`, etc
> - Special cases: `srl`, `sll`, etc

> I-Format (Immediate format: `op $r1, $r2, Immd`)
>
> - Instructions which use 1 source register, 1 immediate value and 1 destination register
> - e.g. `addi`, `andi`, `ori`, `slti`, `lw`, `sw`, `beq`, `bne`, etc

> J-Format (Jump Format: `op Immd`)
>
> - `j` instruction uses only one immediate value

> 1. **按操作数分类的指令**：
>    - 同种类型的操作数的指令具有相同的编码格式。这意味着，具有相似操作数结构的指令会按照相同的模式进行编码。
> 2. **R-Format (寄存器格式)**：
>    - 这类指令使用两个源寄存器和一个目标寄存器。
>    - 示例：`add`, `sub`, `and`, `or`, `nor`, `slt` 等都是 R-格式的指令。
>    - 特殊情况：像 `srl` 和 `sll` 这样的位移指令也是 R-格式的指令，但它们有些特别，因为它们可能涉及到一个立即数值（位移的数量）。
> 3. **I-Format (立即数格式)**：
>    - 这类指令使用一个源寄存器，一个立即数值（通常是一个具体的数值，而不是另一个寄存器的值），以及一个目标寄存器。
>    - 示例：`addi`, `andi`, `ori`, `slti`（这些都是与常数值进行操作的算术和逻辑指令），以及 `lw`, `sw`（加载和存储指令），`beq`, `bne`（分支指令）等都是 I-格式的指令。
> 4. **J-Format (跳转格式)**：
>    - 这类指令主要与跳转操作有关。
>    - `j` 指令就是一个示例，它只使用一个立即数值来表示跳转的目标地址。

## 5.4 MIPS Registers

- For simplicity, register numbers (`$0, $1,..., $31`) will be used in examples here instead of register names

![image-20231015160647920](https://images.wu.engineer/images/2023/10/15/image-20231015160647920.png)

## 5.5 R-Format

- Define fields with the following number of bits each:
  - 6+5+5+5+5+6=32 bits

![image-20231015204738023](https://images.wu.engineer/images/2023/10/15/image-20231015204738023.png)

- Each field has a name:

![image-20231015204755446](https://images.wu.engineer/images/2023/10/15/image-20231015204755446.png)

- Each field is an independent 5 or 6 bits unsigned integer
  - A 5-bit field can represent any number 0-31
  - A 6-bit field can represent any number 0-63

![image-20231015204925147](https://images.wu.engineer/images/2023/10/15/image-20231015204925147.png)

> MIPS R-Format 指令用于表示那些涉及两个源寄存器和一个目的地寄存器的指令，如加法、减法和位逻辑操作等。这些字段将 32 位的指令分解为特定的部分，每个部分有其特定的功能和意义。
>
> 以下是对每个字段的解释：
>
> 1. **opcode**：操作码字段，用于部分指定指令的类型。对于所有的 R-Format 指令，opcode 都设置为 0。
> 2. **funct**：函数代码字段，与 opcode 一起合并，可以准确地指定指令的类型（例如，加法、减法等）。
> 3. **rs (Source Register)**：源寄存器字段，指定第一个操作数的寄存器。
> 4. **rt (Target Register)**：目标寄存器字段，指定第二个操作数的寄存器。
> 5. **rd (Destination Register)**：目的地寄存器字段，指定存放操作结果的寄存器。
> 6. **shamt**：位移量字段，用于指定位移指令（如 srl 和 sll）的位移量。此字段有 5 位，因此可以表示从 0 到 31 的值。对于非位移指令，此字段设置为 0。
>
> 总体来说，这些字段组合在一起，形成了一个 32 位的 R-Format 指令，允许处理器知道它需要执行什么操作以及操作的操作数是哪些。这些字段是指令编码的基础，使得处理器能够快速地解码和执行这些指令。

### 5.5.1 R-Format: Example

![image-20231016172121689](https://images.wu.engineer/images/2023/10/16/image-20231016172121689.png)

![image-20231016172359137](https://images.wu.engineer/images/2023/10/16/image-20231016172359137.png)

![image-20231016172408013](https://images.wu.engineer/images/2023/10/16/image-20231016172408013.png)

## 5.6 I-Format

- 5-bit `shamt` field can only represent 0 to 31
- Immediates may be much larger than this
  - e.g. `lw`, `sw` instructions require bigger offset
- Compromise: Define a new instruction format partially consistent with R-format
  - If instruction has immediate, then it uses at most 2 registers
- Define fields with the following number of bits each:

![image-20231016174302290](https://images.wu.engineer/images/2023/10/16/image-20231016174302290.png)

- I-Format has no `funct` field, so the `opcode` uniquely specifies an instruction
- `rs` field specifies the source register operand
- `rt` field specifies the register to receive the result
- Immediate treated as a **single integer**

### 5.6.1 Instruction Address: Overview

- As instructions are stored in memory, they too have addresses
  - Conrtol flow instructions uses these addresses
- As instructions are 32-bit long, instruction addresses are word-aligned as well
- Program Counter(PC) is a special register that keeps address of instruction being executed in the processor

> 在介绍I-format指令时引入program counter (PC) 是因为一些I-format指令，特别是那些涉及分支和跳转的指令，使用立即数值作为基于当前PC值的偏移。这样的偏移方式允许指令跳转到程序内的特定位置。

### 5.6.2 Branch: PC-Relative Addressing

- Use I-Format

![image-20231016180351931](https://images.wu.engineer/images/2023/10/16/image-20231016180351931.png)

- `opcode` specifies `beq`, `bne`
- `rs` and `rt` specify registers to compare
- `immediate` is only 16 bits, the memory address is 32 bits. `immediate` is not enough to specify the entire target address
- Solution: Specify target address relative to the PC
- Target address is generated as :
  - PC + 16-bit `immediate` field
  - The `immediate` field is a signed two’s complement integer

![image-20231016182626018](https://images.wu.engineer/images/2023/10/16/image-20231016182626018.png)

> **相对寻址**：许多I-format指令，如`beq` (branch if equal) 和 `bne` (branch if not equal)，使用立即字段作为跳转偏移量。这些偏移量是相对于当前的PC值的。通过这种方法，指令可以确定跳转到程序中的哪个位置。
>
> 1. **`immediate` is only 16 bits**：在I-format指令中，
>
> 立即数字段（immediate field）的大小是固定的16位。这意味着它可以直接表示的值的范围是从0到65535（如果被视为无符号数）或从-32768到32767（如果被视为有符号数）。
>
> 1. **the memory address is 32 bits**：在MIPS架构中，完整的内存地址是32位的。这意味着系统可以直接访问的内存地址范围是从0到4GB。
> 2. **`immediate` is not enough to specify the entire target address**：由于立即数字段只有16位，它不能直接表示32位的完整内存地址。换句话说，一个16位的值不足以覆盖整个4GB的内存空间。
>
> 这有什么意义呢？
>
> 当使用I-format指令（如加载和存储指令）访问内存时，通常使用一个基址寄存器和一个16位的偏移量（即立即数）来确定目标地址。例如，在`lw $t0, 4($t1)`这样的指令中，`$t1`包含一个基地址，而4是一个16位的偏移量。最终的内存访问地址是`$t1`中的值加上4。
>
> 此外，对于跳转和分支指令，16位的立即数经常被解释为相对于当前指令地址（即程序计数器，PC）的偏移量。这允许指令跳转到相对近的位置，而不需要指定完整的32位地址。
>
> 综上所述，尽管16位的立即数不能直接指定完整的32位地址，但通过与其他值（如基址寄存器或当前PC值）结合，可以有效地指定或计算目标地址。

#### Branches

- We usually use branches by `if-else`, `while`, `for`
- Loops are generally small:
  - Typically up to 50 instructions
- Unconditional jumps are done using jump instruction `j`, not the branches
- Conclusion: A branch often changes PC by a small amount
- Can the branch target range be enlarged?
- Observation: Instructions are word-aligned
  - Number of bytes to add to the PC will always be a multiple of 4 (Since each MIPS instruction is 32-bit)
  - Interpret the `immediate` as a number of words, i.e. automatically multiplied by $4_{10}$($100_2$)
- Can branch to $\pm 2^{15}$ words from the PC
  - i.e. $\pm 2^{17}$ bytes from the PC

#### Branch Calculation

![image-20231016183036379](https://images.wu.engineer/images/2023/10/16/image-20231016183036379.png)

- `immediate` field specifies the number of words to jump, which is the same as the number of instructions to ‘skip over’
- `immediate` field can be positive or negative
- Due to hardware design, add `immediate` to (PC+4), not to PC

> 即如果没有进入branch，则跳转到下一个指令，由于每个MIPS指令是32 bits，所以在PC上加4字节
>
> 如果进入了branch，则跳转到一个新的地址来执行指令，这个新的地址是基于当前PC值，偏移量（即下一条指令的位置PC+4），以及由分支指令中的立即字段(`immediate`)给出的额外偏移量计算出来的
>
> 立即数字段(`immediate`)被解释为word的数量，而每个word有4字节，所以被乘以4

## 5.7 J-Format

- For branches, PC-relative addressing was used, because we do not need to branch too far
- For general jump `j`, we may jump to anywhere in memory
- The ideal case is to specify a 32-bit memory address to jump to.

> J-format 是 MIPS 指令集中用于跳转（jump）指令的格式。虽然理论上我们确实希望直接指明一个32位的内存地址以进行跳转，但在实际的指令编码中，由于指令的长度也是32位，不可能在单一的指令中同时包含操作码、其他字段和一个完整的32位地址。
>
> 考虑到这个限制，J-format 被设计为只包含一个26位的跳转目标地址字段。这意味着我们不能直接指定整个32位的跳转目标地址。但是，由于所有指令都是字对齐的，这意味着指令的地址的最后两位总是00（因为指令长度为4字节，或32位）。这为我们提供了一个小小的优势：我们只需要指定高26位的地址，而低2位则可以简单地置为0。
>
> 此外，J-format 的跳转是基于绝对地址的，而不是相对于当前 PC 的偏移。这意味着 J-format 跳转指令可以跳转到内存中的任何位置，只要这个位置在那26位地址范围内。
>
> 总的来说，虽然我们希望能够直接指明一个32位的地址进行跳转，但由于指令长度的限制和字对齐的特性，J-format 只提供了一个26位的地址字段来进行跳转。

- Define fields of the following number of bits each

![image-20231016185642605](https://images.wu.engineer/images/2023/10/16/image-20231016185642605.png)

- Keep `opcode` field identical to R-format and I-format for consistency
- Combine all other fields to make room for larger target address
- We can only specify 26-bits of 32 bits address
- Optimization:
  - Just like with branches, jumps will only jump to word-aligned addresses, so last two bits are always `00`
  - So, let’s assume the address ends with `00` and leave them out
  - Now we can specify **28 bits** of 32-bit address
- Where do we get the other 4 bits?
  - MIPS choose to take the 4 most significant bits from PC+4
  - This means that we cannnot jump to anywhere in memory, but it should be sufficient most of the time
  - The maximum jump range is **256MB**
- Special instruction if the program straddles 256MB boundary
  - `jr`: use `load` instruction to load full 32-bit memory address to register, then use `jr` instruction to jump
  - Target address is specified through a register

> 在MIPS中，使用J-format的`j`指令时，我们确实只有26位来指定跳转地址。这26位的地址是如何转化为完整的32位地址的呢？它是通过将这26位的跳转字段左移2位（因为每个指令是4字节或32位）来实现的，然后再与当前指令地址的高4位进行组合，从而生成完整的32位跳转地址。
>
> 因此，这26位地址可以指定 $2^{26}$ 不同的跳转目标，也就是 67,108,864 个可能的目标。由于每个指令都是4字节，所以跳转范围是 $2^{26} * 4$ 字节，也就是 268,435,456 字节或 256 MB。

![image-20231016191127695](https://images.wu.engineer/images/2023/10/16/image-20231016191127695.png)

## 5.8 Addressing Modes

- **Register addressing**: operand is a register

![image-20231016191156878](https://images.wu.engineer/images/2023/10/16/image-20231016191156878.png)

- Immediate addressing: operand is a constant within the instruction itself (`addi`, `andi`, `ori`, `slti`)

![image-20231016191320558](https://images.wu.engineer/images/2023/10/16/image-20231016191320558.png)

- Base addressing (displacement addressing): operand is at the memory location whose address is sum of a register and a constant in the instruction (`lw`, `sw`)

![image-20231016191412023](https://images.wu.engineer/images/2023/10/16/image-20231016191412023.png)

- PC-relative addressing: address is sum of PC and constant in the instruction (`beq`, `bne`)

![image-20231016191443325](https://images.wu.engineer/images/2023/10/16/image-20231016191443325.png)

- Pseudo-direct addressing: 26-bit of instruction concatenated with upper 4-bits of PC (`j`)

![image-20231016191516576](https://images.wu.engineer/images/2023/10/16/image-20231016191516576.png)

## 5.9 Summary

- MIPS instruction:

  - 32 bits representing a single instruction, for each format (R, I, J) the fields included are different

  ![image-20231016191613707](https://images.wu.engineer/images/2023/10/16/image-20231016191613707.png)

  - Branches and load/store are both I-format instructions; but branches use PC-relative addressing, whereas load/store use base addressing
  - Branches use PC-relative addressing; jumps use pseudo-direct addressing
  - Shifts use R-format, but other immediate instructions (`addi`, `andi`, `ori`) use I-format

![image-20231016191754835](https://images.wu.engineer/images/2023/10/16/image-20231016191754835.png)

# 6 - Datapath Design

## 6.1 Building a Processor: Datapath & Control

- Two major components for a processor:
  1. Datapath
     - Collection of components that process data
     - Performs the arithmetic, logical and memory operations
  2. Control
     - Tells the datapath, memory and I/O devices what to do according to program instructions

## 6.2 MIPS Processor: Implementation

- Simplest possible implementation of a subset of the core MIPS ISA:
  - Arithmetic and Logical operations
    - `add`, `sub`, `and`, `or`, `addi`, `andi`, `ori`, `slt`
  - Data transfer instructions
    - `lw`, `sw`
  - Branches
    - `beq`, `bne`
- Shift instructions (`sll`, `srl`) and J-type instructions (`j`) will not be discussed

## 6.3 Instruction Execution Cycle

![image-20231016194352422](https://images.wu.engineer/images/2023/10/16/image-20231016194352422.png)

1. Fetch:
   - Get instruction from memory
   - Address is in Program Counter (PC) Register
2. Decode:
   - Find out the operation required
3. Operand Fetch
   - Get operand(s) needed for operation
4. Execute:
   - Perform the required operation
5. Result Write (Store):
   - Store the result of the operation

## 6.4 MIPS Instruction Execution

- Show the actual steps for 3 representative MIPS instructions
- Fetch and Decode stage not shown, the standard steps are performed

![image-20231016201526168](https://images.wu.engineer/images/2023/10/16/image-20231016201526168.png)

- `opr` = operand, `ofst` = offset, `MemAddr` = Memory Address

- Design changes:
  - Merge Decode and Operand Fetch - Decode is simple for MIPS
  - Split Execute into ALU (Calculation) and Memory Access

![image-20231016201726353](https://images.wu.engineer/images/2023/10/16/image-20231016201726353.png)

- `inst.` = instruction

## 6.5 Build a MIPS Processor

- What we are going to do:
  - Look at each stage closely, figure out the requirements and processes
  - Sketch a high level block diagram, then zoom in for each elements
  - With the simple starting design, check whether different type of instructions can be handled
    - Add modifications when needed

### 6.5.1 Fetch Stage

- Instruction **Fetch Stage**:
  1. Use the Program Counter (PC) to fetch the instruction from *memory*
     - PC is implemented as a special register in the processor
  2. Increment the PC by 4 to get the address of the next instruction:
     - Since each instruction is 32 bit, which is 4 bytes
     - Note the exception when branch/jump instruction is executed
- Output to the next stage (**Decode**)”
  - The instruction to be executed

![image-20231016205753511](https://images.wu.engineer/images/2023/10/16/image-20231016205753511.png)

#### Element: Instruction Memory

- Storage element for the instructions
  - It is a sequential circuit
  - Has an internal state that stores information
  - Clock signal is assumed and not shown

![image-20231016210025279](https://images.wu.engineer/images/2023/10/16/image-20231016210025279.png)

- Supply instruction given the address
  - Given instruction address M as input, the memory outputs the content at address M
  - Conceptual diagram of the memory layout is given on the below

![image-20231016210019599](https://images.wu.engineer/images/2023/10/16/image-20231016210019599.png)

> 1. **存储元素**：这里提到的存储元素是指用于存储指令的硬件部件。在计算机中，这通常是指主存储器或RAM。
> 2. **它是一个顺序电路**：与组合电路不同，顺序电路有一定的内部状态，并且其输出不仅取决于当前的输入，还取决于之前的输入或状态。这意味着存储元素可以维持和存储信息。
> 3. **有内部状态用于存储信息**：这意味着该电路具有某种记忆能力，能够保存数据或状态信息，直到被更改或清除。
> 4. **时钟信号是假设的并且未显示**：顺序电路通常需要一个时钟信号来同步其操作。但是，在某些描述或图解中，为了简化表示，时钟信号可能不会明确显示。
> 5. **提供指令给定地址**：存储元素的主要功能之一是，当提供一个指令地址`M`时，它能够输出存储在地址`M`的内容。这就是计算机从内存中获取指令并执行它们的方式。

#### Element: Adder

- Combinational logic to implement the addition of two numbers
- Inputs:
  - Two 32-bit numbers A,B
- Output:
  - Sum of the input number A+B

![image-20231016221949416](https://images.wu.engineer/images/2023/10/16/image-20231016221949416.png)

#### The idea of clocking

- PC is read during the first half of the clock period and it is updated with PC+4 at the next rising clock edge

![image-20231016222047514](https://images.wu.engineer/images/2023/10/16/image-20231016222047514.png)

### 6.5.2 Decode Stage

- Instruction Decode Stage:
  - Gather data from the instruction fields:
    1. Read the `opcode` to determine instruction type and field lengths
    2. Read data from all necessary registers
- Input from previous stage (Fetch):
  - Instruction to be executed
- Output to the next stage (ALU):
  - Operation and the necessary operands

![image-20231016222237654](https://images.wu.engineer/images/2023/10/16/image-20231016222237654.png)

#### Element: Register File

- A collection of 32 registers
  - Each 32-bit wide; can be read/written by specifying register number 
  - Read at most two register per instruction
  - Write at most one register per instruction
- `RegWrite` is a control signal to indicate:
  - Writing of register
  - 1 (True) = Write, 0 (False) = No Write

![image-20231016224916744](https://images.wu.engineer/images/2023/10/16/image-20231016224916744.png)

#### R-Format Instruction

![image-20231016224938561](https://images.wu.engineer/images/2023/10/16/image-20231016224938561.png)

#### I-Format Instruction

![image-20231016231441750](https://images.wu.engineer/images/2023/10/16/image-20231016231441750.png)

![image-20231016231455234](https://images.wu.engineer/images/2023/10/16/image-20231016231455234.png)

> 1. **不同的指令格式**：MIPS指令集包括R-format、I-format和J-format等不同格式的指令。这些指令格式中，寄存器的编号和位置可能会不同。
> 2. **写入寄存器的选择**：在R-format指令中，通常使用`rd`字段（也就是`Inst[15:11]`）来指定结果的写入寄存器。但是，在I-format指令（如`addi`）中，结果是写入`rt`字段指定的寄存器，也就是`Inst[20:16]`。
> 3. **multiplexer的作用**：为了能够处理这种不同，我们需要一个选择器，即`multiplexer`。根据指令的类型（R-format还是I-format），`multiplexer`决定应该使用`Inst[20:16]`还是`Inst[15:11]`来确定写入寄存器的编号。
> 4. **控制信号`RegDst`**：这是一个控制信号，用于告诉`multiplexer`该选择哪个输入。例如，对于I-format指令，`RegDst`会设置为选择`Inst[20:16]`；对于R-format指令，它会设置为选择`Inst[15:11]`。

#### Multiplexer

- Function: Selects one input from multiple input lines
- Inputs: n lines of same width
- Control: m bits where $n=2^m$
- Output: Select i-th input line if control = i

![image-20231016231608167](https://images.wu.engineer/images/2023/10/16/image-20231016231608167.png)

![image-20231016232635452](https://images.wu.engineer/images/2023/10/16/image-20231016232635452.png)

> 这张图中显示了完整的decoder处理I-format指令的流程。
>
> 首先在左侧的输入部分，由于I format指令少一个寄存器的输入，所以先加入一个MUX将rt部分和原先属于rd部分的寄存器输入，根据指令的类型选择输出一个到decoder中。最后，对immediate的后半部分（16位）加长到32位后连到data read 2后面的MUX中。
>
> sign extend操作是这样的：首先检查immediate的最高位（第15位，也称为符号位）。如果符号位是0（即该值是正数或零），那么在32位值的前16位都填充0。如果符号位是1（即该值是负数），那么在32位值的前16位都填充1。
>
> 由于MIPS的I format指令中的immediate字段一开始就被设计成16位，所以在decode阶段中截断成16位再延长至32位的操作不会导致数据的损失
>
> 在右半部分，如果指令是I format的，那么左侧的MUX会输入rt，右侧的MUX会选择immediate。最终decode阶段输出的是一个register值和一个immediate值

#### Branch Instruction

![image-20231016233736925](https://images.wu.engineer/images/2023/10/16/image-20231016233736925.png)

### 6.5.3 ALU Stage

- Instruction ALU stage:
  - ALU = Arithmetic Logic Unit
  - Also called the Execution stage
  - Perform the real work for most instruction here
    - Arithmetic (e.g. `add`, `sub`), shifting(`sll`), Logical (`and`, `or`)
    - Memory operation (`lw`, `sw`): Address calculation
    - Branch operation (`bne`, `beq`): Perform register comparison and target address calculation
- Input from previous stage (Decode):
  - Operations and operands
- Output to the next stage (Memory):
  - Calculation result

![image-20231016234343349](https://images.wu.engineer/images/2023/10/16/image-20231016234343349.png)

#### Element: Arithmetic Logic Unit

- ALU is a combinational logic to implement arithmetic and logical operations
- Inputs: two 32-bit numbers
- Control: 4-bit to decide the particular operation
- Outputs: Result of arithmetic/logical operation, and a 1-bit signal to indicate whether the result is zero

![image-20231016234517713](https://images.wu.engineer/images/2023/10/16/image-20231016234517713.png)

#### Decode & ALU Stage: Non-Branch Instructions

![image-20231016234536132](https://images.wu.engineer/images/2023/10/16/image-20231016234536132.png)

#### ALU Stage: Branch Instructions

- Branch Instruction is harder as we need to perform two calculations, for example `beq $9, $0, 3`

  1. Branch Outcome
     - Use ALU to compare the register
     - The 1-bit `isZero` signal is enough to handle equal/not equal-check.
  2. Branch Target Address:
     - Introduce additional logic to calculate the address
     - Need PC (from Fetch Stage)
     - Need Offset (from Decode Stage)

  ![image-20231016234809191](https://images.wu.engineer/images/2023/10/16/image-20231016234809191.png)

### 6.5.4 Memory Stage

- Instruction Memory Access Stage:
  - Only the load and store instructions need to perform operation in this stage:
    - Use memory address calculated by ALU stage
    - Read from or write to data memory
  - All other instruction remain idle
    - Result from ALU stage will pass through to be used in Register Write stage if applicable
- Input from previous stage (ALU):
  - Computation result to be used as memory address (if applicable)
- Output to next stage (Register Write):
  - Result to be stored (if applicable)

![image-20231016235031518](https://images.wu.engineer/images/2023/10/16/image-20231016235031518.png)

#### Element: Data Memory

- Storage element for the data of a program
- Inputs: (1) Memory address, (2) data to be written (Write Data) for store instructions
- Output: Data read from memory (Read Data) for load instructions

![image-20231016235241418](https://images.wu.engineer/images/2023/10/16/image-20231016235241418.png)

#### Load Instruction

![image-20231016235305649](https://images.wu.engineer/images/2023/10/16/image-20231016235305649.png)

#### Store Instruction

![image-20231016235340119](https://images.wu.engineer/images/2023/10/16/image-20231016235340119.png)

> 1. **lw (Load Word) 指令**：它的功能是从内存中加载一个字（word，通常为32位）到寄存器中。该指令需要提供一个基址寄存器和一个偏移量来确定要读取的内存地址。例如，指令 `lw $t0, 4($t1)` 会从内存地址 `$t1 + 4` 加载一个字并存放到寄存器 `$t0` 中。
> 2. **sw (Store Word) 指令**：与 `lw` 指令相反，`sw` 的功能是将一个寄存器中的字存储到内存中。同样，这需要一个基址寄存器和一个偏移量来确定要写入的内存地址。例如，指令 `sw $t0, 4($t1)` 会将寄存器 `$t0` 中的内容存储到内存地址 `$t1 + 4`。

#### For Non-Memory Instruction (`add`)

![image-20231016235611237](https://images.wu.engineer/images/2023/10/16/image-20231016235611237.png)

### 6.5.5 Register Write Stage

- Instruction Register Write Stage:
  - Most instructions write the result of some computation into a register
    - Examples: arithmetic, logical, shifts, loads, set-less-than
    - Need destination register number and computation result
  - Exceptions are stores, branches, jumps
    - These are no result to be written
    - These instructions remain idle in this stage
- Input from previous stage (Memory):
  - Computation result either from memory or ALU

![image-20231017000051417](https://images.wu.engineer/images/2023/10/16/image-20231017000051417.png)

- Result Write stage has no additional element:
  - Basically just route the correct result into register file
  - The Write Register number is generated way back in the Decode Stage

#### Routing

![image-20231017000148789](https://images.wu.engineer/images/2023/10/16/image-20231017000148789.png)

## 6.6 Complete Datapath

![image-20231017000411760](https://images.wu.engineer/images/2023/10/16/image-20231017000411760.png)

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
