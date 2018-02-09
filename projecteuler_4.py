"""
Project Euler Problem 4: find the largest palindrome which is expressible
as a product of two 3-digit numbers.

To solve this problem, instead of checking if a palindrome is factors into
a product of two 3-digit numbers. We shall instead check pairs of 3-digit
numbers to see if the number is a Palindrome. To start, we define a function
'palin_check(<int>)' which will check whether the argument <int> is a palindrome.
Next we will define the main function to systematically multiply pairs of
3-digit integers and run paline_check() on the product.
"""

def palin_check(num):
    
    """Turns the input number into a string, sets a sentinel value to 0. The function
    then checks if the i-th element equals the (l-i)-th element, where l is the
    length of the string. If any of such pairs are not equal, the sentinel is set to
    1 and the function returns false. Otherwise, the sentinel remains at 0 and the
    function returns true."""
    x=str(num)
    l=len(x)
    sentinel=0
    for i in range(l):
        if x[i]!=x[(l-1)-i]:
            sentinel=1

    if sentinel==0:
        return True

    else:
        return False




def main():
    n=0
    S=[]
    for i in range(999,100,-1):
        for j in range(999-n,100,-1):
            x=i*j
            if palin_check(x)==True:
                print("{} * {} = {}".format(i,j,x))
                S.append(x)
        n=n+1

    print()
    print("The answer is {}".format(max(S)))


if __name__=='__main__':
    main()
