import gym
from gym import spaces
import numpy as np

class TicTacToeEnv(gym.Env):
    def __init__(self):
        super(TicTacToeEnv, self).__init__()
        self.action_space = spaces.Discrete(9)  # 9 possible cells (0-8)
        self.observation_space = spaces.Box(low=0, high=2, shape=(3, 3), dtype=np.int8)
        self.reset()
        
    def reset(self):
        """Reset the environment to the initial state."""
        self.state = np.zeros((3, 3), dtype=np.int8)
        self.current_player = 1  # Player 1 (X) starts
        self.done = False
        return self.state.copy()  # Return a copy to prevent external modifications
        
    def get_valid_actions(self):
        """Return a list of valid actions (empty cells)."""
        return [i for i in range(9) if self.state[i // 3, i % 3] == 0]
        
    def step(self, action):
        """
        Execute one step in the environment.
        
        Args:
            action (int): An integer from 0-8 representing the cell to play
            
        Returns:
            tuple: (observation, reward, done, info)
        """
        if self.done:
            raise RuntimeError("Game is already finished")
            
        if action not in self.get_valid_actions():
            raise ValueError(f"Invalid action: {action}")
            
        # Apply the action
        row, col = action // 3, action % 3
        self.state[row, col] = self.current_player
        
        # Check winning condition
        reward = self.check_win()
        if reward == 1:  # Current player wins
            self.done = True
            return self.state.copy(), 1.0, True, {"winner": self.current_player}
            
        # Check draw condition
        if len(self.get_valid_actions()) == 0:
            self.done = True
            return self.state.copy(), 0.0, True, {"winner": None}
            
        # Switch players
        self.current_player = 3 - self.current_player  # Toggle between 1 and 2
        return self.state.copy(), 0.0, False, {}
        
    def render(self, mode='human'):
        """Render the current game state."""
        if mode != 'human':
            raise NotImplementedError(f"Render mode {mode} is not supported")
            
        symbols = {0: ".", 1: "X", 2: "O"}
        board = "\n".join([
            " ".join([symbols[cell] for cell in row])
            for row in self.state
        ])
        print(f"\nCurrent player: {symbols[self.current_player]}")
        print(board)
        print()
        
    def check_win(self):
        """Check if the current player has won."""
        player = self.current_player
        
        # Check rows and columns
        for i in range(3):
            if np.all(self.state[i, :] == player) or np.all(self.state[:, i] == player):
                return 1
                
        # Check diagonals
        if np.all(np.diag(self.state) == player) or np.all(np.diag(np.fliplr(self.state)) == player):
            return 1
            
        return 0

def play_random_game():
    """Play a random game for testing."""
    env = TicTacToeEnv()
    state = env.reset()
    env.render()
    
    while not env.done:
        valid_actions = env.get_valid_actions()
        action = np.random.choice(valid_actions)
        state, reward, done, info = env.step(action)
        env.render()
        print(f"Action: {action}, Reward: {reward}")
        
        if done:
            winner = info.get("winner")
            if winner:
                print(f"Player {winner} wins!")
            else:
                print("Game ended in a draw!")

if __name__ == "__main__":
    play_random_game()