t = (5, 8, 2, 10, 3)

total = 0
highest = t[0]
lowest = t[0]

for num in t:
    total += num
    
    if num > highest:
        highest = num
        
    if num < lowest:
        lowest = num

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)