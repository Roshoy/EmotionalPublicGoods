class Greedy:
    gratitude_level = 0

    def __init__(self, greed_level=1.0):
        if greed_level > 1.0 or greed_level < 0.0:
            raise Exception('Greed level must be in range 0.0 - 1.0')
        self.greed_level = greed_level

    def calculate_contribution(self, agent_deposit, payoff_delta=None):
        max_contribution = 0.2 * agent_deposit  # bardzo szczodry chciwy agent
        contribution = max_contribution * (1.0 - self.greed_level)
        return contribution

    def calculate_contribution_with_last_payoff(self, agent_deposit, last_payoff):
        # TODO: implement in future
        pass

    def __str__(self):
        return 'GREEDY strategy'


class Cooperative:
    def __init__(self, cooperation_level=1.0):
        if cooperation_level > 1.0 or cooperation_level < 0.0:
            raise Exception('Cooperation level must be in range 0.0 - 1.0')
        self.cooperation_level = cooperation_level

    def calculate_contribution(self, agent_deposit, payoff_delta=None):
        max_contribution = agent_deposit
        min_contribution = 0.8 * max_contribution
        contribution = min_contribution + ((max_contribution - min_contribution) * self.cooperation_level)
        return contribution

    def calculate_contribution_with_last_payoff(self, agent_deposit, last_payoff):
        # TODO: implement in future
        pass

    def __str__(self):
        return 'COOPERATIVE strategy'


class EmotionalStrategy:
    def __init__(self, anger_threshold=2, gratitude_threshold=2):
        if (not isinstance(anger_threshold, int)) or (not isinstance(gratitude_threshold, int)) \
                or anger_threshold < 1 or gratitude_threshold < 1:
            raise Exception('Anger and gratitude thresholds must be integers greater or equal than 1')
        self.anger_threshold = anger_threshold
        self.gratitude_threshold = gratitude_threshold
        self.anger_level = 0
        self.gratitude_level = 0

    def calculate_contribution(self, agent_deposit, payoff_delta):
        if payoff_delta < 0:
            self.anger_level += 1
        else:
            self.gratitude_level += 1

        # If one of these values is equal to or greater than the corresponding simulated emotional threshold, then
        # the value gets reset and the agent’s behaviour changes due to the threshold being reached.
        if self.anger_level == self.anger_threshold:
            self.anger_level = 0
            return 0.0

        if self.gratitude_level == self.gratitude_threshold:
            self.gratitude_level = 0
            return agent_deposit

        # default "neutral" payoff
        return 0.5 * agent_deposit
