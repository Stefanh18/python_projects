# The Sales class goes here
def read_data_from_file(filename):
    file_1 = open(filename,'r')           
    data = []
    for line in file_1:
        data.append(float(line.strip())) 
    return data        
class Sales():   
    def __init__(self, data):
        self.__data = data    
    def get_average(self):
        return sum(self.__data) / len(self.__data)
    def add_sale(self,sale_2):
        self.__data.append(sale_2)
# The main program starts here
def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()