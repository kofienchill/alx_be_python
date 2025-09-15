monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)
print(f"Your monthly savings are ${monthly_savings}")
print(f"Your projected annual savings with 5% interest is ${projected_savings}")