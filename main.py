#SENIH UCAR
import bankaccount

if __name__ == "__main__":

    while True:
        try:
            name = str(input("Please, enter account name :\n"))
            balance = float(input("Please, enter balance :\n"))
            account1 = bankaccount.BankAccount(name,balance)
            account1.displayDetails()
            break
        except ValueError as e:
            print(str(e))
            print('Incorrect input, try again\n')
            continue
    while True:
        try:
            choice = int(input("\n\tPlease, select transaction type:\n1 - Deposit\n2 - Withdraw\n"))
            if choice == 1:
                print("your choice is  'Deposit' ")
                deposit_amount = float(input("Enter, deposit amount: "))
                account1.methodDeposit(deposit_amount)
                account1.displayDetails()
                another_transaction = input("Do you want to make another transaction? yes/no: ")
                if another_transaction == "yes":
                    continue
                else:
                    break
            if choice == 2:
                print("your choice is  'Withdraw' ")
                withdraw_amount = float(input("Enter, withdraw amount: "))
                account1.methodWithdraw(withdraw_amount)
                account1.displayDetails()
                another_transaction = input("Do you want to make another transaction? yes/no: ")
                if another_transaction == "yes":
                    continue
                else:
                    break
            else:
                raise ValueError("invalid choice")
        except ValueError as e:
            print(str(e))
            another_transaction = input("Do you want to make another transaction? yes/no: ")
            if another_transaction == "yes":
                continue
            else:
                break
            pass
