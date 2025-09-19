# Write your code here
bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80
income = sum([bubblegum, toffee, ice_cream, milk_chocolate, doughnut, pancake])

print(f"""Earned amount:
Bubblegum: ${bubblegum}
Toffee: ${toffee}
Ice cream: ${ice_cream}
Milk chocolate: ${milk_chocolate}
Doughnut: ${doughnut}
Pancake: ${pancake}

Income: ${income}
""")
staff_expenses = int(input("Staff expenses:"))
other_expenses = int(input("Other expenses:"))
print(f"Net income: ${income - staff_expenses - other_expenses}")