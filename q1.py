#The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34

no1=0
no2=1
value=1
while (value<=34):
    print(value)
    value=no1+no2
    no1=no2
    no2=value
    
    

