# Cael McCormick
# 09/24/2026
# end of week assignment 5

# Exercise 1

# account_statement.py
customer_name = input("Enter customer name: ")
account_balance = float(input("Enter account balance: "))
account_number = int(input("Enter account number: "))
print(f"Customer: {customer_name} | Account #: {account_number} | Balance: ${account_balance:,.2f}")


# Exercise 2 - email-domain

email_id = input("Please enter your email address: ")

user_name, domain = email_id.split("@")

print("the domain of the given email is ", domain)


# Exercise 3 - Transactions

with open("transactions.txt", "r") as file:
    
    for line in file: 
        customer,amount = line.strip().split(",")
        amount = float(amount)
        
        print(f" Customer: | {customer} | Amount Due : ${amount:,2f}")

# Exercise 4
# sales_report.py

while True:
    sale = input("Enter sale amount (or 'done' to finish): ")
    if sale.lower() == "done":
        break

with open("sales_report.txt", "a") as file:
    file.write(sale + "\n")

print("Sales report saved.")

# Exercise 5

sale = input("Enter a sales amount (or type 'done' to finish): ")

while sale.lower() != "done":
    
    with open("sales_report.txt", "a") as file:
        file.write(f"{float(sale):.2f}\n")

sale = input("Enter a sales amount (or type 'done' to finish): ")

print("Sales entry complete. Values saved to sales_report.txt")





