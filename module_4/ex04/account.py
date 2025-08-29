from utils import format_cents

class Account:
    def __init__(self, account_id: int, cpf: str):
        self.account_id = account_id
        self.cpf = cpf
        self.__balance = 0
        self__operations = list[str]

    def deposit(self, amount: int, description: str):
        if amount < 0:
            raise ValueError("valor deve ser > 0")
        if not description:
            return None
        self_operations.append(description)
        self.__balance += amount
        
    def withdraw(self, amount: int, description: str):
        if amount < 0:
            raise ValueError("valor deve ser > 0")
        if not description:
            return None
        self_operations.append(description)
        self.__balance -= amount

    def statement(self):
        for i in self.__operations:
            print(i)
        print (f"Balance: {format_cents(self.__balance)}")

    def __str__(self) -> str:
        return f"Account: {self.account_id}\nBalance: {format_cents(self.__balance)}"

    def __repr__(self) -> str:
        return f"Account({self.account_id}, '{self.cpf}')"
    