account_balance = 0.0
def deposit(x):
     global account_balance
     if x > 0:
        account_balance += x
        print(f"Deposited: ${x:.2f}")
     else:
        print("Deposit amount must be positive.")


def withdraw(y):
    global account_balance
    if y > 0:
        if y <= account_balance:
            account_balance -= y
            print(f"Withdraw: ${y:.2f}")
        else:
            print("Insufficient funds.")
    else:
        return "Withdrawal amount must be positive."




def check_balance():
    print(f"Current balance: ${account_balance:.2f}")
    return check_balance


print(f"Amount need to be deposited :", {deposit(1000.0)})
withdraw(250.0)
check_balance()

withdraw(700.67)
check_balance()