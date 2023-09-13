# IT5002 - Tutorial 1

## 1. 2’s complement

> In  2’s  complement  representation,  “sign  extension”  is  used  when  we  want  to represent an n-bit signed integer as an m-bit signed integer, where m > n. We do this by copying the sign-bit of the n-bit signed m – n times to the left of the n-bit number to create an m-bit number.  
>
> So for example, we want to sign-extend 0b0110 to an 8-bit number. Here n = 4, m = 8, and thus we copy the sign but m – n = 4 times, giving us 0b00000110.  
>
> Similarly  if  we  want  to  sign-extend  0b1010  to  an  8-bit  number,  we  would  get 0b11111010.  
>
> **Show that IN GENERAL sign extension is value-preserving. For example, 0b00000110 = 0b0110 and 0b11111010 = 0b1010.**

In 2’s complement, the MSB shows the sign of the number. For instance, the MSB with 0 is the positive number, and MSB with 1 is the negative number. In this case, the equations can be concluded for both sign numbers’ computation.

First let’s say the positive number, 18, for example, has the binary code `0001 0010`. Each bit of the binary code has its fixed value, and the sign of 1 or 0 means the position is counted or not. In this case, only the second and the fifth position has been signed to 1. So the decimal number can be calculated by:
$$
\begin{aligned}
& 2^0 \times 0 + 2^1\times 1 + 2^2\times0 + 2^3\times0 + 2^4\times1 + 2^5\times0 + 2^6\times0 + 2^7\times0 + 2^8\times0 \\
=\ & 2^1 + 2^4 \\
=\ & 2+16 \\
=\ &18
\end{aligned}
$$
In this case, if the sign extension need to be performed, let’s say, extend from 8-bit to 16-bit, the binary code should from `0001 0010` to `0000 0000 0001 0010`. Since it is the positive number so the thing need to do is to adding `0` on the front (left). Now, the decimal presentation of the extended binary code is still the same, since the added `0` will not influence the computing process, which prove the value preserving of the sign extension of the positive number.

For negative number in 2’s complement, it usually requires to convert the positive number’s binary code to 1’s complement, then add 1. For example, to convert 18 to -18, we need to first take 1’s complement for the binary code `0001 0010`, which is `1110 1101`. Then add 1 to `1110 1110`. The correctness of the 2’s complement is not necessary to prove since we compute the negative number by taking 1’s complement then plus 1. 

Now for the sign extension, the negative number will add 1 in the front. Hence `1110 1110` changes to `1111 1111 1110 1110`. In this case, to prove the value preserving, we take the 1’s complement of the number, which is `0000 0000 0001 0001`, then add 1, to `0000 0000 0001 0010`. Which is the same as the previous number.

## 2. (r-1)’s complement

> We generalize (r – 1)’s-complement (also called radix diminished complement) to include fraction as follows:
>
>  **(r – 1)’s complement of $N = r^n – r^{–m} – N$ **
>
> Where $n$ is the number of integer digits and $m$ the number of fractional digits. (If there are no  fractional digits, then $m  =  0$ and the formula becomes $rn  –  1  –  N$ as given in class.) 
>
> For example, the 1’s complement of `011.01` is $(2^3  –  2^{–2})  –  011.01 =  (1000 – 0.01) – 011.01 = 111.11 – 011.01 = 100.10$. 
>
> Perform the following binary subtractions of values represented in 1’s complement representation by using addition instead. (Note: Recall that when dealing with complement representations, the two operands must have the same number of digits.)  
>
> Is sign extension used in your working? If so, highlight it. 
>
> Check your answers by converting the operands and answers to their actual decimal values.

(a) `0101.11 - 010.0101`
$$
\begin{aligned}
&0101.11_2 - 010.0101_2 \\
=\ & 0101.11_2 + (0010.0101)_{1s} \\
=\ & 0101.11_2 + ((10000_{2} - 0.0001_2)-0010.0101_2+1_2) \\
=\ & 0101.11_2 + (1111.1111_2 - 0010.0101_2+1_2) \\
=\ & 0101.1100_2 + 1101.1011_2 \\
=\ & 0011.0111_2
\end{aligned}
$$
(b) `010111.101 - 0111010.11`
$$
\begin{aligned}
&010111.101 - 0111010.11 \\
=\ & 0010111.101_2 + (0111010.11)_{1s} \\
=\ & 0010111.101_2 + 1000101.01_2 \\
=\ & 011100.111_2 \\
\end{aligned}
$$

## 3.Floting Point

> Convert the following numbers to fixed-point binary in 2’s complement, with 4 bits for the integer portion and 3 bits for the fraction portion:

(a) 1.75

`0001.110`

(b) -2.5

`0010.100 -> 1101.011 + 1 -> 1101.100`

(c) 3.876 (approximated as 3.875)

`0011.111`

(d) 2.1 (approximated as 2.125) 

`0010.001`

## 4.IEEE 754

> How would you represent the decimal value –0.078125 in the IEEE 754 single-precision representation? Express your answer in hexadecimal. Show your working.

$$
-0.078125 = (-1)^S\times2^{E-1023}\times(1+M) \\
S=1; \\
E=1023 \\
M=0.078125
$$

IEEE 754 single-precision representation (also known as float) uses 32 bits: 1 bit for the sign, 8 bits for the exponent, and 23 bits for the fraction (mantissa). 

- The sign bit will be `1` since the number is negative. 

$$
1000\ 0000\ 0000\ 0000\ 0000\ 0000\ 0000\ 0000
$$

**Exponent**
$$
\begin{aligned}
0.078125 &= \frac 5 {64} \\
&= \frac 1 {64} + \frac 1 {16} \\
&= 0.000101_2
\end{aligned}
$$
**Normalize the binary number**:
$$
\begin{aligned}
0.000101_2 = 1.01_2 \times 2^{-4}
\end{aligned}
$$

- Where the exponent will be $-4$
- $-4+127 = 123 = 01111011_2$

$$
1011\ 1101\ 1000\ 0000\ 0000\ 0000\ 0000\ 0000_2 = \text{BD800000}_{16}
$$

## 5. MIPS

> Write the following in MIPS Assembly, using as few instructions as possible. You may rewrite the equations if necessary to minimize instructions.
>
> In all parts you can assume that integer variables a, b, c and d are mapped to registers $s0, $ $s1$, $s2$ and $s3$ respectively. Each part is independent of the others.

(a) `c = a + b`

```assembly
add $s2, $s0, $s1 ;c = a + b
```

(b) `d = a + b - c`

```assembly
add $s3, $s0, $s1 ; d = a + b
sub $s3, $s3, $s2 ; d = d - c
```

(c) `c = 2b + (a - 2)`

```
add $s2, $s1, $s1 ; c = b + b
subi $s0, $s0, 2  ; a = a - 2
add $s2, $s2, $s0 ; c = c + a
```

(d) `d = 6a + 3(b - 2c)`

```assembly
sll $s3, $s0, 2   ; d = 4a
sll $s0, $s0, 1   ; a = 2a
add $s3, $s3, $s0 ; d = d(4a) + a(2a)
sll $t0, $s1, 1   ; t0 = 2b
add $s3, $s3, $t0 ; d = d + t0 = 6a + 3b
sll $t1, $s2, 2   ; t1 = 4c
sll $s2, $s2, 1   ; c = 2c
sub $s3, $s3, $t1 ; d = d + t1 = 6a + 3b - 4c
sub $s3, $s3, $s2 ; d = d - c(2c) = 6a + 3b - 6c
```

