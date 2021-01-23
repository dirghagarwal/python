print("Hello and Welcome to  the TIP CALCULATOR ")
#ENTER THE TOTAL AMOUNT OF THE BILL
totalbill = int(input("what is the total amount of bill?\n"))
#ENTER THE TOTAL NUMBER OF PERSONS THAT WILL SPLIT UP THE BILL.
people = int(input("how many poeple will split the bill?\n"))
#ENTER WHETHER YOU WOULD LIKE TOO GIVE A TIP OR NOT
QUESTION = input("WOULD YOU LIKE TO GIVE A TIP?(answer in 'y' or 'n')\n")

if (QUESTION=='y'):
  tip = int(input("how much tip would you like too give?\n"))

  if (QUESTION=='y'):
    print(f"Each Person Will Have To Pay {round((totalbill+tip)/people,2)}")
else : 
  print(f"Each Person Will Have To Pay {round((totalbill/people),2)}")

