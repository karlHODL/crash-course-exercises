age = 10
if age < 4:
    admission_cost = 0  
elif age < 18:
    admission_cost = 25
elif age < 65:
    admission_cost = 20
else:
    admission_cost = 40

print(f"Your admission cost is ${admission_cost}.")