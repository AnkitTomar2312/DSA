print("Welcome to the tip calculator")
totalBill=float(input("Enter the Total Bill: $"))
tipPercentage=float(input("Enter the percentage of tip: eg..12,15 18"))
NumPeople=float(input("Enter the number of people to share the bill: "))
percentageNum=totalBill*(tipPercentage/100)
newTotalBill=percentageNum+totalBill

perHead=round(newTotalBill//NumPeople,2)
print(perHead)