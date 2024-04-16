from exercise_1_1 import CreditCard

class PredatoryCreditCard(CreditCard):
    # ”””An extension to CreditCard that compounds interest and fees.”””
    LATE_FEE = 100

    def __init__(self, customer, bank, acnt, limit, apr, min_month_payment=0, month_payment=0, percent_min_month_payment = 0.1):
    # ”””Create a new predatory credit card instance.

    # The initial balance is zero.

    # customer the name of the customer (e.g., John Bowman )
    # bank the name of the bank (e.g., California Savings )
    # acnt the acount identifier (e.g., 5391 0375 9387 5309 )
    # limit credit limit (measured in dollars)
    # apr annual percentage rate (e.g., 0.0825 for 8.25% APR)

        super().__init__(customer, bank, acnt, limit) # call super constructor
        self._apr = apr
        self._min_month_payment = min_month_payment
        self._month_payment = month_payment
        self._percent_min_month_payment = percent_min_month_payment

    def charge(self, price):
    # Charge given price to the card, assuming sufficient credit limit.

    # Return True if charge was processed.
    # Return False and assess 5 fee if charge is denied.

        success = super().charge(price) # call inherited method
        if not success:
            self._balance += 5 # assess penalty
        return success # caller expects return value

    def process_month(self):

        if self._month_payment < self._min_month_payment:
            self._balance += PredatoryCreditCard.LATE_FEE

    # Assess monthly interest on outstanding balance.
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
        self._month_payment = 0
        self._min_month_payment = self._balance*self._percent_min_month_payment

    def make_payment(self, amount):
        self._month_payment += amount
        return super().make_payment(amount)
    

if __name__ == "__main__":
    c = PredatoryCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 1000, 0.08)

    # Test charge, and no fee first month
    control = 0
    c.charge(500)
    control += 500
    c.charge(200)
    control += 200
    assert(c._balance==control)
    print(c._balance)
    c.process_month()
    control *=pow(1 + 0.08, 1/12)
    print(c._balance)
    print(control)
    assert(c._balance==control)

    # Second month no fee, because payment
    c.charge(200)
    control += 200
    c.make_payment(100)
    control -= 100
    print(c._balance)
    assert(c._balance==control)
    c.process_month()
    control *=pow(1 + 0.08, 1/12)
    assert(c._balance==control)
    print(c._balance)

    # Third month fee
    c.process_month()
    control += 100
    control *=pow(1 + 0.08, 1/12)
    assert(c._balance==control)

