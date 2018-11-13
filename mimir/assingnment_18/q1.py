# Write a class 'Pair' that initializes two values 'v1' and 'v2' to '0' by default.

class Pair:
    def __init__(self, v1 = 0, v2 = 0):
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        return "Value 1: {}, Value 2: {}".format(self.v1, self.v2)

    def __add__(self, other):
        v1 = self.v1 + other.v1
        v2 = self.v2 + other.v2
        return Pair(v1, v2)

# It should print the values in this form: "Value 1: 20, Value 2: 30".

def main():
    a = Pair(20, 30)
    b = Pair()
    c = a + b

    print(c)


main()