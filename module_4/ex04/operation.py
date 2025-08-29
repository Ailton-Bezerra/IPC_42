from utils import format_cents

class Operation:
    def __init__(self, cents: int, description: str):
        if cents == 0:
            raise ValueError
        self.operation_type = "credit" if cents > 0 else "debit"
        self.cents = cents
        self.description = description

    def __repr__(self) -> str:
        return f"Operation(cents={self.cents}, operation_type='{self.operation_type}', description='{self.description}')"
    
    def __str__(self) -> str:
        return f"{format_cents(self.cents)} ({self.description})"