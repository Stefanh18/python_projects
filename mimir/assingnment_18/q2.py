# x Write a class MyString() such that it has a method that gives the difference between the size of strings when the
# '-' (subtraction) operator is used between 
# the two objects of the class. 
# Additionally, implement a method that returns True if object 1 is greater than object 2 and False otherwise when the (>) 
# (greater than) operator is used. 
# Object 1 is greater than object 2 if the string it stores is longer than the string stored in object 2.


class MyString:
    def __init__(self, obj):
        self.obj1 = len(obj)
        self.obj2 = len(obj)

    def __gt__(self, other):
        if self > other:
            return True
    
    def __sub__(self, other):
        if self > other:
            return len(self) - len(other)
        else:
            pass
def main():
    obj1 = MyString('enbody')
    obj2 = MyString('alireza')
    print(obj1>obj2) == print('False')
    assert str(obj1>obj2) == 'False'


main()