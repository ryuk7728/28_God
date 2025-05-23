import numpy as np
from random import shuffle
import time
import sys

class Kunh:

    def __init__(self):
        self.nodeMap = {}
        self.expected_game_value = 0
        self.n_cards = 3
        self.nash_equilibrium = dict()
        self.current_player = 0
        self.deck = np.array([2,1,0])
        self.n_actions = 2

    def train(self, n_iterations=50000):
        expected_game_value = 0
        for iteration in range(n_iterations):
            shuffle(self.deck)
            print(f"\nIteration {iteration + 1}:") if iteration == 0 else None
            print(f"Deck after shuffle: {self.deck}") if iteration == 0 else None

            result = self.cfr('', 1, 1, iteration == 0)
            expected_game_value += result

            if iteration == 0:
                print(f"Expected game value after first iteration: {expected_game_value}")

            for _, v in self.nodeMap.items():
                if iteration == 0:
                    print(f"Updating strategy for node: {v.key}")
                    print(f"Before update: {v}")
                v.update_strategy()
                if iteration == 0:
                    print(f"After update: {v}")

        expected_game_value /= n_iterations
        display_results(expected_game_value, self.nodeMap)
        print(2+3)

    def cfr(self, history, pr_1, pr_2, debug=False): #history of past actions, pr_1 and pr_2 is the probability of reaching the particular state by player 1 and 2
        n = len(history) 
        is_player_1 = n % 2 == 0 #If length of history is even Player 1 chance else Player 2 chance
        player_card = self.deck[0] if is_player_1 else self.deck[1]

        if debug:
            print(f"\nCurrent history: {history}")
            print(f"Player {'1' if is_player_1 else '2'}'s turn")
            print(f"Player card: {player_card}")

        if self.is_terminal(history):
            card_player = self.deck[0] if is_player_1 else self.deck[1]
            card_opponent = self.deck[1] if is_player_1 else self.deck[0]
            reward = self.get_reward(history, card_player, card_opponent)
            if debug:
                print(f"Terminal state reached with history: {history}")
                print(f"Player card: {card_player}, Opponent card: {card_opponent}, Reward: {reward}")
            return reward

        node = self.get_node(player_card, history)
        strategy = node.strategy

        if debug:
            print(f"Node for state ({player_card}, '{history}'):")
            print(f"Current strategy: {strategy}")

        # Counterfactual utility per action.
        action_utils = np.zeros(self.n_actions)

        for act in range(self.n_actions):
            next_history = history + node.action_dict[act]
            if debug:
                print(f"Evaluating action '{node.action_dict[act]}' leading to history '{next_history}'")
###
            if is_player_1:
                action_utils[act] = -1 * self.cfr(next_history, pr_1 * strategy[act], pr_2, debug)
            else:
                action_utils[act] = -1 * self.cfr(next_history, pr_1, pr_2 * strategy[act], debug)

        # Utility of information set.
        util = sum(action_utils * strategy)
        regrets = action_utils - util

        if debug:
            print(f"Action utilities: {action_utils}")
            print(f"Utility of information set: {util}")
            print(f"Regrets: {regrets}")

        if is_player_1:
            node.reach_pr = pr_1
            node.regret_sum += pr_2 * regrets
        else:
            node.reach_pr = pr_2
            node.regret_sum += pr_1 * regrets

        return util

    @staticmethod
    def is_terminal(history):
        if history[-2:] == 'pp' or history[-2:] == "bb" or history[-2:] == 'bp':
            return True

    @staticmethod
    def get_reward(history, player_card, opponent_card):
        terminal_pass = history[-1] == 'p'
        double_bet = history[-2:] == "bb"
        if terminal_pass:
            if history[-2:] == 'pp':
                return 1 if player_card > opponent_card else -1
            else:
                return 1
        elif double_bet:
            return 2 if player_card > opponent_card else -2

    def get_node(self, card, history):
        key = str(card) + " " + history
        if key not in self.nodeMap:
            action_dict = {0: 'p', 1: 'b'}
            info_set = Node(key, action_dict)
            self.nodeMap[key] = info_set
            return info_set
        return self.nodeMap[key]

class Node:
    def __init__(self, key, action_dict, n_actions=2):
        self.key = key
        self.n_actions = n_actions
        self.regret_sum = np.zeros(self.n_actions)
        self.strategy_sum = np.zeros(self.n_actions)
        self.action_dict = action_dict
        self.strategy = np.repeat(1/self.n_actions, self.n_actions) #Explores all actions equally w/o bias
        self.reach_pr = 0
        self.reach_pr_sum = 0

    def update_strategy(self):
        #Accounts for the strategy used in the current iteration
        self.strategy_sum += self.reach_pr * self.strategy
        self.reach_pr_sum += self.reach_pr
        #Develops the strategy of the next iteration, based on the results of the current iteration
        self.strategy = self.get_strategy()
        self.reach_pr = 0

    def get_strategy(self):
        regrets = self.regret_sum
        regrets[regrets < 0] = 0
        normalizing_sum = sum(regrets)
        if normalizing_sum > 0:
            return regrets / normalizing_sum
        else:
            return np.repeat(1/self.n_actions, self.n_actions)

    def get_average_strategy(self):
        strategy = self.strategy_sum / self.reach_pr_sum
        # Re-normalize
        total = sum(strategy)
        strategy /= total
        return strategy

    def __str__(self):
        strategies = ['{:03.2f}'.format(x)
                      for x in self.get_average_strategy()]
        return '{} {}'.format(self.key.ljust(6), strategies)

def display_results(ev, i_map):
    print('player 1 expected value: {}'.format(ev))
    print('player 2 expected value: {}'.format(-1 * ev))

    print()
    print('player 1 strategies:')
    sorted_items = sorted(i_map.items(), key=lambda x: x[0])
    for _, v in filter(lambda x: len(x[0]) % 2 == 0, sorted_items):
        print(v)
    print()
    print('player 2 strategies:')
    for _, v in filter(lambda x: len(x[0]) % 2 == 1, sorted_items):
        print(v)

if __name__ == "__main__":
    time1 = time.time()
    trainer = Kunh()
    trainer.train(n_iterations=250000)
    print(f"Total time taken: {abs(time1 - time.time())} seconds")
    print(f"Size of trainer object: {sys.getsizeof(trainer)} bytes")
