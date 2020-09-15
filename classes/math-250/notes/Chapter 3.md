<!--
Special symbols: x̄ ⋅ ᵢ
-->
<style>
.over {
   text-decoration:overline;
}
</style>


# Chapter 3 - Descriptive Measures

## 3.1 Measures of Center
There are various way to represent the "center" of a data set, depending on application. Here are some of the most common.

***Median***
1. Arrange the data in *ascending order*
2. If the number of observations is *odd*, then the median is the observation *exactly in the middle* of the ordered list  
   If the number of observations is *even*, then the median is the mean of the two middle values in the data set

***Mode***
1. Find the *frequency* of each value in the data set
2. If no values occur more than once, then the data set has *no mode*.  
   Else, any value that occurs with the *greatest frequency* is a mode of the data set.

***Mean***

### Relation between "center" and skew

*put Figure 3.1 here*

<br/>

## 3.2 Measures of  Variation


### Standard Deviation

*You gotta go back and fill in these gaps*

### Sample Standard Deviation
For a variable, X, the standard deviation of the observations for a sample is called a **sample standard deviation**. It is denotes *s<sub>x</sub>* or, when no confuion will arise, simply *s*. We have...
> &nbsp; &nbsp; &nbsp; &nbsp; / <span class="over"> &nbsp;sum( x<sub>i</sub> - x̄ )<sup>2</sup></span>  
>s = / &nbsp; --------------  
> &nbsp; &nbsp; √ &nbsp; &nbsp; &nbsp; &nbsp; n - 1

You're missing some formulas for this seciton

<br/>

## Chebyshev's Rule and the Empirical Rule

### Chebyshev's Rule
For any quantitiative date set and any real number *k* >= 1, at least 1 - 1/k<sup>2</sup> of the observations like within *k* standard deviations to either side of the mean, that is, between x̄ - k ⋅ s and x̄ + k ⋅ s

### Empirical Rule
For any quantitative data set with roughly a bell-shaped distribution, the following properties hold:
1. Approximately ***68%*** of the observations lie within *one* standard deviation to either side of the mean.
   - i.e. between x̄ - s and x̄ + s
2. Approximately ***95%*** of the observations lie within *two* standard devations to either side of the mean
3. Approximately ***99.7%*** of the observations lie within *three* standard deviations to either side of the mean

Emphasis on *roughly*

...


### Quartiles
- Q<sub>1</sub> is the median of the bottom half of the data set
- Q<sub>2</sub> is the median of the *entire* data set
- Q<sub>3</sub> is the median of the top half of the data set

***Procedure***
1. Arrange the data in increasing order
2. Find the median of the entire dataset. This becomes Q<sub>2</sub>
3. Divided the (ordered) dataset into two halves - bottom and top
4. If the number of observations is odd, include the median in *both* halves

Note: If the number of obersvations is odd, then the total median, aka Q<sub>2</sub>, is used to find Q<sub>1</sub> and Q<sub>3</sub>.

### Lower and Upper Limits
The ***lower limit*** and ***upper limit*** of a dataset are:
- lower limit =- Q<sub>1</sub> - 1.5 ⋅ IQR
- upper limit =- Q<sub>3</sub> + 1.5 ⋅ IQR

In data analysis, the identification of **outliers** - observations that fall well outside the overall pattern of the data - is important

Observations taht lie below the lower limit or above the upper limit are **potential outliers**

*Go back and rewatch 09/15 lecture.*
- Test on Tuesday, 09/22
  - No class
  - Test on Pearson; make sure you log in on that day to submit
- Latest homework due Thursday, 09/17