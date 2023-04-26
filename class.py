from math import factorial

print("****QUESTION 1****")
n = int(input("Enter a number:"))
x = int(input("Enter a number: "))

result = sum([n ** i / factorial(i) for i in range(x + 1)])
print(result)

print()
print("****QUESTION 2****")
def calculate_sum(n):

    global x
    if n == 1:
        x = 1.0
        return x
    else:
        x = (-1) ** (n + 1) / n + calculate_sum(n - 1)
        return x


n = int(input("Enter a number: "))
calculate_sum(n)
print(x)

