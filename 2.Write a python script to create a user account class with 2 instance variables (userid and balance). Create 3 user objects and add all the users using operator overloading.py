class UserAccount:
    def __init__(self,userId,balance):
        self.userId = userId
        self.balance = balance

    def __str__(self):
        return f"UserId:{self.userId} and Balance:{self.balance}"
    
    def __add__(self, other):
        
        return self.balance + other.balance
    



list1 = []
N = int(input("Enter the total number of object:"))

for i in range(N) :

    userId:int = int(input("Enter the Id:"))
    balance:int = int(input("Enter the balance:"))

    i : UserAccount = UserAccount(userId, balance)
    list1.append(i)



for i in list1:
    print(i)

sum1=0
for i in list1:
    sum1+=i.balance

print(f"Total sum:{sum1}")