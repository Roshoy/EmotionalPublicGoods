

class Agent:
    def __init__(self, name, goodnes):
        self.first_goodness = goodnes
        self.money = 20
        self.last_money = 0
        self.name = name
        self.willingnes_to_contribute = goodnes

    def contribute(self):
        if self.last_money < self.money:
            self.willingnes_to_contribute *= 0.9
        else:
            self.willingnes_to_contribute *= 1.1
            self.willingnes_to_contribute = min(self.willingnes_to_contribute, 1)

        donation = self.willingnes_to_contribute * self.money
        self.last_money = self.money
        self.money -= donation
        # print('Contribution ', donation)
        return donation
    
    def recieve(self, amount):
        self.money += amount
        # print('Recieved ', amount)
    
    def __str__(self):
        return f'{self.name}: {self.money:.2f} | {self.willingnes_to_contribute:.4f} | {self.first_goodness:.4f}'