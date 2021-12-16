
# The function to find the super digit taking number as the string and n as the k times the string will be concatenated
def super(number,n):
    # initializing the sum to 0
    sum=0
    # making the number a string and then concatenating it n times
    n=str(number)*n
    # a for loop to make the sum of the numbers in the string concatenated
    for i in n:
        # updating the sum
        sum+=int(i)
    # an if statement to ensure that the process stops when the sum is one digit
    if sum>=10:
        # printing the superdigits to easily track the process
        print("Super digit ("+str(sum)+")")
        # a recursion calling again the function with the sum as the number and also no need of concatenating it
        return super(sum,1)
    # Else statement to print the last sum of one digit
    else:
        return print(sum)
# capture the number they want a superdigit for
n=int(input("Enter the number you want a super digit for-[n]-: "))
# capture number of times it should be concatenated
k=int(input("How many times should it be repeated?-[k]-: "))
# an if statement to ensure the constraints given
if 1 <= n < 10100000 and 1 <= k <= 105:
    super(n,k)
else:
    print("Out of our constraints")