def is_prime(numbers):
    if numbers < 2:
        return False
    for i in range(2,int(numbers**0.5)+1):
        if numbers%i == 0:
            continue
        else:
            return i 
def greater_than_sum_of_primes(numbers,list1):
    for i in range(0,len(list1)):
        x+=list1[i]
    prime_sum =x
    for num in numbers:
        if num > prime_sum :
            print(num)
            return num
        else:
            continue
numbers = input("enter a list of numbers,seprated by space:").split()
numbers = [int(num) for num in numbers]
i=is_prime(numbers)
list1=[]
list1.append(i)
resault = greater_than_sum_of_primes(numbers)
print("numbers greater than the sum of the prime numbers:",resault)
