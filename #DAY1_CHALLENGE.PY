#HELLO THIS IS CHALLENGE #1 OF #100DAYSOFCODE

city = (input("what is the name of the city you grew up in : \n"))

#THIS IS FOR THOSE WHO DON'T HAVE ANY PETS
bool = input("DO YOU HAVE PETS/n (answer in 'true' or 'false') ")

if ( bool == 'true') :
  pet_name = (input("what is the name of your pet : \n"))
  
  print("the name of your band can be",city + pet_name)
else :
  work = (input("what are you. (for example: drummer, guitarist , etc. ): "))

  print("The name of your band can be",city + work)
