#Write a Python program to count the number of even and odd numbers from a series of numbers.
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
#Expected Output :
#Number of even numbers : 4
#Number of odd numbers : 5


no=(1,2,3,4,5,6,7,8,9)
print("given input numbers : ",no)
even_count=0
odd_count=0
for i in range(len(no)):
    if no[i]%2==0:
        even_count+=1
    elif no[i]%2!=0:
        odd_count+=1
print("number of even numbers  ",even_count)
print("number of odd numbers  ",odd_count)




        




