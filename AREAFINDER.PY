print('THIS PROGRANM IS TO FIND THE AREA OF A TRIANGLE')
a = int(input("EHTER THE LENGTH OF FIRST SIDE : "))
b = int(input("EHTER THE LENGTH OF SECOND SIDE : "))
c = int(input("EHTER THE LENGTH OF THIRD SIDE : "))
#semi_perimeter
s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("THE AREA OF THE TRIANGLE WITH GIVEN DIMENSIONS IS",area)