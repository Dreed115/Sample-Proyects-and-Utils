class CreditCard:
    """ A Consumer credit card """
    def __init__(self, customer, bank, acnt, limit):
        """ 
        Create a new credit card instance.
        The initial balance is zero 

        customer    the name of the customer (e.g., 'Jhon Beown')
        bank        the name of the bank (e.g., 'California Savings')
        acnt        the acount identifier (e.g., '5391 0381 9381 3122')
        limit       credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    def get_customer(self):
        """ Return name of the customer """
        return self._customer
    
    def get_bank(self):
        """ Return the bank's name """
        return self._bank
    
    def get_account(self):
        """ Return the card identifying number (typically stored as a string) """
        return self._account
    
    def get_limit(self):
        """ Return current credit limit """
        return self._limit
    
    def get_balance(self):
        """ Return current balance """
        return self._balance

    def charge(self, price):
        """ 
        Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was declined.
        """
        if price + self._balance > self._limit:     #If chage would exceed limit
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """ Process customer payment that reduces balance """
        self._balance -= amount


class PredetoryCreditCard(CreditCard):
    """ An extension to CreditCard that compundds interest and fees """
    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied.
        """
        success = super().charge(price) 
        if not success:
            self._balance += 5
        
        return success
    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

cc = CreditCard('Gojo Storu', '1st Bank', '1234 5678 9012 3456', 1000)

a = PredetoryCreditCard('Gojo Storu', '1st Bank', '1234 5678 9012 3456', 1000, 0.0825)
a.charge(900)
a.process_month()

print(a.get_balance())

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Gojo Storu', '1st Bank', '1234 5678 9012 3456', 1000))
    wallet.append(CreditCard('Gojo Storu', '1st Bank', '0987 6543 2109 8765', 2000))
    wallet.append(CreditCard('Gojo Storu', '1st Bank', '3726 6296 3179 6309', 10000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New Balance =', wallet[c].get_balance())
        print()
