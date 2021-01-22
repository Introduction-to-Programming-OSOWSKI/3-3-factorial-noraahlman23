def factorial(x):
    
    ans = 1
    
    for i in range(1,x + 1):
        ans = ans * i

    return ans

print (factorial(5))