import copy

class Agent:
    def __init__(self, name, strategy, start_deposit=20):
        self.money = start_deposit
        self.last_payoff = 0
        self.current_payoff = 0
        self.name = name
        self.strategy = strategy
        self.payoff_summary = 0
        self.strategy_changed_count = 0

    def contribute(self):
        payoff_delta = self.current_payoff - self.last_payoff
        contribution = self.strategy.calculate_contribution(self.money, payoff_delta=payoff_delta)
        self.money -= contribution
        self.payoff_summary -= contribution
        return contribution

    def receive(self, amount):
        self.last_payoff = self.current_payoff
        self.current_payoff = amount
        self.money += amount
        self.payoff_summary += amount

    def get_inspired(self, other_agents):
        inspiring_agent = self.strategy.update_to_other_agents(other_agents, self)
        if inspiring_agent is None:
            return
        print(str(self) + ' getting inspired by ' + str(inspiring_agent))
        self.strategy = copy.deepcopy(inspiring_agent.strategy)
        self.strategy_changed_count += 1

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
