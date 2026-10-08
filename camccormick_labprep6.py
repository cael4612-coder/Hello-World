# Cael McCormick
# 09/30/2026
# lab-prep assignment week 6


# Exercise 1


# Create three lists for January sales, February sales, and March sales with the following values:
jan_sales = [1250, 2300, 1800, 1950]
feb_sales = [1550, 8900, 2588]
mar_sales = [5000, 4500, 5250, 5690, 4550]
# Print each of the lists and label them
print(f"January sales: {jan_sales} ")
print(f"February sales: {feb_sales} ")
print(f"March sales: {mar_sales} ")
# Append
jan_sales.append(5675)

print(f"January sales (appended): {jan_sales} ")

# Q1

q_one = jan_sales + feb_sales + mar_sales
print(f"Quarter one: {q_one} ")

# Totals

total_sales = sum(q_one)
average_sales = sum(q_one) / len(q_one)
largest_sale = max(q_one)
smallest_sale = min(q_one)

print(f"Total sales: ${total_sales:.2f} ")
print(f"Average sales: ${average_sales:.2f} ")
print(f"Largest sale: ${largest_sale:.2f} ")
print(f"Smallest sale: ${smallest_sale:.2f} ")






