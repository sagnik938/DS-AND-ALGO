def sieve_gen(num):
    arr = [True for i in range(num+1)]
    arr[0] = arr[1] = False
    p = 2
    while(p*p<=num):
        if(arr[p] == True):
            for i in range(p*p,num+1,p):
                arr[i] = False
        p+=1
    return(arr)

num = int(input("Enter Limit Number"))
sieve=sieve_gen(num)
primes = [ i for i in range(num+1) if sieve[i]]
print(primes)