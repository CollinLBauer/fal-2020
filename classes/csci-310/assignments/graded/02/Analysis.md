omfg I'm an idiot on some of these

---

## 3.1

---

## 3.2

### 2.
- a) You worded this differently, but I belive this was more or less correct.
- b) You were on the right track, but the answer was not sufficient.
  - Tip: You can use the properties of modulo (look it up) to find the answer
  - Distributive property: ab mod n = [(a mod n)(b mod n)] mod n.
  - ergo: a<sup>i</sup> mod m = ((a<sup>i-1</sup> mod m) * (a mod m)) mod m, for all i = 0, 1, 2, ... 



### 8.
A *proper* insertion sort does not swap every time. Instead, it remembers what the lowest value is (and the index of that value), and if it is lower than th the current index, swaps those two.
- Note that you did not have to write out the comparisons, just the swaps. Regardless, here's the corrected answer.

> 0. Start with original list {E, X, A, M, P, L, E}
> 1. Set minimum index to 0
> 2. Compare E to X. E comes first
> 3. Compare E to A. A comes first (swap index = 2)
> 4. Compare A to M. A comes first
> 5. Compare A to P. A comes first
> 6. Compare A to L. A comes first
> 7. Compare A to E. A comes first
> 8. Swap E and A. Set minimum index to 1  
>    {A| X, E, M, P, L, E}  
> 9. Compare X to E. E comes first (swap index = 2)
> 10. Compare E to M. E comes first
> 11. Compare E to P. E comes first
> 12. Compare E to L. E comes first
> 13. Compare E to E. Values are equal
> 14. Swap X and E. Set minimum index to 2  
>     {A, E| X, M, P, L, E}
> 15. Compare X to M. M comes first (swap index = 3)
> 16. Compare M to P. M comes first
> 17. Compare M to L. L comes first (swap index = 5}
> 18. Compare L to E. E comes first (swap index = 6)
> 19. Swap X and E. Set minimum index to 3  
>     {A, E, E| M, P, L, X}
> 20. Compare M to P. M comes first
> 21. Compare M to L. L comes first (swap index = 5)
> 22. Comapre L to X. L comes first
> 23. Swap M and L. Set minimum index to 4  
>     {A, E, E, L| P, M, X}
> 24. Compare P to M. M comes first (swap index = 5)
> 25. Compare M to X. M comes first
> 26. Swap P and M. Set minimum index to 5
>     {A, E, E, L, M| P, X}
> 27. Compare P to X. P comes first
>
> Done.

### 9.
No. Selection sort is *not* stable.
- It may end up swapping two unique but equivalent values to different positions, although only indirectly. 