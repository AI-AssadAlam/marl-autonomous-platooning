# 🚛 MARL-Autonomous-Platooning

[![AI Training Pipeline](https://github.com/AI-AssadAlam/marl-autonomous-platooning/actions/workflows/ai-pipeline.yml/badge.svg)](https://github.com/AI-AssadAlam/marl-autonomous-platooning/actions)

A professional framework for **Multi-Agent Reinforcement Learning (MARL)** applied to autonomous vehicle platooning and decentralized coordination. This project serves as a technical bridge between **Optimal Control Theory** and **Agentic AI** for next-generation 6G infrastructure.

## 🌟 Vision
This repository demonstrates a **Decentralized Multi-Agent Coordination** architecture. In high-density 6G environments, static controllers are replaced by autonomous agents that optimize both local safety (inter-vehicle distance) and global efficiency (reduced fuel consumption and emissions via optimized velocity trajectories).

## 🏗 Key Features
- **Dynamic Platooning Environment:** A custom-built simulation modeling the physics of heavy-duty vehicles (HDVs), including position, velocity, and communication latency.
- **Agentic AI Framework:** Utilizes Multi-Agent Reinforcement Learning (MARL) with decentralized policy optimization to account for communication delays and vehicle heterogeneity.
- **Automated MLOps:** Integrated CI/CD pipeline for simulation-based model training and validation via GitHub Actions.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- PyTorch
- NumPy

### Installation
`ash
git clone https://github.com/AI-AssadAlam/marl-autonomous-platooning.git
cd marl-autonomous-platooning
pip install -r requirements.txt
`

### Running the Simulation
To train the multi-agent system and observe the coordination dynamics:
`ash
export PYTHONPATH=pwd/src
python src/train.py
`

## 🛠 Project Structure
- src/environment.py: Multi-agent platooning dynamics and reward modeling.
- src/agent.py: Policy Network architecture for MARL agents.
- src/train.py: Training script for autonomous coordination.
- .github/workflows/: Automated AI training pipeline.

## 🤝 Research & Collaboration
This project is an open framework for research in **Multi-Agent Systems (MAS)**, **6G AI-Native Networks**, and **Autonomous Transport**. Contributions in the areas of **safety-critical RL** and **decentralized world models** are welcome.

---
*Developed by **Assad Alam, Ph.D.**, Principal Researcher @ Ericsson Research.*