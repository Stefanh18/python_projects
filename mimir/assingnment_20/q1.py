def chance_of_input(cost, amount_payed):
    print("A packet of candy costs $ {:.2f}. You have inserted $ {:.2f}.".format(cost,amount_payed))
    print("Please insert coins:")
    print("\t{}".format("n - Nickel"))
    print("\t{}".format("d - Dime"))
    print("\t{}".format("q - Quarter"))
    print("\t{}".format("D - Dollar"))
    return input()               
             
def coin_input(amount):
    if amount == "n":
        amount_payed = 0.05
    elif amount == "d":
        amount_payed = 0.1
    elif amount == "q":
        amount_payed = 0.25
    elif amount == "D":
        amount_payed = 1.0
    else:
        print("'{}' is not a valid coin.".format(amount)) 
        amount_payed = 0
    return amount_payed

def change(amount):
    cost = 1.50
    change = amount - cost
    return print("Enjoy your candies. Your change is $ {:.2f}. Please visit again.".format(change))

def main():
    cost = 1.50
    amount_payed = 0.00
    while cost > amount_payed:
        amount = chance_of_input(cost, amount_payed)
        amount_payed += coin_input(amount)
    change(amount_payed)

main()