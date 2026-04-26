
# CASE 1: Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in a class using method overloading.

class Multiple:
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result
    
obj : Multiple = Multiple()

print("Multiplying 2 numbers: ", obj.multiply(2, 3))
print("Multiplying 3 numbers: ", obj.multiply(2, 3, 4))
print("Multiplying 4 numbers: ", obj.multiply(2, 3, 4, 5))




# CASE 2: Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in a class using method overloading.

class Multiple:
    def __init__(self,no1,no2,no3=None,no4=None):
        self.no1 = no1
        self.no2 = no2
        self.no3 = no3
        self.no4 = no4

    def multiply(self):

        if self.no3 == None and self.no4 ==None:
            return self.no1 * self.no2
        elif self.no4 == None:
            return self.no1 * self.no2 *self.no3
        else:
            return self.no1 * self.no2 *self.no3 *self.no4
        

obj1 : Multiple = Multiple(2, 3)
obj2 : Multiple = Multiple(2, 3, 4)
obj3 : Multiple = Multiple(2, 3, 4, 5)

print("Multiplying 2 numbers: ", obj1.multiply())
print("Multiplying 3 numbers: ", obj2.multiply())
print("Multiplying 4 numbers: ", obj3.multiply())


