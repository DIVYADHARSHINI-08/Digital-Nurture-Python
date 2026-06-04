def split(bill_amount , people):
    if people<=0:
        print("Number of people must be greater than zero.")
    else:
        amount = bill_amount/people
        print(f"Each person should pay:{amount}")

bill_amount = 1250
people = 4
split(bill_amount,people)