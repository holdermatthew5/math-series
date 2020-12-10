Author: Matthew Holder

Version: 0.1.0

Last PR: https://github.com/holdermatthew5/math-series/pull/1#issue-535680498

Problem Domain:
- Create a method that takes in a number (n) and returns the nth number in the Fibonacci sequence.
- Create a method that takes in a number (n) and returns the nth number of the lucas numbers.
- Create a method that takes in one mandatory number (n) and 2 optional numbers (x and y). The method should return the nth number in the fibonacci sequence where the sequence starts with numbers x and y. If x and y are not entered as arguments use 0 and 1 to take their place.

Description:
- Fibonacci:
  - Purpose: This function takes in a single number(n) of any size and returns the nth value from the Fibonacci sequence.
  - Use: To use the Fibonacci method paste `from math_series.series import fibonacci` in the file intended to use it. Then call `fibonacci()` passing in a single number of any size as an argument.
- Lucas:
  - Purpose: This function takes in a single number(n) of any size and returns the nth value from the lucas numbers (not to be confused with lucas primes).
  - Use: To use the Lucas method paste `from math_series.series import lucas` in the file intended to use it. Then call `lucas()` passing in a single number of any size as an argument.
- Sum Series:
  - Purpose: This function takes one mandatory(n) and 2 optional numbers(x, y). If x and y are not provided, the nth value from the Fibonacci sequence is returned. If both optional arguments are provided, the nth value wil be returned using the Fibonacci algorithm starting with x and y instead of 0 and 1.
  - Use: To use Sum Series method paste `from math_series.series import sum_series` in the file intended to use it. Then call `sum_series(n, x, y)` passing in n at a minimum in place of 'n' (order matters). If you do not wish to pass in x and y simply call `sum_series(n)`.
