"""
Module used to describe all of the different data types
"""


class Wallet:
    """
    Stores data relevant to a users wallet such as balance and
    currency
    """

#    def __init__(self, wType, currency, balance, unsettled_interest):
    def __init__(self, data):
# https://docs.bitfinex.com/reference#ws-auth-wallets
        self.type = data[0] #wType
        self.currency = data[1] #currency
        self.balance = data[2] #balance
        self.unsettled_interest = data[3] #unsettled_interest
        self.balance_avail = data[4] #BALANCE_AVAILABLE
        self.description = data[5] #DESCRIPTION
        self.meta = data[6] #META
        self.key = "{}_{}".format(self.type, self.currency)

    def set_balance(self, data):
        """
        Set the balance of the wallet
        """
        self.balance = data

    def set_unsettled_interest(self, data):
        """
        Set the unsettled interest of the wallet
        """
        self.unsettled_interest = data

    def __str__(self):
        return "Wallet <'{}_{}' balance='{}' balance_avail='{}' unsettled='{}' meta={}>".format(
            self.type, self.currency, self.balance, self.balance_avail, self.unsettled_interest, self.meta)
