print("Enter Marks Obtained in 3 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())

tot = markOne+markTwo+markThree
avg = tot/3

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif  avg<41:
    print("Your Grade is D")

else:
    print("Invalid Input!")