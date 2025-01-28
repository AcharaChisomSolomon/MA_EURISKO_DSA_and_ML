def is_prime(N):
    if N <= 1:
        return False
    
    for i in range(2, (N // 2) + 1):
        if N % i == 0:
            return False
    
    return True