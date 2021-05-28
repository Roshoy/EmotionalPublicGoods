from Qlearning import get_next_action, update_q_table


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

    def update_to_other_agents(self, other_agents, agent):
        pass

    def reset(self):
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

    def update_to_other_agents(self, other_agents, agent):
        pass
    
    def reset(self):
        pass

    def __str__(self):
        return 'COOPERATIVE strategy'


class EmotionalStrategy:
    def __init__(self, anger_threshold=2, gratitude_threshold=2, admiration_threshold=2, is_smart=False):
        if (not isinstance(anger_threshold, int)) or (not isinstance(gratitude_threshold, int)) \
                or (not isinstance(admiration_threshold, int)) \
                or anger_threshold < 1 or gratitude_threshold < 1 or admiration_threshold < 1:
            raise Exception('Anger and gratitude thresholds must be integers greater or equal than 1')
        self.anger_threshold = anger_threshold
        self.gratitude_threshold = gratitude_threshold
        self.admiration_threshold = admiration_threshold
        self.is_smart = is_smart
        self.anger_level = 0
        self.gratitude_level = 0
        self.admiration = {}

    def update_to_other_agents(self, other_agents, agent):  # admiration
        if self.is_smart:
            return None
        max_payoff_agent = None
        for other in other_agents:
            if other.payoff_summary <= agent.payoff_summary:
                continue

            if other.name not in self.admiration.keys():
                self.admiration[other.name] = 1
            else:
                self.admiration[other.name] += 1

            if self.admiration[other.name] >= self.admiration_threshold:
                if max_payoff_agent is None \
                        or max_payoff_agent.payoff_summary < other.payoff_summary:
                    max_payoff_agent = other
        return max_payoff_agent

    def calculate_contribution(self, agent_deposit, payoff_delta, last_action=None):
        previous_state = (self.anger_level, self.gratitude_level)
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

        if self.is_smart:
            current_state = (self.anger_level, self.gratitude_level)
            action = get_next_action(current_state)  # action = 0/1, (0 - not pay, 1 - pay)
            reward = payoff_delta
            update_q_table(previous_state, current_state, action, reward)
            return action * agent_deposit

        # default "neutral" payoff
        return 0.5 * agent_deposit

    def reset(self):
        self.anger_level = 0
        self.gratitude_level = 0
        self.admiration = {}

    def __str__(self):
        return f'EmotionalStrategy: ({self.anger_threshold},{self.gratitude_threshold},{self.admiration_threshold})'
