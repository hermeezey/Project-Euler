# projecteuler_2.py
#   Sum all the even fibonacci numbers less than 4,000,000


# We begin by constructing a function to compute all fibonacci numbers less
# than N for any given N and place them in a list. We shall use this as a
# chance to practice the principle of modular design.


def fibonacci_gen(n):
    a=1
    b=1
    S=[a]
    count=0                 # add loop counter for testing
    while b<n and count<n:
        S.append(b)
        a,b=b,a+b
        count=count+1

    return S


# Now, call the 'fibonacci_gen()' function in 'main()' and check each of the
# items in the outlist for parity:


def main():
    answer=0
    n=int(input("Please enter the upperbound: "))
    print('\n')
    fib_set=fibonacci_gen(n)
    for i in fib_set:
        if i%2==0:
            answer=answer+i
    print("The set is: \n")
    print(fib_set)
    print('\n')
    print("The sum is {}".format(answer))

    
if __name__=='__main__':
    main()
        

    
