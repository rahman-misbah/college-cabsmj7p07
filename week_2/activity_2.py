from typing import Union, TypeIs, Any

# Helper type and type checker
type Numeric = Union[int, float]

def isNumeric(user_in: Any) -> TypeIs[Numeric]:
    return isinstance(user_in, (int, float))

# Main BankAccount class
class BankAccount:
    _current_account_no = 1

    def __init__(self):
        self._account_no = BankAccount._current_account_no
        self._balance = 0.0

        BankAccount._current_account_no += 1

    @property
    def account_no(self):
        return self._account_no

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount:Numeric) -> None:
        # Checks
        if not isNumeric(amount): raise TypeError("Amount type must be a number")

        self._balance += amount

    def withdraw(self, amount:Numeric) -> None:
        # Checks
        if not isNumeric(amount): raise TypeError("Amount type must be a number")
        if amount > self.balance: raise ValueError("Not enough funds")

        self._balance -= amount

# Testing class
if __name__ == "__main__":
    account = BankAccount()

    try:
        # Deposit 500
        account.deposit(500)

        # Withdraw 200
        account.withdraw(200)

        # Withdraw 400
        account.withdraw(400)

    except Exception as e:
        print(e)

    finally:
        print("Final Balance:", account.balance)