numbers = [12, 45, 7, 89, 23]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest =", largest)