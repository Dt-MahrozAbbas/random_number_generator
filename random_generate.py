 # type: ignore
from random import randint
class randomgenerate:   
    @staticmethod
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

    def prime(n1=1,n2=100000):
        pr=randint(n1,n2)
        flag=randomgenerate.__is_prime__(pr)
        check_li={pr}
        while not flag:
            pr=randint(n1,n2)
            flag=randomgenerate.__is_prime__(pr)
            check_li.add(pr)
            if len(check_li)==abs(n2-n1)+1:
                return "not exist in this range"    
        return pr  
    
    staticmethod(prime) 

    def composite(n1=1,n2=100000):
        comp=randint(n1,n2)
        while randomgenerate.__is_prime__(comp):
            comp=randint(1,10000)
        return comp
    
    staticmethod(composite)

    @staticmethod
    def  even(n1=1,n2=100000):
        even=randint(n1,n2)
        while even%2!=0:
            even=randint(n1,n2)
        return even
    
    @staticmethod
    def odd(n1=1,n2=10000):
        od=randint(n1,n2)
        while od%2==0:
            od =randint(n1,n2) 
        return(od)



r1=randomgenerate.even()          
r2=randomgenerate.odd()          
r3=randomgenerate.prime(24,28)          
r4=randomgenerate.composite()
print('even',r1)          
print('odd',r2)          
print('prime',r3)          
print('comp',r4)  
