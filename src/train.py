import numpy as np
from environment import PlatooningEnv
from agent import MARLAgent

def train_platooning():
    env = PlatooningEnv(num_agents=4)
    state_dim = env.num_agents * 2
    action_dim = env.num_agents
    
    agent = MARLAgent(state_dim, action_dim)
    
    print("Starting Multi-Agent Training for Platooning Dynamics...")
    for episode in range(10):
        state = env.reset()
        episode_reward = 0
        
        for step in range(50):
            actions = agent.select_action(state)
            next_state, reward, done, _ = env.step(actions)
            agent.update(state, actions, reward)
            
            state = next_state
            episode_reward += reward
        
        print(f"Episode {episode+1}/10, Average Reward: {episode_reward/50:.4f}")

if __name__ == "__main__":
    train_platooning()