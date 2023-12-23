num = int(input("enter your number : "))

prime =True

for i in range(2,num):
        if(num%i == 0):
             
             prime = False
             break
if prime:
       print("it is prime num")
else:
       print("it is not prime num")