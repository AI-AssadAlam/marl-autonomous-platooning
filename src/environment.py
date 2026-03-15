import numpy as np

class PlatooningEnv:
    \"\"\"
    A simplified Multi-Agent environment simulating autonomous vehicle platooning.
    Each vehicle (agent) aims to maintain a target distance from the one ahead
    while optimizing fuel consumption (minimizing acceleration jitter).
    \"\"\"
    def __init__(self, num_agents=4, target_dist=5.0):
        self.num_agents = num_agents
        self.target_dist = target_dist
        self.state = np.zeros((num_agents, 2)) # [position, velocity]
        self.reset()

    def reset(self):
        # Initial positions and velocities
        for i in range(self.num_agents):
            self.state[i] = [i * -10.0, 20.0] # 10m apart, 20m/s
        return self.state.flatten()

    def step(self, actions):
        # actions: acceleration for each agent
        dt = 0.1
        rewards = []
        
        # Lead vehicle moves at relatively constant speed with slight noise
        self.state[0][1] += actions[0] * dt + np.random.normal(0, 0.05)
        self.state[0][0] += self.state[0][1] * dt
        
        for i in range(1, self.num_agents):
            self.state[i][1] += actions[i] * dt
            self.state[i][0] += self.state[i][1] * dt
            
            # Distance to vehicle ahead
            dist = self.state[i-1][0] - self.state[i][0]
            
            # Reward function: proximity to target_dist - penalty for high accel
            dist_error = abs(dist - self.target_dist)
            reward = -dist_error - 0.1 * (actions[i]**2)
            rewards.append(reward)
            
        return self.state.flatten(), np.mean(rewards), False, {}