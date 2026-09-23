sales = [ 500, 300, 1100, 1300, 6000]

total_sales = 0
high_sales = 0

for sale in sales:
    total_sales += sale
    if sale > 1000:
        high_sales += 1
        print(f"Sale: {sale} - High Sale")
    else:
        print(f"Sale: {sale} - Low Sale")   

print()

print("Total Sales:", total_sales)
print("Number of High sales:", high_sales)