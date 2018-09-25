def amount():
    while True:
        amount1 = input("Enter number of shares: ")
        try:
            int(amount1)
            break
        except:
            print("Invalid number!")
            continue
    return amount1

def price():
    while True:
        price = input("Enter price (dollars, numerator, denominator): ")
        new_price = price.replace(" ", "")
        denominator = new_price[-1]
        numerator = new_price[-2]
        dollars = new_price[:-2]
        try:
            int(new_price)
            break
        except:
            print("Invalid price!")
            continue
    worth = int(dollars) + (int(numerator)/int(denominator))
    worth_str = dollars + " " + numerator + "/" + denominator
    return worth,worth_str

def allstock(worth,amount1):
    finalprice =  int(amount1) * worth
    return finalprice

def afram():
    yes_no = input("Continue: ")
    if yes_no == "y":
        return True
    else:
        return False
        
afram2 = True
while afram2 == True:
    amount1 = amount()
    worth, worth_str = price() 
    finalprice = allstock(worth, amount1)
    print("{} shares with market price {} have value ${:0.2f}".format(amount1, worth_str, finalprice))
    afram2 = afram()