def input_vector(size):
    vector = []
    for i in range(1,size+1):
        hlutur = float(input("Element no {}: ".format(i)))
        vector.append(hlutur)
    return vector

def dot_product(vector1, vector2):
    sum1 = 0
    for i in range(0,len(vector1)):
        sum1 += vector1[i] * vector2[i] 
    return sum1

size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))