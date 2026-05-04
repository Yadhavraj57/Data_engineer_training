numbers = [12, 45, 7, 89, 23]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print("Smallest =", smallest)