'''for symbol in "Internshala":
    print(symbol)
    
    output
    I
    n
    t
    e
    r
    n
    s
    h
    a
    l
    a
'''
    
#calculate factorial

num=int(input("enter a number: "))
fact=1
for x in range(1,num+1):
    fact=fact*x
print("the factorial of {} is {}".format(num,fact))
