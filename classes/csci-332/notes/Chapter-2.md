# Pothering's Chapter 2 - Relational Algebra and Tuple Calculus
### Book chapters covered:
- 4:
- 5: Relational Algebra and Relational Calculus
- ?

### Lectures included:
- 09/03
- 09/08
- 09/15

---

<br/>

# Chapter 5: Relational Algebra and Relational Calculus

This chapter makes heavy use of the [model database](./Staff%20Model%20Database.md). Refer back to it when reading.

<br/>

## Unary Operations

### Projection ( Π )
The **projection** operation works on a single relation R and defines a relation that contains a vertical subset of R, extracting the values of specified attributess and eliminating duplicates
- Format: Π<sub>a1,....,an</sub>(R)

***Example***: Produce a list of salaries for all staff, showing only the `staffNo`, `fName`, `IName`, and `salary` details.
- Π<sub>staffNo,fName,IName,salary</sub>(Staff)


>| staffNo | fName | IName | salary |
>|-|-|-|-|
>| SL21 | John | White | 30000 |
>| SG37 | Ann | Beech | 12000 |
>| SG14 | David | Ford | 18000 |
>| SA9 | Mary | Howe | 9000 |
>| SG5 | Susan | Brand | 24000 |
>| SL41 | Julie | Lee | 9000 |

<br/>

### Selection
The **selection** operation works on a single relation R and defines a relation that contains only those tuples of R that satisfy the specified condition (*predicate*).
- Format: σ<sub>predicate</sub>(R)

***Example***: List all staff with a salary greater than $10,000
- σ<sub>salary > 10000</sub>(Staff)

>| staffNo | fName | IName | position | sex | DOB | salary | branchNo|
>|-|-|-|-|-|-|-|-|
>| SL21 | John | White | Manager | M | 1-Oct-45 | 30000 | B005 |
>| SG37 | Ann | Beech | Assistant | F | 10-Nov-60 | 12000 | B003 |
>| SG14 | David | Ford | Supervisor | M | 24-Mar-58 | 18000 | B003 |
>| SG5 | Susan | Brand | Manager | F | 3-Jun-40 | 24000 | B003 |

<br/>

## Set Operations

Set operations are binary operations, meaning they operate between two tables. To use set operations, the relations need to be **union-compatible**. Two relations are union-compatible if they...
- have the same number of attributes
- each pair of attributes has the same domain

Often times, set operations need to be used on relations which are not union-compatible. Projections may be used to extract union-compatible data.


### Union ( ∪ )

### Intersection ( ∩ )

### Difference ( - )

### Catesian Product ( X )

<br/>

## Join operations

### Theta join ( R |x|<sub>f</sub> S)

Note that Theta join may be rewritten as a Selection of a Cartesian product.
- R |x|<sub>F</sub> S = σ<sub>F</sub>(R X S)

### Equijoin

### Natural join ( R |x| S)