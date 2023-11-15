print("Hello, welcome to the Copington Adventure Theme Park")

print("child = £12.00")
print("adult = £20.00")
print("senior_citizen = £11.00")

adult_ticket = int(input("how many adult tickets are required?"))
child_ticket = int(input("how many child tickets are required?"))
citizen_ticket = int(input("how many senior citizen tickets are required?"))
wristband = int(input("how many of the visitors would like wristbands for the rides?"))
lead_booker_surname = input("may I please have the lead booker's surname?")
parking_pass = input("do you require a parking pass for the park?")
total = 0.00
total += adult_ticket * 20
total += child_ticket * 12
total += citizen_ticket * 11
total += wristband * 20
payment = 0
balance = total
while balance > 0:
    print("what would you like to pay")
    print("press 1 for £10 and 2 for £20")
    notes = input
    if notes == "1":
        balance -= 10
    elif notes == "2":
        balance -= 20




    
