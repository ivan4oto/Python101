class Bill:
    def __init__(self, amount):
        if amount < 0:
            raise ValueError('Amount must be a positive integer !')
        elif type(amount) != int:
            raise TypeError('Amount should be of integer type !')
        else:
            self.amount = amount

    def __str__(self):
        return 'A {}$ bill'.format(self.amount)

    def __eq__(self,other):
        return self.amount == other.amount

    def __int__(self):
        return int(self.amount)


    def __hash__(self):
        return hash(self.amount)


class BillBatch:
    def __init__(self, bills):
        self.bills = bills
    
    def __len__(self):
        return len(self.bills)

    def total(self):
        x = sum(int(b) for b in self.bills)
        return x

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:
    def __init__(self):
        self.desk = []

    def take_money(self, money):
        self.desk.append(money)

    def total(self):
        result = 0
        for i in self.desk:
            if isinstance(i, Bill):
                result += int(i)
            elif isinstance(i, BillBatch):
                result += i.total()
        return result 

    def __getitem__(self, index):
        return self.desk[index]

    def inspect(self):
        pass





def main():
    pass


if __name__ == "__main__":
    main()  