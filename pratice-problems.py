TA = float(input("Total Amount Of Bill To Pay = "))
TipAmount=int(input("Tip percentage they wanna Give = "))
Splitbill=int(input("Number of people who are splitting bill = "))
FAP = TA+TipAmount
x=FAP/Splitbill
print(f"The Total Amount Should Be Paid is {FAP}. And Each Person Should Pay {x}. Mode Of Payment is Cash or Card Sir??")