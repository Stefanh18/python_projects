loan = float(input("Input the cost of the item in $: "))
loan2 = loan
monthly_payment = 50.0
over_thousand_interest = 0.02
under_thousand_interest = 0.015
months = 0
sum_of_interest = 0

while loan > 0.0 and loan < 2500:
    if loan2 > 1000.0:
        decreased_loan = loan - monthly_payment + (over_thousand_interest * loan) 
        interest = loan * over_thousand_interest
        loan = decreased_loan
        months += 1
        sum_of_interest += interest
        if decreased_loan < 0:
            monthly_payment += round(decreased_loan, 2)
            decreased_loan = 0.0
        print("Month:", months, "Payment:", round(monthly_payment, 2), "Interest paid:", round(interest, 2), "Remaining debt:", round(decreased_loan, 2))
    else:
        decreased_loan = loan - monthly_payment + (under_thousand_interest * loan)
        interest = loan * under_thousand_interest
        loan = decreased_loan
        months += 1
        sum_of_interest += interest
        if decreased_loan < 0:
            monthly_payment += round(decreased_loan, 2)
            decreased_loan = 0.0
        
        print("Month:", months, "Payment:", monthly_payment, "Interest paid:", round(interest, 2), "Remaining debt:", round(decreased_loan, 2))

print()
print("Number of months:", months)
print("Total interest paid:", round(sum_of_interest, 2))