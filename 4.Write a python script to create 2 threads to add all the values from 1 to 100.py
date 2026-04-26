import threading

class Thread:
    def __init__(self):
      self.total = 0
      self.result =0


    def threadOne(self,start,end):
        for i in range(start,end+1):
            self.total+=i

        self.result = self.total
       

    def __add__(self, other):
        
        return self.result+other.result
    
start : int = int(input("Start value:"))
end : int = int(input("End value:"))

obj : Thread = Thread()
obj2: Thread = Thread()


t1 : threading = threading.Thread(target=obj.threadOne,args=(1,50))
t2 : threading = threading.Thread(target=obj2.threadOne,args=(51,100))

t1.start()
t2.start()

t1.join()
t2.join()

print("First Thrade:",obj.result)
print("Second Thrade:",obj2.result)

print("Total sum:",obj+obj2)


print("Program end!!!!")