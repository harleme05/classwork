from typing import List


def get_factors(num: int, prime:bool = False)-> List[int]:
    """
    Docstring for get_factors
    
    Returns a list of factors for the provided num
    
    Args:
        num(int): The number for wich we want to factor
        prime(bool): 
    Return:
        List[int]: The list of factors of the num
    """
    factors = []
    for n in range(1,num+1):
        if num%n==0:
            factors.append(n)
    if prime:
        factors = [
            f for f in factors if len(get_factors(f))==2
            ]
    return factors

def get_prime_factors(num:int)-> List[int]:
    primes = []
    for i in get_factors(num):
        factors = get_factors(i)
        if len(factors)==2:
            primes.append(i)
    return(primes)
    
    
    