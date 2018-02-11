"""Project Euler Problem 5: Find the smallest number divisible by the integers
1, 2, 3, ... , 19, 20

This problem can be solved relatively elegantly without the use of an algorithm
or hardcore computation. The divisors of any number is unique determined by a
number's prime factorization. In particular, let x be the number in quesiton.
We will find the prime factorization of x.

Since x is the least common multiple of 1, 2, 3,..., 19, 20, the only prime
divisors of x must be primes between 1 and 20. These primes are precisely:
2, 3, 5, 7, 11, 13, 17, and 19. Since 5^2 = 25, it follows immediately that:

x = (2^a)(3^b)(5)(7)(11)(13)(17)(19)

is the prime factorizaiton of x. Furthermore, the largest powers of 2 and 3
which lie between 1 and 20 are 2^4=16 and 3^2=9, respectively. Therefore:

x=(2^4)(3^2)(5)(7)(11)(13)(17)(19)

And we are done"""


x=(2**4)*(3**2)*5*7*11*13*17*19

print("The answer is {}".format(x))
