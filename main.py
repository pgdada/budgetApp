# Mock 2: Budget App
# Author : @pgdada

class Budget:
    def __init__(self, amount):
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        print('Deposit sucessful!')

    def check_balance(self):
        return self.amount
        # print(f'Available balance: {self.amount}')

    def withdraw(self, amount):
        if self.amount > amount:
            self.amount -= amount
            print('Withdrawal sucessful!')
        else:
            # raise ValueError(f'You can only withdraw amount less than {self.amount}')
            print(f'Sorry, you can only withdraw amount less than or equal to {self.amount}')

    def transfer(self, other, amount):
        # Transfer of funds from self -> other
        self.withdraw(amount);
        other.deposit(amount);
        print('Transfer successful!')
        

# Food, Clothing, Car, Entertainment, Education

class Category(Budget):
    # Budget Category
    def __init__(self, amount):
        super().__init__(amount)

    def __repr__(self):
        return f"Budget Category, currently allocated {self.amount} USD"

    def __eq__(self, other: object) -> bool:
        return self.amount == other.amount

    def __gt__(self, other: object) -> bool:
        return self.amount > other.amount

    def __lt__(self, other: object) -> bool:
        return self.amount < other.amount


# Budget Category instantiations:
food = Category(500)
clothing = Category(1000)
car = Category(500)
entertainment = Category(5000)
education = Category(10000)

# Methods demonstrations:
print(f'Clothing balance: {clothing.check_balance()}')

print(f'Food balance: {food.check_balance()}')
food.withdraw(520)  # withdrawal
print(f'Food balance: {food.check_balance()}')

print(f'Education balance: {education.check_balance()}')
education.deposit(10000) # deposit
print(f'Education balance: {education.check_balance()}')

print(f'Entertainment balance: {entertainment.check_balance()}')
print(f'Car balance: {car.check_balance()}')
entertainment.transfer(car, 2000) # tranfer
print(f'Entertainment balance: {entertainment.check_balance()}')
print(f'Car balance: {car.check_balance()}')

print(education)