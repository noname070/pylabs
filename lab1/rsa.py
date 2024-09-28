import random
from typing import List, Tuple


# утилка. решето эратосфена - один из самых быстрых способов узнать простое ли число
PRIMES = []
def eratosthenes_sieve(limit: int) -> List[int,]:
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for n in range(2, int(limit **.5) + 1):
        if sieve[n]:
            for m in range(n**2, limit + 1, n):
                sieve[m] = False
    primes = [n for n, is_prime in enumerate(sieve) if is_prime] # все нормально скоупы разрешают
    return primes

def is_prime(n):
    if not PRIMES:
        eratosthenes_sieve((int(n**.5) + 1 ) << 3) # ну вдруг пригодиться
         
    if n < 2:
        return False

    for prime in PRIMES:
        if prime > n**.5: 
            break
        if n % prime == 0:
            return False

    return True

def gcd(a: int, b: int) -> int:
    # ну это база
    while b != 0:
        a, b = b, a % b
    return a

def gcdpp(a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = gcdpp(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def multiplicative_inverse(e: int, phi: int) -> int:
    # for d in range(1, phi): # поифг на расширенный алгоритм, переборчиком найдем
    #     if (e * d) % phi == 1:
    #         return d
    
    # вот тут я понял что чиселки 12+ знаков не очень прикольно перебирать
    gcd, x, _ = gcdpp(e, phi)
    if gcd != 1:
        return -1 # не существует.
    return x % phi


def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # n:int = (p)(q) А МНЕ ГОВОРИЛИ ЧТО ТАК МОЖНО, А Я ИМ ГОВОРИЛ НА ПРОШЛОЙ ПАРЕ ЧТО БУДЕТ INT OBJ NOT CALLABLE. 
    n: int = p*q
    # PUT YOUR CODE HERE

    phi: int = (p-1)*(q-1)
    # PUT YOUR CODE HERE

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


if __name__ == "__main__":
    print(generate_keypair(234234, 45634223)) # -> ну оно чуть чуть подумает и выдаст `((2905262148217, 10689086590182), (1411982437873, 10689086590182))` можно сравнить с уже готовым алгоритмом но мне за это балы не дают 🤡🤗😼