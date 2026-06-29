from abc import ABC, abstractmethod


class BaseAccount(ABC):
    bank_name = "Vietcombank"

    def __init__(self, account_number, owner_name, balance=0):
        if not self.validate_account_number(account_number):
            raise ValueError("Account number must contain exactly 10 digits.")

        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = balance


    @property
    def owner_name(self):
        return self.__owner_name

    @owner_name.setter
    def owner_name(self, value):
        self.__owner_name = " ".join(value.strip().upper().split())


    @property
    def balance(self):
        return self.__balance

    def _set_balance(self, amount):
        self.__balance = amount


    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __add__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance + other.balance

    def __lt__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance < other.balance


    @staticmethod
    def validate_account_number(account_number):
        return (
            isinstance(account_number, str)
            and len(account_number) == 10
            and account_number.isdigit()
        )

    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name


class SavingsAccount(BaseAccount):

    def __init__(self, account_number, owner_name, interest_rate, balance=0):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        self._set_balance(self.balance + amount)

        print("Deposit successfully.")
        print(f"Balance: {self.balance:,.0f} VND")

    def withdraw(self, amount):

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        fee = amount * 0.02
        total = amount + fee

        if total > self.balance:
            print("Insufficient balance.")
            return

        self._set_balance(self.balance - total)

        print("Withdraw successfully.")
        print(f"Withdraw: {amount:,.0f} VND")
        print(f"Penalty Fee (2%): {fee:,.0f} VND")
        print(f"Balance: {self.balance:,.0f} VND")

    def apply_interest(self):

        interest = self.balance * self.interest_rate
        self._set_balance(self.balance + interest)

        print(f"Interest: +{interest:,.0f} VND")
        print(f"Balance: {self.balance:,.0f} VND")


class CreditAccount(BaseAccount):

    def __init__(self, account_number, owner_name, credit_limit, balance=0):
        super().__init__(account_number, owner_name, balance)
        self.credit_limit = credit_limit

    def deposit(self, amount):

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        self._set_balance(self.balance + amount)

        print("Deposit successfully.")
        print(f"Balance: {self.balance:,.0f} VND")

    def withdraw(self, amount):

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if self.balance - amount < -self.credit_limit:
            print("Exceeded credit limit.")
            return

        self._set_balance(self.balance - amount)

        print("Withdraw successfully.")
        print(f"Balance: {self.balance:,.0f} VND")


class DigitalPremiumMixin:

    def cashback_reward(self, amount):

        if amount > 5_000_000:
            cashback = amount * 0.01
            self.deposit(cashback)

            print(f"[Premium Reward] Cashback: {cashback:,.0f} VND")


class HybridAccount(SavingsAccount, DigitalPremiumMixin):

    def __init__(self, account_number, owner_name, interest_rate, balance=0):
        super().__init__(account_number, owner_name, interest_rate, balance)


class VNPayGateway:

    def execute_pay(self, account, amount):

        print(f"[VNPay] Connecting to account " f"{account.account_number}...")

        account.withdraw(amount)

        print(f"Payment: {amount:,.0f} VND")


class ViettelMoneyGateway:

    def execute_pay(self, account, amount):

        print(f"[Viettel Money] Connecting to account " f"{account.account_number}...")

        account.withdraw(amount)

        print(f"Payment: {amount:,.0f} VND")


def process_payment(payment_gateway, account, amount):

    try:
        payment_gateway.execute_pay(account, amount)

    except AttributeError:
        print("Invalid payment gateway or not integrated.")
