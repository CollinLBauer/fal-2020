### Binomial probability
- the chance that, given *n* trials with each having the probability *p* of success, *x* of those trials will be successful
- formula: <sub>n</sub>C<sub>x</sub> * p<sup>x</sup> * (1 - p)<sup>n-x</sup>
  - recall the combination formula: nCx = n!/(x!(n - x)!)
- This formula gives you the probability of EXACTLY x successes.
  - For less than, greater than, etc., calculate this value for every possible outcome and sum them together

### Example
- What is the chance of flipping a coin 10 times and getting a head at exactly 6 times?
  - n = 10 flips
  - x = 6 heads
  - p = 50%, or 1/2
- <sub>n</sub>C<sub>x</sub> * p<sup>x</sup> * (1 - p)<sup>n-x</sup>