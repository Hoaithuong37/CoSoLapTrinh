x=int(input("yrsOfService = "))
y=int(input("Salary = "))
z=int(input("bonus = "))
if x < 5:
    if y < 500:
        z = 100
    else:
        z = 200
else:
    z = 700
print("Bonus amount: ",z)