

## 1.1 Systems of Linear Equations

A ***Linear Equation*** is an equation with *n* variables, each raised to a power of 1. Its result will be a straight line in *n* dimensions.
- Each variable may multiplied by a unique constant, including 0.

What a *linear equation* looks like:
- a<sub>1</sub>X<sub>1</sub> + a<sub>2</sub>X<sub>2</sub> + ... + a<sub>n</sub>X<sub>n</sub> = b

EXamples:
- 4X<sub>1</sub> - 5X<sub>2</sub> + 2 = X<sub>1<sub>
- X<sub>2</sub> = 2(√(6) - X<sub>1</sub> + X<sub>3</sub>)

### Systems

A ***System of Linear Equations*** is a set of different linear equations.

A system of linear equations has either
- *1 solution* (lines intersect exactly once)
- *no solution* (lines never intersect)
- *infinitely many solutions* (the equations represent the same line)

Two linear systems are **equivalent systems** if they have the same solution set.

<br/>

## Matricies

Consider the following system of equations...
> X<sub>1</sub> - 2X<sub>2</sub> + X<sub>3</sub> = 0  
> 2X<sub>2</sub> + X<sub>3</sub> = 8  
> -4X<sub>1</sub> + 5X<sub>2</sub> + 9X<sub>3</sub> = -9

It's coefficient matrix would be:
> | | | |
> |-|-|-|
> | 1 | -2 | 1 |
> | 0 | 2 | -8 |
> | -4 | 5 | 9 |

...while it's full, augmented matrix would be:
> | | | | | |
> |-|-|-|-|-|
> | 1 | -2 | 1 | │ | 0 |
> | 0 | 2 | -8 | │ | 8 |
> | -4 | 5 | 9 | │ | -9 |

<br/>

### Operations

There are three ***Elementary Row Operations***
1. **Replacement**: add one row to a multiple of another row
2. **Interchange**: Interchange (swap) two rows
3. **Scaling**: Multiply all entries in a row by a *nonzero* constant

***Reducing a matrix***
1. Make the first entry in the first row nonzero (if possible) by interchanging rows if necessary. You can also make the entry 1 by scaling the row.
2. Use the first entry of the first row to "clear" all of the entries below it in the 1st collumn  
...   
I know what he's saying, but the wording is a little odd. I'll come back to this.



Two matricies are **row equivalent** if one may be transforemed into the other using a sequence of elementary row operations
- If two linear ystems are row equivalent, then they have the same solution set.

...

### Consistent and Dependent Systems
- A system is **consistent** if it has *at least* one solution.
  - If a consistent system has *exactly one* solution, then it is **independent**.
  - If a consistent system has *infinite* solutions, then it is **dependent**.
- A system is **inconsistent** if there is *no* solution.
