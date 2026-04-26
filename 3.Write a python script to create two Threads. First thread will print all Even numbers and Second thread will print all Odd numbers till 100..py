import threading

class Threading:
    def __init__(self,n):
        self.n = n

    def printEvenNo(self):

        for i in range(0,self.n+1,2):
            print(i,end=" ")
        print()

    def printOddNo(self):

        for i in range(1,self.n+1,2):
            print(i,end=" ")
        print()


        
n:int = int(input("Enter the value of N:"))
obj : Threading = Threading(n)


T1 : threading = threading.Thread(target=obj.printEvenNo)
T2 : threading = threading.Thread(target=obj.printOddNo)

T1.start()
T2.start()

T1.join()
T2.join()

print("Execution finished!!!!")