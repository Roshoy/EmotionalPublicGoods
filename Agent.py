class Agent:
    def __init__(self, name, strategy, start_deposit=20):
        self.money = start_deposit
        self.last_money = 0
        self.name = name
        self.strategy = strategy

    def contribute(self):
        contribution = self.strategy.calculate_contribution(self.money)
        self.money -= contribution
        return contribution

    def receive(self, amount):
        self.money += amount

    def __str__(self):
        return f'{self.name}: {self.money:.2f} | {self.strategy}'

    # def contribute(self):
    #     if self.last_money < self.money:
    #         self.willingness_to_contribute *= 0.9
    #     else:
    #         self.willingness_to_contribute *= 1.1
    #         self.willingness_to_contribute = min(self.willingness_to_contribute, 1)
    #
    #     donation = self.willingness_to_contribute * self.money
    #     self.last_money = self.money
    #     self.money -= donation
    #     # print('Contribution ', donation)
    #     return donation
