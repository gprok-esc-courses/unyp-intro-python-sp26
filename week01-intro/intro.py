
balance = 400

amount = input("Type amount to withdraw: ")
amount = int(amount)

print(amount)

if balance >= amount:
    balance = balance - amount
    print("Transaction completed")
else:
    print("Insufficient balance")

print(balance)