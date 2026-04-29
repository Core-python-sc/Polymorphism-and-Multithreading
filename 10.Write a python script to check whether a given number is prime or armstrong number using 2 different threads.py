import threading

def primeNo(no:int):
    i:int = 1
    flag:int = 0
    while i<=no:
        if no%i == 0:
            flag+=1
        i+=1
    if flag == 2:
        print(f"{no} is prime number.")
    else:
         print(f"{no} is not prime number.")
            



def amstrong(no2:int):
    no3:int = no2
    sum:int =0
    while no3!=0:
        rem:int = no3%10
        sum:int = sum+(rem**3)
        no3:int = no3//10

    if sum == no2:
        print(f"{no2} is amstrong number.")
    else:
        print(f"{no2} is not amstrong number.")




t1 = threading.Thread(target=primeNo, args=(5,))
t2 = threading.Thread(target=amstrong, args=(153,))

t1.start()
t2.start()

t1.join()
t2.join()

print("The execution end!!!!!")