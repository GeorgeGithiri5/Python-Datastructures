max = int(input("Enter max Number: "))

odd_numbers = []

for i in range(max):
    if i%2 == 1:
        odd_numbers.append(i)
        
print("Odd numbers: ", odd_numbers)