def power(p, n):
    if n == 0:         
        return 1
    else:
        return p * power(p, n - 1)   

p = float(input("Enter principal growth factor (p): "))
n = int(input("Enter number of years (n): "))

result = power(p, n)
print("Result (p^n) =", result)
