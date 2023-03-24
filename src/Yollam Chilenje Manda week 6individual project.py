# Initialize variables
initial_stock = 0
num_months = 0
planned_sales = []
production_quantities = []

# Get initial stock level from user
initial_stock = int(input("Please enter an initial stock level: "))

# Get number of months to plan from user
num_months = int(input("Please enter the number of months to plan: "))

# Get planned sales quantity for each month from user
for i in range(num_months):
  planned_sales.append(int(input(f"Please enter the planned sales quantity for month {i + 1}: ")))

# Calculate production quantities using zero-stock level strategy
stock_level = initial_stock
for i in range(num_months):
  if planned_sales[i] > stock_level:
    production_quantities.append(planned_sales[i] - stock_level)
    stock_level = 0
  else:
    production_quantities.append(0)
    stock_level = stock_level - planned_sales[i]

# Print production quantities
for i in range(num_months):
  print(f"Production quantity month {i + 1} - {production_quantities[i]}")
