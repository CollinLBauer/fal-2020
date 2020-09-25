<!--
Superscript: ⁰¹²³⁴⁵⁶⁷⁸⁹
Subscript:   ₀₁₂₃₄₅₆₇₈₉
Other: ≈
-->

Collin Bauer

## CSCI 310 - Advanced Algorithms

Assignment 1

*Please forgive the makeshift notation. This is the best I can do with current tools. I may switch to LaTeX to avoid this in the future.*

---

## 2.1

### 9.
For each of the following pairs of functions, indicate whether the first function of each of the following pairs has a lower, same, or higher order of growth (to within a constant multiple) than the second function.

- a) Same order of growth:  
  > lim <sub>n → ∞</sub> n(n + 1) / 2000n²  
  > ≈ lim <sub>n → ∞</sub> n²/2000n² = 1/2000 = Constant

- b) 100n² grows slower than 100n² 0.01n³:  
  > lim <sub>n → ∞</sub> 100n² / 0.01n³  
  > = lim <sub>n → ∞</sub> 100 / 0.01n = 0

- c)  Same order of growth:  
  > lim <sub>n → ∞</sub> log₂(n) / ln(n)  
  > lim <sub>n → ∞</sub> (ln(n)/ (ln(n) * ln(2)) = 1/ln(2) = Constant

- d) I don't like this notation *at all*. But, if I'm interpreting them correctly...  
    log₂²(n) grows faster than log₂(n²):  
  > lim <sub>n → ∞</sub> log₂²(n) / log₂(n²)  
  > = lim <sub>n → ∞</sub> log₂(n)² / 2log₂(n)  
  > = lim <sub>n → ∞</sub> log₂(n) / 2 = ∞

- e) Same order of growth:
  > lim <sub>n → ∞</sub> 2<sup>n - 1</sup> / 2<sup>n</sup
  > = lim <sub>n → ∞</sub> 2<sup>n</sup>/ 2<sup>n + 1</sup> = 1/2 = Constant

- f) Skipping for now...

<br/>

---

## 2.2

### 6.
- a)
- b)

<br/>

---

## 2.3

### 1.
Compute the following sums.

- b) 2046

- c) SUM<sub>[i = 3 → n + 1]</sub>(1)  
  = 1 + 1 + ... + 1  
  = n - 2

- d) SUM<sub>[i = 3 → n + 1]</sub>(i)  
  = 3 + 4 + 5 + ... + n + (n + 1)  
  = n² + n - 2 = (n + 2)(n - 1)

- e) SUM<sub>[i = 0 → n - 1]</sub>(i + 1)  
  = 2 + 3 + 4 + ... + (n - 2) + (n - 1)  
  = n² - n - 2 = (n - 2)(n + 1)

- g) SUM<sub>[i = 1 → n]</sub>( SUM<sub>[j = 1 → n]</sub>( ij ))  
  = SUM<sub>[i = 1 → n]</sub>( i + 2i + 3i + ... + ni )  
  = SUM<sub>[i = 1 → n]</sub>( in² )  
  = n² + 2n² + 3n² + ... + n³  
  = n⁴

- h) SUM<sub>[i = 1 → n]</sub>( 1/i (i+1) ) *<= Ambiguous notation. I'm going to assume the (i+1) is suppsoed to be in the numerator.*  
  = SUM<sub>[i = 1 → n]</sub>( (i + 1)/i )  
  = SUM <sub>[i = 1 → n]</sub>( i/i + 1/i )  
  = SUM<sub>[i = 1 → n]</sub>( 1 + 1/i)  
  = (1 + 1) + (1 + 1/2) + (1 + 1/3) + ... + (1 + 1/n)  
  = n + ln(n)

### 5.

- a) This algorithm computes the the the difference of the maximum and minimum values, or the *range*, of a data set.

- b) Its basic operation is comparing values to the maxval and minval variables.

- c) The basic opperation happens about 2 times the number of values in the set, or 2(n - 1).

- d) The efficiency class is O(n).

- e) The algorithm is already efficient.

### 6. 

- a) The algorithm checks a matric and returns whether it is symmetric.

- b) Its basic operation is comparing A[i,j] to A[j,i].

- c) The basic operation happens n² times

- d) The efficiency class is O(n²)

- e) The algorithm is already efficient.

<br/>

---

## 2.4

### 1.

- c) x(1) = 0, x(2) = 0 + 5 = 5, x(3) = 5 + 5 = 10  
  x(n) = 5n - 5

- e) 

### 3.

- a) S(n) = S(n - 1) + n³  
  S(1) = 1  
  ...  
  S(2) = 1 + 2³, S(3) = (1 + 2³) + 3³
  S(n) = n⁴ - n³


- b) The efficiency of the more straightforward algorithm is O(n), since the basic operation of adding cubes happens n times. The recursive algorithm, by comparison, still has the same basic operation and complexity of O(n), but its efficiency in practice may not be as good due to the small tax recursion has on computers.

### 9.

- a) This algorithm computes the smallest element in an array.

- b) R(1) = A[0]  
  R(n) = R(n - 1)


### 10.
