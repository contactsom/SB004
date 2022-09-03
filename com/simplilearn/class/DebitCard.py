class DabitCard:

    def __init__(self, number, expdate, ccv): # 3. This is the Three parameter Construtor
        self.number = number
        self.expdate = expdate
        self.ccv = ccv

    def debitDetails(self):
        print("My DEBIT CARD Number ",self.number)
        print("My DEBIT CARD Expiry  ", self.expdate)
        print("My DEBIT CARD CCV  ", self.ccv)

d1=DabitCard(123,2022,980)
d1.debitDetails()

