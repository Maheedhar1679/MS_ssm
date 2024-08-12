monthly_budget = 15000

rent = 8000
utilities = 1500
groceries = 2000
transportation = 1000
miscellaneous = 500

total_expenses = rent + utilities + groceries + transportation + miscellaneous

remaining_budget = monthly_budget - total_expenses

print("Monthly Budget: ", monthly_budget)
print("Total Expenses: ", total_expenses)
print("Remaining Budget: ", remaining_budget)

percentage_used = (total_expenses / monthly_budget) * 100
print(percentage_used)