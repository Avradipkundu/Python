pet=input("Enter pet name:")
year=int(input("Enter a year:"))

if (pet=="dog") and (year <2):
    print("Puppy food")
elif (pet=="cat") and (year>5):
    print("Senior cat food")
else:
    print("adult food")
