print("THIS PROGRAM IS TO FIND IF A NUMBER IS A PRIME NUMBR OR NOT")
num = int(input("Enter a number: "))  
prime = true
for i in range (2,num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print(num + " is a prime number")
else :
    print(num + " is not a prime number")