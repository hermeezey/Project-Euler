# projecteuler_1.py
#   Sum all the multiples of 3 and the multiples of 5 which are less than 1000


# We begin by finding all the multiples of 3 and 5. To do this, we construct
# function which stores the multiples of 3 in a list and the multiples of 5
# in a list.


def main():
    mult3=[]
    x=1
    while x<1000:
        if x%3==0:
            mult3.append(x)
           
        x=x+1
        
    mult5=[]
    y=1
    while y<1000:
        if y%5==0:
            mult5.append(y)

        y=y+1

    mult_total=mult3+mult5

    answer=0
    for num in mult_total:
        answer=answer+num

    print("The answer is {}".format(answer))


if __name__=='__main__':
    main()
        
           
