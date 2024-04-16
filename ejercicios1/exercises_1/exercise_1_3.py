from exercise_1_1 import CreditCard

class PredatoryCreditCard(CreditCard):
    # ”””An extension to CreditCard that compounds interest and fees.”””

    def __init__(self, customer, bank, acnt, limit, apr, charge_calls=0, max_charge_calls=10):
    # ”””Create a new predatory credit card instance.

    # The initial balance is zero.

    # customer the name of the customer (e.g., John Bowman )
    # bank the name of the bank (e.g., California Savings )
    # acnt the acount identifier (e.g., 5391 0375 9387 5309 )
    # limit credit limit (measured in dollars)
    # apr annual percentage rate (e.g., 0.0825 for 8.25% APR)

        super().__init__(customer, bank, acnt, limit) # call super constructor
        self._apr = apr
        self._charge_calls = charge_calls
        self._max_charge_calls = max_charge_calls

    def charge(self, price):
    # Charge given price to the card, assuming sufficient credit limit.

    # Return True if charge was processed.
    # Return False and assess 5 fee if charge is denied.

        success = super().charge(price) # call inherited method
        if not success:
            self._balance += 5 # assess penalty
        else:
            self._charge_calls += 1
            if self._charge_calls > self._max_charge_calls:
                self._balance += 1 # assess penalty
        return success # caller expects return value

    def process_month(self):
    # Assess monthly interest on outstanding balance.
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

        self._charge_calls = 0


if __name__ == "__main__":
    c = PredatoryCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 1000, 0.08)

    # Test charge, and no fee first month
    assert(c._charge_calls==0)
    for _ in range(10):
        c.charge(10)
    assert(c._balance==100)
    c.charge(10)
    assert(c._balance==111)
    
    c.process_month()
    assert(c._charge_calls==0)
