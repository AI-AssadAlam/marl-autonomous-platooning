import torch
import torch.nn as nn
import torch.optim as optim

class PolicyNetwork(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, output_dim),
            nn.Tanh() # Normalized acceleration [-1, 1]
        )

    def forward(self, x):
        return self.fc(x)

class MARLAgent:
    def __init__(self, state_dim, action_dim):
        self.policy = PolicyNetwork(state_dim, action_dim)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=1e-3)

    def select_action(self, state):
        state_tensor = torch.FloatTensor(state)
        with torch.no_grad():
            action = self.policy(state_tensor)
        return action.numpy()

    def update(self, state, action, reward):
        # Simplified update logic for demonstration
        state_tensor = torch.FloatTensor(state)
        action_tensor = torch.FloatTensor(action)
        reward_tensor = torch.FloatTensor([reward])
        
        predicted_action = self.policy(state_tensor)
        loss = nn.MSELoss()(predicted_action, action_tensor) * (-reward_tensor) # Policy Gradient intuition
        
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()