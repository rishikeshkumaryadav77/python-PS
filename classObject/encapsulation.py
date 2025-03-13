from abc import ABC, abstractmethod

# Abstract Class
class Bank(ABC):
    @abstractmethod
    def loan_interest(self):
        pass

# Concrete Class 1
class SBI(Bank):
    def loan_interest(self):
        return "SBI Loan Interest: 7%"

# Concrete Class 2
class HDFC(Bank):
    def loan_interest(self):
        return "HDFC Loan Interest: 8.5%"

# Creating objects
bank1 = SBI()
bank2 = HDFC()

print(bank1.loan_interest())
print(bank2.loan_interest())
