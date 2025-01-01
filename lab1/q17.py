# Create a class BankAccount with private attributes balance and account_number.
# Implement methods deposit() and withdraw() to modify the balance. Ensure that the
# balance cannot be accessed directly from outside the class.

class BankAccount:
    __balance = 0
    __account_number = 0

    def __init__(self, balance, accoutno):

        try:
            balance = float(balance)
            if balance <= 0:
                raise Exception('ammount cannot be non-positive')
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        
        self.__account_number = accoutno
        self.__balance = balance
        
    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise Exception('ammount cannot be non-positive')
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        self.__balance += amount
        print(f'{amount} has be deposited to {self.__account_number}.')
        print(f'{self.__account_number} has total balance, after deposit = Rs. {self.__balance}')
    
    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise Exception('ammount cannot be non-positive')
            if amount > self.__balance:
                raise Exception('cannot withdraw more than your balance amount')
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        self.__balance -= amount
        print(f'Rs. {amount} has been withdrawn from {self.__account_number}')
        print(f'{self.__account_number} has total balance, after the withdraw = Rs. {self.__balance}')

def main():
    account = BankAccount('4578.0', '1288999910001')
    account.deposit(456.8)
    account.withdraw(500)

if __name__ == '__main__':
    main()