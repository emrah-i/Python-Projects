print("Welcome to Emrah's Tip Calculator")

total = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? "))
split = int(input("How many people will split the bill? "))
each_person = total * (1 + (tip / 100)) / split

# print(type(each_person))

print(f"{each_person:.2f}")