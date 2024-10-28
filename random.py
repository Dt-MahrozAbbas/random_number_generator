 # type: ignore
from random import *
class randomgenerate:   
    def __is_prime__(num):
        if num==2:
            return True
        elif num%2==0:
            return False
        else:
            ran=int(num**.5)+1
            for i in range(3,ran,2):
                if num%i==0:
                    return False
        return True  
    staticmethod(__is_prime__)

    def prime(n1=1,n2=100000):
        pr=randint(n1,n2)
        while not (random.__is_prime__(pr)):
            pr=randint(n1,n2)
        return pr  
    
    staticmethod(prime) 

    def composite(n1=1,n2=100000):
        comp=randint(n1,n2)
        while randomgenerate.__is_prime__(comp):
            comp=randint(1,10000)
        return comp
    
    staticmethod(composite)

    def  even(n1=1,n2=100000):
        even=randint(n1,n2)
        while even%2!=0:
            even=randint(n1,n2)
        return even