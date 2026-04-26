import threading
import random
class Thread:
    def __init__(self):
        self.list1:list = []
        self.result=0

    def printOneToHunderd(self):

        for i in range(101):
            value : int = random.randrange(1,101)
            self.list1.append(value)

        self.result = self.list1






obj : Thread = Thread()

t1 : threading = threading.Thread(target=obj.printOneToHunderd)
t2: threading = threading.Thread(target=obj.printOneToHunderd)
t3 : threading = threading.Thread(target=obj.printOneToHunderd)
t4: threading = threading.Thread(target=obj.printOneToHunderd)
t5 : threading = threading.Thread(target=obj.printOneToHunderd)


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print("LIST:",obj.result)

        
