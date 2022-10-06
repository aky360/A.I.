import math

class PrimeInRangeN:
    
    def seiveOfEratoSthenes(self, num: int) -> list:
        isPrime = [True]*(num+1)
        isPrime[0] = False
        isPrime[1] = False
        
        for i in range(2, (int)(math.sqrt(num))+1):
            for j in range(2*i, num+1, i):
                isPrime[j] = False
        
        return isPrime
        
        
        
solution = PrimeInRangeN()

if __name__ == "__main__":
    print(solution.seiveOfEratoSthenes(20))
