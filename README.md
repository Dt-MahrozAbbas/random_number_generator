# random_number_generator
A Python class for generating random even, odd, prime, and composite numbers within a specified range.

## Features
The `randomgenerate` class provides the following methods:

- **`even(n1=1, n2=100000)`** - Generates a random even integer within the range `[n1, n2]`.
- **`odd(n1=1, n2=100000)`** - Generates a random odd integer within the range `[n1, n2]`.
- **`prime(n1=1, n2=100000)`** - Generates a random prime integer within the range `[n1, n2]`.
- **`composite(n1=1, n2=100000)`** - Generates a random composite integer within the range `[n1, n2]`.

## Usage
Instantiate the `randomgenerate` class to use the static methods directly for generating different types of random numbers.

Example:
```python
from random import randint

r1 = randomgenerate.even()          
r2 = randomgenerate.odd()          
r3 = randomgenerate.prime()          
r4 = randomgenerate.composite()

print('Even:', r1)          
print('Odd:', r2)          
print('Prime:', r3)          
print('Composite:', r4) 
```

## Limitations
1. **Prime Range Restrictions:** If `n1` and `n2` are chosen such that no prime numbers exist within the range (e.g., `(14, 15)`), the `prime()` method will enter an infinite loop. To avoid this, ensure the range includes at least one prime number.
   
2. **Composite Range Restrictions:** Similarly, if the range includes only prime numbers or numbers less than 4 (the smallest composite number), the `composite()` method may loop indefinitely.
   
3. **Random Sampling Range Consistency:** In the `composite()` method, if a composite number is not found, the method currently resamples within a smaller fixed range `(1, 10000)` instead of the provided range.

4. **Large Range Performance:** For large ranges, performance may decrease as the algorithm repeatedly samples until finding a number that meets the required condition (especially for prime and composite generation).

## Improvements
To enhance usability and performance:
- Add validation checks to ensure a suitable range for each method.
- Implement a timeout or maximum attempts to avoid infinite loops in case of unsatisfiable ranges.
- Consider caching prime/composite numbers within common ranges to speed up repeated calls.

