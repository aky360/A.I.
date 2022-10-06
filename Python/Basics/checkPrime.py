import math

class Prime:
    def findPrime(self, num: int) -> bool:
        for i in range(2, (int)(math.sqrt(num))+1):
            if(num%i == 0):
                return False
        return True
        
        
sol = Prime()
if __name__ == "__main__":
    print(sol.findPrime(55))
