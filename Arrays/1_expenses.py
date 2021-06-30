# expenses List:
#     1. January - 2200
#     2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
    
exp = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compared to Jan
print("In Feb this much extra was spent compared to Jan:", exp[1] - exp[0])

# 2. Find out your total expense in the first quarter?
print("Expense for first quarter:", exp[0]+exp[1]+exp[2])

# 3. Find out if you spent exactly 2000 dollars in any month?
print("Did I spent 2000$ in any month?", 2000 in exp)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("Expenses at the end of June: ", exp)

exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:", exp)