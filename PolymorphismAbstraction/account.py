class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    def handle_transaction(self, transaction_amount):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        return self.handle_transaction(amount)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other: "Account"):
        return self.balance > other.balance

    def __ge__(self, other: "Account"):
        return self.balance >= other.balance

    def __eq__(self, other: "Account"):
        return self.balance == other.balance

    def __add__(self, other: "Account"):
        new_owner = f"{self.owner}&{other.owner}"
        new_amount = self.amount + other.amount
        new_account = Account(owner=new_owner, amount=new_amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account
