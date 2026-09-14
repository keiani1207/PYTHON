#Bill & Tip Calculator
TA = float(input("Total Amount Of Bill To Pay = "))
TipAm=int(input("Tip percentage they wanna Give = "))
TipAmount=TA*(TipAm/100)
Splitbill=int(input("Number of people who are splitting bill = "))
FAP = TA+TipAmount
x=FAP/Splitbill
print(f"The Total Amount Should Be Paid is {FAP}. And Each Person Should Pay {x}. Mode Of Payment is Cash or Card Sir??")

#Time Converter
TS=int(input("Enter The Total Number Of Seconds = "))
x=TS//3600
a=TS%3600
y=a//60
b=a%60
print(f"{x} Hours {y} Minutes {b}seconds")