# projecteuler_3.py
#   Find the largest prime factor of 600851475143


# The well-known approach for finding primes is Eratosthenes' number sieve
# Since we are looking for prime factors of a number, there is an added comp
# -putation needed after a prime p is found to check whether p divides the
# number given above.


# Our strategy will be to take the number sieve and augment it find the
# prime factorization of 600851475143. The key insight for us, is that
# we can actually reduce the size of the number after dividing out a prime
# factor.


# First we construct a function to check whether a number is prime. We shall
# use a result from analysis/number theory to make our lives easier:

#   Proposition: If n is composite, then n has a divisor d s.t. d <= sqrt(n)
#
#   proof: Suppose n is composite and write n=ab. Then either a <= sqrt(n) or
#   b <= sqrt(n). Indeed suppose by way of contradiciton that both a and b are
#   greater than sqrt(n). Then:
#
#               n = a*b > sqrt(n)*b > sqrt(n)*sqrt(n) = n, a contradiction.
#   and so we are done.
#
# In particular, the proposition guarantees that if n has no divisors less
# than sqrt(n), then n must in fact be prime.


import math


def prime_verify(p):
    k=int(math.sqrt(p))
    divisors=0
    for i in range(1,k+1):      
        if p%i==0:              
            divisors=divisors+1

    if divisors > 1:
        return False
    else:
        return True


# Next, we use an indefinite loop to repeatedly factor the number in question:


def main(n):
    p=2
    factors=[]
    while n > 1:
        
        if prime_verify(p)==True:
           
            if n%p==0:
                factors.append(p)
                n=n//p              # Note we do not tick up p here because
                                    # we want the algorithm to keep dividing
            else:                   # until all factors of p are gone.
                p=p+1
        else:
            p=p+1                   
            

    print(factors)
    
    return factors


if __name__=='__main__':
    main(600851475143)
        
        

        
    
    
